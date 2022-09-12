# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: page/models/section/PageSectionTemplate.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from page.models.design import DesignModel_pb2 as page_dot_models_dot_design_dot_DesignModel__pb2
from page.models.component import UIComponentTemplate_pb2 as page_dot_models_dot_component_dot_UIComponentTemplate__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='page/models/section/PageSectionTemplate.proto',
  package='fkhp.page.layer.models.section',
  syntax='proto3',
  serialized_options=_b('\n\036fkhp.page.layer.models.sectionP\001'),
  serialized_pb=_b('\n-page/models/section/PageSectionTemplate.proto\x12\x1e\x66khp.page.layer.models.section\x1a$page/models/design/DesignModel.proto\x1a/page/models/component/UIComponentTemplate.proto\"\xd9\x01\n\x13PageSectionTemplate\x12\x11\n\tsectionId\x18\x01 \x01(\t\x12\r\n\x05order\x18\x02 \x01(\x05\x12\x13\n\x0bsectionType\x18\x03 \x01(\t\x12?\n\x0b\x64\x65signModel\x18\x04 \x01(\x0b\x32*.fkhp.page.layer.models.design.DesignModel\x12J\n\x0buiComponent\x18\x05 \x03(\x0b\x32\x35.fkhp.page.layer.models.component.UIComponentTemplateB\"\n\x1e\x66khp.page.layer.models.sectionP\x01\x62\x06proto3')
  ,
  dependencies=[page_dot_models_dot_design_dot_DesignModel__pb2.DESCRIPTOR,page_dot_models_dot_component_dot_UIComponentTemplate__pb2.DESCRIPTOR,])




_PAGESECTIONTEMPLATE = _descriptor.Descriptor(
  name='PageSectionTemplate',
  full_name='fkhp.page.layer.models.section.PageSectionTemplate',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='sectionId', full_name='fkhp.page.layer.models.section.PageSectionTemplate.sectionId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='order', full_name='fkhp.page.layer.models.section.PageSectionTemplate.order', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sectionType', full_name='fkhp.page.layer.models.section.PageSectionTemplate.sectionType', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='designModel', full_name='fkhp.page.layer.models.section.PageSectionTemplate.designModel', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='uiComponent', full_name='fkhp.page.layer.models.section.PageSectionTemplate.uiComponent', index=4,
      number=5, type=11, cpp_type=10, label=3,
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
  serialized_start=169,
  serialized_end=386,
)

_PAGESECTIONTEMPLATE.fields_by_name['designModel'].message_type = page_dot_models_dot_design_dot_DesignModel__pb2._DESIGNMODEL
_PAGESECTIONTEMPLATE.fields_by_name['uiComponent'].message_type = page_dot_models_dot_component_dot_UIComponentTemplate__pb2._UICOMPONENTTEMPLATE
DESCRIPTOR.message_types_by_name['PageSectionTemplate'] = _PAGESECTIONTEMPLATE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PageSectionTemplate = _reflection.GeneratedProtocolMessageType('PageSectionTemplate', (_message.Message,), dict(
  DESCRIPTOR = _PAGESECTIONTEMPLATE,
  __module__ = 'page.models.section.PageSectionTemplate_pb2'
  # @@protoc_insertion_point(class_scope:fkhp.page.layer.models.section.PageSectionTemplate)
  ))
_sym_db.RegisterMessage(PageSectionTemplate)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
