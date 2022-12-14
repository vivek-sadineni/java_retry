# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: executor/response/PreWalletInfoViewResponse.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from executor.models import statusInfo_pb2 as executor_dot_models_dot_statusInfo__pb2
from executor.models import walletType_pb2 as executor_dot_models_dot_walletType__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='executor/response/PreWalletInfoViewResponse.proto',
  package='fkhp.data.layer.executor.response',
  syntax='proto3',
  serialized_options=_b('\n!fkhp.data.layer.executor.responseP\001'),
  serialized_pb=_b('\n1executor/response/PreWalletInfoViewResponse.proto\x12!fkhp.data.layer.executor.response\x1a executor/models/statusInfo.proto\x1a executor/models/walletType.proto\"\xa5\x01\n\x19PreWalletInfoViewResponse\x12?\n\nstatusInfo\x18\x01 \x01(\x0b\x32+.fkhp.data.layer.executor.models.StatusInfo\x12G\n\rpreWalletInfo\x18\x02 \x03(\x0b\x32\x30.fkhp.data.layer.executor.response.PreWalletInfo\"y\n\rPreWalletInfo\x12\x10\n\x08imageUrl\x18\x01 \x01(\t\x12\x15\n\rwalletBalance\x18\x02 \x01(\t\x12?\n\nwalletType\x18\x03 \x01(\x0e\x32+.fkhp.data.layer.executor.models.WalletTypeB%\n!fkhp.data.layer.executor.responseP\x01\x62\x06proto3')
  ,
  dependencies=[executor_dot_models_dot_statusInfo__pb2.DESCRIPTOR,executor_dot_models_dot_walletType__pb2.DESCRIPTOR,])




_PREWALLETINFOVIEWRESPONSE = _descriptor.Descriptor(
  name='PreWalletInfoViewResponse',
  full_name='fkhp.data.layer.executor.response.PreWalletInfoViewResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='statusInfo', full_name='fkhp.data.layer.executor.response.PreWalletInfoViewResponse.statusInfo', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='preWalletInfo', full_name='fkhp.data.layer.executor.response.PreWalletInfoViewResponse.preWalletInfo', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=157,
  serialized_end=322,
)


_PREWALLETINFO = _descriptor.Descriptor(
  name='PreWalletInfo',
  full_name='fkhp.data.layer.executor.response.PreWalletInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='imageUrl', full_name='fkhp.data.layer.executor.response.PreWalletInfo.imageUrl', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='walletBalance', full_name='fkhp.data.layer.executor.response.PreWalletInfo.walletBalance', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='walletType', full_name='fkhp.data.layer.executor.response.PreWalletInfo.walletType', index=2,
      number=3, type=14, cpp_type=8, label=1,
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
  serialized_start=324,
  serialized_end=445,
)

_PREWALLETINFOVIEWRESPONSE.fields_by_name['statusInfo'].message_type = executor_dot_models_dot_statusInfo__pb2._STATUSINFO
_PREWALLETINFOVIEWRESPONSE.fields_by_name['preWalletInfo'].message_type = _PREWALLETINFO
_PREWALLETINFO.fields_by_name['walletType'].enum_type = executor_dot_models_dot_walletType__pb2._WALLETTYPE
DESCRIPTOR.message_types_by_name['PreWalletInfoViewResponse'] = _PREWALLETINFOVIEWRESPONSE
DESCRIPTOR.message_types_by_name['PreWalletInfo'] = _PREWALLETINFO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PreWalletInfoViewResponse = _reflection.GeneratedProtocolMessageType('PreWalletInfoViewResponse', (_message.Message,), dict(
  DESCRIPTOR = _PREWALLETINFOVIEWRESPONSE,
  __module__ = 'executor.response.PreWalletInfoViewResponse_pb2'
  # @@protoc_insertion_point(class_scope:fkhp.data.layer.executor.response.PreWalletInfoViewResponse)
  ))
_sym_db.RegisterMessage(PreWalletInfoViewResponse)

PreWalletInfo = _reflection.GeneratedProtocolMessageType('PreWalletInfo', (_message.Message,), dict(
  DESCRIPTOR = _PREWALLETINFO,
  __module__ = 'executor.response.PreWalletInfoViewResponse_pb2'
  # @@protoc_insertion_point(class_scope:fkhp.data.layer.executor.response.PreWalletInfo)
  ))
_sym_db.RegisterMessage(PreWalletInfo)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
