# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: executor/response/WalletAmountInfosViewResponse.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from executor.models import statusInfo_pb2 as executor_dot_models_dot_statusInfo__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='executor/response/WalletAmountInfosViewResponse.proto',
  package='fkhp.data.layer.executor.response',
  syntax='proto3',
  serialized_options=_b('\n!fkhp.data.layer.executor.responseP\001'),
  serialized_pb=_b('\n5executor/response/WalletAmountInfosViewResponse.proto\x12!fkhp.data.layer.executor.response\x1a executor/models/statusInfo.proto\"\x89\x01\n\x1dWalletAmountInfosViewResponse\x12?\n\nstatusInfo\x18\x01 \x01(\x0b\x32+.fkhp.data.layer.executor.models.StatusInfo\x12\x10\n\x08imageUrl\x18\x02 \x01(\t\x12\x15\n\rwalletBalance\x18\x03 \x01(\tB%\n!fkhp.data.layer.executor.responseP\x01\x62\x06proto3')
  ,
  dependencies=[executor_dot_models_dot_statusInfo__pb2.DESCRIPTOR,])




_WALLETAMOUNTINFOSVIEWRESPONSE = _descriptor.Descriptor(
  name='WalletAmountInfosViewResponse',
  full_name='fkhp.data.layer.executor.response.WalletAmountInfosViewResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='statusInfo', full_name='fkhp.data.layer.executor.response.WalletAmountInfosViewResponse.statusInfo', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='imageUrl', full_name='fkhp.data.layer.executor.response.WalletAmountInfosViewResponse.imageUrl', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='walletBalance', full_name='fkhp.data.layer.executor.response.WalletAmountInfosViewResponse.walletBalance', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=127,
  serialized_end=264,
)

_WALLETAMOUNTINFOSVIEWRESPONSE.fields_by_name['statusInfo'].message_type = executor_dot_models_dot_statusInfo__pb2._STATUSINFO
DESCRIPTOR.message_types_by_name['WalletAmountInfosViewResponse'] = _WALLETAMOUNTINFOSVIEWRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

WalletAmountInfosViewResponse = _reflection.GeneratedProtocolMessageType('WalletAmountInfosViewResponse', (_message.Message,), dict(
  DESCRIPTOR = _WALLETAMOUNTINFOSVIEWRESPONSE,
  __module__ = 'executor.response.WalletAmountInfosViewResponse_pb2'
  # @@protoc_insertion_point(class_scope:fkhp.data.layer.executor.response.WalletAmountInfosViewResponse)
  ))
_sym_db.RegisterMessage(WalletAmountInfosViewResponse)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
