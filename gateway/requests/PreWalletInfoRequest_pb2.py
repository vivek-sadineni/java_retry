# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: gateway/requests/PreWalletInfoRequest.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='gateway/requests/PreWalletInfoRequest.proto',
  package='fkhp.gateway.layer.client.requests',
  syntax='proto3',
  serialized_options=_b('\n\"fkhp.gateway.layer.client.requestsP\001'),
  serialized_pb=_b('\n+gateway/requests/PreWalletInfoRequest.proto\x12\"fkhp.gateway.layer.client.requests\",\n\x14PreWalletInfoRequest\x12\x14\n\x0cmobileNumber\x18\x01 \x01(\tB&\n\"fkhp.gateway.layer.client.requestsP\x01\x62\x06proto3')
)




_PREWALLETINFOREQUEST = _descriptor.Descriptor(
  name='PreWalletInfoRequest',
  full_name='fkhp.gateway.layer.client.requests.PreWalletInfoRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='mobileNumber', full_name='fkhp.gateway.layer.client.requests.PreWalletInfoRequest.mobileNumber', index=0,
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
  serialized_start=83,
  serialized_end=127,
)

DESCRIPTOR.message_types_by_name['PreWalletInfoRequest'] = _PREWALLETINFOREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PreWalletInfoRequest = _reflection.GeneratedProtocolMessageType('PreWalletInfoRequest', (_message.Message,), dict(
  DESCRIPTOR = _PREWALLETINFOREQUEST,
  __module__ = 'gateway.requests.PreWalletInfoRequest_pb2'
  # @@protoc_insertion_point(class_scope:fkhp.gateway.layer.client.requests.PreWalletInfoRequest)
  ))
_sym_db.RegisterMessage(PreWalletInfoRequest)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
