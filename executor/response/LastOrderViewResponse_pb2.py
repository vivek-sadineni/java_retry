# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: executor/response/LastOrderViewResponse.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from executor.models import actionResponse_pb2 as executor_dot_models_dot_actionResponse__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='executor/response/LastOrderViewResponse.proto',
  package='fkhp.data.layer.executor.response',
  syntax='proto3',
  serialized_options=_b('\n!fkhp.data.layer.executor.responseP\001'),
  serialized_pb=_b('\n-executor/response/LastOrderViewResponse.proto\x12!fkhp.data.layer.executor.response\x1a$executor/models/actionResponse.proto\"\xb4\x01\n\x15LastOrderViewResponse\x12G\n\x0e\x61\x63tionResponse\x18\x01 \x01(\x0b\x32/.fkhp.data.layer.executor.models.ActionResponse\x12R\n\x0e\x64omainResponse\x18\x02 \x01(\x0b\x32:.fkhp.data.layer.executor.response.LastOrderDomainResponse\"b\n\x17LastOrderDomainResponse\x12\r\n\x05title\x18\x02 \x01(\t\x12\x12\n\ndeliveryBy\x18\x03 \x01(\t\x12\x11\n\ttrackLink\x18\x04 \x01(\t\x12\x11\n\ttimeStamp\x18\x05 \x01(\tB%\n!fkhp.data.layer.executor.responseP\x01\x62\x06proto3')
  ,
  dependencies=[executor_dot_models_dot_actionResponse__pb2.DESCRIPTOR,])




_LASTORDERVIEWRESPONSE = _descriptor.Descriptor(
  name='LastOrderViewResponse',
  full_name='fkhp.data.layer.executor.response.LastOrderViewResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='actionResponse', full_name='fkhp.data.layer.executor.response.LastOrderViewResponse.actionResponse', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='domainResponse', full_name='fkhp.data.layer.executor.response.LastOrderViewResponse.domainResponse', index=1,
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
  serialized_start=123,
  serialized_end=303,
)


_LASTORDERDOMAINRESPONSE = _descriptor.Descriptor(
  name='LastOrderDomainResponse',
  full_name='fkhp.data.layer.executor.response.LastOrderDomainResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='title', full_name='fkhp.data.layer.executor.response.LastOrderDomainResponse.title', index=0,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='deliveryBy', full_name='fkhp.data.layer.executor.response.LastOrderDomainResponse.deliveryBy', index=1,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='trackLink', full_name='fkhp.data.layer.executor.response.LastOrderDomainResponse.trackLink', index=2,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timeStamp', full_name='fkhp.data.layer.executor.response.LastOrderDomainResponse.timeStamp', index=3,
      number=5, type=9, cpp_type=9, label=1,
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
  serialized_start=305,
  serialized_end=403,
)

_LASTORDERVIEWRESPONSE.fields_by_name['actionResponse'].message_type = executor_dot_models_dot_actionResponse__pb2._ACTIONRESPONSE
_LASTORDERVIEWRESPONSE.fields_by_name['domainResponse'].message_type = _LASTORDERDOMAINRESPONSE
DESCRIPTOR.message_types_by_name['LastOrderViewResponse'] = _LASTORDERVIEWRESPONSE
DESCRIPTOR.message_types_by_name['LastOrderDomainResponse'] = _LASTORDERDOMAINRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

LastOrderViewResponse = _reflection.GeneratedProtocolMessageType('LastOrderViewResponse', (_message.Message,), dict(
  DESCRIPTOR = _LASTORDERVIEWRESPONSE,
  __module__ = 'executor.response.LastOrderViewResponse_pb2'
  # @@protoc_insertion_point(class_scope:fkhp.data.layer.executor.response.LastOrderViewResponse)
  ))
_sym_db.RegisterMessage(LastOrderViewResponse)

LastOrderDomainResponse = _reflection.GeneratedProtocolMessageType('LastOrderDomainResponse', (_message.Message,), dict(
  DESCRIPTOR = _LASTORDERDOMAINRESPONSE,
  __module__ = 'executor.response.LastOrderViewResponse_pb2'
  # @@protoc_insertion_point(class_scope:fkhp.data.layer.executor.response.LastOrderDomainResponse)
  ))
_sym_db.RegisterMessage(LastOrderDomainResponse)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
