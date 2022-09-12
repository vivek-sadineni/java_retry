# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: executor/response/NearestAreaViewResponse.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from executor.models import actionResponse_pb2 as executor_dot_models_dot_actionResponse__pb2
from executor.models import nearestAreaInfo_pb2 as executor_dot_models_dot_nearestAreaInfo__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='executor/response/NearestAreaViewResponse.proto',
  package='fkhp.data.layer.executor.response',
  syntax='proto3',
  serialized_options=_b('\n!fkhp.data.layer.executor.responseP\001'),
  serialized_pb=_b('\n/executor/response/NearestAreaViewResponse.proto\x12!fkhp.data.layer.executor.response\x1a$executor/models/actionResponse.proto\x1a%executor/models/nearestAreaInfo.proto\"\xb2\x01\n\x17NearestAreaViewResponse\x12G\n\x0e\x61\x63tionResponse\x18\x01 \x01(\x0b\x32/.fkhp.data.layer.executor.models.ActionResponse\x12N\n\x0e\x64omainResponse\x18\x02 \x01(\x0b\x32\x36.fkhp.data.layer.executor.response.NearestAreaResponse\"Y\n\x13NearestAreaResponse\x12\x42\n\x08\x61reaList\x18\x01 \x03(\x0b\x32\x30.fkhp.data.layer.executor.models.NearestAreaInfoB%\n!fkhp.data.layer.executor.responseP\x01\x62\x06proto3')
  ,
  dependencies=[executor_dot_models_dot_actionResponse__pb2.DESCRIPTOR,executor_dot_models_dot_nearestAreaInfo__pb2.DESCRIPTOR,])




_NEARESTAREAVIEWRESPONSE = _descriptor.Descriptor(
  name='NearestAreaViewResponse',
  full_name='fkhp.data.layer.executor.response.NearestAreaViewResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='actionResponse', full_name='fkhp.data.layer.executor.response.NearestAreaViewResponse.actionResponse', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='domainResponse', full_name='fkhp.data.layer.executor.response.NearestAreaViewResponse.domainResponse', index=1,
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
  serialized_start=164,
  serialized_end=342,
)


_NEARESTAREARESPONSE = _descriptor.Descriptor(
  name='NearestAreaResponse',
  full_name='fkhp.data.layer.executor.response.NearestAreaResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='areaList', full_name='fkhp.data.layer.executor.response.NearestAreaResponse.areaList', index=0,
      number=1, type=11, cpp_type=10, label=3,
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
  serialized_start=344,
  serialized_end=433,
)

_NEARESTAREAVIEWRESPONSE.fields_by_name['actionResponse'].message_type = executor_dot_models_dot_actionResponse__pb2._ACTIONRESPONSE
_NEARESTAREAVIEWRESPONSE.fields_by_name['domainResponse'].message_type = _NEARESTAREARESPONSE
_NEARESTAREARESPONSE.fields_by_name['areaList'].message_type = executor_dot_models_dot_nearestAreaInfo__pb2._NEARESTAREAINFO
DESCRIPTOR.message_types_by_name['NearestAreaViewResponse'] = _NEARESTAREAVIEWRESPONSE
DESCRIPTOR.message_types_by_name['NearestAreaResponse'] = _NEARESTAREARESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

NearestAreaViewResponse = _reflection.GeneratedProtocolMessageType('NearestAreaViewResponse', (_message.Message,), dict(
  DESCRIPTOR = _NEARESTAREAVIEWRESPONSE,
  __module__ = 'executor.response.NearestAreaViewResponse_pb2'
  # @@protoc_insertion_point(class_scope:fkhp.data.layer.executor.response.NearestAreaViewResponse)
  ))
_sym_db.RegisterMessage(NearestAreaViewResponse)

NearestAreaResponse = _reflection.GeneratedProtocolMessageType('NearestAreaResponse', (_message.Message,), dict(
  DESCRIPTOR = _NEARESTAREARESPONSE,
  __module__ = 'executor.response.NearestAreaViewResponse_pb2'
  # @@protoc_insertion_point(class_scope:fkhp.data.layer.executor.response.NearestAreaResponse)
  ))
_sym_db.RegisterMessage(NearestAreaResponse)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
