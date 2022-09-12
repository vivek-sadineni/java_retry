# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: page/models/page/pmp/PageModelVersion.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from page.models.enums import PageStatus_pb2 as page_dot_models_dot_enums_dot_PageStatus__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='page/models/page/pmp/PageModelVersion.proto',
  package='fkhp.page.layer.models.page.pmp',
  syntax='proto3',
  serialized_options=_b('\n\037fkhp.page.layer.models.page.pmpP\001'),
  serialized_pb=_b('\n+page/models/page/pmp/PageModelVersion.proto\x12\x1f\x66khp.page.layer.models.page.pmp\x1a\"page/models/enums/PageStatus.proto\"\xc8\x01\n\x10PageModelVersion\x12\x0f\n\x07version\x18\x01 \x01(\x05\x12\x11\n\tcreatedBy\x18\x02 \x01(\t\x12\x11\n\tcreatedAt\x18\x03 \x01(\t\x12\x11\n\tupdatedAt\x18\x04 \x01(\t\x12\x13\n\x0bpublishedAt\x18\x05 \x01(\t\x12<\n\npageStatus\x18\x06 \x01(\x0e\x32(.fkhp.page.layer.models.enums.PageStatus\x12\x17\n\x0fpageDescription\x18\x07 \x01(\tB#\n\x1f\x66khp.page.layer.models.page.pmpP\x01\x62\x06proto3')
  ,
  dependencies=[page_dot_models_dot_enums_dot_PageStatus__pb2.DESCRIPTOR,])




_PAGEMODELVERSION = _descriptor.Descriptor(
  name='PageModelVersion',
  full_name='fkhp.page.layer.models.page.pmp.PageModelVersion',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='version', full_name='fkhp.page.layer.models.page.pmp.PageModelVersion.version', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='createdBy', full_name='fkhp.page.layer.models.page.pmp.PageModelVersion.createdBy', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='createdAt', full_name='fkhp.page.layer.models.page.pmp.PageModelVersion.createdAt', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='updatedAt', full_name='fkhp.page.layer.models.page.pmp.PageModelVersion.updatedAt', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='publishedAt', full_name='fkhp.page.layer.models.page.pmp.PageModelVersion.publishedAt', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pageStatus', full_name='fkhp.page.layer.models.page.pmp.PageModelVersion.pageStatus', index=5,
      number=6, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pageDescription', full_name='fkhp.page.layer.models.page.pmp.PageModelVersion.pageDescription', index=6,
      number=7, type=9, cpp_type=9, label=1,
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
  serialized_start=117,
  serialized_end=317,
)

_PAGEMODELVERSION.fields_by_name['pageStatus'].enum_type = page_dot_models_dot_enums_dot_PageStatus__pb2._PAGESTATUS
DESCRIPTOR.message_types_by_name['PageModelVersion'] = _PAGEMODELVERSION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PageModelVersion = _reflection.GeneratedProtocolMessageType('PageModelVersion', (_message.Message,), dict(
  DESCRIPTOR = _PAGEMODELVERSION,
  __module__ = 'page.models.page.pmp.PageModelVersion_pb2'
  # @@protoc_insertion_point(class_scope:fkhp.page.layer.models.page.pmp.PageModelVersion)
  ))
_sym_db.RegisterMessage(PageModelVersion)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
