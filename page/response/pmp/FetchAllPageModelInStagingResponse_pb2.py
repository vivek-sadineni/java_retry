# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: page/response/pmp/FetchAllPageModelInStagingResponse.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from page.models.page.pmp import PageUserInputModel_pb2 as page_dot_models_dot_page_dot_pmp_dot_PageUserInputModel__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='page/response/pmp/FetchAllPageModelInStagingResponse.proto',
  package='fkhp.page.layer.response.pmp',
  syntax='proto3',
  serialized_options=_b('\n\034fkhp.page.layer.response.pmpP\001'),
  serialized_pb=_b('\n:page/response/pmp/FetchAllPageModelInStagingResponse.proto\x12\x1c\x66khp.page.layer.response.pmp\x1a-page/models/page/pmp/PageUserInputModel.proto\"}\n\"FetchAllPageModelInStagingResponse\x12\x0e\n\x06status\x18\x01 \x01(\t\x12G\n\npageModels\x18\x02 \x03(\x0b\x32\x33.fkhp.page.layer.models.page.pmp.PageUserInputModelB \n\x1c\x66khp.page.layer.response.pmpP\x01\x62\x06proto3')
  ,
  dependencies=[page_dot_models_dot_page_dot_pmp_dot_PageUserInputModel__pb2.DESCRIPTOR,])




_FETCHALLPAGEMODELINSTAGINGRESPONSE = _descriptor.Descriptor(
  name='FetchAllPageModelInStagingResponse',
  full_name='fkhp.page.layer.response.pmp.FetchAllPageModelInStagingResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='fkhp.page.layer.response.pmp.FetchAllPageModelInStagingResponse.status', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pageModels', full_name='fkhp.page.layer.response.pmp.FetchAllPageModelInStagingResponse.pageModels', index=1,
      number=2, type=11, cpp_type=10, label=3,
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
  serialized_start=139,
  serialized_end=264,
)

_FETCHALLPAGEMODELINSTAGINGRESPONSE.fields_by_name['pageModels'].message_type = page_dot_models_dot_page_dot_pmp_dot_PageUserInputModel__pb2._PAGEUSERINPUTMODEL
DESCRIPTOR.message_types_by_name['FetchAllPageModelInStagingResponse'] = _FETCHALLPAGEMODELINSTAGINGRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

FetchAllPageModelInStagingResponse = _reflection.GeneratedProtocolMessageType('FetchAllPageModelInStagingResponse', (_message.Message,), dict(
  DESCRIPTOR = _FETCHALLPAGEMODELINSTAGINGRESPONSE,
  __module__ = 'page.response.pmp.FetchAllPageModelInStagingResponse_pb2'
  # @@protoc_insertion_point(class_scope:fkhp.page.layer.response.pmp.FetchAllPageModelInStagingResponse)
  ))
_sym_db.RegisterMessage(FetchAllPageModelInStagingResponse)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
