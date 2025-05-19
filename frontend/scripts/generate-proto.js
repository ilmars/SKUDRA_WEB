import path from 'path';
import { fileURLToPath } from 'url';
import { execSync } from 'child_process';
import fs from 'fs';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const projectRoot = path.resolve(__dirname, '..');

// Use relative paths from the project root
const PROTO_DIR = 'src/grpcModule/proto';
const MODEL_DIR = 'src/grpcModule/generated';

// Create the generated directory if it doesn't exist
if (!fs.existsSync(path.join(projectRoot, MODEL_DIR))) {
  fs.mkdirSync(path.join(projectRoot, MODEL_DIR), { recursive: true });
}

// Get all .proto files
const protoFiles = fs.readdirSync(path.join(projectRoot, PROTO_DIR))
  .filter(file => file.endsWith('.proto'));

if (protoFiles.length === 0) {
  console.error('No .proto files found in', PROTO_DIR);
  process.exit(1);
}

// Clean existing generated files
console.log('Cleaning existing generated files...');
fs.readdirSync(path.join(projectRoot, MODEL_DIR))
  .filter(file => file.endsWith('.js') || file.endsWith('.ts'))
  .forEach(file => {
    fs.unlinkSync(path.join(projectRoot, MODEL_DIR, file));
  });

// Generate JavaScript code for each proto file
protoFiles.forEach(protoFile => {
  console.log(`Processing ${protoFile}...`);
  try {
    // Generate ES6 modules
    const protocCmd = `protoc \
      --js_out=import_style=commonjs,binary:${MODEL_DIR} \
      --grpc-web_out=import_style=commonjs,mode=grpcwebtext:${MODEL_DIR} \
      -I ${PROTO_DIR} \
      ${PROTO_DIR}/${protoFile}`;

    console.log('Running command:', protocCmd);
    execSync(protocCmd, { 
      cwd: projectRoot,
      stdio: 'inherit'
    });

    // Post-process to convert to pure ES modules
    const jsFiles = fs.readdirSync(path.join(projectRoot, MODEL_DIR))
      .filter(file => file.endsWith('.js'));

    jsFiles.forEach(jsFile => {
      const filePath = path.join(projectRoot, MODEL_DIR, jsFile);
      let content = fs.readFileSync(filePath, 'utf8');

      // Only do proto namespace logic for *_pb.js files (not *_grpc_web_pb.js)
      const isProtoMsgFile = jsFile.endsWith('_pb.js') && !jsFile.endsWith('_grpc_web_pb.js');

      // Convert requires to imports at the top
      const imports = new Set();
      content = content.replace(
        /(?:var|const)\s+(\w+)\s*=\s*require\(['"]([^'"]+)['"]\);?/g,
        (match, varName, importPath) => {
          if (importPath === 'google-protobuf') {
            imports.add(`import * as jspb from 'google-protobuf';`);
            return '';
          }
          if (importPath === 'grpc-web') {
            imports.add(`import * as grpcWeb from 'grpc-web';`);
            return 'const grpc = { web: grpcWeb };';
          }
          if (importPath.startsWith('./')) {
            importPath = importPath.replace(/\.js$/, '') + '.js';
            imports.add(`import * as ${varName} from '${importPath}';`);
            return '';
          }
          if (importPath.startsWith('google-protobuf/')) {
            importPath = importPath.replace(/\.js$/, '') + '.js';
            imports.add(`import * as ${varName} from '${importPath}';`);
            return '';
          }
          return match;
        }
      );

      if (isProtoMsgFile) {
        // Remove any duplicate jspb declarations after import
        content = content.replace(/^(var|const)\s+jspb\s*=.*;$/gm, '');

        // Initialize proto namespace with proper structure
        const namespace = jsFile.replace('_pb.js', '').replace(/[.-]/g, '_');
        content = content.replace(
          /(var|const)\s+proto\s*=\s*{};/,
          `const proto = {};\nproto.${namespace} = {};`
        );

        // Ensure proto is defined at the top level
        if (!/^const proto = {};/m.test(content)) {
          // Insert after the last import
          const importBlockMatch = content.match(/^(import .+\n)+/);
          if (importBlockMatch) {
            const importBlock = importBlockMatch[0];
            content = content.replace(importBlock, importBlock + 'const proto = {};\n');
          } else {
            content = 'const proto = {};\n' + content;
          }
        }

        // Collect all proto class names
        const protoClasses = new Set();
        const classMatches = content.matchAll(/proto\.\w+\.(\w+)\s*=\s*function/g);
        for (const match of classMatches) {
          protoClasses.add(match[1]);
        }

        // Export all proto classes (deduplicate)
        const exported = new Set();
        const exports = [];
        for (const className of protoClasses) {
          if (!exported.has(className)) {
            exports.push(`export const ${className} = proto.${namespace}.${className};`);
            exported.add(className);
          }
        }
        // Only export proto once
        if (!exported.has('proto') && protoClasses.size > 0) {
          exports.push('export { proto };');
          exported.add('proto');
        }

        // Combine everything
        content = Array.from(imports).join('\n') +
          (imports.size > 0 ? '\n\n' : '') +
          content.trim() + '\n\n' +
          exports.join('\n');

        // Remove duplicate export lines
        content = content.replace(/^export const (\w+) = proto\.\w+\.\1;$(?:\r?\n)?/gm, (match, p1, offset, str) => {
          return str.indexOf(match) === offset ? match : '';
        });
        content = content.replace(/^export { proto };$(?:\r?\n)?/gm, (match, offset, str) => {
          return str.indexOf(match) === offset ? match : '';
        });

        // Clean up formatting
        content = content.replace(/\n\s*\n\s*\n/g, '\n\n');
        content = content.trim() + '\n';
      } else {
        // For *_grpc_web_pb.js files, just clean up formatting and write as-is
        content = content.replace(/\n\s*\n\s*\n/g, '\n\n');
        content = content.trim() + '\n';
      }

      fs.writeFileSync(filePath, content);
    });

    console.log(`✓ Successfully processed ${protoFile}`);
  } catch (error) {
    console.error(`✗ Failed to process ${protoFile}:`, error.message);
    process.exit(1);
  }
});

console.log('\nProto generation complete!');