# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: executor/models/errorMessage.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='executor/models/errorMessage.proto',
  package='fkhp.data.layer.executor.models',
  syntax='proto3',
  serialized_options=_b('\n\037fkhp.data.layer.executor.modelsP\001'),
  serialized_pb=_b('\n\"executor/models/errorMessage.proto\x12\x1f\x66khp.data.layer.executor.models\"2\n\x0c\x45rrorMessage\x12\x0f\n\x07message\x18\x01 \x01(\t\x12\x11\n\terrorCode\x18\x02 \x01(\tB#\n\x1f\x66khp.data.layer.executor.modelsP\x01\x62\x06proto3')
)




_ERRORMESSAGE = _descriptor.Descriptor(
  name='ErrorMessage',
  full_name='fkhp.data.layer.executor.models.ErrorMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='fkhp.data.layer.executor.models.ErrorMessage.message', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='errorCode', full_name='fkhp.data.layer.executor.models.ErrorMessage.errorCode', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_start=71,
  serialized_end=121,
)

DESCRIPTOR.message_types_by_name['ErrorMessage'] = _ERRORMESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ErrorMessage = _reflection.GeneratedProtocolMessageType('ErrorMessage', (_message.Message,), dict(
  DESCRIPTOR = _ERRORMESSAGE,
  __module__ = 'executor.models.errorMessage_pb2'
  # @@protoc_insertion_point(class_scope:fkhp.data.layer.executor.models.ErrorMessage)
  ))
_sym_db.RegisterMessage(ErrorMessage)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
