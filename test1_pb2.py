# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: test1.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='test1.proto',
  package='test1',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0btest1.proto\x12\x05test1\"\x14\n\x04Text\x12\x0c\n\x04text\x18\x01 \x01(\t\"\x16\n\x05\x41udio\x12\r\n\x05\x61udio\x18\x01 \x01(\x0c\x32;\n\x0e\x41udioStreaming\x12)\n\x08GetAudio\x12\x0b.test1.Text\x1a\x0c.test1.Audio\"\x00\x30\x01\x62\x06proto3'
)




_TEXT = _descriptor.Descriptor(
  name='Text',
  full_name='test1.Text',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='text', full_name='test1.Text.text', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=22,
  serialized_end=42,
)


_AUDIO = _descriptor.Descriptor(
  name='Audio',
  full_name='test1.Audio',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='audio', full_name='test1.Audio.audio', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=44,
  serialized_end=66,
)

DESCRIPTOR.message_types_by_name['Text'] = _TEXT
DESCRIPTOR.message_types_by_name['Audio'] = _AUDIO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Text = _reflection.GeneratedProtocolMessageType('Text', (_message.Message,), {
  'DESCRIPTOR' : _TEXT,
  '__module__' : 'test1_pb2'
  # @@protoc_insertion_point(class_scope:test1.Text)
  })
_sym_db.RegisterMessage(Text)

Audio = _reflection.GeneratedProtocolMessageType('Audio', (_message.Message,), {
  'DESCRIPTOR' : _AUDIO,
  '__module__' : 'test1_pb2'
  # @@protoc_insertion_point(class_scope:test1.Audio)
  })
_sym_db.RegisterMessage(Audio)



_AUDIOSTREAMING = _descriptor.ServiceDescriptor(
  name='AudioStreaming',
  full_name='test1.AudioStreaming',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=68,
  serialized_end=127,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetAudio',
    full_name='test1.AudioStreaming.GetAudio',
    index=0,
    containing_service=None,
    input_type=_TEXT,
    output_type=_AUDIO,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_AUDIOSTREAMING)

DESCRIPTOR.services_by_name['AudioStreaming'] = _AUDIOSTREAMING

# @@protoc_insertion_point(module_scope)