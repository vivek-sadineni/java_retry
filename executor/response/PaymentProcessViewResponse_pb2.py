# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: executor/response/PaymentProcessViewResponse.proto

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
  name='executor/response/PaymentProcessViewResponse.proto',
  package='fkhp.data.layer.executor.response',
  syntax='proto3',
  serialized_options=_b('\n!fkhp.data.layer.executor.responseP\001'),
  serialized_pb=_b('\n2executor/response/PaymentProcessViewResponse.proto\x12!fkhp.data.layer.executor.response\x1a executor/models/statusInfo.proto\x1a\x1c\x65xecutor/models/pgInfo.proto\x1a\x1e\x65xecutor/models/bankInfo.proto\"\xbf\x01\n\x1aPaymentProcessViewResponse\x12?\n\nstatusInfo\x18\x01 \x01(\x0b\x32+.fkhp.data.layer.executor.models.StatusInfo\x12\x13\n\x0btotalAmount\x18\x02 \x01(\t\x12\x13\n\x0b\x63\x61llbackUrl\x18\x03 \x01(\t\x12\x0b\n\x03mid\x18\x04 \x01(\t\x12\x0f\n\x07orderId\x18\x05 \x01(\t\x12\x18\n\x10transactionToken\x18\x06 \x01(\tB%\n!fkhp.data.layer.executor.responseP\x01\x62\x06proto3')
  ,
  dependencies=[executor_dot_models_dot_statusInfo__pb2.DESCRIPTOR,executor_dot_models_dot_pgInfo__pb2.DESCRIPTOR,executor_dot_models_dot_bankInfo__pb2.DESCRIPTOR,])




_PAYMENTPROCESSVIEWRESPONSE = _descriptor.Descriptor(
  name='PaymentProcessViewResponse',
  full_name='fkhp.data.layer.executor.response.PaymentProcessViewResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='statusInfo', full_name='fkhp.data.layer.executor.response.PaymentProcessViewResponse.statusInfo', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='totalAmount', full_name='fkhp.data.layer.executor.response.PaymentProcessViewResponse.totalAmount', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='callbackUrl', full_name='fkhp.data.layer.executor.response.PaymentProcessViewResponse.callbackUrl', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='mid', full_name='fkhp.data.layer.executor.response.PaymentProcessViewResponse.mid', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='orderId', full_name='fkhp.data.layer.executor.response.PaymentProcessViewResponse.orderId', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='transactionToken', full_name='fkhp.data.layer.executor.response.PaymentProcessViewResponse.transactionToken', index=5,
      number=6, type=9, cpp_type=9, label=1,
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
  serialized_start=186,
  serialized_end=377,
)

_PAYMENTPROCESSVIEWRESPONSE.fields_by_name['statusInfo'].message_type = executor_dot_models_dot_statusInfo__pb2._STATUSINFO
DESCRIPTOR.message_types_by_name['PaymentProcessViewResponse'] = _PAYMENTPROCESSVIEWRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PaymentProcessViewResponse = _reflection.GeneratedProtocolMessageType('PaymentProcessViewResponse', (_message.Message,), dict(
  DESCRIPTOR = _PAYMENTPROCESSVIEWRESPONSE,
  __module__ = 'executor.response.PaymentProcessViewResponse_pb2'
  # @@protoc_insertion_point(class_scope:fkhp.data.layer.executor.response.PaymentProcessViewResponse)
  ))
_sym_db.RegisterMessage(PaymentProcessViewResponse)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
