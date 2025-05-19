#!/bin/bash

# Get the script's directory
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
PROJECT_ROOT="$SCRIPT_DIR/../.."
FRONTEND_DIR="$PROJECT_ROOT/frontend"
PROTO_DIR="$FRONTEND_DIR/src/grpcModule/proto"
OUTPUT_DIR="$PROJECT_ROOT/etc/envoy"

# Create proto descriptor output directory if it doesn't exist
mkdir -p "$OUTPUT_DIR"

echo "Generating proto descriptor..."
echo "Proto directory: $PROTO_DIR"
echo "Output directory: $OUTPUT_DIR"

# Find protoc's well-known protos directory
PROTOC_INCLUDE=$(protoc --version | sed -n 's/.*\([0-9]\.[0-9]\+\.[0-9]\+\)$/\/usr\/local\/include/p')

if [ ! -d "$PROTOC_INCLUDE" ]; then
    # Try alternative location for Windows
    PROTOC_INCLUDE="C:/Program Files/protoc/include"
fi

echo "Using protoc include path: $PROTOC_INCLUDE"

# Generate the proto descriptor including all imports
protoc \
    --proto_path="$PROTOC_INCLUDE" \
    --proto_path="$PROTO_DIR" \
    --include_imports \
    --include_source_info \
    --descriptor_set_out="$OUTPUT_DIR/proto.pb" \
    "$PROTO_DIR"/*.proto

if [ $? -eq 0 ]; then
    echo "✓ Proto descriptor successfully generated at $OUTPUT_DIR/proto.pb"
    
    # Verify the contents
    echo "Verifying proto descriptor contents..."
    protoc --decode=google.protobuf.FileDescriptorSet --proto_path="$PROTOC_INCLUDE" google/protobuf/descriptor.proto < "$OUTPUT_DIR/proto.pb" | grep "name:" | sort
else
    echo "✗ Failed to generate proto descriptor"
    exit 1
fi 