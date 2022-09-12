# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: gateway/responses/AddAddressResponse.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from gateway.models import HeaderValue_pb2 as gateway_dot_models_dot_HeaderValue__pb2
from executor.response import AddAndUpdateAddressViewResponse_pb2 as executor_dot_response_dot_AddAndUpdateAddressViewResponse__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='gateway/responses/AddAddressResponse.proto',
  package='fkhp.gateway.layer.client.response',
  syntax='proto3',
  serialized_options=_b('\n\"fkhp.gateway.layer.client.responseP\001'),
  serialized_pb=_b('\n*gateway/responses/AddAddressResponse.proto\x12\"fkhp.gateway.layer.client.response\x1a gateway/models/HeaderValue.proto\x1a\x37\x65xecutor/response/AddAndUpdateAddressViewResponse.proto\"\xa2\x02\n\x12\x41\x64\x64\x41\x64\x64ressResponse\x12T\n\x08response\x18\x01 \x01(\x0b\x32\x42.fkhp.data.layer.executor.response.AddAndUpdateAddressViewResponse\x12V\n\x08metadata\x18\x02 \x03(\x0b\x32\x44.fkhp.gateway.layer.client.response.AddAddressResponse.MetadataEntry\x1a^\n\rMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12<\n\x05value\x18\x02 \x01(\x0b\x32-.fkhp.gateway.layer.client.models.HeaderValue:\x02\x38\x01\x42&\n\"fkhp.gateway.layer.client.responseP\x01\x62\x06proto3')
  ,
  dependencies=[gateway_dot_models_dot_HeaderValue__pb2.DESCRIPTOR,executor_dot_response_dot_AddAndUpdateAddressViewResponse__pb2.DESCRIPTOR,])




_ADDADDRESSRESPONSE_METADATAENTRY = _descriptor.Descriptor(
  name='MetadataEntry',
  full_name='fkhp.gateway.layer.client.response.AddAddressResponse.MetadataEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='fkhp.gateway.layer.client.response.AddAddressResponse.MetadataEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='fkhp.gateway.layer.client.response.AddAddressResponse.MetadataEntry.value', index=1,
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
  serialized_start=370,
  serialized_end=464,
)

_ADDADDRESSRESPONSE = _descriptor.Descriptor(
  name='AddAddressResponse',
  full_name='fkhp.gateway.layer.client.response.AddAddressResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='response', full_name='fkhp.gateway.layer.client.response.AddAddressResponse.response', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='metadata', full_name='fkhp.gateway.layer.client.response.AddAddressResponse.metadata', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_ADDADDRESSRESPONSE_METADATAENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=174,
  serialized_end=464,
)

_ADDADDRESSRESPONSE_METADATAENTRY.fields_by_name['value'].message_type = gateway_dot_models_dot_HeaderValue__pb2._HEADERVALUE
_ADDADDRESSRESPONSE_METADATAENTRY.containing_type = _ADDADDRESSRESPONSE
_ADDADDRESSRESPONSE.fields_by_name['response'].message_type = executor_dot_response_dot_AddAndUpdateAddressViewResponse__pb2._ADDANDUPDATEADDRESSVIEWRESPONSE
_ADDADDRESSRESPONSE.fields_by_name['metadata'].message_type = _ADDADDRESSRESPONSE_METADATAENTRY
DESCRIPTOR.message_types_by_name['AddAddressResponse'] = _ADDADDRESSRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AddAddressResponse = _reflection.GeneratedProtocolMessageType('AddAddressResponse', (_message.Message,), dict(

  MetadataEntry = _reflection.GeneratedProtocolMessageType('MetadataEntry', (_message.Message,), dict(
    DESCRIPTOR = _ADDADDRESSRESPONSE_METADATAENTRY,
    __module__ = 'gateway.responses.AddAddressResponse_pb2'
    # @@protoc_insertion_point(class_scope:fkhp.gateway.layer.client.response.AddAddressResponse.MetadataEntry)
    ))
  ,
  DESCRIPTOR = _ADDADDRESSRESPONSE,
  __module__ = 'gateway.responses.AddAddressResponse_pb2'
  # @@protoc_insertion_point(class_scope:fkhp.gateway.layer.client.response.AddAddressResponse)
  ))
_sym_db.RegisterMessage(AddAddressResponse)
_sym_db.RegisterMessage(AddAddressResponse.MetadataEntry)


DESCRIPTOR._options = None
_ADDADDRESSRESPONSE_METADATAENTRY._options = None
# @@protoc_insertion_point(module_scope)
