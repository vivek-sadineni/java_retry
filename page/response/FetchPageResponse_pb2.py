# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: page/response/FetchPageResponse.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from page.response import PageConcrete_pb2 as page_dot_response_dot_PageConcrete__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='page/response/FetchPageResponse.proto',
  package='fkhp.page.layer.response',
  syntax='proto3',
  serialized_options=_b('\n\030fkhp.page.layer.responseP\001'),
  serialized_pb=_b('\n%page/response/FetchPageResponse.proto\x12\x18\x66khp.page.layer.response\x1a page/response/PageConcrete.proto\"\xf6\x01\n\x11\x46\x65tchPageResponse\x12<\n\x0cpageConcrete\x18\x01 \x01(\x0b\x32&.fkhp.page.layer.response.PageConcrete\x12K\n\x08metadata\x18\x02 \x03(\x0b\x32\x39.fkhp.page.layer.response.FetchPageResponse.MetadataEntry\x1aV\n\rMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x34\n\x05value\x18\x02 \x01(\x0b\x32%.fkhp.page.layer.response.HeaderValue:\x02\x38\x01\"\x1c\n\x0bHeaderValue\x12\r\n\x05value\x18\x01 \x03(\tB\x1c\n\x18\x66khp.page.layer.responseP\x01\x62\x06proto3')
  ,
  dependencies=[page_dot_response_dot_PageConcrete__pb2.DESCRIPTOR,])




_FETCHPAGERESPONSE_METADATAENTRY = _descriptor.Descriptor(
  name='MetadataEntry',
  full_name='fkhp.page.layer.response.FetchPageResponse.MetadataEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='fkhp.page.layer.response.FetchPageResponse.MetadataEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='fkhp.page.layer.response.FetchPageResponse.MetadataEntry.value', index=1,
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
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=262,
  serialized_end=348,
)

_FETCHPAGERESPONSE = _descriptor.Descriptor(
  name='FetchPageResponse',
  full_name='fkhp.page.layer.response.FetchPageResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='pageConcrete', full_name='fkhp.page.layer.response.FetchPageResponse.pageConcrete', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='metadata', full_name='fkhp.page.layer.response.FetchPageResponse.metadata', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_FETCHPAGERESPONSE_METADATAENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=102,
  serialized_end=348,
)


_HEADERVALUE = _descriptor.Descriptor(
  name='HeaderValue',
  full_name='fkhp.page.layer.response.HeaderValue',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='fkhp.page.layer.response.HeaderValue.value', index=0,
      number=1, type=9, cpp_type=9, label=3,
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
  serialized_start=350,
  serialized_end=378,
)

_FETCHPAGERESPONSE_METADATAENTRY.fields_by_name['value'].message_type = _HEADERVALUE
_FETCHPAGERESPONSE_METADATAENTRY.containing_type = _FETCHPAGERESPONSE
_FETCHPAGERESPONSE.fields_by_name['pageConcrete'].message_type = page_dot_response_dot_PageConcrete__pb2._PAGECONCRETE
_FETCHPAGERESPONSE.fields_by_name['metadata'].message_type = _FETCHPAGERESPONSE_METADATAENTRY
DESCRIPTOR.message_types_by_name['FetchPageResponse'] = _FETCHPAGERESPONSE
DESCRIPTOR.message_types_by_name['HeaderValue'] = _HEADERVALUE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

FetchPageResponse = _reflection.GeneratedProtocolMessageType('FetchPageResponse', (_message.Message,), dict(

  MetadataEntry = _reflection.GeneratedProtocolMessageType('MetadataEntry', (_message.Message,), dict(
    DESCRIPTOR = _FETCHPAGERESPONSE_METADATAENTRY,
    __module__ = 'page.response.FetchPageResponse_pb2'
    # @@protoc_insertion_point(class_scope:fkhp.page.layer.response.FetchPageResponse.MetadataEntry)
    ))
  ,
  DESCRIPTOR = _FETCHPAGERESPONSE,
  __module__ = 'page.response.FetchPageResponse_pb2'
  # @@protoc_insertion_point(class_scope:fkhp.page.layer.response.FetchPageResponse)
  ))
_sym_db.RegisterMessage(FetchPageResponse)
_sym_db.RegisterMessage(FetchPageResponse.MetadataEntry)

HeaderValue = _reflection.GeneratedProtocolMessageType('HeaderValue', (_message.Message,), dict(
  DESCRIPTOR = _HEADERVALUE,
  __module__ = 'page.response.FetchPageResponse_pb2'
  # @@protoc_insertion_point(class_scope:fkhp.page.layer.response.HeaderValue)
  ))
_sym_db.RegisterMessage(HeaderValue)


DESCRIPTOR._options = None
_FETCHPAGERESPONSE_METADATAENTRY._options = None
# @@protoc_insertion_point(module_scope)
