# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: executor/models/couponAppliedInfo.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='executor/models/couponAppliedInfo.proto',
  package='fkhp.data.layer.executor.models',
  syntax='proto3',
  serialized_options=_b('\n\037fkhp.data.layer.executor.modelsP\001'),
  serialized_pb=_b('\n\'executor/models/couponAppliedInfo.proto\x12\x1f\x66khp.data.layer.executor.models\"f\n\x11\x43ouponAppliedInfo\x12\x10\n\x08\x63ouponId\x18\x01 \x01(\t\x12\x12\n\ncouponName\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12\x16\n\x0e\x64iscountAmount\x18\x04 \x01(\x05\x42#\n\x1f\x66khp.data.layer.executor.modelsP\x01\x62\x06proto3')
)




_COUPONAPPLIEDINFO = _descriptor.Descriptor(
  name='CouponAppliedInfo',
  full_name='fkhp.data.layer.executor.models.CouponAppliedInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='couponId', full_name='fkhp.data.layer.executor.models.CouponAppliedInfo.couponId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='couponName', full_name='fkhp.data.layer.executor.models.CouponAppliedInfo.couponName', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='description', full_name='fkhp.data.layer.executor.models.CouponAppliedInfo.description', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='discountAmount', full_name='fkhp.data.layer.executor.models.CouponAppliedInfo.discountAmount', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=76,
  serialized_end=178,
)

DESCRIPTOR.message_types_by_name['CouponAppliedInfo'] = _COUPONAPPLIEDINFO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CouponAppliedInfo = _reflection.GeneratedProtocolMessageType('CouponAppliedInfo', (_message.Message,), dict(
  DESCRIPTOR = _COUPONAPPLIEDINFO,
  __module__ = 'executor.models.couponAppliedInfo_pb2'
  # @@protoc_insertion_point(class_scope:fkhp.data.layer.executor.models.CouponAppliedInfo)
  ))
_sym_db.RegisterMessage(CouponAppliedInfo)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
