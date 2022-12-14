# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: gateway/clients/WalletService.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from gateway.requests import WalletAddMoneyRequest_pb2 as gateway_dot_requests_dot_WalletAddMoneyRequest__pb2
from gateway.requests import WalletLinkRequest_pb2 as gateway_dot_requests_dot_WalletLinkRequest__pb2
from gateway.requests import WalletSendOtpRequest_pb2 as gateway_dot_requests_dot_WalletSendOtpRequest__pb2
from gateway.requests import WalletUnlinkRequest_pb2 as gateway_dot_requests_dot_WalletUnlinkRequest__pb2
from gateway.requests import PreWalletInfoRequest_pb2 as gateway_dot_requests_dot_PreWalletInfoRequest__pb2
from gateway.requests import WalletHistoryRequest_pb2 as gateway_dot_requests_dot_WalletHistoryRequest__pb2
from gateway.responses import WalletAddMoneyResponse_pb2 as gateway_dot_responses_dot_WalletAddMoneyResponse__pb2
from gateway.responses import WalletLinkResponse_pb2 as gateway_dot_responses_dot_WalletLinkResponse__pb2
from gateway.responses import WalletSendOtpResponse_pb2 as gateway_dot_responses_dot_WalletSendOtpResponse__pb2
from gateway.responses import WalletUnlinkResponse_pb2 as gateway_dot_responses_dot_WalletUnlinkResponse__pb2
from gateway.responses import PreWalletInfoResponse_pb2 as gateway_dot_responses_dot_PreWalletInfoResponse__pb2
from gateway.responses import WalletHistoryResponse_pb2 as gateway_dot_responses_dot_WalletHistoryResponse__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='gateway/clients/WalletService.proto',
  package='fkhp.gateway.layer.client',
  syntax='proto3',
  serialized_options=_b('\n\031fkhp.gateway.layer.clientP\001'),
  serialized_pb=_b('\n#gateway/clients/WalletService.proto\x12\x19\x66khp.gateway.layer.client\x1a,gateway/requests/WalletAddMoneyRequest.proto\x1a(gateway/requests/WalletLinkRequest.proto\x1a+gateway/requests/WalletSendOtpRequest.proto\x1a*gateway/requests/WalletUnlinkRequest.proto\x1a+gateway/requests/PreWalletInfoRequest.proto\x1a+gateway/requests/WalletHistoryRequest.proto\x1a.gateway/responses/WalletAddMoneyResponse.proto\x1a*gateway/responses/WalletLinkResponse.proto\x1a-gateway/responses/WalletSendOtpResponse.proto\x1a,gateway/responses/WalletUnlinkResponse.proto\x1a-gateway/responses/PreWalletInfoResponse.proto\x1a-gateway/responses/WalletHistoryResponse.proto2\xb4\x06\n\rWalletService\x12\x83\x01\n\x08\x61\x64\x64Money\x12\x39.fkhp.gateway.layer.client.requests.WalletAddMoneyRequest\x1a:.fkhp.gateway.layer.client.response.WalletAddMoneyResponse\"\x00\x12~\n\x0blinkAccount\x12\x35.fkhp.gateway.layer.client.requests.WalletLinkRequest\x1a\x36.fkhp.gateway.layer.client.response.WalletLinkResponse\"\x00\x12\x80\x01\n\x07sendOtp\x12\x38.fkhp.gateway.layer.client.requests.WalletSendOtpRequest\x1a\x39.fkhp.gateway.layer.client.response.WalletSendOtpResponse\"\x00\x12\x84\x01\n\runlinkAccount\x12\x37.fkhp.gateway.layer.client.requests.WalletUnlinkRequest\x1a\x38.fkhp.gateway.layer.client.response.WalletUnlinkResponse\"\x00\x12\x86\x01\n\rpreWalletInfo\x12\x38.fkhp.gateway.layer.client.requests.PreWalletInfoRequest\x1a\x39.fkhp.gateway.layer.client.response.PreWalletInfoResponse\"\x00\x12\x89\x01\n\x10getWalletHistory\x12\x38.fkhp.gateway.layer.client.requests.WalletHistoryRequest\x1a\x39.fkhp.gateway.layer.client.response.WalletHistoryResponse\"\x00\x42\x1d\n\x19\x66khp.gateway.layer.clientP\x01\x62\x06proto3')
  ,
  dependencies=[gateway_dot_requests_dot_WalletAddMoneyRequest__pb2.DESCRIPTOR,gateway_dot_requests_dot_WalletLinkRequest__pb2.DESCRIPTOR,gateway_dot_requests_dot_WalletSendOtpRequest__pb2.DESCRIPTOR,gateway_dot_requests_dot_WalletUnlinkRequest__pb2.DESCRIPTOR,gateway_dot_requests_dot_PreWalletInfoRequest__pb2.DESCRIPTOR,gateway_dot_requests_dot_WalletHistoryRequest__pb2.DESCRIPTOR,gateway_dot_responses_dot_WalletAddMoneyResponse__pb2.DESCRIPTOR,gateway_dot_responses_dot_WalletLinkResponse__pb2.DESCRIPTOR,gateway_dot_responses_dot_WalletSendOtpResponse__pb2.DESCRIPTOR,gateway_dot_responses_dot_WalletUnlinkResponse__pb2.DESCRIPTOR,gateway_dot_responses_dot_PreWalletInfoResponse__pb2.DESCRIPTOR,gateway_dot_responses_dot_WalletHistoryResponse__pb2.DESCRIPTOR,])



_sym_db.RegisterFileDescriptor(DESCRIPTOR)


DESCRIPTOR._options = None

_WALLETSERVICE = _descriptor.ServiceDescriptor(
  name='WalletService',
  full_name='fkhp.gateway.layer.client.WalletService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=613,
  serialized_end=1433,
  methods=[
  _descriptor.MethodDescriptor(
    name='addMoney',
    full_name='fkhp.gateway.layer.client.WalletService.addMoney',
    index=0,
    containing_service=None,
    input_type=gateway_dot_requests_dot_WalletAddMoneyRequest__pb2._WALLETADDMONEYREQUEST,
    output_type=gateway_dot_responses_dot_WalletAddMoneyResponse__pb2._WALLETADDMONEYRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='linkAccount',
    full_name='fkhp.gateway.layer.client.WalletService.linkAccount',
    index=1,
    containing_service=None,
    input_type=gateway_dot_requests_dot_WalletLinkRequest__pb2._WALLETLINKREQUEST,
    output_type=gateway_dot_responses_dot_WalletLinkResponse__pb2._WALLETLINKRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='sendOtp',
    full_name='fkhp.gateway.layer.client.WalletService.sendOtp',
    index=2,
    containing_service=None,
    input_type=gateway_dot_requests_dot_WalletSendOtpRequest__pb2._WALLETSENDOTPREQUEST,
    output_type=gateway_dot_responses_dot_WalletSendOtpResponse__pb2._WALLETSENDOTPRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='unlinkAccount',
    full_name='fkhp.gateway.layer.client.WalletService.unlinkAccount',
    index=3,
    containing_service=None,
    input_type=gateway_dot_requests_dot_WalletUnlinkRequest__pb2._WALLETUNLINKREQUEST,
    output_type=gateway_dot_responses_dot_WalletUnlinkResponse__pb2._WALLETUNLINKRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='preWalletInfo',
    full_name='fkhp.gateway.layer.client.WalletService.preWalletInfo',
    index=4,
    containing_service=None,
    input_type=gateway_dot_requests_dot_PreWalletInfoRequest__pb2._PREWALLETINFOREQUEST,
    output_type=gateway_dot_responses_dot_PreWalletInfoResponse__pb2._PREWALLETINFORESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='getWalletHistory',
    full_name='fkhp.gateway.layer.client.WalletService.getWalletHistory',
    index=5,
    containing_service=None,
    input_type=gateway_dot_requests_dot_WalletHistoryRequest__pb2._WALLETHISTORYREQUEST,
    output_type=gateway_dot_responses_dot_WalletHistoryResponse__pb2._WALLETHISTORYRESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_WALLETSERVICE)

DESCRIPTOR.services_by_name['WalletService'] = _WALLETSERVICE

# @@protoc_insertion_point(module_scope)
