# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: page/models/element/PaginationContext.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='page/models/element/PaginationContext.proto',
  package='fkhp.page.layer.models.element',
  syntax='proto3',
  serialized_options=_b('\n\036fkhp.page.layer.models.elementP\001'),
  serialized_pb=_b('\n+page/models/element/PaginationContext.proto\x12\x1e\x66khp.page.layer.models.element\"\\\n\x11PaginationContext\x12\x19\n\x11searchResultsSize\x18\x01 \x01(\x05\x12\x1b\n\x13searchResultsOffset\x18\x02 \x01(\x05\x12\x0f\n\x07hasMore\x18\x03 \x01(\x08\x42\"\n\x1e\x66khp.page.layer.models.elementP\x01\x62\x06proto3')
)




_PAGINATIONCONTEXT = _descriptor.Descriptor(
  name='PaginationContext',
  full_name='fkhp.page.layer.models.element.PaginationContext',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='searchResultsSize', full_name='fkhp.page.layer.models.element.PaginationContext.searchResultsSize', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='searchResultsOffset', full_name='fkhp.page.layer.models.element.PaginationContext.searchResultsOffset', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='hasMore', full_name='fkhp.page.layer.models.element.PaginationContext.hasMore', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=79,
  serialized_end=171,
)

DESCRIPTOR.message_types_by_name['PaginationContext'] = _PAGINATIONCONTEXT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PaginationContext = _reflection.GeneratedProtocolMessageType('PaginationContext', (_message.Message,), dict(
  DESCRIPTOR = _PAGINATIONCONTEXT,
  __module__ = 'page.models.element.PaginationContext_pb2'
  # @@protoc_insertion_point(class_scope:fkhp.page.layer.models.element.PaginationContext)
  ))
_sym_db.RegisterMessage(PaginationContext)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
