# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: gateway/models/enums/ProductType.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='gateway/models/enums/ProductType.proto',
  package='fkhp.gateway.layer.client.models.enums',
  syntax='proto3',
  serialized_options=_b('\n&fkhp.gateway.layer.client.models.enumsP\001'),
  serialized_pb=_b('\n&gateway/models/enums/ProductType.proto\x12&fkhp.gateway.layer.client.models.enums**\n\x0bProductType\x12\x0c\n\x08MEDICINE\x10\x00\x12\r\n\tHOUSEHOLD\x10\x01\x42*\n&fkhp.gateway.layer.client.models.enumsP\x01\x62\x06proto3')
)

_PRODUCTTYPE = _descriptor.EnumDescriptor(
  name='ProductType',
  full_name='fkhp.gateway.layer.client.models.enums.ProductType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='MEDICINE', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='HOUSEHOLD', index=1, number=1,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=82,
  serialized_end=124,
)
_sym_db.RegisterEnumDescriptor(_PRODUCTTYPE)

ProductType = enum_type_wrapper.EnumTypeWrapper(_PRODUCTTYPE)
MEDICINE = 0
HOUSEHOLD = 1


DESCRIPTOR.enum_types_by_name['ProductType'] = _PRODUCTTYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
