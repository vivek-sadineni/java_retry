# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: executor/request/AutoLoginViewRequest.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='executor/request/AutoLoginViewRequest.proto',
  package='fkhp.data.layer.executor.request',
  syntax='proto3',
  serialized_options=_b('\n fkhp.data.layer.executor.requestP\001'),
  serialized_pb=_b('\n+executor/request/AutoLoginViewRequest.proto\x12 fkhp.data.layer.executor.request\"u\n\x14\x41utoLoginViewRequest\x12\x10\n\x08mobileNo\x18\x01 \x01(\t\x12\x0f\n\x07\x65mailId\x18\x02 \x01(\t\x12\x11\n\tfirstName\x18\x03 \x01(\t\x12\x10\n\x08lastName\x18\x04 \x01(\t\x12\x15\n\ridentityToken\x18\x05 \x01(\tB$\n fkhp.data.layer.executor.requestP\x01\x62\x06proto3')
)




_AUTOLOGINVIEWREQUEST = _descriptor.Descriptor(
  name='AutoLoginViewRequest',
  full_name='fkhp.data.layer.executor.request.AutoLoginViewRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='mobileNo', full_name='fkhp.data.layer.executor.request.AutoLoginViewRequest.mobileNo', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='emailId', full_name='fkhp.data.layer.executor.request.AutoLoginViewRequest.emailId', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='firstName', full_name='fkhp.data.layer.executor.request.AutoLoginViewRequest.firstName', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='lastName', full_name='fkhp.data.layer.executor.request.AutoLoginViewRequest.lastName', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='identityToken', full_name='fkhp.data.layer.executor.request.AutoLoginViewRequest.identityToken', index=4,
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
  serialized_start=81,
  serialized_end=198,
)

DESCRIPTOR.message_types_by_name['AutoLoginViewRequest'] = _AUTOLOGINVIEWREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AutoLoginViewRequest = _reflection.GeneratedProtocolMessageType('AutoLoginViewRequest', (_message.Message,), dict(
  DESCRIPTOR = _AUTOLOGINVIEWREQUEST,
  __module__ = 'executor.request.AutoLoginViewRequest_pb2'
  # @@protoc_insertion_point(class_scope:fkhp.data.layer.executor.request.AutoLoginViewRequest)
  ))
_sym_db.RegisterMessage(AutoLoginViewRequest)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
