# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: gateway/models/enums/UserAddressType.proto

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
  name='gateway/models/enums/UserAddressType.proto',
  package='fkhp.gateway.layer.client.models.enums',
  syntax='proto3',
  serialized_options=_b('\n&fkhp.gateway.layer.client.models.enumsP\001'),
  serialized_pb=_b('\n*gateway/models/enums/UserAddressType.proto\x12&fkhp.gateway.layer.client.models.enums*0\n\x0fUserAddressType\x12\x08\n\x04HOME\x10\x00\x12\x08\n\x04WORK\x10\x01\x12\t\n\x05OTHER\x10\x02\x42*\n&fkhp.gateway.layer.client.models.enumsP\x01\x62\x06proto3')
)

_USERADDRESSTYPE = _descriptor.EnumDescriptor(
  name='UserAddressType',
  full_name='fkhp.gateway.layer.client.models.enums.UserAddressType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='HOME', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='WORK', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OTHER', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=86,
  serialized_end=134,
)
_sym_db.RegisterEnumDescriptor(_USERADDRESSTYPE)

UserAddressType = enum_type_wrapper.EnumTypeWrapper(_USERADDRESSTYPE)
HOME = 0
WORK = 1
OTHER = 2


DESCRIPTOR.enum_types_by_name['UserAddressType'] = _USERADDRESSTYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
