# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: gateway/models/enums/AddressSuggestionType.proto

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
  name='gateway/models/enums/AddressSuggestionType.proto',
  package='fkhp.gateway.layer.client.models.enums',
  syntax='proto3',
  serialized_options=_b('\n&fkhp.gateway.layer.client.models.enumsP\001'),
  serialized_pb=_b('\n0gateway/models/enums/AddressSuggestionType.proto\x12&fkhp.gateway.layer.client.models.enums*\xc5\x01\n\x15\x41\x64\x64ressSuggestionType\x12\x1b\n\x17\x41\x44\x44RESS_SUGGESTION_TYPE\x10\x00\x12\n\n\x06TYPEAP\x10\x01\x12\x0b\n\x07TYPEPOI\x10\x02\x12\x0b\n\x07TYPELOC\x10\x03\x12\x0c\n\x08TYPESUBL\x10\x04\x12\x0c\n\x08TYPESSLC\x10\x05\x12\x0b\n\x07TYPECTY\x10\x06\x12\x0c\n\x08TYPESCTY\x10\x07\x12\x0b\n\x07TYPEDST\x10\x08\x12\x0b\n\x07TYPESDB\x10\t\x12\x0b\n\x07TYPEVLG\x10\n\x12\x0b\n\x07TYPEPIN\x10\x0b\x42*\n&fkhp.gateway.layer.client.models.enumsP\x01\x62\x06proto3')
)

_ADDRESSSUGGESTIONTYPE = _descriptor.EnumDescriptor(
  name='AddressSuggestionType',
  full_name='fkhp.gateway.layer.client.models.enums.AddressSuggestionType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ADDRESS_SUGGESTION_TYPE', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TYPEAP', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TYPEPOI', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TYPELOC', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TYPESUBL', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TYPESSLC', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TYPECTY', index=6, number=6,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TYPESCTY', index=7, number=7,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TYPEDST', index=8, number=8,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TYPESDB', index=9, number=9,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TYPEVLG', index=10, number=10,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TYPEPIN', index=11, number=11,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=93,
  serialized_end=290,
)
_sym_db.RegisterEnumDescriptor(_ADDRESSSUGGESTIONTYPE)

AddressSuggestionType = enum_type_wrapper.EnumTypeWrapper(_ADDRESSSUGGESTIONTYPE)
ADDRESS_SUGGESTION_TYPE = 0
TYPEAP = 1
TYPEPOI = 2
TYPELOC = 3
TYPESUBL = 4
TYPESSLC = 5
TYPECTY = 6
TYPESCTY = 7
TYPEDST = 8
TYPESDB = 9
TYPEVLG = 10
TYPEPIN = 11


DESCRIPTOR.enum_types_by_name['AddressSuggestionType'] = _ADDRESSSUGGESTIONTYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)