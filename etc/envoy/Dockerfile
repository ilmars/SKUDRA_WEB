FROM envoyproxy/envoy:v1.27.0

# Install protoc and required tools
RUN apt-get update && apt-get install -y \
    protobuf-compiler \
    git \
    && rm -rf /var/lib/apt/lists/*

# Create directory for proto files
WORKDIR /tmp/protos

# Download Google API proto files
RUN git clone --depth 1 https://github.com/googleapis/googleapis.git /tmp/googleapis

# Copy proto files
COPY GrpcProtos/*.proto ./

# Generate the descriptor file
RUN protoc \
    --proto_path=. \
    --proto_path=/tmp/googleapis \
    --include_imports \
    --include_source_info \
    --descriptor_set_out=/etc/envoy/test_proto.pb \
    welcome.proto simple_mode_grpc.proto advanced_mode_grpc.proto common.proto decimal_value.proto shared_architecture.proto

# Clean up
RUN rm -rf /tmp/protos /tmp/googleapis

# Copy Envoy configuration
COPY envoy/envoy.yaml /etc/envoy/envoy.yaml 