# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: executor/models/paymentType.proto

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
  name='executor/models/paymentType.proto',
  package='fkhp.data.layer.executor.models',
  syntax='proto3',
  serialized_options=_b('\n\037fkhp.data.layer.executor.modelsP\001'),
  serialized_pb=_b('\n!executor/models/paymentType.proto\x12\x1f\x66khp.data.layer.executor.models*H\n\x0bPaymentType\x12\x0b\n\x07PAYTMPG\x10\x00\x12\x0b\n\x07PHONEPE\x10\x01\x12\x07\n\x03\x43OD\x10\x02\x12\x06\n\x02QC\x10\x03\x12\x0e\n\nFKH_WALLET\x10\x04\x42#\n\x1f\x66khp.data.layer.executor.modelsP\x01\x62\x06proto3')
)

_PAYMENTTYPE = _descriptor.EnumDescriptor(
  name='PaymentType',
  full_name='fkhp.data.layer.executor.models.PaymentType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='PAYTMPG', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PHONEPE', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COD', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='QC', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FKH_WALLET', index=4, number=4,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=70,
  serialized_end=142,
)
_sym_db.RegisterEnumDescriptor(_PAYMENTTYPE)

PaymentType = enum_type_wrapper.EnumTypeWrapper(_PAYMENTTYPE)
PAYTMPG = 0
PHONEPE = 1
COD = 2
QC = 3
FKH_WALLET = 4


DESCRIPTOR.enum_types_by_name['PaymentType'] = _PAYMENTTYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
