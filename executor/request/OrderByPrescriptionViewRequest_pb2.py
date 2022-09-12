# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: executor/request/OrderByPrescriptionViewRequest.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from executor.models import requestMetaInfo_pb2 as executor_dot_models_dot_requestMetaInfo__pb2
from executor.models import userInfo_pb2 as executor_dot_models_dot_userInfo__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='executor/request/OrderByPrescriptionViewRequest.proto',
  package='fkhp.data.layer.executor.request',
  syntax='proto3',
  serialized_options=_b('\n fkhp.data.layer.executor.requestP\001'),
  serialized_pb=_b('\n5executor/request/OrderByPrescriptionViewRequest.proto\x12 fkhp.data.layer.executor.request\x1a%executor/models/requestMetaInfo.proto\x1a\x1e\x65xecutor/models/userInfo.proto\"\xca\x02\n\x1eOrderByPrescriptionViewRequest\x12;\n\x08userInfo\x18\x01 \x01(\x0b\x32).fkhp.data.layer.executor.models.UserInfo\x12I\n\x0frequestMetaInfo\x18\x02 \x01(\x0b\x32\x30.fkhp.data.layer.executor.models.RequestMetaInfo\x12\x11\n\taddressId\x18\x03 \x01(\t\x12\x17\n\x0fprescriptionIds\x18\x04 \x03(\t\x12L\n\x05\x66iles\x18\x05 \x03(\x0b\x32=.fkhp.data.layer.executor.request.OrderByPrescriptionFileData\x12&\n\x1eisUploadPrescriptionFromDevice\x18\x06 \x01(\x08\"9\n\x1bOrderByPrescriptionFileData\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0c\n\x04\x64\x61ta\x18\x02 \x01(\x0c\x42$\n fkhp.data.layer.executor.requestP\x01\x62\x06proto3')
  ,
  dependencies=[executor_dot_models_dot_requestMetaInfo__pb2.DESCRIPTOR,executor_dot_models_dot_userInfo__pb2.DESCRIPTOR,])




_ORDERBYPRESCRIPTIONVIEWREQUEST = _descriptor.Descriptor(
  name='OrderByPrescriptionViewRequest',
  full_name='fkhp.data.layer.executor.request.OrderByPrescriptionViewRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='userInfo', full_name='fkhp.data.layer.executor.request.OrderByPrescriptionViewRequest.userInfo', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='requestMetaInfo', full_name='fkhp.data.layer.executor.request.OrderByPrescriptionViewRequest.requestMetaInfo', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='addressId', full_name='fkhp.data.layer.executor.request.OrderByPrescriptionViewRequest.addressId', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='prescriptionIds', full_name='fkhp.data.layer.executor.request.OrderByPrescriptionViewRequest.prescriptionIds', index=3,
      number=4, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='files', full_name='fkhp.data.layer.executor.request.OrderByPrescriptionViewRequest.files', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='isUploadPrescriptionFromDevice', full_name='fkhp.data.layer.executor.request.OrderByPrescriptionViewRequest.isUploadPrescriptionFromDevice', index=5,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=163,
  serialized_end=493,
)


_ORDERBYPRESCRIPTIONFILEDATA = _descriptor.Descriptor(
  name='OrderByPrescriptionFileData',
  full_name='fkhp.data.layer.executor.request.OrderByPrescriptionFileData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='fkhp.data.layer.executor.request.OrderByPrescriptionFileData.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='fkhp.data.layer.executor.request.OrderByPrescriptionFileData.data', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
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
  serialized_start=495,
  serialized_end=552,
)

_ORDERBYPRESCRIPTIONVIEWREQUEST.fields_by_name['userInfo'].message_type = executor_dot_models_dot_userInfo__pb2._USERINFO
_ORDERBYPRESCRIPTIONVIEWREQUEST.fields_by_name['requestMetaInfo'].message_type = executor_dot_models_dot_requestMetaInfo__pb2._REQUESTMETAINFO
_ORDERBYPRESCRIPTIONVIEWREQUEST.fields_by_name['files'].message_type = _ORDERBYPRESCRIPTIONFILEDATA
DESCRIPTOR.message_types_by_name['OrderByPrescriptionViewRequest'] = _ORDERBYPRESCRIPTIONVIEWREQUEST
DESCRIPTOR.message_types_by_name['OrderByPrescriptionFileData'] = _ORDERBYPRESCRIPTIONFILEDATA
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

OrderByPrescriptionViewRequest = _reflection.GeneratedProtocolMessageType('OrderByPrescriptionViewRequest', (_message.Message,), dict(
  DESCRIPTOR = _ORDERBYPRESCRIPTIONVIEWREQUEST,
  __module__ = 'executor.request.OrderByPrescriptionViewRequest_pb2'
  # @@protoc_insertion_point(class_scope:fkhp.data.layer.executor.request.OrderByPrescriptionViewRequest)
  ))
_sym_db.RegisterMessage(OrderByPrescriptionViewRequest)

OrderByPrescriptionFileData = _reflection.GeneratedProtocolMessageType('OrderByPrescriptionFileData', (_message.Message,), dict(
  DESCRIPTOR = _ORDERBYPRESCRIPTIONFILEDATA,
  __module__ = 'executor.request.OrderByPrescriptionViewRequest_pb2'
  # @@protoc_insertion_point(class_scope:fkhp.data.layer.executor.request.OrderByPrescriptionFileData)
  ))
_sym_db.RegisterMessage(OrderByPrescriptionFileData)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)