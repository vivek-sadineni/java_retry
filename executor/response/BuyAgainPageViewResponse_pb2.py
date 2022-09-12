# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: executor/response/BuyAgainPageViewResponse.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from executor.models import listingInfo_pb2 as executor_dot_models_dot_listingInfo__pb2
from executor.models import buyAgainItem_pb2 as executor_dot_models_dot_buyAgainItem__pb2
from executor.models import pageMetaInfo_pb2 as executor_dot_models_dot_pageMetaInfo__pb2
from executor.models import buyAgainInfo_pb2 as executor_dot_models_dot_buyAgainInfo__pb2
from executor.models import statusInfo_pb2 as executor_dot_models_dot_statusInfo__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='executor/response/BuyAgainPageViewResponse.proto',
  package='fkhp.data.layer.executor.response',
  syntax='proto3',
  serialized_options=_b('\n!fkhp.data.layer.executor.responseP\001'),
  serialized_pb=_b('\n0executor/response/BuyAgainPageViewResponse.proto\x12!fkhp.data.layer.executor.response\x1a\x19google/protobuf/any.proto\x1a!executor/models/listingInfo.proto\x1a\"executor/models/buyAgainItem.proto\x1a\"executor/models/pageMetaInfo.proto\x1a\"executor/models/buyAgainInfo.proto\x1a executor/models/statusInfo.proto\"\xf3\x01\n\x18\x42uyAgainPageViewResponse\x12\x43\n\x0cpageMetaInfo\x18\x01 \x01(\x0b\x32-.fkhp.data.layer.executor.models.PageMetaInfo\x12?\n\nstatusInfo\x18\x02 \x01(\x0b\x32+.fkhp.data.layer.executor.models.StatusInfo\x12Q\n\x12\x62uyAgainPageDetail\x18\x03 \x03(\x0b\x32\x35.fkhp.data.layer.executor.response.BuyAgainPageDetail\"}\n\x12\x42uyAgainPageDetail\x12\x11\n\tpatientId\x18\x01 \x01(\t\x12?\n\x08listings\x18\x02 \x03(\x0b\x32-.fkhp.data.layer.executor.models.BuyAgainItem\x12\x13\n\x0bpatientName\x18\x03 \x01(\tB%\n!fkhp.data.layer.executor.responseP\x01\x62\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_any__pb2.DESCRIPTOR,executor_dot_models_dot_listingInfo__pb2.DESCRIPTOR,executor_dot_models_dot_buyAgainItem__pb2.DESCRIPTOR,executor_dot_models_dot_pageMetaInfo__pb2.DESCRIPTOR,executor_dot_models_dot_buyAgainInfo__pb2.DESCRIPTOR,executor_dot_models_dot_statusInfo__pb2.DESCRIPTOR,])




_BUYAGAINPAGEVIEWRESPONSE = _descriptor.Descriptor(
  name='BuyAgainPageViewResponse',
  full_name='fkhp.data.layer.executor.response.BuyAgainPageViewResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='pageMetaInfo', full_name='fkhp.data.layer.executor.response.BuyAgainPageViewResponse.pageMetaInfo', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='statusInfo', full_name='fkhp.data.layer.executor.response.BuyAgainPageViewResponse.statusInfo', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='buyAgainPageDetail', full_name='fkhp.data.layer.executor.response.BuyAgainPageViewResponse.buyAgainPageDetail', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=292,
  serialized_end=535,
)


_BUYAGAINPAGEDETAIL = _descriptor.Descriptor(
  name='BuyAgainPageDetail',
  full_name='fkhp.data.layer.executor.response.BuyAgainPageDetail',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='patientId', full_name='fkhp.data.layer.executor.response.BuyAgainPageDetail.patientId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='listings', full_name='fkhp.data.layer.executor.response.BuyAgainPageDetail.listings', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='patientName', full_name='fkhp.data.layer.executor.response.BuyAgainPageDetail.patientName', index=2,
      number=3, type=9, cpp_type=9, label=1,
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
  serialized_start=537,
  serialized_end=662,
)

_BUYAGAINPAGEVIEWRESPONSE.fields_by_name['pageMetaInfo'].message_type = executor_dot_models_dot_pageMetaInfo__pb2._PAGEMETAINFO
_BUYAGAINPAGEVIEWRESPONSE.fields_by_name['statusInfo'].message_type = executor_dot_models_dot_statusInfo__pb2._STATUSINFO
_BUYAGAINPAGEVIEWRESPONSE.fields_by_name['buyAgainPageDetail'].message_type = _BUYAGAINPAGEDETAIL
_BUYAGAINPAGEDETAIL.fields_by_name['listings'].message_type = executor_dot_models_dot_buyAgainItem__pb2._BUYAGAINITEM
DESCRIPTOR.message_types_by_name['BuyAgainPageViewResponse'] = _BUYAGAINPAGEVIEWRESPONSE
DESCRIPTOR.message_types_by_name['BuyAgainPageDetail'] = _BUYAGAINPAGEDETAIL
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

BuyAgainPageViewResponse = _reflection.GeneratedProtocolMessageType('BuyAgainPageViewResponse', (_message.Message,), dict(
  DESCRIPTOR = _BUYAGAINPAGEVIEWRESPONSE,
  __module__ = 'executor.response.BuyAgainPageViewResponse_pb2'
  # @@protoc_insertion_point(class_scope:fkhp.data.layer.executor.response.BuyAgainPageViewResponse)
  ))
_sym_db.RegisterMessage(BuyAgainPageViewResponse)

BuyAgainPageDetail = _reflection.GeneratedProtocolMessageType('BuyAgainPageDetail', (_message.Message,), dict(
  DESCRIPTOR = _BUYAGAINPAGEDETAIL,
  __module__ = 'executor.response.BuyAgainPageViewResponse_pb2'
  # @@protoc_insertion_point(class_scope:fkhp.data.layer.executor.response.BuyAgainPageDetail)
  ))
_sym_db.RegisterMessage(BuyAgainPageDetail)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)