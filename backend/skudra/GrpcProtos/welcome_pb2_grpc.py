# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from skudra.GrpcProtos import welcome_pb2 as welcome__pb2

GRPC_GENERATED_VERSION = '1.71.0'
GRPC_VERSION = grpc.__version__
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    raise RuntimeError(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in welcome_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class WelcomeGrpcStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Handshake = channel.unary_unary(
                '/welcome_grpc.WelcomeGrpc/Handshake',
                request_serializer=welcome__pb2.HandshakeRequest.SerializeToString,
                response_deserializer=welcome__pb2.HandshakeReply.FromString,
                _registered_method=True)
        self.StreamReceiverList = channel.unary_stream(
                '/welcome_grpc.WelcomeGrpc/StreamReceiverList',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=welcome__pb2.ReceiverListGrpc.FromString,
                _registered_method=True)


class WelcomeGrpcServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Handshake(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def StreamReceiverList(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_WelcomeGrpcServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Handshake': grpc.unary_unary_rpc_method_handler(
                    servicer.Handshake,
                    request_deserializer=welcome__pb2.HandshakeRequest.FromString,
                    response_serializer=welcome__pb2.HandshakeReply.SerializeToString,
            ),
            'StreamReceiverList': grpc.unary_stream_rpc_method_handler(
                    servicer.StreamReceiverList,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=welcome__pb2.ReceiverListGrpc.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'welcome_grpc.WelcomeGrpc', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('welcome_grpc.WelcomeGrpc', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class WelcomeGrpc(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Handshake(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/welcome_grpc.WelcomeGrpc/Handshake',
            welcome__pb2.HandshakeRequest.SerializeToString,
            welcome__pb2.HandshakeReply.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def StreamReceiverList(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(
            request,
            target,
            '/welcome_grpc.WelcomeGrpc/StreamReceiverList',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            welcome__pb2.ReceiverListGrpc.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
