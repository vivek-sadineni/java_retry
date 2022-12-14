# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from gateway.requests import AddressFromLocationPointRequest_pb2 as gateway_dot_requests_dot_AddressFromLocationPointRequest__pb2
from gateway.requests import AddressSuggestionRequest_pb2 as gateway_dot_requests_dot_AddressSuggestionRequest__pb2
from gateway.requests import GeocodingRequest_pb2 as gateway_dot_requests_dot_GeocodingRequest__pb2
from gateway.responses import AddressFromLocationPointResponse_pb2 as gateway_dot_responses_dot_AddressFromLocationPointResponse__pb2
from gateway.responses import AddressSuggestionResponse_pb2 as gateway_dot_responses_dot_AddressSuggestionResponse__pb2
from gateway.responses import GeocodingResponse_pb2 as gateway_dot_responses_dot_GeocodingResponse__pb2


class FlipMapServiceStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.reverseGeocoding = channel.unary_unary(
        '/fkhp.gateway.layer.client.FlipMapService/reverseGeocoding',
        request_serializer=gateway_dot_requests_dot_AddressFromLocationPointRequest__pb2.AddressFromLocationPointRequest.SerializeToString,
        response_deserializer=gateway_dot_responses_dot_AddressFromLocationPointResponse__pb2.AddressFromLocationPointResponse.FromString,
        )
    self.addressSuggestion = channel.unary_unary(
        '/fkhp.gateway.layer.client.FlipMapService/addressSuggestion',
        request_serializer=gateway_dot_requests_dot_AddressSuggestionRequest__pb2.AddressSuggestionRequest.SerializeToString,
        response_deserializer=gateway_dot_responses_dot_AddressSuggestionResponse__pb2.AddressSuggestionResponse.FromString,
        )
    self.geocoding = channel.unary_unary(
        '/fkhp.gateway.layer.client.FlipMapService/geocoding',
        request_serializer=gateway_dot_requests_dot_GeocodingRequest__pb2.GeocodingRequest.SerializeToString,
        response_deserializer=gateway_dot_responses_dot_GeocodingResponse__pb2.GeocodingResponse.FromString,
        )


class FlipMapServiceServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def reverseGeocoding(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def addressSuggestion(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def geocoding(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_FlipMapServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'reverseGeocoding': grpc.unary_unary_rpc_method_handler(
          servicer.reverseGeocoding,
          request_deserializer=gateway_dot_requests_dot_AddressFromLocationPointRequest__pb2.AddressFromLocationPointRequest.FromString,
          response_serializer=gateway_dot_responses_dot_AddressFromLocationPointResponse__pb2.AddressFromLocationPointResponse.SerializeToString,
      ),
      'addressSuggestion': grpc.unary_unary_rpc_method_handler(
          servicer.addressSuggestion,
          request_deserializer=gateway_dot_requests_dot_AddressSuggestionRequest__pb2.AddressSuggestionRequest.FromString,
          response_serializer=gateway_dot_responses_dot_AddressSuggestionResponse__pb2.AddressSuggestionResponse.SerializeToString,
      ),
      'geocoding': grpc.unary_unary_rpc_method_handler(
          servicer.geocoding,
          request_deserializer=gateway_dot_requests_dot_GeocodingRequest__pb2.GeocodingRequest.FromString,
          response_serializer=gateway_dot_responses_dot_GeocodingResponse__pb2.GeocodingResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'fkhp.gateway.layer.client.FlipMapService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
