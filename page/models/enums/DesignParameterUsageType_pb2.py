# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: page/models/enums/DesignParameterUsageType.proto

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
  name='page/models/enums/DesignParameterUsageType.proto',
  package='fkhp.page.layer.models.enums',
  syntax='proto3',
  serialized_options=_b('\n\034fkhp.page.layer.models.enumsP\001'),
  serialized_pb=_b('\n0page/models/enums/DesignParameterUsageType.proto\x12\x1c\x66khp.page.layer.models.enums*E\n\x18\x44\x65signParameterUsageType\x12\x12\n\x0e\x44\x45\x46\x41ULT_DESIGN\x10\x00\x12\t\n\x05REACT\x10\x01\x12\n\n\x06\x43USTOM\x10\x02\x42 \n\x1c\x66khp.page.layer.models.enumsP\x01\x62\x06proto3')
)

_DESIGNPARAMETERUSAGETYPE = _descriptor.EnumDescriptor(
  name='DesignParameterUsageType',
  full_name='fkhp.page.layer.models.enums.DesignParameterUsageType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='DEFAULT_DESIGN', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='REACT', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CUSTOM', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=82,
  serialized_end=151,
)
_sym_db.RegisterEnumDescriptor(_DESIGNPARAMETERUSAGETYPE)

DesignParameterUsageType = enum_type_wrapper.EnumTypeWrapper(_DESIGNPARAMETERUSAGETYPE)
DEFAULT_DESIGN = 0
REACT = 1
CUSTOM = 2


DESCRIPTOR.enum_types_by_name['DesignParameterUsageType'] = _DESIGNPARAMETERUSAGETYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)