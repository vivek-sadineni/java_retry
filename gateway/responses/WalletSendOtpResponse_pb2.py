# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: gateway/responses/WalletSendOtpResponse.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from executor.response import WalletSendOtpViewResponse_pb2 as executor_dot_response_dot_WalletSendOtpViewResponse__pb2
from gateway.models import HeaderValue_pb2 as gateway_dot_models_dot_HeaderValue__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='gateway/responses/WalletSendOtpResponse.proto',
  package='fkhp.gateway.layer.client.response',
  syntax='proto3',
  serialized_options=_b('\n\"fkhp.gateway.layer.client.responseP\001'),
  serialized_pb=_b('\n-gateway/responses/WalletSendOtpResponse.proto\x12\"fkhp.gateway.layer.client.response\x1a\x31\x65xecutor/response/WalletSendOtpViewResponse.proto\x1a gateway/models/HeaderValue.proto\"\xa2\x02\n\x15WalletSendOtpResponse\x12N\n\x08response\x18\x01 \x01(\x0b\x32<.fkhp.data.layer.executor.response.WalletSendOtpViewResponse\x12Y\n\x08metadata\x18\x02 \x03(\x0b\x32G.fkhp.gateway.layer.client.response.WalletSendOtpResponse.MetadataEntry\x1a^\n\rMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12<\n\x05value\x18\x02 \x01(\x0b\x32-.fkhp.gateway.layer.client.models.HeaderValue:\x02\x38\x01\x42&\n\"fkhp.gateway.layer.client.responseP\x01\x62\x06proto3')
  ,
  dependencies=[executor_dot_response_dot_WalletSendOtpViewResponse__pb2.DESCRIPTOR,gateway_dot_models_dot_HeaderValue__pb2.DESCRIPTOR,])




_WALLETSENDOTPRESPONSE_METADATAENTRY = _descriptor.Descriptor(
  name='MetadataEntry',
  full_name='fkhp.gateway.layer.client.response.WalletSendOtpResponse.MetadataEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='fkhp.gateway.layer.client.response.WalletSendOtpResponse.MetadataEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='fkhp.gateway.layer.client.response.WalletSendOtpResponse.MetadataEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=367,
  serialized_end=461,
)

_WALLETSENDOTPRESPONSE = _descriptor.Descriptor(
  name='WalletSendOtpResponse',
  full_name='fkhp.gateway.layer.client.response.WalletSendOtpResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='response', full_name='fkhp.gateway.layer.client.response.WalletSendOtpResponse.response', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='metadata', full_name='fkhp.gateway.layer.client.response.WalletSendOtpResponse.metadata', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_WALLETSENDOTPRESPONSE_METADATAENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=171,
  serialized_end=461,
)

_WALLETSENDOTPRESPONSE_METADATAENTRY.fields_by_name['value'].message_type = gateway_dot_models_dot_HeaderValue__pb2._HEADERVALUE
_WALLETSENDOTPRESPONSE_METADATAENTRY.containing_type = _WALLETSENDOTPRESPONSE
_WALLETSENDOTPRESPONSE.fields_by_name['response'].message_type = executor_dot_response_dot_WalletSendOtpViewResponse__pb2._WALLETSENDOTPVIEWRESPONSE
_WALLETSENDOTPRESPONSE.fields_by_name['metadata'].message_type = _WALLETSENDOTPRESPONSE_METADATAENTRY
DESCRIPTOR.message_types_by_name['WalletSendOtpResponse'] = _WALLETSENDOTPRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

WalletSendOtpResponse = _reflection.GeneratedProtocolMessageType('WalletSendOtpResponse', (_message.Message,), dict(

  MetadataEntry = _reflection.GeneratedProtocolMessageType('MetadataEntry', (_message.Message,), dict(
    DESCRIPTOR = _WALLETSENDOTPRESPONSE_METADATAENTRY,
    __module__ = 'gateway.responses.WalletSendOtpResponse_pb2'
    # @@protoc_insertion_point(class_scope:fkhp.gateway.layer.client.response.WalletSendOtpResponse.MetadataEntry)
    ))
  ,
  DESCRIPTOR = _WALLETSENDOTPRESPONSE,
  __module__ = 'gateway.responses.WalletSendOtpResponse_pb2'
  # @@protoc_insertion_point(class_scope:fkhp.gateway.layer.client.response.WalletSendOtpResponse)
  ))
_sym_db.RegisterMessage(WalletSendOtpResponse)
_sym_db.RegisterMessage(WalletSendOtpResponse.MetadataEntry)


DESCRIPTOR._options = None
_WALLETSENDOTPRESPONSE_METADATAENTRY._options = None
# @@protoc_insertion_point(module_scope)
