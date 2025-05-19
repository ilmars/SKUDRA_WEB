// Plugins
import AutoImport from 'unplugin-auto-import/vite'
import Components from 'unplugin-vue-components/vite'
import Fonts from 'unplugin-fonts/vite'
import Layouts from 'vite-plugin-vue-layouts'
import Vue from '@vitejs/plugin-vue'
import VueRouter from 'unplugin-vue-router/vite'
import Vuetify, { transformAssetUrls } from 'vite-plugin-vuetify'

// Utilities
import { defineConfig } from 'vite'
import { fileURLToPath, URL } from 'node:url'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [
    VueRouter({
      dts: 'src/typed-router.d.ts',
    }),
    Layouts(),
    AutoImport({
      imports: [
        'vue',
        {
          'vue-router/auto': ['useRoute', 'useRouter'],
        }
      ],
      dts: 'src/auto-imports.d.ts',
      eslintrc: {
        enabled: true,
      },
      vueTemplate: true,
    }),
    Components({
      dts: 'src/components.d.ts',
    }),
    Vue({
      template: { transformAssetUrls },
    }),
    // https://github.com/vuetifyjs/vuetify-loader/tree/master/packages/vite-plugin#readme
    Vuetify({
      autoImport: true,
      styles: {
        configFile: 'src/styles/settings.scss',
      },
    }),
    Fonts({
      google: {
        families: [ {
          name: 'Roboto',
          styles: 'wght@100;300;400;500;700;900',
        }],
      },
    }),
  ],
  define: { 'process.env': {} },
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url)),
    },
    extensions: [
      '.js',
      '.json',
      '.jsx',
      '.mjs',
      '.ts',
      '.tsx',
      '.vue',
    ],
  },
  server: {
    port: 3000,
    proxy: {
      '/api': {
        target: 'http://127.0.0.1:8000',
        changeOrigin: true,
        headers: {
          'Access-Control-Allow-Methods': 'GET, POST, PUT, DELETE, OPTIONS',
          'Access-Control-Allow-Headers': 'X-Requested-With, content-type, Authorization, x-xsrf-token'
        }
      },
      '/static': {
        target: 'http://127.0.0.1:8000',
        changeOrigin: true
      },
      '/patrol/init': {
        target: 'http://127.0.0.1:8000',
        changeOrigin: true
      },
      '/admin': {
        target: 'http://127.0.0.1:8000',
        changeOrigin: true
      },
      '/__debug__': {
        target: 'http://127.0.0.1:8000',
        changeOrigin: true
      },
      // Uncomment this if you need websocket proxy support
      // '/ws': {
      //   target: 'http://localhost:3000/socket.io/',
      //   changeOrigin: true,
      //   ws: true, // Enable WebSockets
      //   onError(err, req, res) {
      //     res.end(''); // Send an empty response to suppress ECONNREFUSED errors
      //   }
      // }
    }
  },
  css: {
    preprocessorOptions: {
      sass: {
        api: 'modern-compiler',
      },
    },
  },
})
