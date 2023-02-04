# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mediapipe/tasks/cc/audio/audio_embedder/proto/audio_embedder_graph_options.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from mediapipe.framework import calculator_pb2 as mediapipe_dot_framework_dot_calculator__pb2
mediapipe_dot_framework_dot_calculator__options__pb2 = mediapipe_dot_framework_dot_calculator__pb2.mediapipe_dot_framework_dot_calculator__options__pb2
from mediapipe.framework import calculator_options_pb2 as mediapipe_dot_framework_dot_calculator__options__pb2
from mediapipe.tasks.cc.components.processors.proto import embedder_options_pb2 as mediapipe_dot_tasks_dot_cc_dot_components_dot_processors_dot_proto_dot_embedder__options__pb2
from mediapipe.tasks.cc.core.proto import base_options_pb2 as mediapipe_dot_tasks_dot_cc_dot_core_dot_proto_dot_base__options__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='mediapipe/tasks/cc/audio/audio_embedder/proto/audio_embedder_graph_options.proto',
  package='mediapipe.tasks.audio.audio_embedder.proto',
  syntax='proto2',
  serialized_pb=_b('\nPmediapipe/tasks/cc/audio/audio_embedder/proto/audio_embedder_graph_options.proto\x12*mediapipe.tasks.audio.audio_embedder.proto\x1a$mediapipe/framework/calculator.proto\x1a,mediapipe/framework/calculator_options.proto\x1a\x45mediapipe/tasks/cc/components/processors/proto/embedder_options.proto\x1a\x30mediapipe/tasks/cc/core/proto/base_options.proto\"\xa8\x02\n\x19\x41udioEmbedderGraphOptions\x12=\n\x0c\x62\x61se_options\x18\x01 \x01(\x0b\x32\'.mediapipe.tasks.core.proto.BaseOptions\x12V\n\x10\x65mbedder_options\x18\x02 \x01(\x0b\x32<.mediapipe.tasks.components.processors.proto.EmbedderOptions2t\n\x03\x65xt\x12\x1c.mediapipe.CalculatorOptions\x18\xe9\x85\xad\xe8\x01 \x01(\x0b\x32\x45.mediapipe.tasks.audio.audio_embedder.proto.AudioEmbedderGraphOptionsBV\n4com.google.mediapipe.tasks.audio.audioembedder.protoB\x1e\x41udioEmbedderGraphOptionsProto')
  ,
  dependencies=[mediapipe_dot_framework_dot_calculator__pb2.DESCRIPTOR,mediapipe_dot_framework_dot_calculator__options__pb2.DESCRIPTOR,mediapipe_dot_tasks_dot_cc_dot_components_dot_processors_dot_proto_dot_embedder__options__pb2.DESCRIPTOR,mediapipe_dot_tasks_dot_cc_dot_core_dot_proto_dot_base__options__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_AUDIOEMBEDDERGRAPHOPTIONS = _descriptor.Descriptor(
  name='AudioEmbedderGraphOptions',
  full_name='mediapipe.tasks.audio.audio_embedder.proto.AudioEmbedderGraphOptions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='base_options', full_name='mediapipe.tasks.audio.audio_embedder.proto.AudioEmbedderGraphOptions.base_options', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='embedder_options', full_name='mediapipe.tasks.audio.audio_embedder.proto.AudioEmbedderGraphOptions.embedder_options', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
    _descriptor.FieldDescriptor(
      name='ext', full_name='mediapipe.tasks.audio.audio_embedder.proto.AudioEmbedderGraphOptions.ext', index=0,
      number=487277289, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=True, extension_scope=None,
      options=None),
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=334,
  serialized_end=630,
)

_AUDIOEMBEDDERGRAPHOPTIONS.fields_by_name['base_options'].message_type = mediapipe_dot_tasks_dot_cc_dot_core_dot_proto_dot_base__options__pb2._BASEOPTIONS
_AUDIOEMBEDDERGRAPHOPTIONS.fields_by_name['embedder_options'].message_type = mediapipe_dot_tasks_dot_cc_dot_components_dot_processors_dot_proto_dot_embedder__options__pb2._EMBEDDEROPTIONS
DESCRIPTOR.message_types_by_name['AudioEmbedderGraphOptions'] = _AUDIOEMBEDDERGRAPHOPTIONS

AudioEmbedderGraphOptions = _reflection.GeneratedProtocolMessageType('AudioEmbedderGraphOptions', (_message.Message,), dict(
  DESCRIPTOR = _AUDIOEMBEDDERGRAPHOPTIONS,
  __module__ = 'mediapipe.tasks.cc.audio.audio_embedder.proto.audio_embedder_graph_options_pb2'
  # @@protoc_insertion_point(class_scope:mediapipe.tasks.audio.audio_embedder.proto.AudioEmbedderGraphOptions)
  ))
_sym_db.RegisterMessage(AudioEmbedderGraphOptions)

_AUDIOEMBEDDERGRAPHOPTIONS.extensions_by_name['ext'].message_type = _AUDIOEMBEDDERGRAPHOPTIONS
mediapipe_dot_framework_dot_calculator__options__pb2.CalculatorOptions.RegisterExtension(_AUDIOEMBEDDERGRAPHOPTIONS.extensions_by_name['ext'])

DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n4com.google.mediapipe.tasks.audio.audioembedder.protoB\036AudioEmbedderGraphOptionsProto'))
# @@protoc_insertion_point(module_scope)
