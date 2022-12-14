# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from gateway.requests import ChangeSellerRequest_pb2 as gateway_dot_requests_dot_ChangeSellerRequest__pb2
from gateway.responses import ChangeSellerResponse_pb2 as gateway_dot_responses_dot_ChangeSellerResponse__pb2


class HeathBuddyServiceStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.changeSeller = channel.unary_unary(
        '/fkhp.gateway.layer.client.HeathBuddyService/changeSeller',
        request_serializer=gateway_dot_requests_dot_ChangeSellerRequest__pb2.ChangeSellerRequest.SerializeToString,
        response_deserializer=gateway_dot_responses_dot_ChangeSellerResponse__pb2.ChangeSellerResponse.FromString,
        )


class HeathBuddyServiceServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def changeSeller(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_HeathBuddyServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'changeSeller': grpc.unary_unary_rpc_method_handler(
          servicer.changeSeller,
          request_deserializer=gateway_dot_requests_dot_ChangeSellerRequest__pb2.ChangeSellerRequest.FromString,
          response_serializer=gateway_dot_responses_dot_ChangeSellerResponse__pb2.ChangeSellerResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'fkhp.gateway.layer.client.HeathBuddyService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
