# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: executor/models/fileInfo.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='executor/models/fileInfo.proto',
  package='fkhp.data.layer.executor.models',
  syntax='proto3',
  serialized_options=_b('\n\037fkhp.data.layer.executor.modelsP\001'),
  serialized_pb=_b('\n\x1e\x65xecutor/models/fileInfo.proto\x12\x1f\x66khp.data.layer.executor.models\"-\n\x08\x46ileInfo\x12\x0f\n\x07\x66ileUrl\x18\x01 \x01(\t\x12\x10\n\x08\x66ileName\x18\x02 \x01(\tB#\n\x1f\x66khp.data.layer.executor.modelsP\x01\x62\x06proto3')
)




_FILEINFO = _descriptor.Descriptor(
  name='FileInfo',
  full_name='fkhp.data.layer.executor.models.FileInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='fileUrl', full_name='fkhp.data.layer.executor.models.FileInfo.fileUrl', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='fileName', full_name='fkhp.data.layer.executor.models.FileInfo.fileName', index=1,
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
  serialized_start=67,
  serialized_end=112,
)

DESCRIPTOR.message_types_by_name['FileInfo'] = _FILEINFO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

FileInfo = _reflection.GeneratedProtocolMessageType('FileInfo', (_message.Message,), dict(
  DESCRIPTOR = _FILEINFO,
  __module__ = 'executor.models.fileInfo_pb2'
  # @@protoc_insertion_point(class_scope:fkhp.data.layer.executor.models.FileInfo)
  ))
_sym_db.RegisterMessage(FileInfo)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)