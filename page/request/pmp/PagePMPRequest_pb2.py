# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: page/request/pmp/PagePMPRequest.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='page/request/pmp/PagePMPRequest.proto',
  package='fkhp.page.layer.request.pmp',
  syntax='proto3',
  serialized_options=_b('\n\033fkhp.page.layer.request.pmpP\001'),
  serialized_pb=_b('\n%page/request/pmp/PagePMPRequest.proto\x12\x1b\x66khp.page.layer.request.pmp\"1\n\x0ePagePMPRequest\x12\x0e\n\x06pageId\x18\x01 \x01(\t\x12\x0f\n\x07version\x18\x02 \x01(\x05\x42\x1f\n\x1b\x66khp.page.layer.request.pmpP\x01\x62\x06proto3')
)




_PAGEPMPREQUEST = _descriptor.Descriptor(
  name='PagePMPRequest',
  full_name='fkhp.page.layer.request.pmp.PagePMPRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='pageId', full_name='fkhp.page.layer.request.pmp.PagePMPRequest.pageId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='version', full_name='fkhp.page.layer.request.pmp.PagePMPRequest.version', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=70,
  serialized_end=119,
)

DESCRIPTOR.message_types_by_name['PagePMPRequest'] = _PAGEPMPREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PagePMPRequest = _reflection.GeneratedProtocolMessageType('PagePMPRequest', (_message.Message,), dict(
  DESCRIPTOR = _PAGEPMPREQUEST,
  __module__ = 'page.request.pmp.PagePMPRequest_pb2'
  # @@protoc_insertion_point(class_scope:fkhp.page.layer.request.pmp.PagePMPRequest)
  ))
_sym_db.RegisterMessage(PagePMPRequest)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
