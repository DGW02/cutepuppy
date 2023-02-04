# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mediapipe/calculators/core/split_vector_calculator.proto

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


DESCRIPTOR = _descriptor.FileDescriptor(
  name='mediapipe/calculators/core/split_vector_calculator.proto',
  package='mediapipe',
  syntax='proto2',
  serialized_pb=_b('\n8mediapipe/calculators/core/split_vector_calculator.proto\x12\tmediapipe\x1a$mediapipe/framework/calculator.proto\"#\n\x05Range\x12\r\n\x05\x62\x65gin\x18\x01 \x01(\x05\x12\x0b\n\x03\x65nd\x18\x02 \x01(\x05\"\xd4\x01\n\x1cSplitVectorCalculatorOptions\x12 \n\x06ranges\x18\x01 \x03(\x0b\x32\x10.mediapipe.Range\x12\x1b\n\x0c\x65lement_only\x18\x02 \x01(\x08:\x05\x66\x61lse\x12\x1e\n\x0f\x63ombine_outputs\x18\x03 \x01(\x08:\x05\x66\x61lse2U\n\x03\x65xt\x12\x1c.mediapipe.CalculatorOptions\x18\x8e\xed\xda{ \x01(\x0b\x32\'.mediapipe.SplitVectorCalculatorOptions')
  ,
  dependencies=[mediapipe_dot_framework_dot_calculator__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_RANGE = _descriptor.Descriptor(
  name='Range',
  full_name='mediapipe.Range',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='begin', full_name='mediapipe.Range.begin', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='end', full_name='mediapipe.Range.end', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
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
  serialized_start=109,
  serialized_end=144,
)


_SPLITVECTORCALCULATOROPTIONS = _descriptor.Descriptor(
  name='SplitVectorCalculatorOptions',
  full_name='mediapipe.SplitVectorCalculatorOptions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ranges', full_name='mediapipe.SplitVectorCalculatorOptions.ranges', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='element_only', full_name='mediapipe.SplitVectorCalculatorOptions.element_only', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='combine_outputs', full_name='mediapipe.SplitVectorCalculatorOptions.combine_outputs', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
    _descriptor.FieldDescriptor(
      name='ext', full_name='mediapipe.SplitVectorCalculatorOptions.ext', index=0,
      number=259438222, type=11, cpp_type=10, label=1,
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
  serialized_start=147,
  serialized_end=359,
)

_SPLITVECTORCALCULATOROPTIONS.fields_by_name['ranges'].message_type = _RANGE
DESCRIPTOR.message_types_by_name['Range'] = _RANGE
DESCRIPTOR.message_types_by_name['SplitVectorCalculatorOptions'] = _SPLITVECTORCALCULATOROPTIONS

Range = _reflection.GeneratedProtocolMessageType('Range', (_message.Message,), dict(
  DESCRIPTOR = _RANGE,
  __module__ = 'mediapipe.calculators.core.split_vector_calculator_pb2'
  # @@protoc_insertion_point(class_scope:mediapipe.Range)
  ))
_sym_db.RegisterMessage(Range)

SplitVectorCalculatorOptions = _reflection.GeneratedProtocolMessageType('SplitVectorCalculatorOptions', (_message.Message,), dict(
  DESCRIPTOR = _SPLITVECTORCALCULATOROPTIONS,
  __module__ = 'mediapipe.calculators.core.split_vector_calculator_pb2'
  # @@protoc_insertion_point(class_scope:mediapipe.SplitVectorCalculatorOptions)
  ))
_sym_db.RegisterMessage(SplitVectorCalculatorOptions)

_SPLITVECTORCALCULATOROPTIONS.extensions_by_name['ext'].message_type = _SPLITVECTORCALCULATOROPTIONS
mediapipe_dot_framework_dot_calculator__options__pb2.CalculatorOptions.RegisterExtension(_SPLITVECTORCALCULATOROPTIONS.extensions_by_name['ext'])

# @@protoc_insertion_point(module_scope)
