# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mediapipe/calculators/tensor/feedback_tensors_calculator.proto

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
  name='mediapipe/calculators/tensor/feedback_tensors_calculator.proto',
  package='mediapipe',
  syntax='proto2',
  serialized_pb=_b('\n>mediapipe/calculators/tensor/feedback_tensors_calculator.proto\x12\tmediapipe\x1a$mediapipe/framework/calculator.proto\"\xbb\x03\n FeedbackTensorsCalculatorOptions\x12V\n\x15\x66\x65\x65\x64\x62\x61\x63k_tensor_shape\x18\x01 \x01(\x0b\x32\x37.mediapipe.FeedbackTensorsCalculatorOptions.TensorShape\x12\x1f\n\x14num_feedback_tensors\x18\x02 \x01(\x05:\x01\x31\x12_\n\x08location\x18\x03 \x01(\x0e\x32\x43.mediapipe.FeedbackTensorsCalculatorOptions.FeedbackTensorsLocation:\x08\x41PPENDED\x1a\x1f\n\x0bTensorShape\x12\x10\n\x04\x64ims\x18\x01 \x03(\x05\x42\x02\x10\x01\"@\n\x17\x46\x65\x65\x64\x62\x61\x63kTensorsLocation\x12\x08\n\x04NONE\x10\x00\x12\r\n\tPREPENDED\x10\x01\x12\x0c\n\x08\x41PPENDED\x10\x02\x32Z\n\x03\x65xt\x12\x1c.mediapipe.CalculatorOptions\x18\xfc\xf9\xa0\xe2\x01 \x01(\x0b\x32+.mediapipe.FeedbackTensorsCalculatorOptions')
  ,
  dependencies=[mediapipe_dot_framework_dot_calculator__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_FEEDBACKTENSORSCALCULATOROPTIONS_FEEDBACKTENSORSLOCATION = _descriptor.EnumDescriptor(
  name='FeedbackTensorsLocation',
  full_name='mediapipe.FeedbackTensorsCalculatorOptions.FeedbackTensorsLocation',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NONE', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PREPENDED', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='APPENDED', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=403,
  serialized_end=467,
)
_sym_db.RegisterEnumDescriptor(_FEEDBACKTENSORSCALCULATOROPTIONS_FEEDBACKTENSORSLOCATION)


_FEEDBACKTENSORSCALCULATOROPTIONS_TENSORSHAPE = _descriptor.Descriptor(
  name='TensorShape',
  full_name='mediapipe.FeedbackTensorsCalculatorOptions.TensorShape',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='dims', full_name='mediapipe.FeedbackTensorsCalculatorOptions.TensorShape.dims', index=0,
      number=1, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\020\001'))),
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
  serialized_start=370,
  serialized_end=401,
)

_FEEDBACKTENSORSCALCULATOROPTIONS = _descriptor.Descriptor(
  name='FeedbackTensorsCalculatorOptions',
  full_name='mediapipe.FeedbackTensorsCalculatorOptions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='feedback_tensor_shape', full_name='mediapipe.FeedbackTensorsCalculatorOptions.feedback_tensor_shape', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='num_feedback_tensors', full_name='mediapipe.FeedbackTensorsCalculatorOptions.num_feedback_tensors', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='location', full_name='mediapipe.FeedbackTensorsCalculatorOptions.location', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=2,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
    _descriptor.FieldDescriptor(
      name='ext', full_name='mediapipe.FeedbackTensorsCalculatorOptions.ext', index=0,
      number=474496252, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=True, extension_scope=None,
      options=None),
  ],
  nested_types=[_FEEDBACKTENSORSCALCULATOROPTIONS_TENSORSHAPE, ],
  enum_types=[
    _FEEDBACKTENSORSCALCULATOROPTIONS_FEEDBACKTENSORSLOCATION,
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=116,
  serialized_end=559,
)

_FEEDBACKTENSORSCALCULATOROPTIONS_TENSORSHAPE.containing_type = _FEEDBACKTENSORSCALCULATOROPTIONS
_FEEDBACKTENSORSCALCULATOROPTIONS.fields_by_name['feedback_tensor_shape'].message_type = _FEEDBACKTENSORSCALCULATOROPTIONS_TENSORSHAPE
_FEEDBACKTENSORSCALCULATOROPTIONS.fields_by_name['location'].enum_type = _FEEDBACKTENSORSCALCULATOROPTIONS_FEEDBACKTENSORSLOCATION
_FEEDBACKTENSORSCALCULATOROPTIONS_FEEDBACKTENSORSLOCATION.containing_type = _FEEDBACKTENSORSCALCULATOROPTIONS
DESCRIPTOR.message_types_by_name['FeedbackTensorsCalculatorOptions'] = _FEEDBACKTENSORSCALCULATOROPTIONS

FeedbackTensorsCalculatorOptions = _reflection.GeneratedProtocolMessageType('FeedbackTensorsCalculatorOptions', (_message.Message,), dict(

  TensorShape = _reflection.GeneratedProtocolMessageType('TensorShape', (_message.Message,), dict(
    DESCRIPTOR = _FEEDBACKTENSORSCALCULATOROPTIONS_TENSORSHAPE,
    __module__ = 'mediapipe.calculators.tensor.feedback_tensors_calculator_pb2'
    # @@protoc_insertion_point(class_scope:mediapipe.FeedbackTensorsCalculatorOptions.TensorShape)
    ))
  ,
  DESCRIPTOR = _FEEDBACKTENSORSCALCULATOROPTIONS,
  __module__ = 'mediapipe.calculators.tensor.feedback_tensors_calculator_pb2'
  # @@protoc_insertion_point(class_scope:mediapipe.FeedbackTensorsCalculatorOptions)
  ))
_sym_db.RegisterMessage(FeedbackTensorsCalculatorOptions)
_sym_db.RegisterMessage(FeedbackTensorsCalculatorOptions.TensorShape)

_FEEDBACKTENSORSCALCULATOROPTIONS.extensions_by_name['ext'].message_type = _FEEDBACKTENSORSCALCULATOROPTIONS
mediapipe_dot_framework_dot_calculator__options__pb2.CalculatorOptions.RegisterExtension(_FEEDBACKTENSORSCALCULATOROPTIONS.extensions_by_name['ext'])

_FEEDBACKTENSORSCALCULATOROPTIONS_TENSORSHAPE.fields_by_name['dims'].has_options = True
_FEEDBACKTENSORSCALCULATOROPTIONS_TENSORSHAPE.fields_by_name['dims']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\020\001'))
# @@protoc_insertion_point(module_scope)
