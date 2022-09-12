# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: executor/response/ProductPageViewResponse.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from executor.models import listingInfo_pb2 as executor_dot_models_dot_listingInfo__pb2
from executor.models import productInfo_pb2 as executor_dot_models_dot_productInfo__pb2
from executor.models import ratingInfo_pb2 as executor_dot_models_dot_ratingInfo__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='executor/response/ProductPageViewResponse.proto',
  package='fkhp.data.layer.executor.response',
  syntax='proto3',
  serialized_options=_b('\n!fkhp.data.layer.executor.responseP\001'),
  serialized_pb=_b('\n/executor/response/ProductPageViewResponse.proto\x12!fkhp.data.layer.executor.response\x1a!executor/models/listingInfo.proto\x1a!executor/models/productInfo.proto\x1a executor/models/ratingInfo.proto\"b\n\x17ProductPageViewResponse\x12G\n\rproductDetail\x18\x02 \x01(\x0b\x32\x30.fkhp.data.layer.executor.response.ProductDetail\"\xdd\x01\n\rProductDetail\x12\x41\n\x0blistingInfo\x18\x01 \x01(\x0b\x32,.fkhp.data.layer.executor.models.ListingInfo\x12\x41\n\x0bproductInfo\x18\x02 \x01(\x0b\x32,.fkhp.data.layer.executor.models.ProductInfo\x12\x46\n\x11ratingsAndReviews\x18\x03 \x01(\x0b\x32+.fkhp.data.layer.executor.models.RatingInfoB%\n!fkhp.data.layer.executor.responseP\x01\x62\x06proto3')
  ,
  dependencies=[executor_dot_models_dot_listingInfo__pb2.DESCRIPTOR,executor_dot_models_dot_productInfo__pb2.DESCRIPTOR,executor_dot_models_dot_ratingInfo__pb2.DESCRIPTOR,])




_PRODUCTPAGEVIEWRESPONSE = _descriptor.Descriptor(
  name='ProductPageViewResponse',
  full_name='fkhp.data.layer.executor.response.ProductPageViewResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='productDetail', full_name='fkhp.data.layer.executor.response.ProductPageViewResponse.productDetail', index=0,
      number=2, type=11, cpp_type=10, label=1,
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
  serialized_start=190,
  serialized_end=288,
)


_PRODUCTDETAIL = _descriptor.Descriptor(
  name='ProductDetail',
  full_name='fkhp.data.layer.executor.response.ProductDetail',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='listingInfo', full_name='fkhp.data.layer.executor.response.ProductDetail.listingInfo', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='productInfo', full_name='fkhp.data.layer.executor.response.ProductDetail.productInfo', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ratingsAndReviews', full_name='fkhp.data.layer.executor.response.ProductDetail.ratingsAndReviews', index=2,
      number=3, type=11, cpp_type=10, label=1,
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
  serialized_start=291,
  serialized_end=512,
)

_PRODUCTPAGEVIEWRESPONSE.fields_by_name['productDetail'].message_type = _PRODUCTDETAIL
_PRODUCTDETAIL.fields_by_name['listingInfo'].message_type = executor_dot_models_dot_listingInfo__pb2._LISTINGINFO
_PRODUCTDETAIL.fields_by_name['productInfo'].message_type = executor_dot_models_dot_productInfo__pb2._PRODUCTINFO
_PRODUCTDETAIL.fields_by_name['ratingsAndReviews'].message_type = executor_dot_models_dot_ratingInfo__pb2._RATINGINFO
DESCRIPTOR.message_types_by_name['ProductPageViewResponse'] = _PRODUCTPAGEVIEWRESPONSE
DESCRIPTOR.message_types_by_name['ProductDetail'] = _PRODUCTDETAIL
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ProductPageViewResponse = _reflection.GeneratedProtocolMessageType('ProductPageViewResponse', (_message.Message,), dict(
  DESCRIPTOR = _PRODUCTPAGEVIEWRESPONSE,
  __module__ = 'executor.response.ProductPageViewResponse_pb2'
  # @@protoc_insertion_point(class_scope:fkhp.data.layer.executor.response.ProductPageViewResponse)
  ))
_sym_db.RegisterMessage(ProductPageViewResponse)

ProductDetail = _reflection.GeneratedProtocolMessageType('ProductDetail', (_message.Message,), dict(
  DESCRIPTOR = _PRODUCTDETAIL,
  __module__ = 'executor.response.ProductPageViewResponse_pb2'
  # @@protoc_insertion_point(class_scope:fkhp.data.layer.executor.response.ProductDetail)
  ))
_sym_db.RegisterMessage(ProductDetail)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)