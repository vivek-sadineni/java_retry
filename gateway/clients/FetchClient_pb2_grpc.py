# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from gateway.requests import FetchPageRequest_pb2 as gateway_dot_requests_dot_FetchPageRequest__pb2
from gateway.responses import FetchResponse_pb2 as gateway_dot_responses_dot_FetchResponse__pb2


class FetchClientStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.fetch = channel.unary_unary(
        '/fkhp.gateway.layer.client.FetchClient/fetch',
        request_serializer=gateway_dot_requests_dot_FetchPageRequest__pb2.FetchPageRequest.SerializeToString,
        response_deserializer=gateway_dot_responses_dot_FetchResponse__pb2.FetchResponse.FromString,
        )


class FetchClientServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def fetch(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_FetchClientServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'fetch': grpc.unary_unary_rpc_method_handler(
          servicer.fetch,
          request_deserializer=gateway_dot_requests_dot_FetchPageRequest__pb2.FetchPageRequest.FromString,
          response_serializer=gateway_dot_responses_dot_FetchResponse__pb2.FetchResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'fkhp.gateway.layer.client.FetchClient', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))