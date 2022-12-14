# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: page/client/PageService.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from page.request import FetchRequest_pb2 as page_dot_request_dot_FetchRequest__pb2
from page.response import FetchPageResponse_pb2 as page_dot_response_dot_FetchPageResponse__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='page/client/PageService.proto',
  package='fkhp.page.layer.client',
  syntax='proto3',
  serialized_options=_b('\n\026fkhp.page.layer.clientP\001'),
  serialized_pb=_b('\n\x1dpage/client/PageService.proto\x12\x16\x66khp.page.layer.client\x1a\x1fpage/request/FetchRequest.proto\x1a%page/response/FetchPageResponse.proto2p\n\x0bPageService\x12\x61\n\tfetchPage\x12%.fkhp.page.layer.request.FetchRequest\x1a+.fkhp.page.layer.response.FetchPageResponse\"\x00\x42\x1a\n\x16\x66khp.page.layer.clientP\x01\x62\x06proto3')
  ,
  dependencies=[page_dot_request_dot_FetchRequest__pb2.DESCRIPTOR,page_dot_response_dot_FetchPageResponse__pb2.DESCRIPTOR,])



_sym_db.RegisterFileDescriptor(DESCRIPTOR)


DESCRIPTOR._options = None

_PAGESERVICE = _descriptor.ServiceDescriptor(
  name='PageService',
  full_name='fkhp.page.layer.client.PageService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=129,
  serialized_end=241,
  methods=[
  _descriptor.MethodDescriptor(
    name='fetchPage',
    full_name='fkhp.page.layer.client.PageService.fetchPage',
    index=0,
    containing_service=None,
    input_type=page_dot_request_dot_FetchRequest__pb2._FETCHREQUEST,
    output_type=page_dot_response_dot_FetchPageResponse__pb2._FETCHPAGERESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_PAGESERVICE)

DESCRIPTOR.services_by_name['PageService'] = _PAGESERVICE

# @@protoc_insertion_point(module_scope)
