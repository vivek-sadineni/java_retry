# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: executor/response/MyPrescriptionViewResponse.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from executor.models import userInfo_pb2 as executor_dot_models_dot_userInfo__pb2
from executor.models import doctorInfo_pb2 as executor_dot_models_dot_doctorInfo__pb2
from executor.models import fileInfo_pb2 as executor_dot_models_dot_fileInfo__pb2
from executor.models import prescriptionDetailInfo_pb2 as executor_dot_models_dot_prescriptionDetailInfo__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='executor/response/MyPrescriptionViewResponse.proto',
  package='fkhp.data.layer.executor.response',
  syntax='proto3',
  serialized_options=_b('\n!fkhp.data.layer.executor.responseP\001'),
  serialized_pb=_b('\n2executor/response/MyPrescriptionViewResponse.proto\x12!fkhp.data.layer.executor.response\x1a\x19google/protobuf/any.proto\x1a\x1e\x65xecutor/models/userInfo.proto\x1a executor/models/doctorInfo.proto\x1a\x1e\x65xecutor/models/fileInfo.proto\x1a,executor/models/prescriptionDetailInfo.proto\"e\n\x1aMyPrescriptionViewResponse\x12G\n\rprescriptions\x18\x02 \x03(\x0b\x32\x30.fkhp.data.layer.executor.response.Prescriptions\"l\n\rPrescriptions\x12\x0c\n\x04\x64\x61te\x18\x01 \x01(\t\x12M\n\x10prescriptionList\x18\x02 \x03(\x0b\x32\x33.fkhp.data.layer.executor.response.PrescriptionList\"\xb5\x02\n\x10PrescriptionList\x12;\n\x08userInfo\x18\x01 \x01(\x0b\x32).fkhp.data.layer.executor.models.UserInfo\x12?\n\ndoctorInfo\x18\x02 \x01(\x0b\x32+.fkhp.data.layer.executor.models.DoctorInfo\x12;\n\x08\x66ileInfo\x18\x03 \x01(\x0b\x32).fkhp.data.layer.executor.models.FileInfo\x12Q\n\x10prescriptionInfo\x18\x04 \x01(\x0b\x32\x37.fkhp.data.layer.executor.models.PrescriptionDetailInfo\x12\x13\n\x0bPatientName\x18\x05 \x01(\tB%\n!fkhp.data.layer.executor.responseP\x01\x62\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_any__pb2.DESCRIPTOR,executor_dot_models_dot_userInfo__pb2.DESCRIPTOR,executor_dot_models_dot_doctorInfo__pb2.DESCRIPTOR,executor_dot_models_dot_fileInfo__pb2.DESCRIPTOR,executor_dot_models_dot_prescriptionDetailInfo__pb2.DESCRIPTOR,])




_MYPRESCRIPTIONVIEWRESPONSE = _descriptor.Descriptor(
  name='MyPrescriptionViewResponse',
  full_name='fkhp.data.layer.executor.response.MyPrescriptionViewResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='prescriptions', full_name='fkhp.data.layer.executor.response.MyPrescriptionViewResponse.prescriptions', index=0,
      number=2, type=11, cpp_type=10, label=3,
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
  serialized_start=260,
  serialized_end=361,
)


_PRESCRIPTIONS = _descriptor.Descriptor(
  name='Prescriptions',
  full_name='fkhp.data.layer.executor.response.Prescriptions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='date', full_name='fkhp.data.layer.executor.response.Prescriptions.date', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='prescriptionList', full_name='fkhp.data.layer.executor.response.Prescriptions.prescriptionList', index=1,
      number=2, type=11, cpp_type=10, label=3,
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
  serialized_start=363,
  serialized_end=471,
)


_PRESCRIPTIONLIST = _descriptor.Descriptor(
  name='PrescriptionList',
  full_name='fkhp.data.layer.executor.response.PrescriptionList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='userInfo', full_name='fkhp.data.layer.executor.response.PrescriptionList.userInfo', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='doctorInfo', full_name='fkhp.data.layer.executor.response.PrescriptionList.doctorInfo', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='fileInfo', full_name='fkhp.data.layer.executor.response.PrescriptionList.fileInfo', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='prescriptionInfo', full_name='fkhp.data.layer.executor.response.PrescriptionList.prescriptionInfo', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='PatientName', full_name='fkhp.data.layer.executor.response.PrescriptionList.PatientName', index=4,
      number=5, type=9, cpp_type=9, label=1,
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
  serialized_start=474,
  serialized_end=783,
)

_MYPRESCRIPTIONVIEWRESPONSE.fields_by_name['prescriptions'].message_type = _PRESCRIPTIONS
_PRESCRIPTIONS.fields_by_name['prescriptionList'].message_type = _PRESCRIPTIONLIST
_PRESCRIPTIONLIST.fields_by_name['userInfo'].message_type = executor_dot_models_dot_userInfo__pb2._USERINFO
_PRESCRIPTIONLIST.fields_by_name['doctorInfo'].message_type = executor_dot_models_dot_doctorInfo__pb2._DOCTORINFO
_PRESCRIPTIONLIST.fields_by_name['fileInfo'].message_type = executor_dot_models_dot_fileInfo__pb2._FILEINFO
_PRESCRIPTIONLIST.fields_by_name['prescriptionInfo'].message_type = executor_dot_models_dot_prescriptionDetailInfo__pb2._PRESCRIPTIONDETAILINFO
DESCRIPTOR.message_types_by_name['MyPrescriptionViewResponse'] = _MYPRESCRIPTIONVIEWRESPONSE
DESCRIPTOR.message_types_by_name['Prescriptions'] = _PRESCRIPTIONS
DESCRIPTOR.message_types_by_name['PrescriptionList'] = _PRESCRIPTIONLIST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

MyPrescriptionViewResponse = _reflection.GeneratedProtocolMessageType('MyPrescriptionViewResponse', (_message.Message,), dict(
  DESCRIPTOR = _MYPRESCRIPTIONVIEWRESPONSE,
  __module__ = 'executor.response.MyPrescriptionViewResponse_pb2'
  # @@protoc_insertion_point(class_scope:fkhp.data.layer.executor.response.MyPrescriptionViewResponse)
  ))
_sym_db.RegisterMessage(MyPrescriptionViewResponse)

Prescriptions = _reflection.GeneratedProtocolMessageType('Prescriptions', (_message.Message,), dict(
  DESCRIPTOR = _PRESCRIPTIONS,
  __module__ = 'executor.response.MyPrescriptionViewResponse_pb2'
  # @@protoc_insertion_point(class_scope:fkhp.data.layer.executor.response.Prescriptions)
  ))
_sym_db.RegisterMessage(Prescriptions)

PrescriptionList = _reflection.GeneratedProtocolMessageType('PrescriptionList', (_message.Message,), dict(
  DESCRIPTOR = _PRESCRIPTIONLIST,
  __module__ = 'executor.response.MyPrescriptionViewResponse_pb2'
  # @@protoc_insertion_point(class_scope:fkhp.data.layer.executor.response.PrescriptionList)
  ))
_sym_db.RegisterMessage(PrescriptionList)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
