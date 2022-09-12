# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: gateway/models/user/UserAddress.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from gateway.models.enums import UserAddressType_pb2 as gateway_dot_models_dot_enums_dot_UserAddressType__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='gateway/models/user/UserAddress.proto',
  package='fkhp.gateway.layer.client.models.user',
  syntax='proto3',
  serialized_options=_b('\n%fkhp.gateway.layer.client.models.userP\001'),
  serialized_pb=_b('\n%gateway/models/user/UserAddress.proto\x12%fkhp.gateway.layer.client.models.user\x1a*gateway/models/enums/UserAddressType.proto\"\xcf\x01\n\x0bUserAddress\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x14\n\x0cmobileNumber\x18\x02 \x01(\t\x12\x0f\n\x07\x61\x64\x64ress\x18\x03 \x01(\t\x12\x10\n\x08landmark\x18\x04 \x01(\t\x12\x0f\n\x07pinCode\x18\x05 \x01(\t\x12\x0c\n\x04\x63ity\x18\x06 \x01(\t\x12\x0c\n\x04\x61rea\x18\x07 \x01(\t\x12L\n\x0b\x61\x64\x64ressType\x18\x08 \x01(\x0e\x32\x37.fkhp.gateway.layer.client.models.enums.UserAddressTypeB)\n%fkhp.gateway.layer.client.models.userP\x01\x62\x06proto3')
  ,
  dependencies=[gateway_dot_models_dot_enums_dot_UserAddressType__pb2.DESCRIPTOR,])




_USERADDRESS = _descriptor.Descriptor(
  name='UserAddress',
  full_name='fkhp.gateway.layer.client.models.user.UserAddress',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='fkhp.gateway.layer.client.models.user.UserAddress.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='mobileNumber', full_name='fkhp.gateway.layer.client.models.user.UserAddress.mobileNumber', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='address', full_name='fkhp.gateway.layer.client.models.user.UserAddress.address', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='landmark', full_name='fkhp.gateway.layer.client.models.user.UserAddress.landmark', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pinCode', full_name='fkhp.gateway.layer.client.models.user.UserAddress.pinCode', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='city', full_name='fkhp.gateway.layer.client.models.user.UserAddress.city', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='area', full_name='fkhp.gateway.layer.client.models.user.UserAddress.area', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='addressType', full_name='fkhp.gateway.layer.client.models.user.UserAddress.addressType', index=7,
      number=8, type=14, cpp_type=8, label=1,
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
  serialized_start=125,
  serialized_end=332,
)

_USERADDRESS.fields_by_name['addressType'].enum_type = gateway_dot_models_dot_enums_dot_UserAddressType__pb2._USERADDRESSTYPE
DESCRIPTOR.message_types_by_name['UserAddress'] = _USERADDRESS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

UserAddress = _reflection.GeneratedProtocolMessageType('UserAddress', (_message.Message,), dict(
  DESCRIPTOR = _USERADDRESS,
  __module__ = 'gateway.models.user.UserAddress_pb2'
  # @@protoc_insertion_point(class_scope:fkhp.gateway.layer.client.models.user.UserAddress)
  ))
_sym_db.RegisterMessage(UserAddress)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)