# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: executor/request/GetArticlesViewRequest.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from executor.models import query_pb2 as executor_dot_models_dot_query__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='executor/request/GetArticlesViewRequest.proto',
  package='fkhp.data.layer.executor.request',
  syntax='proto3',
  serialized_options=_b('\n fkhp.data.layer.executor.requestP\001'),
  serialized_pb=_b('\n-executor/request/GetArticlesViewRequest.proto\x12 fkhp.data.layer.executor.request\x1a\x1b\x65xecutor/models/query.proto\"\xa7\x01\n\x16GetArtcilesViewRequest\x12@\n\x08language\x18\x01 \x01(\x0e\x32..fkhp.data.layer.executor.request.LanguageType\x12\x0c\n\x04size\x18\x02 \x01(\t\x12=\n\tqueryInfo\x18\x03 \x01(\x0b\x32*.fkhp.data.layer.executor.models.QueryInfo*3\n\x0cLanguageType\x12\x0b\n\x07\x45NGLISH\x10\x00\x12\t\n\x05HINDI\x10\x01\x12\x0b\n\x07\x42\x45NGALI\x10\x02\x42$\n fkhp.data.layer.executor.requestP\x01\x62\x06proto3')
  ,
  dependencies=[executor_dot_models_dot_query__pb2.DESCRIPTOR,])

_LANGUAGETYPE = _descriptor.EnumDescriptor(
  name='LanguageType',
  full_name='fkhp.data.layer.executor.request.LanguageType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ENGLISH', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='HINDI', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BENGALI', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=282,
  serialized_end=333,
)
_sym_db.RegisterEnumDescriptor(_LANGUAGETYPE)

LanguageType = enum_type_wrapper.EnumTypeWrapper(_LANGUAGETYPE)
ENGLISH = 0
HINDI = 1
BENGALI = 2



_GETARTCILESVIEWREQUEST = _descriptor.Descriptor(
  name='GetArtcilesViewRequest',
  full_name='fkhp.data.layer.executor.request.GetArtcilesViewRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='language', full_name='fkhp.data.layer.executor.request.GetArtcilesViewRequest.language', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='size', full_name='fkhp.data.layer.executor.request.GetArtcilesViewRequest.size', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='queryInfo', full_name='fkhp.data.layer.executor.request.GetArtcilesViewRequest.queryInfo', index=2,
      number=3, type=11, cpp_type=10, label=1,
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
  serialized_start=113,
  serialized_end=280,
)

_GETARTCILESVIEWREQUEST.fields_by_name['language'].enum_type = _LANGUAGETYPE
_GETARTCILESVIEWREQUEST.fields_by_name['queryInfo'].message_type = executor_dot_models_dot_query__pb2._QUERYINFO
DESCRIPTOR.message_types_by_name['GetArtcilesViewRequest'] = _GETARTCILESVIEWREQUEST
DESCRIPTOR.enum_types_by_name['LanguageType'] = _LANGUAGETYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetArtcilesViewRequest = _reflection.GeneratedProtocolMessageType('GetArtcilesViewRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETARTCILESVIEWREQUEST,
  __module__ = 'executor.request.GetArticlesViewRequest_pb2'
  # @@protoc_insertion_point(class_scope:fkhp.data.layer.executor.request.GetArtcilesViewRequest)
  ))
_sym_db.RegisterMessage(GetArtcilesViewRequest)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
