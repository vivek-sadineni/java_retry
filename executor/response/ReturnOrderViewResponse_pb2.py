# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: executor/response/ReturnOrderViewResponse.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from executor.models import statusInfo_pb2 as executor_dot_models_dot_statusInfo__pb2
from executor.models import priceInfo_pb2 as executor_dot_models_dot_priceInfo__pb2
from executor.models import multiMediaInfo_pb2 as executor_dot_models_dot_multiMediaInfo__pb2
from executor.models import actionResponse_pb2 as executor_dot_models_dot_actionResponse__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='executor/response/ReturnOrderViewResponse.proto',
  package='fkhp.data.layer.executor.response',
  syntax='proto3',
  serialized_options=_b('\n!fkhp.data.layer.executor.responseP\001'),
  serialized_pb=_b('\n/executor/response/ReturnOrderViewResponse.proto\x12!fkhp.data.layer.executor.response\x1a executor/models/statusInfo.proto\x1a\x1f\x65xecutor/models/priceInfo.proto\x1a$executor/models/multiMediaInfo.proto\x1a$executor/models/actionResponse.proto\"\xaf\x01\n\x17ReturnOrderViewResponse\x12G\n\x0e\x61\x63tionResponse\x18\x01 \x01(\x0b\x32/.fkhp.data.layer.executor.models.ActionResponse\x12K\n\x0e\x64omainResponse\x18\x02 \x01(\x0b\x32\x33.fkhp.data.layer.executor.response.ReturnSubmitInfo\"l\n\x10ReturnSubmitInfo\x12\x15\n\rreturnMessage\x18\x01 \x01(\t\x12\x12\n\npickupDate\x18\x02 \x01(\t\x12\x14\n\x0crefundAmount\x18\x03 \x01(\x01\x12\x17\n\x0f\x63ustomerAddress\x18\x04 \x01(\tB%\n!fkhp.data.layer.executor.responseP\x01\x62\x06proto3')
  ,
  dependencies=[executor_dot_models_dot_statusInfo__pb2.DESCRIPTOR,executor_dot_models_dot_priceInfo__pb2.DESCRIPTOR,executor_dot_models_dot_multiMediaInfo__pb2.DESCRIPTOR,executor_dot_models_dot_actionResponse__pb2.DESCRIPTOR,])




_RETURNORDERVIEWRESPONSE = _descriptor.Descriptor(
  name='ReturnOrderViewResponse',
  full_name='fkhp.data.layer.executor.response.ReturnOrderViewResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='actionResponse', full_name='fkhp.data.layer.executor.response.ReturnOrderViewResponse.actionResponse', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='domainResponse', full_name='fkhp.data.layer.executor.response.ReturnOrderViewResponse.domainResponse', index=1,
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
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=230,
  serialized_end=405,
)


_RETURNSUBMITINFO = _descriptor.Descriptor(
  name='ReturnSubmitInfo',
  full_name='fkhp.data.layer.executor.response.ReturnSubmitInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='returnMessage', full_name='fkhp.data.layer.executor.response.ReturnSubmitInfo.returnMessage', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pickupDate', full_name='fkhp.data.layer.executor.response.ReturnSubmitInfo.pickupDate', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='refundAmount', full_name='fkhp.data.layer.executor.response.ReturnSubmitInfo.refundAmount', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='customerAddress', full_name='fkhp.data.layer.executor.response.ReturnSubmitInfo.customerAddress', index=3,
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
  serialized_start=407,
  serialized_end=515,
)

_RETURNORDERVIEWRESPONSE.fields_by_name['actionResponse'].message_type = executor_dot_models_dot_actionResponse__pb2._ACTIONRESPONSE
_RETURNORDERVIEWRESPONSE.fields_by_name['domainResponse'].message_type = _RETURNSUBMITINFO
DESCRIPTOR.message_types_by_name['ReturnOrderViewResponse'] = _RETURNORDERVIEWRESPONSE
DESCRIPTOR.message_types_by_name['ReturnSubmitInfo'] = _RETURNSUBMITINFO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ReturnOrderViewResponse = _reflection.GeneratedProtocolMessageType('ReturnOrderViewResponse', (_message.Message,), dict(
  DESCRIPTOR = _RETURNORDERVIEWRESPONSE,
  __module__ = 'executor.response.ReturnOrderViewResponse_pb2'
  # @@protoc_insertion_point(class_scope:fkhp.data.layer.executor.response.ReturnOrderViewResponse)
  ))
_sym_db.RegisterMessage(ReturnOrderViewResponse)

ReturnSubmitInfo = _reflection.GeneratedProtocolMessageType('ReturnSubmitInfo', (_message.Message,), dict(
  DESCRIPTOR = _RETURNSUBMITINFO,
  __module__ = 'executor.response.ReturnOrderViewResponse_pb2'
  # @@protoc_insertion_point(class_scope:fkhp.data.layer.executor.response.ReturnSubmitInfo)
  ))
_sym_db.RegisterMessage(ReturnSubmitInfo)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
