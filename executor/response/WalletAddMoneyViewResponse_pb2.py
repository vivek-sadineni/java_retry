# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: executor/response/WalletAddMoneyViewResponse.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from executor.models import actionResponse_pb2 as executor_dot_models_dot_actionResponse__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='executor/response/WalletAddMoneyViewResponse.proto',
  package='fkhp.data.layer.executor.response',
  syntax='proto3',
  serialized_options=_b('\n!fkhp.data.layer.executor.responseP\001'),
  serialized_pb=_b('\n2executor/response/WalletAddMoneyViewResponse.proto\x12!fkhp.data.layer.executor.response\x1a$executor/models/actionResponse.proto\"\xbe\x01\n\x1aWalletAddMoneyViewResponse\x12G\n\x0e\x61\x63tionResponse\x18\x01 \x01(\x0b\x32/.fkhp.data.layer.executor.models.ActionResponse\x12W\n\x0e\x64omainResponse\x18\x02 \x01(\x0b\x32?.fkhp.data.layer.executor.response.WalletAddMoneyDomainResponse\"\xc3\x01\n\x1cWalletAddMoneyDomainResponse\x12_\n\x08\x66ormData\x18\x01 \x03(\x0b\x32M.fkhp.data.layer.executor.response.WalletAddMoneyDomainResponse.FormDataEntry\x12\x11\n\tactionUrl\x18\x02 \x01(\t\x1a/\n\rFormDataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x42%\n!fkhp.data.layer.executor.responseP\x01\x62\x06proto3')
  ,
  dependencies=[executor_dot_models_dot_actionResponse__pb2.DESCRIPTOR,])




_WALLETADDMONEYVIEWRESPONSE = _descriptor.Descriptor(
  name='WalletAddMoneyViewResponse',
  full_name='fkhp.data.layer.executor.response.WalletAddMoneyViewResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='actionResponse', full_name='fkhp.data.layer.executor.response.WalletAddMoneyViewResponse.actionResponse', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='domainResponse', full_name='fkhp.data.layer.executor.response.WalletAddMoneyViewResponse.domainResponse', index=1,
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
  serialized_start=128,
  serialized_end=318,
)


_WALLETADDMONEYDOMAINRESPONSE_FORMDATAENTRY = _descriptor.Descriptor(
  name='FormDataEntry',
  full_name='fkhp.data.layer.executor.response.WalletAddMoneyDomainResponse.FormDataEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='fkhp.data.layer.executor.response.WalletAddMoneyDomainResponse.FormDataEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='fkhp.data.layer.executor.response.WalletAddMoneyDomainResponse.FormDataEntry.value', index=1,
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
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=469,
  serialized_end=516,
)

_WALLETADDMONEYDOMAINRESPONSE = _descriptor.Descriptor(
  name='WalletAddMoneyDomainResponse',
  full_name='fkhp.data.layer.executor.response.WalletAddMoneyDomainResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='formData', full_name='fkhp.data.layer.executor.response.WalletAddMoneyDomainResponse.formData', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='actionUrl', full_name='fkhp.data.layer.executor.response.WalletAddMoneyDomainResponse.actionUrl', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_WALLETADDMONEYDOMAINRESPONSE_FORMDATAENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=321,
  serialized_end=516,
)

_WALLETADDMONEYVIEWRESPONSE.fields_by_name['actionResponse'].message_type = executor_dot_models_dot_actionResponse__pb2._ACTIONRESPONSE
_WALLETADDMONEYVIEWRESPONSE.fields_by_name['domainResponse'].message_type = _WALLETADDMONEYDOMAINRESPONSE
_WALLETADDMONEYDOMAINRESPONSE_FORMDATAENTRY.containing_type = _WALLETADDMONEYDOMAINRESPONSE
_WALLETADDMONEYDOMAINRESPONSE.fields_by_name['formData'].message_type = _WALLETADDMONEYDOMAINRESPONSE_FORMDATAENTRY
DESCRIPTOR.message_types_by_name['WalletAddMoneyViewResponse'] = _WALLETADDMONEYVIEWRESPONSE
DESCRIPTOR.message_types_by_name['WalletAddMoneyDomainResponse'] = _WALLETADDMONEYDOMAINRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

WalletAddMoneyViewResponse = _reflection.GeneratedProtocolMessageType('WalletAddMoneyViewResponse', (_message.Message,), dict(
  DESCRIPTOR = _WALLETADDMONEYVIEWRESPONSE,
  __module__ = 'executor.response.WalletAddMoneyViewResponse_pb2'
  # @@protoc_insertion_point(class_scope:fkhp.data.layer.executor.response.WalletAddMoneyViewResponse)
  ))
_sym_db.RegisterMessage(WalletAddMoneyViewResponse)

WalletAddMoneyDomainResponse = _reflection.GeneratedProtocolMessageType('WalletAddMoneyDomainResponse', (_message.Message,), dict(

  FormDataEntry = _reflection.GeneratedProtocolMessageType('FormDataEntry', (_message.Message,), dict(
    DESCRIPTOR = _WALLETADDMONEYDOMAINRESPONSE_FORMDATAENTRY,
    __module__ = 'executor.response.WalletAddMoneyViewResponse_pb2'
    # @@protoc_insertion_point(class_scope:fkhp.data.layer.executor.response.WalletAddMoneyDomainResponse.FormDataEntry)
    ))
  ,
  DESCRIPTOR = _WALLETADDMONEYDOMAINRESPONSE,
  __module__ = 'executor.response.WalletAddMoneyViewResponse_pb2'
  # @@protoc_insertion_point(class_scope:fkhp.data.layer.executor.response.WalletAddMoneyDomainResponse)
  ))
_sym_db.RegisterMessage(WalletAddMoneyDomainResponse)
_sym_db.RegisterMessage(WalletAddMoneyDomainResponse.FormDataEntry)


DESCRIPTOR._options = None
_WALLETADDMONEYDOMAINRESPONSE_FORMDATAENTRY._options = None
# @@protoc_insertion_point(module_scope)