# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: page/response/pmp/SearchPageByFieldResponse.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='page/response/pmp/SearchPageByFieldResponse.proto',
  package='fkhp.page.layer.response.pmp',
  syntax='proto3',
  serialized_options=_b('\n\034fkhp.page.layer.response.pmpP\001'),
  serialized_pb=_b('\n1page/response/pmp/SearchPageByFieldResponse.proto\x12\x1c\x66khp.page.layer.response.pmp\"3\n\x19SearchPageByFieldResponse\x12\x16\n\x0esearchResponse\x18\x01 \x03(\tB \n\x1c\x66khp.page.layer.response.pmpP\x01\x62\x06proto3')
)




_SEARCHPAGEBYFIELDRESPONSE = _descriptor.Descriptor(
  name='SearchPageByFieldResponse',
  full_name='fkhp.page.layer.response.pmp.SearchPageByFieldResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='searchResponse', full_name='fkhp.page.layer.response.pmp.SearchPageByFieldResponse.searchResponse', index=0,
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
  serialized_start=83,
  serialized_end=134,
)

DESCRIPTOR.message_types_by_name['SearchPageByFieldResponse'] = _SEARCHPAGEBYFIELDRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SearchPageByFieldResponse = _reflection.GeneratedProtocolMessageType('SearchPageByFieldResponse', (_message.Message,), dict(
  DESCRIPTOR = _SEARCHPAGEBYFIELDRESPONSE,
  __module__ = 'page.response.pmp.SearchPageByFieldResponse_pb2'
  # @@protoc_insertion_point(class_scope:fkhp.page.layer.response.pmp.SearchPageByFieldResponse)
  ))
_sym_db.RegisterMessage(SearchPageByFieldResponse)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
