# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: page/request/pmp/FetchPageMetaDataRequest.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='page/request/pmp/FetchPageMetaDataRequest.proto',
  package='fkhp.page.layer.request.pmp',
  syntax='proto3',
  serialized_options=_b('\n\033fkhp.page.layer.request.pmpP\001'),
  serialized_pb=_b('\n/page/request/pmp/FetchPageMetaDataRequest.proto\x12\x1b\x66khp.page.layer.request.pmp\"*\n\x18\x46\x65tchPageMetaDataRequest\x12\x0e\n\x06pageId\x18\x01 \x01(\tB\x1f\n\x1b\x66khp.page.layer.request.pmpP\x01\x62\x06proto3')
)




_FETCHPAGEMETADATAREQUEST = _descriptor.Descriptor(
  name='FetchPageMetaDataRequest',
  full_name='fkhp.page.layer.request.pmp.FetchPageMetaDataRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='pageId', full_name='fkhp.page.layer.request.pmp.FetchPageMetaDataRequest.pageId', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_start=80,
  serialized_end=122,
)

DESCRIPTOR.message_types_by_name['FetchPageMetaDataRequest'] = _FETCHPAGEMETADATAREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

FetchPageMetaDataRequest = _reflection.GeneratedProtocolMessageType('FetchPageMetaDataRequest', (_message.Message,), dict(
  DESCRIPTOR = _FETCHPAGEMETADATAREQUEST,
  __module__ = 'page.request.pmp.FetchPageMetaDataRequest_pb2'
  # @@protoc_insertion_point(class_scope:fkhp.page.layer.request.pmp.FetchPageMetaDataRequest)
  ))
_sym_db.RegisterMessage(FetchPageMetaDataRequest)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)