# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: executor/request/UserDetailRequest.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='executor/request/UserDetailRequest.proto',
  package='fkhp.data.layer.executor.request',
  syntax='proto3',
  serialized_options=_b('\n fkhp.data.layer.executor.requestP\001'),
  serialized_pb=_b('\n(executor/request/UserDetailRequest.proto\x12 fkhp.data.layer.executor.request\"\x13\n\x11UserDetailRequestB$\n fkhp.data.layer.executor.requestP\x01\x62\x06proto3')
)




_USERDETAILREQUEST = _descriptor.Descriptor(
  name='UserDetailRequest',
  full_name='fkhp.data.layer.executor.request.UserDetailRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=78,
  serialized_end=97,
)

DESCRIPTOR.message_types_by_name['UserDetailRequest'] = _USERDETAILREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

UserDetailRequest = _reflection.GeneratedProtocolMessageType('UserDetailRequest', (_message.Message,), dict(
  DESCRIPTOR = _USERDETAILREQUEST,
  __module__ = 'executor.request.UserDetailRequest_pb2'
  # @@protoc_insertion_point(class_scope:fkhp.data.layer.executor.request.UserDetailRequest)
  ))
_sym_db.RegisterMessage(UserDetailRequest)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
