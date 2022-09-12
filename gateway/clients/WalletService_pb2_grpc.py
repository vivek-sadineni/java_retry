# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from gateway.requests import PreWalletInfoRequest_pb2 as gateway_dot_requests_dot_PreWalletInfoRequest__pb2
from gateway.requests import WalletAddMoneyRequest_pb2 as gateway_dot_requests_dot_WalletAddMoneyRequest__pb2
from gateway.requests import WalletHistoryRequest_pb2 as gateway_dot_requests_dot_WalletHistoryRequest__pb2
from gateway.requests import WalletLinkRequest_pb2 as gateway_dot_requests_dot_WalletLinkRequest__pb2
from gateway.requests import WalletSendOtpRequest_pb2 as gateway_dot_requests_dot_WalletSendOtpRequest__pb2
from gateway.requests import WalletUnlinkRequest_pb2 as gateway_dot_requests_dot_WalletUnlinkRequest__pb2
from gateway.responses import PreWalletInfoResponse_pb2 as gateway_dot_responses_dot_PreWalletInfoResponse__pb2
from gateway.responses import WalletAddMoneyResponse_pb2 as gateway_dot_responses_dot_WalletAddMoneyResponse__pb2
from gateway.responses import WalletHistoryResponse_pb2 as gateway_dot_responses_dot_WalletHistoryResponse__pb2
from gateway.responses import WalletLinkResponse_pb2 as gateway_dot_responses_dot_WalletLinkResponse__pb2
from gateway.responses import WalletSendOtpResponse_pb2 as gateway_dot_responses_dot_WalletSendOtpResponse__pb2
from gateway.responses import WalletUnlinkResponse_pb2 as gateway_dot_responses_dot_WalletUnlinkResponse__pb2


class WalletServiceStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.addMoney = channel.unary_unary(
        '/fkhp.gateway.layer.client.WalletService/addMoney',
        request_serializer=gateway_dot_requests_dot_WalletAddMoneyRequest__pb2.WalletAddMoneyRequest.SerializeToString,
        response_deserializer=gateway_dot_responses_dot_WalletAddMoneyResponse__pb2.WalletAddMoneyResponse.FromString,
        )
    self.linkAccount = channel.unary_unary(
        '/fkhp.gateway.layer.client.WalletService/linkAccount',
        request_serializer=gateway_dot_requests_dot_WalletLinkRequest__pb2.WalletLinkRequest.SerializeToString,
        response_deserializer=gateway_dot_responses_dot_WalletLinkResponse__pb2.WalletLinkResponse.FromString,
        )
    self.sendOtp = channel.unary_unary(
        '/fkhp.gateway.layer.client.WalletService/sendOtp',
        request_serializer=gateway_dot_requests_dot_WalletSendOtpRequest__pb2.WalletSendOtpRequest.SerializeToString,
        response_deserializer=gateway_dot_responses_dot_WalletSendOtpResponse__pb2.WalletSendOtpResponse.FromString,
        )
    self.unlinkAccount = channel.unary_unary(
        '/fkhp.gateway.layer.client.WalletService/unlinkAccount',
        request_serializer=gateway_dot_requests_dot_WalletUnlinkRequest__pb2.WalletUnlinkRequest.SerializeToString,
        response_deserializer=gateway_dot_responses_dot_WalletUnlinkResponse__pb2.WalletUnlinkResponse.FromString,
        )
    self.preWalletInfo = channel.unary_unary(
        '/fkhp.gateway.layer.client.WalletService/preWalletInfo',
        request_serializer=gateway_dot_requests_dot_PreWalletInfoRequest__pb2.PreWalletInfoRequest.SerializeToString,
        response_deserializer=gateway_dot_responses_dot_PreWalletInfoResponse__pb2.PreWalletInfoResponse.FromString,
        )
    self.getWalletHistory = channel.unary_unary(
        '/fkhp.gateway.layer.client.WalletService/getWalletHistory',
        request_serializer=gateway_dot_requests_dot_WalletHistoryRequest__pb2.WalletHistoryRequest.SerializeToString,
        response_deserializer=gateway_dot_responses_dot_WalletHistoryResponse__pb2.WalletHistoryResponse.FromString,
        )


class WalletServiceServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def addMoney(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def linkAccount(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def sendOtp(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def unlinkAccount(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def preWalletInfo(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def getWalletHistory(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_WalletServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'addMoney': grpc.unary_unary_rpc_method_handler(
          servicer.addMoney,
          request_deserializer=gateway_dot_requests_dot_WalletAddMoneyRequest__pb2.WalletAddMoneyRequest.FromString,
          response_serializer=gateway_dot_responses_dot_WalletAddMoneyResponse__pb2.WalletAddMoneyResponse.SerializeToString,
      ),
      'linkAccount': grpc.unary_unary_rpc_method_handler(
          servicer.linkAccount,
          request_deserializer=gateway_dot_requests_dot_WalletLinkRequest__pb2.WalletLinkRequest.FromString,
          response_serializer=gateway_dot_responses_dot_WalletLinkResponse__pb2.WalletLinkResponse.SerializeToString,
      ),
      'sendOtp': grpc.unary_unary_rpc_method_handler(
          servicer.sendOtp,
          request_deserializer=gateway_dot_requests_dot_WalletSendOtpRequest__pb2.WalletSendOtpRequest.FromString,
          response_serializer=gateway_dot_responses_dot_WalletSendOtpResponse__pb2.WalletSendOtpResponse.SerializeToString,
      ),
      'unlinkAccount': grpc.unary_unary_rpc_method_handler(
          servicer.unlinkAccount,
          request_deserializer=gateway_dot_requests_dot_WalletUnlinkRequest__pb2.WalletUnlinkRequest.FromString,
          response_serializer=gateway_dot_responses_dot_WalletUnlinkResponse__pb2.WalletUnlinkResponse.SerializeToString,
      ),
      'preWalletInfo': grpc.unary_unary_rpc_method_handler(
          servicer.preWalletInfo,
          request_deserializer=gateway_dot_requests_dot_PreWalletInfoRequest__pb2.PreWalletInfoRequest.FromString,
          response_serializer=gateway_dot_responses_dot_PreWalletInfoResponse__pb2.PreWalletInfoResponse.SerializeToString,
      ),
      'getWalletHistory': grpc.unary_unary_rpc_method_handler(
          servicer.getWalletHistory,
          request_deserializer=gateway_dot_requests_dot_WalletHistoryRequest__pb2.WalletHistoryRequest.FromString,
          response_serializer=gateway_dot_responses_dot_WalletHistoryResponse__pb2.WalletHistoryResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'fkhp.gateway.layer.client.WalletService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))