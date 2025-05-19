#!/bin/bash

# Create a temporary directory for proto files
mkdir -p /tmp/protos

# Copy all proto files to the temporary directory
cp ../GrpcProtos/*.proto /tmp/protos/

# Generate the descriptor file
protoc \
  --proto_path=/tmp/protos \
  --include_imports \
  --include_source_info \
  --descriptor_set_out=test_proto.pb \
  /tmp/protos/*.proto

# Clean up
rm -rf /tmp/protos

echo "Proto descriptor file generated successfully!" 