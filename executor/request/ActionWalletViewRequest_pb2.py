# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: executor/request/ActionWalletViewRequest.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from executor.models import requestMetaInfo_pb2 as executor_dot_models_dot_requestMetaInfo__pb2
from executor.models import walletType_pb2 as executor_dot_models_dot_walletType__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='executor/request/ActionWalletViewRequest.proto',
  package='fkhp.data.layer.executor.request',
  syntax='proto3',
  serialized_options=_b('\n fkhp.data.layer.executor.requestP\001'),
  serialized_pb=_b('\n.executor/request/ActionWalletViewRequest.proto\x12 fkhp.data.layer.executor.request\x1a%executor/models/requestMetaInfo.proto\x1a executor/models/walletType.proto\"\xb1\x02\n\x17\x41\x63tionWalletViewRequest\x12I\n\x0frequestMetaInfo\x18\x01 \x01(\x0b\x32\x30.fkhp.data.layer.executor.models.RequestMetaInfo\x12\x14\n\x0cmobileNumber\x18\x02 \x01(\t\x12\x42\n\x0brequestType\x18\x03 \x01(\x0e\x32-.fkhp.data.layer.executor.request.RequestType\x12\x0b\n\x03otp\x18\x04 \x01(\t\x12\r\n\x05state\x18\x05 \x01(\t\x12\x14\n\x0cwalletAmount\x18\x06 \x01(\t\x12?\n\nwalletType\x18\x07 \x01(\x0e\x32+.fkhp.data.layer.executor.models.WalletType*P\n\x0bRequestType\x12\x0c\n\x08SEND_OTP\x10\x00\x12\x10\n\x0cLINK_ACCOUNT\x10\x01\x12\x12\n\x0eUNLINK_ACCOUNT\x10\x02\x12\r\n\tADD_MONEY\x10\x03\x42$\n fkhp.data.layer.executor.requestP\x01\x62\x06proto3')
  ,
  dependencies=[executor_dot_models_dot_requestMetaInfo__pb2.DESCRIPTOR,executor_dot_models_dot_walletType__pb2.DESCRIPTOR,])

_REQUESTTYPE = _descriptor.EnumDescriptor(
  name='RequestType',
  full_name='fkhp.data.layer.executor.request.RequestType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='SEND_OTP', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LINK_ACCOUNT', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UNLINK_ACCOUNT', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ADD_MONEY', index=3, number=3,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=465,
  serialized_end=545,
)
_sym_db.RegisterEnumDescriptor(_REQUESTTYPE)

RequestType = enum_type_wrapper.EnumTypeWrapper(_REQUESTTYPE)
SEND_OTP = 0
LINK_ACCOUNT = 1
UNLINK_ACCOUNT = 2
ADD_MONEY = 3



_ACTIONWALLETVIEWREQUEST = _descriptor.Descriptor(
  name='ActionWalletViewRequest',
  full_name='fkhp.data.layer.executor.request.ActionWalletViewRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='requestMetaInfo', full_name='fkhp.data.layer.executor.request.ActionWalletViewRequest.requestMetaInfo', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='mobileNumber', full_name='fkhp.data.layer.executor.request.ActionWalletViewRequest.mobileNumber', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='requestType', full_name='fkhp.data.layer.executor.request.ActionWalletViewRequest.requestType', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='otp', full_name='fkhp.data.layer.executor.request.ActionWalletViewRequest.otp', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='state', full_name='fkhp.data.layer.executor.request.ActionWalletViewRequest.state', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='walletAmount', full_name='fkhp.data.layer.executor.request.ActionWalletViewRequest.walletAmount', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='walletType', full_name='fkhp.data.layer.executor.request.ActionWalletViewRequest.walletType', index=6,
      number=7, type=14, cpp_type=8, label=1,
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
  serialized_end=463,
)

_ACTIONWALLETVIEWREQUEST.fields_by_name['requestMetaInfo'].message_type = executor_dot_models_dot_requestMetaInfo__pb2._REQUESTMETAINFO
_ACTIONWALLETVIEWREQUEST.fields_by_name['requestType'].enum_type = _REQUESTTYPE
_ACTIONWALLETVIEWREQUEST.fields_by_name['walletType'].enum_type = executor_dot_models_dot_walletType__pb2._WALLETTYPE
DESCRIPTOR.message_types_by_name['ActionWalletViewRequest'] = _ACTIONWALLETVIEWREQUEST
DESCRIPTOR.enum_types_by_name['RequestType'] = _REQUESTTYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ActionWalletViewRequest = _reflection.GeneratedProtocolMessageType('ActionWalletViewRequest', (_message.Message,), dict(
  DESCRIPTOR = _ACTIONWALLETVIEWREQUEST,
  __module__ = 'executor.request.ActionWalletViewRequest_pb2'
  # @@protoc_insertion_point(class_scope:fkhp.data.layer.executor.request.ActionWalletViewRequest)
  ))
_sym_db.RegisterMessage(ActionWalletViewRequest)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)