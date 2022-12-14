# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: executor/response/PaymentGatewayViewResponse.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from executor.models import statusInfo_pb2 as executor_dot_models_dot_statusInfo__pb2
from executor.models import pgInfo_pb2 as executor_dot_models_dot_pgInfo__pb2
from executor.models import bankInfo_pb2 as executor_dot_models_dot_bankInfo__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='executor/response/PaymentGatewayViewResponse.proto',
  package='fkhp.data.layer.executor.response',
  syntax='proto3',
  serialized_options=_b('\n!fkhp.data.layer.executor.responseP\001'),
  serialized_pb=_b('\n2executor/response/PaymentGatewayViewResponse.proto\x12!fkhp.data.layer.executor.response\x1a executor/models/statusInfo.proto\x1a\x1c\x65xecutor/models/pgInfo.proto\x1a\x1e\x65xecutor/models/bankInfo.proto\"\xd5\x01\n\x1aPaymentGatewayViewResponse\x12?\n\nstatusInfo\x18\x01 \x01(\x0b\x32+.fkhp.data.layer.executor.models.StatusInfo\x12\x39\n\x06pgList\x18\x02 \x03(\x0b\x32).fkhp.data.layer.executor.response.PGList\x12;\n\x08\x62\x61nkInfo\x18\x03 \x03(\x0b\x32).fkhp.data.layer.executor.models.BankInfo\"x\n\x06PGList\x12\r\n\x05title\x18\x01 \x01(\t\x12\x10\n\x08subtitle\x18\x02 \x01(\t\x12;\n\npgInfoList\x18\x03 \x03(\x0b\x32\'.fkhp.data.layer.executor.models.PgInfo\x12\x10\n\x08viewType\x18\x04 \x01(\tB%\n!fkhp.data.layer.executor.responseP\x01\x62\x06proto3')
  ,
  dependencies=[executor_dot_models_dot_statusInfo__pb2.DESCRIPTOR,executor_dot_models_dot_pgInfo__pb2.DESCRIPTOR,executor_dot_models_dot_bankInfo__pb2.DESCRIPTOR,])




_PAYMENTGATEWAYVIEWRESPONSE = _descriptor.Descriptor(
  name='PaymentGatewayViewResponse',
  full_name='fkhp.data.layer.executor.response.PaymentGatewayViewResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='statusInfo', full_name='fkhp.data.layer.executor.response.PaymentGatewayViewResponse.statusInfo', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pgList', full_name='fkhp.data.layer.executor.response.PaymentGatewayViewResponse.pgList', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bankInfo', full_name='fkhp.data.layer.executor.response.PaymentGatewayViewResponse.bankInfo', index=2,
      number=3, type=11, cpp_type=10, label=3,
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
  serialized_start=186,
  serialized_end=399,
)


_PGLIST = _descriptor.Descriptor(
  name='PGList',
  full_name='fkhp.data.layer.executor.response.PGList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='title', full_name='fkhp.data.layer.executor.response.PGList.title', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='subtitle', full_name='fkhp.data.layer.executor.response.PGList.subtitle', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pgInfoList', full_name='fkhp.data.layer.executor.response.PGList.pgInfoList', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='viewType', full_name='fkhp.data.layer.executor.response.PGList.viewType', index=3,
      number=4, type=9, cpp_type=9, label=1,
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
  serialized_start=401,
  serialized_end=521,
)

_PAYMENTGATEWAYVIEWRESPONSE.fields_by_name['statusInfo'].message_type = executor_dot_models_dot_statusInfo__pb2._STATUSINFO
_PAYMENTGATEWAYVIEWRESPONSE.fields_by_name['pgList'].message_type = _PGLIST
_PAYMENTGATEWAYVIEWRESPONSE.fields_by_name['bankInfo'].message_type = executor_dot_models_dot_bankInfo__pb2._BANKINFO
_PGLIST.fields_by_name['pgInfoList'].message_type = executor_dot_models_dot_pgInfo__pb2._PGINFO
DESCRIPTOR.message_types_by_name['PaymentGatewayViewResponse'] = _PAYMENTGATEWAYVIEWRESPONSE
DESCRIPTOR.message_types_by_name['PGList'] = _PGLIST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PaymentGatewayViewResponse = _reflection.GeneratedProtocolMessageType('PaymentGatewayViewResponse', (_message.Message,), dict(
  DESCRIPTOR = _PAYMENTGATEWAYVIEWRESPONSE,
  __module__ = 'executor.response.PaymentGatewayViewResponse_pb2'
  # @@protoc_insertion_point(class_scope:fkhp.data.layer.executor.response.PaymentGatewayViewResponse)
  ))
_sym_db.RegisterMessage(PaymentGatewayViewResponse)

PGList = _reflection.GeneratedProtocolMessageType('PGList', (_message.Message,), dict(
  DESCRIPTOR = _PGLIST,
  __module__ = 'executor.response.PaymentGatewayViewResponse_pb2'
  # @@protoc_insertion_point(class_scope:fkhp.data.layer.executor.response.PGList)
  ))
_sym_db.RegisterMessage(PGList)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
