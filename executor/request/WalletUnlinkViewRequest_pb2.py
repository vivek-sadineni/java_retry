# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: executor/request/WalletUnlinkViewRequest.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from executor.models import requestMetaInfo_pb2 as executor_dot_models_dot_requestMetaInfo__pb2
from executor.models import walletType_pb2 as executor_dot_models_dot_walletType__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='executor/request/WalletUnlinkViewRequest.proto',
  package='fkhp.data.layer.executor.request',
  syntax='proto3',
  serialized_options=_b('\n fkhp.data.layer.executor.requestP\001'),
  serialized_pb=_b('\n.executor/request/WalletUnlinkViewRequest.proto\x12 fkhp.data.layer.executor.request\x1a%executor/models/requestMetaInfo.proto\x1a executor/models/walletType.proto\"\xbb\x01\n\x17WalletUnlinkViewRequest\x12I\n\x0frequestMetaInfo\x18\x01 \x01(\x0b\x32\x30.fkhp.data.layer.executor.models.RequestMetaInfo\x12\x14\n\x0cmobileNumber\x18\x02 \x01(\t\x12?\n\nwalletType\x18\x04 \x01(\x0e\x32+.fkhp.data.layer.executor.models.WalletTypeB$\n fkhp.data.layer.executor.requestP\x01\x62\x06proto3')
  ,
  dependencies=[executor_dot_models_dot_requestMetaInfo__pb2.DESCRIPTOR,executor_dot_models_dot_walletType__pb2.DESCRIPTOR,])




_WALLETUNLINKVIEWREQUEST = _descriptor.Descriptor(
  name='WalletUnlinkViewRequest',
  full_name='fkhp.data.layer.executor.request.WalletUnlinkViewRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='requestMetaInfo', full_name='fkhp.data.layer.executor.request.WalletUnlinkViewRequest.requestMetaInfo', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='mobileNumber', full_name='fkhp.data.layer.executor.request.WalletUnlinkViewRequest.mobileNumber', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='walletType', full_name='fkhp.data.layer.executor.request.WalletUnlinkViewRequest.walletType', index=2,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=158,
  serialized_end=345,
)

_WALLETUNLINKVIEWREQUEST.fields_by_name['requestMetaInfo'].message_type = executor_dot_models_dot_requestMetaInfo__pb2._REQUESTMETAINFO
_WALLETUNLINKVIEWREQUEST.fields_by_name['walletType'].enum_type = executor_dot_models_dot_walletType__pb2._WALLETTYPE
DESCRIPTOR.message_types_by_name['WalletUnlinkViewRequest'] = _WALLETUNLINKVIEWREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

WalletUnlinkViewRequest = _reflection.GeneratedProtocolMessageType('WalletUnlinkViewRequest', (_message.Message,), dict(
  DESCRIPTOR = _WALLETUNLINKVIEWREQUEST,
  __module__ = 'executor.request.WalletUnlinkViewRequest_pb2'
  # @@protoc_insertion_point(class_scope:fkhp.data.layer.executor.request.WalletUnlinkViewRequest)
  ))
_sym_db.RegisterMessage(WalletUnlinkViewRequest)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
