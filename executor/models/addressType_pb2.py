# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: executor/models/addressType.proto

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
  name='executor/models/addressType.proto',
  package='fkhp.data.layer.executor.models',
  syntax='proto3',
  serialized_options=_b('\n\037fkhp.data.layer.executor.modelsP\001'),
  serialized_pb=_b('\n!executor/models/addressType.proto\x12\x1f\x66khp.data.layer.executor.models*C\n\x0b\x41\x64\x64ressType\x12\x08\n\x04HOME\x10\x00\x12\x08\n\x04WORK\x10\x01\x12\t\n\x05OTHER\x10\x02\x12\x15\n\x11\x41\x44\x44RESS_TYPE_NONE\x10\x03\x42#\n\x1f\x66khp.data.layer.executor.modelsP\x01\x62\x06proto3')
)

_ADDRESSTYPE = _descriptor.EnumDescriptor(
  name='AddressType',
  full_name='fkhp.data.layer.executor.models.AddressType',
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
    _descriptor.EnumValueDescriptor(
      name='ADDRESS_TYPE_NONE', index=3, number=3,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=70,
  serialized_end=137,
)
_sym_db.RegisterEnumDescriptor(_ADDRESSTYPE)

AddressType = enum_type_wrapper.EnumTypeWrapper(_ADDRESSTYPE)
HOME = 0
WORK = 1
OTHER = 2
ADDRESS_TYPE_NONE = 3


DESCRIPTOR.enum_types_by_name['AddressType'] = _ADDRESSTYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
