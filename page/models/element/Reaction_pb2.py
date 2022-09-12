# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: page/models/element/Reaction.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from page.models.enums import ReactionType_pb2 as page_dot_models_dot_enums_dot_ReactionType__pb2
from page.models.element import ElementContext_pb2 as page_dot_models_dot_element_dot_ElementContext__pb2
from page.models.element import PaginationContext_pb2 as page_dot_models_dot_element_dot_PaginationContext__pb2
from page.models.element import PostDataContext_pb2 as page_dot_models_dot_element_dot_PostDataContext__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='page/models/element/Reaction.proto',
  package='fkhp.page.layer.models.element',
  syntax='proto3',
  serialized_options=_b('\n\036fkhp.page.layer.models.elementP\001'),
  serialized_pb=_b('\n\"page/models/element/Reaction.proto\x12\x1e\x66khp.page.layer.models.element\x1a$page/models/enums/ReactionType.proto\x1a(page/models/element/ElementContext.proto\x1a+page/models/element/PaginationContext.proto\x1a)page/models/element/PostDataContext.proto\"\xb9\x03\n\x08Reaction\x12T\n\x0ereactionParams\x18\x01 \x03(\x0b\x32<.fkhp.page.layer.models.element.Reaction.ReactionParamsEntry\x12@\n\x0creactionType\x18\x02 \x01(\x0e\x32*.fkhp.page.layer.models.enums.ReactionType\x12\x46\n\x0e\x65lementContext\x18\x03 \x01(\x0b\x32..fkhp.page.layer.models.element.ElementContext\x12L\n\x11paginationContext\x18\x04 \x01(\x0b\x32\x31.fkhp.page.layer.models.element.PaginationContext\x12H\n\x0fpostDataContext\x18\x05 \x01(\x0b\x32/.fkhp.page.layer.models.element.PostDataContext\x1a\x35\n\x13ReactionParamsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x42\"\n\x1e\x66khp.page.layer.models.elementP\x01\x62\x06proto3')
  ,
  dependencies=[page_dot_models_dot_enums_dot_ReactionType__pb2.DESCRIPTOR,page_dot_models_dot_element_dot_ElementContext__pb2.DESCRIPTOR,page_dot_models_dot_element_dot_PaginationContext__pb2.DESCRIPTOR,page_dot_models_dot_element_dot_PostDataContext__pb2.DESCRIPTOR,])




_REACTION_REACTIONPARAMSENTRY = _descriptor.Descriptor(
  name='ReactionParamsEntry',
  full_name='fkhp.page.layer.models.element.Reaction.ReactionParamsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='fkhp.page.layer.models.element.Reaction.ReactionParamsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='fkhp.page.layer.models.element.Reaction.ReactionParamsEntry.value', index=1,
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
  serialized_start=627,
  serialized_end=680,
)

_REACTION = _descriptor.Descriptor(
  name='Reaction',
  full_name='fkhp.page.layer.models.element.Reaction',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='reactionParams', full_name='fkhp.page.layer.models.element.Reaction.reactionParams', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='reactionType', full_name='fkhp.page.layer.models.element.Reaction.reactionType', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='elementContext', full_name='fkhp.page.layer.models.element.Reaction.elementContext', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='paginationContext', full_name='fkhp.page.layer.models.element.Reaction.paginationContext', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='postDataContext', full_name='fkhp.page.layer.models.element.Reaction.postDataContext', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_REACTION_REACTIONPARAMSENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=239,
  serialized_end=680,
)

_REACTION_REACTIONPARAMSENTRY.containing_type = _REACTION
_REACTION.fields_by_name['reactionParams'].message_type = _REACTION_REACTIONPARAMSENTRY
_REACTION.fields_by_name['reactionType'].enum_type = page_dot_models_dot_enums_dot_ReactionType__pb2._REACTIONTYPE
_REACTION.fields_by_name['elementContext'].message_type = page_dot_models_dot_element_dot_ElementContext__pb2._ELEMENTCONTEXT
_REACTION.fields_by_name['paginationContext'].message_type = page_dot_models_dot_element_dot_PaginationContext__pb2._PAGINATIONCONTEXT
_REACTION.fields_by_name['postDataContext'].message_type = page_dot_models_dot_element_dot_PostDataContext__pb2._POSTDATACONTEXT
DESCRIPTOR.message_types_by_name['Reaction'] = _REACTION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Reaction = _reflection.GeneratedProtocolMessageType('Reaction', (_message.Message,), dict(

  ReactionParamsEntry = _reflection.GeneratedProtocolMessageType('ReactionParamsEntry', (_message.Message,), dict(
    DESCRIPTOR = _REACTION_REACTIONPARAMSENTRY,
    __module__ = 'page.models.element.Reaction_pb2'
    # @@protoc_insertion_point(class_scope:fkhp.page.layer.models.element.Reaction.ReactionParamsEntry)
    ))
  ,
  DESCRIPTOR = _REACTION,
  __module__ = 'page.models.element.Reaction_pb2'
  # @@protoc_insertion_point(class_scope:fkhp.page.layer.models.element.Reaction)
  ))
_sym_db.RegisterMessage(Reaction)
_sym_db.RegisterMessage(Reaction.ReactionParamsEntry)


DESCRIPTOR._options = None
_REACTION_REACTIONPARAMSENTRY._options = None
# @@protoc_insertion_point(module_scope)