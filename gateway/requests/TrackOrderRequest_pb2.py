# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: gateway/requests/TrackOrderRequest.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='gateway/requests/TrackOrderRequest.proto',
  package='fkhp.gateway.layer.client.requests',
  syntax='proto3',
  serialized_options=_b('\n\"fkhp.gateway.layer.client.requestsP\001'),
  serialized_pb=_b('\n(gateway/requests/TrackOrderRequest.proto\x12\"fkhp.gateway.layer.client.requests\"$\n\x11TrackOrderRequest\x12\x0f\n\x07orderId\x18\x01 \x01(\tB&\n\"fkhp.gateway.layer.client.requestsP\x01\x62\x06proto3')
)




_TRACKORDERREQUEST = _descriptor.Descriptor(
  name='TrackOrderRequest',
  full_name='fkhp.gateway.layer.client.requests.TrackOrderRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='orderId', full_name='fkhp.gateway.layer.client.requests.TrackOrderRequest.orderId', index=0,
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
  serialized_end=116,
)

DESCRIPTOR.message_types_by_name['TrackOrderRequest'] = _TRACKORDERREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TrackOrderRequest = _reflection.GeneratedProtocolMessageType('TrackOrderRequest', (_message.Message,), dict(
  DESCRIPTOR = _TRACKORDERREQUEST,
  __module__ = 'gateway.requests.TrackOrderRequest_pb2'
  # @@protoc_insertion_point(class_scope:fkhp.gateway.layer.client.requests.TrackOrderRequest)
  ))
_sym_db.RegisterMessage(TrackOrderRequest)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
