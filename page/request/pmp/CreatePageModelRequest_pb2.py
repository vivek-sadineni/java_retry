# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: page/request/pmp/CreatePageModelRequest.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from page.models.enums import PageType_pb2 as page_dot_models_dot_enums_dot_PageType__pb2
from page.models.design.pmp import DesignParameter_pb2 as page_dot_models_dot_design_dot_pmp_dot_DesignParameter__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='page/request/pmp/CreatePageModelRequest.proto',
  package='fkhp.page.layer.request.pmp',
  syntax='proto3',
  serialized_options=_b('\n\033fkhp.page.layer.request.pmpP\001'),
  serialized_pb=_b('\n-page/request/pmp/CreatePageModelRequest.proto\x12\x1b\x66khp.page.layer.request.pmp\x1a page/models/enums/PageType.proto\x1a,page/models/design/pmp/DesignParameter.proto\"\xc2\x01\n\x16\x43reatePageModelRequest\x12\x0e\n\x06pageId\x18\x01 \x01(\t\x12\x10\n\x08pageName\x18\x02 \x01(\t\x12\x38\n\x08pageType\x18\x03 \x01(\x0e\x32&.fkhp.page.layer.models.enums.PageType\x12L\n\x10\x64\x65signParameters\x18\x04 \x03(\x0b\x32\x32.fkhp.page.layer.models.design.pmp.DesignParameterB\x1f\n\x1b\x66khp.page.layer.request.pmpP\x01\x62\x06proto3')
  ,
  dependencies=[page_dot_models_dot_enums_dot_PageType__pb2.DESCRIPTOR,page_dot_models_dot_design_dot_pmp_dot_DesignParameter__pb2.DESCRIPTOR,])




_CREATEPAGEMODELREQUEST = _descriptor.Descriptor(
  name='CreatePageModelRequest',
  full_name='fkhp.page.layer.request.pmp.CreatePageModelRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='pageId', full_name='fkhp.page.layer.request.pmp.CreatePageModelRequest.pageId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pageName', full_name='fkhp.page.layer.request.pmp.CreatePageModelRequest.pageName', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pageType', full_name='fkhp.page.layer.request.pmp.CreatePageModelRequest.pageType', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='designParameters', full_name='fkhp.page.layer.request.pmp.CreatePageModelRequest.designParameters', index=3,
      number=4, type=11, cpp_type=10, label=3,
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
  serialized_start=159,
  serialized_end=353,
)

_CREATEPAGEMODELREQUEST.fields_by_name['pageType'].enum_type = page_dot_models_dot_enums_dot_PageType__pb2._PAGETYPE
_CREATEPAGEMODELREQUEST.fields_by_name['designParameters'].message_type = page_dot_models_dot_design_dot_pmp_dot_DesignParameter__pb2._DESIGNPARAMETER
DESCRIPTOR.message_types_by_name['CreatePageModelRequest'] = _CREATEPAGEMODELREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CreatePageModelRequest = _reflection.GeneratedProtocolMessageType('CreatePageModelRequest', (_message.Message,), dict(
  DESCRIPTOR = _CREATEPAGEMODELREQUEST,
  __module__ = 'page.request.pmp.CreatePageModelRequest_pb2'
  # @@protoc_insertion_point(class_scope:fkhp.page.layer.request.pmp.CreatePageModelRequest)
  ))
_sym_db.RegisterMessage(CreatePageModelRequest)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
