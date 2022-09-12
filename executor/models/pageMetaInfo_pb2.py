# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: executor/models/pageMetaInfo.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='executor/models/pageMetaInfo.proto',
  package='fkhp.data.layer.executor.models',
  syntax='proto3',
  serialized_options=_b('\n\037fkhp.data.layer.executor.modelsP\001'),
  serialized_pb=_b('\n\"executor/models/pageMetaInfo.proto\x12\x1f\x66khp.data.layer.executor.models\"h\n\x0cPageMetaInfo\x12\x12\n\npageNumber\x18\x01 \x01(\t\x12\x13\n\x0bhasMorePage\x18\x02 \x01(\x08\x12\x18\n\x10numberOfListings\x18\x03 \x01(\t\x12\x15\n\rtotalListings\x18\x04 \x01(\tB#\n\x1f\x66khp.data.layer.executor.modelsP\x01\x62\x06proto3')
)




_PAGEMETAINFO = _descriptor.Descriptor(
  name='PageMetaInfo',
  full_name='fkhp.data.layer.executor.models.PageMetaInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='pageNumber', full_name='fkhp.data.layer.executor.models.PageMetaInfo.pageNumber', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='hasMorePage', full_name='fkhp.data.layer.executor.models.PageMetaInfo.hasMorePage', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='numberOfListings', full_name='fkhp.data.layer.executor.models.PageMetaInfo.numberOfListings', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='totalListings', full_name='fkhp.data.layer.executor.models.PageMetaInfo.totalListings', index=3,
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
  serialized_start=71,
  serialized_end=175,
)

DESCRIPTOR.message_types_by_name['PageMetaInfo'] = _PAGEMETAINFO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PageMetaInfo = _reflection.GeneratedProtocolMessageType('PageMetaInfo', (_message.Message,), dict(
  DESCRIPTOR = _PAGEMETAINFO,
  __module__ = 'executor.models.pageMetaInfo_pb2'
  # @@protoc_insertion_point(class_scope:fkhp.data.layer.executor.models.PageMetaInfo)
  ))
_sym_db.RegisterMessage(PageMetaInfo)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)