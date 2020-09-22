# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: appcommon.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='appcommon.proto',
  package='distributed_match_engine',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0f\x61ppcommon.proto\x12\x18\x64istributed_match_engine\"\xa9\x01\n\x07\x41ppPort\x12/\n\x05proto\x18\x01 \x01(\x0e\x32 .distributed_match_engine.LProto\x12\x15\n\rinternal_port\x18\x02 \x01(\x05\x12\x13\n\x0bpublic_port\x18\x03 \x01(\x05\x12\x13\n\x0b\x66qdn_prefix\x18\x05 \x01(\t\x12\x10\n\x08\x65nd_port\x18\x06 \x01(\x05\x12\x0b\n\x03tls\x18\x07 \x01(\x08\x12\r\n\x05nginx\x18\x08 \x01(\x08\"A\n\x07Latency\x12\x0b\n\x03\x61vg\x18\x01 \x01(\x01\x12\x0b\n\x03min\x18\x02 \x01(\x01\x12\x0b\n\x03max\x18\x03 \x01(\x01\x12\x0f\n\x07std_dev\x18\x04 \x01(\x01*?\n\x06LProto\x12\x13\n\x0fL_PROTO_UNKNOWN\x10\x00\x12\x0f\n\x0bL_PROTO_TCP\x10\x01\x12\x0f\n\x0bL_PROTO_UDP\x10\x02\x62\x06proto3'
)

_LPROTO = _descriptor.EnumDescriptor(
  name='LProto',
  full_name='distributed_match_engine.LProto',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='L_PROTO_UNKNOWN', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='L_PROTO_TCP', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='L_PROTO_UDP', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=284,
  serialized_end=347,
)
_sym_db.RegisterEnumDescriptor(_LPROTO)

LProto = enum_type_wrapper.EnumTypeWrapper(_LPROTO)
L_PROTO_UNKNOWN = 0
L_PROTO_TCP = 1
L_PROTO_UDP = 2



_APPPORT = _descriptor.Descriptor(
  name='AppPort',
  full_name='distributed_match_engine.AppPort',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='proto', full_name='distributed_match_engine.AppPort.proto', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='internal_port', full_name='distributed_match_engine.AppPort.internal_port', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='public_port', full_name='distributed_match_engine.AppPort.public_port', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='fqdn_prefix', full_name='distributed_match_engine.AppPort.fqdn_prefix', index=3,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='end_port', full_name='distributed_match_engine.AppPort.end_port', index=4,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='tls', full_name='distributed_match_engine.AppPort.tls', index=5,
      number=7, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='nginx', full_name='distributed_match_engine.AppPort.nginx', index=6,
      number=8, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=46,
  serialized_end=215,
)


_LATENCY = _descriptor.Descriptor(
  name='Latency',
  full_name='distributed_match_engine.Latency',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='avg', full_name='distributed_match_engine.Latency.avg', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='min', full_name='distributed_match_engine.Latency.min', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='max', full_name='distributed_match_engine.Latency.max', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='std_dev', full_name='distributed_match_engine.Latency.std_dev', index=3,
      number=4, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_start=217,
  serialized_end=282,
)

_APPPORT.fields_by_name['proto'].enum_type = _LPROTO
DESCRIPTOR.message_types_by_name['AppPort'] = _APPPORT
DESCRIPTOR.message_types_by_name['Latency'] = _LATENCY
DESCRIPTOR.enum_types_by_name['LProto'] = _LPROTO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AppPort = _reflection.GeneratedProtocolMessageType('AppPort', (_message.Message,), {
  'DESCRIPTOR' : _APPPORT,
  '__module__' : 'appcommon_pb2'
  # @@protoc_insertion_point(class_scope:distributed_match_engine.AppPort)
  })
_sym_db.RegisterMessage(AppPort)

Latency = _reflection.GeneratedProtocolMessageType('Latency', (_message.Message,), {
  'DESCRIPTOR' : _LATENCY,
  '__module__' : 'appcommon_pb2'
  # @@protoc_insertion_point(class_scope:distributed_match_engine.Latency)
  })
_sym_db.RegisterMessage(Latency)


# @@protoc_insertion_point(module_scope)
