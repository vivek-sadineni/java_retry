# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: executor/models/productInfo.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from executor.models import multiMediaInfo_pb2 as executor_dot_models_dot_multiMediaInfo__pb2
from executor.models import saltInfo_pb2 as executor_dot_models_dot_saltInfo__pb2
from executor.models import varietyInfo_pb2 as executor_dot_models_dot_varietyInfo__pb2
from executor.models import moreProductInfo_pb2 as executor_dot_models_dot_moreProductInfo__pb2
from executor.models import medicineInfo_pb2 as executor_dot_models_dot_medicineInfo__pb2
from executor.models import returnInfo_pb2 as executor_dot_models_dot_returnInfo__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='executor/models/productInfo.proto',
  package='fkhp.data.layer.executor.models',
  syntax='proto3',
  serialized_options=_b('\n\037fkhp.data.layer.executor.modelsP\001'),
  serialized_pb=_b('\n!executor/models/productInfo.proto\x12\x1f\x66khp.data.layer.executor.models\x1a$executor/models/multiMediaInfo.proto\x1a\x1e\x65xecutor/models/saltInfo.proto\x1a!executor/models/varietyInfo.proto\x1a%executor/models/moreProductInfo.proto\x1a\"executor/models/medicineInfo.proto\x1a executor/models/returnInfo.proto\"\xd5\x06\n\x0bProductInfo\x12\x41\n\x0bproductType\x18\x01 \x01(\x0e\x32,.fkhp.data.layer.executor.models.ProductType\x12\x1c\n\x14prescriptionRequired\x18\x02 \x01(\x08\x12G\n\x0emultiMediaInfo\x18\x03 \x03(\x0b\x32/.fkhp.data.layer.executor.models.MultiMediaInfo\x12\x13\n\x0bproductName\x18\x04 \x01(\t\x12\x10\n\x08strength\x18\x05 \x01(\t\x12;\n\x08saltInfo\x18\x06 \x03(\x0b\x32).fkhp.data.layer.executor.models.SaltInfo\x12\x12\n\nexpiryDate\x18\x07 \x01(\t\x12\x12\n\ndosageForm\x18\x08 \x01(\t\x12\x41\n\x0bvarietyInfo\x18\t \x03(\x0b\x32,.fkhp.data.layer.executor.models.VarietyInfo\x12\x1e\n\x16manufacturingGroupName\x18\n \x01(\t\x12\x42\n\x08moreInfo\x18\x0b \x03(\x0b\x32\x30.fkhp.data.layer.executor.models.MoreProductInfo\x12\x43\n\x0cmedicineInfo\x18\x0c \x03(\x0b\x32-.fkhp.data.layer.executor.models.MedicineInfo\x12?\n\nreturnInfo\x18\r \x01(\x0b\x32+.fkhp.data.layer.executor.models.ReturnInfo\x12\x1a\n\x12productDescription\x18\x0e \x01(\t\x12\x11\n\tproductId\x18\x0f \x01(\t\x12\r\n\x05\x62rand\x18\x10 \x01(\t\x12\x18\n\x10\x65ncodedProductId\x18\x11 \x01(\t\x12\x43\n\x0c\x63\x61tegoryInfo\x18\x12 \x01(\x0b\x32-.fkhp.data.layer.executor.models.CategoryInfo\x12\x46\n\x0fsubCategoryInfo\x18\x13 \x01(\x0b\x32-.fkhp.data.layer.executor.models.CategoryInfo\"(\n\x0c\x43\x61tegoryInfo\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t**\n\x0bProductType\x12\x0c\n\x08MEDICINE\x10\x00\x12\r\n\tHOUSEHOLD\x10\x01\x42#\n\x1f\x66khp.data.layer.executor.modelsP\x01\x62\x06proto3')
  ,
  dependencies=[executor_dot_models_dot_multiMediaInfo__pb2.DESCRIPTOR,executor_dot_models_dot_saltInfo__pb2.DESCRIPTOR,executor_dot_models_dot_varietyInfo__pb2.DESCRIPTOR,executor_dot_models_dot_moreProductInfo__pb2.DESCRIPTOR,executor_dot_models_dot_medicineInfo__pb2.DESCRIPTOR,executor_dot_models_dot_returnInfo__pb2.DESCRIPTOR,])

_PRODUCTTYPE = _descriptor.EnumDescriptor(
  name='ProductType',
  full_name='fkhp.data.layer.executor.models.ProductType',
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
  serialized_start=1182,
  serialized_end=1224,
)
_sym_db.RegisterEnumDescriptor(_PRODUCTTYPE)

ProductType = enum_type_wrapper.EnumTypeWrapper(_PRODUCTTYPE)
MEDICINE = 0
HOUSEHOLD = 1



_PRODUCTINFO = _descriptor.Descriptor(
  name='ProductInfo',
  full_name='fkhp.data.layer.executor.models.ProductInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='productType', full_name='fkhp.data.layer.executor.models.ProductInfo.productType', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='prescriptionRequired', full_name='fkhp.data.layer.executor.models.ProductInfo.prescriptionRequired', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='multiMediaInfo', full_name='fkhp.data.layer.executor.models.ProductInfo.multiMediaInfo', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='productName', full_name='fkhp.data.layer.executor.models.ProductInfo.productName', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='strength', full_name='fkhp.data.layer.executor.models.ProductInfo.strength', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='saltInfo', full_name='fkhp.data.layer.executor.models.ProductInfo.saltInfo', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='expiryDate', full_name='fkhp.data.layer.executor.models.ProductInfo.expiryDate', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dosageForm', full_name='fkhp.data.layer.executor.models.ProductInfo.dosageForm', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='varietyInfo', full_name='fkhp.data.layer.executor.models.ProductInfo.varietyInfo', index=8,
      number=9, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='manufacturingGroupName', full_name='fkhp.data.layer.executor.models.ProductInfo.manufacturingGroupName', index=9,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='moreInfo', full_name='fkhp.data.layer.executor.models.ProductInfo.moreInfo', index=10,
      number=11, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='medicineInfo', full_name='fkhp.data.layer.executor.models.ProductInfo.medicineInfo', index=11,
      number=12, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='returnInfo', full_name='fkhp.data.layer.executor.models.ProductInfo.returnInfo', index=12,
      number=13, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='productDescription', full_name='fkhp.data.layer.executor.models.ProductInfo.productDescription', index=13,
      number=14, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='productId', full_name='fkhp.data.layer.executor.models.ProductInfo.productId', index=14,
      number=15, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='brand', full_name='fkhp.data.layer.executor.models.ProductInfo.brand', index=15,
      number=16, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='encodedProductId', full_name='fkhp.data.layer.executor.models.ProductInfo.encodedProductId', index=16,
      number=17, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='categoryInfo', full_name='fkhp.data.layer.executor.models.ProductInfo.categoryInfo', index=17,
      number=18, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='subCategoryInfo', full_name='fkhp.data.layer.executor.models.ProductInfo.subCategoryInfo', index=18,
      number=19, type=11, cpp_type=10, label=1,
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
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=285,
  serialized_end=1138,
)


_CATEGORYINFO = _descriptor.Descriptor(
  name='CategoryInfo',
  full_name='fkhp.data.layer.executor.models.CategoryInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='fkhp.data.layer.executor.models.CategoryInfo.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='fkhp.data.layer.executor.models.CategoryInfo.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=1140,
  serialized_end=1180,
)

_PRODUCTINFO.fields_by_name['productType'].enum_type = _PRODUCTTYPE
_PRODUCTINFO.fields_by_name['multiMediaInfo'].message_type = executor_dot_models_dot_multiMediaInfo__pb2._MULTIMEDIAINFO
_PRODUCTINFO.fields_by_name['saltInfo'].message_type = executor_dot_models_dot_saltInfo__pb2._SALTINFO
_PRODUCTINFO.fields_by_name['varietyInfo'].message_type = executor_dot_models_dot_varietyInfo__pb2._VARIETYINFO
_PRODUCTINFO.fields_by_name['moreInfo'].message_type = executor_dot_models_dot_moreProductInfo__pb2._MOREPRODUCTINFO
_PRODUCTINFO.fields_by_name['medicineInfo'].message_type = executor_dot_models_dot_medicineInfo__pb2._MEDICINEINFO
_PRODUCTINFO.fields_by_name['returnInfo'].message_type = executor_dot_models_dot_returnInfo__pb2._RETURNINFO
_PRODUCTINFO.fields_by_name['categoryInfo'].message_type = _CATEGORYINFO
_PRODUCTINFO.fields_by_name['subCategoryInfo'].message_type = _CATEGORYINFO
DESCRIPTOR.message_types_by_name['ProductInfo'] = _PRODUCTINFO
DESCRIPTOR.message_types_by_name['CategoryInfo'] = _CATEGORYINFO
DESCRIPTOR.enum_types_by_name['ProductType'] = _PRODUCTTYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ProductInfo = _reflection.GeneratedProtocolMessageType('ProductInfo', (_message.Message,), dict(
  DESCRIPTOR = _PRODUCTINFO,
  __module__ = 'executor.models.productInfo_pb2'
  # @@protoc_insertion_point(class_scope:fkhp.data.layer.executor.models.ProductInfo)
  ))
_sym_db.RegisterMessage(ProductInfo)

CategoryInfo = _reflection.GeneratedProtocolMessageType('CategoryInfo', (_message.Message,), dict(
  DESCRIPTOR = _CATEGORYINFO,
  __module__ = 'executor.models.productInfo_pb2'
  # @@protoc_insertion_point(class_scope:fkhp.data.layer.executor.models.CategoryInfo)
  ))
_sym_db.RegisterMessage(CategoryInfo)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)