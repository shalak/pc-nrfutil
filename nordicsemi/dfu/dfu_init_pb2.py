# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: dfu_init.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='dfu_init.proto',
  package='dfu',
  serialized_pb=_b('\n\x0e\x64\x66u_init.proto\x12\x03\x64\x66u\"t\n\x07\x63ommand\x12\'\n\x07op_code\x18\x01 \x01(\x0e\x32\x16.dfu.command.op_code_t\x12\x1e\n\x0binit_packet\x18\x02 \x01(\x0b\x32\t.dfu.init\" \n\top_code_t\x12\t\n\x05RESET\x10\x00\x12\x08\n\x04INIT\x10\x01\"\xec\x04\n\x04init\x12\x1e\n\nfw_version\x18\x01 \x01(\r:\n4294967295\x12\x1e\n\nhw_version\x18\x02 \x01(\r:\n4294967295\x12\x12\n\x06sd_req\x18\x03 \x03(\rB\x02\x10\x01\x12!\n\x04type\x18\x04 \x01(\x0e\x32\x13.dfu.init.fw_type_t\x12\x11\n\x07sd_size\x18\x0b \x01(\rH\x00\x12\x11\n\x07\x62l_size\x18\x0c \x01(\rH\x00\x12,\n\nsd_bl_size\x18\r \x01(\x0b\x32\x16.dfu.init.sd_bl_size_tH\x00\x12\x12\n\x08\x61pp_size\x18\x0e \x01(\rH\x00\x12(\n\thash_type\x18\x05 \x01(\x0e\x32\x15.dfu.init.hash_type_t\x12\x0c\n\x04hash\x18\x06 \x01(\x0c\x12\x32\n\x0esignature_type\x18\x07 \x01(\x0e\x32\x1a.dfu.init.signature_type_t\x12\x11\n\tsignatyre\x18\x08 \x01(\x0c\x1a\x30\n\x0csd_bl_size_t\x12\x0f\n\x07sd_size\x18\x01 \x02(\r\x12\x0f\n\x07\x62l_size\x18\x02 \x02(\r\"W\n\tfw_type_t\x12\x0e\n\nSOFTDEVICE\x10\x01\x12\x0e\n\nBOOTLOADER\x10\x02\x12\x19\n\x15SOFTDEVICE_BOOTLOADER\x10\x03\x12\x0f\n\x0b\x41PPLICATION\x10\x04\"/\n\x0bhash_type_t\x12\x0b\n\x07NO_HASH\x10\x00\x12\x07\n\x03\x43RC\x10\x01\x12\n\n\x06SHA128\x10\x02\";\n\x10signature_type_t\x12\x10\n\x0cNO_SIGNATURE\x10\x00\x12\x08\n\x04P256\x10\x01\x12\x0b\n\x07\x45\x44\x32\x35\x35\x31\x39\x10\x02*\x04\x08\t\x10\x0b\x42\x07\n\x05sizes')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_COMMAND_OP_CODE_T = _descriptor.EnumDescriptor(
  name='op_code_t',
  full_name='dfu.command.op_code_t',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='RESET', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INIT', index=1, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=107,
  serialized_end=139,
)
_sym_db.RegisterEnumDescriptor(_COMMAND_OP_CODE_T)

_INIT_FW_TYPE_T = _descriptor.EnumDescriptor(
  name='fw_type_t',
  full_name='dfu.init.fw_type_t',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='SOFTDEVICE', index=0, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BOOTLOADER', index=1, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SOFTDEVICE_BOOTLOADER', index=2, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='APPLICATION', index=3, number=4,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=550,
  serialized_end=637,
)
_sym_db.RegisterEnumDescriptor(_INIT_FW_TYPE_T)

_INIT_HASH_TYPE_T = _descriptor.EnumDescriptor(
  name='hash_type_t',
  full_name='dfu.init.hash_type_t',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NO_HASH', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CRC', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SHA128', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=639,
  serialized_end=686,
)
_sym_db.RegisterEnumDescriptor(_INIT_HASH_TYPE_T)

_INIT_SIGNATURE_TYPE_T = _descriptor.EnumDescriptor(
  name='signature_type_t',
  full_name='dfu.init.signature_type_t',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NO_SIGNATURE', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='P256', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ED25519', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=688,
  serialized_end=747,
)
_sym_db.RegisterEnumDescriptor(_INIT_SIGNATURE_TYPE_T)


_COMMAND = _descriptor.Descriptor(
  name='command',
  full_name='dfu.command',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='op_code', full_name='dfu.command.op_code', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='init_packet', full_name='dfu.command.init_packet', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _COMMAND_OP_CODE_T,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=23,
  serialized_end=139,
)


_INIT_SD_BL_SIZE_T = _descriptor.Descriptor(
  name='sd_bl_size_t',
  full_name='dfu.init.sd_bl_size_t',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='sd_size', full_name='dfu.init.sd_bl_size_t.sd_size', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='bl_size', full_name='dfu.init.sd_bl_size_t.bl_size', index=1,
      number=2, type=13, cpp_type=3, label=2,
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
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=500,
  serialized_end=548,
)

_INIT = _descriptor.Descriptor(
  name='init',
  full_name='dfu.init',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='fw_version', full_name='dfu.init.fw_version', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=True, default_value=4294967295,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='hw_version', full_name='dfu.init.hw_version', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=True, default_value=4294967295,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sd_req', full_name='dfu.init.sd_req', index=2,
      number=3, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\020\001'))),
    _descriptor.FieldDescriptor(
      name='type', full_name='dfu.init.type', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sd_size', full_name='dfu.init.sd_size', index=4,
      number=11, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='bl_size', full_name='dfu.init.bl_size', index=5,
      number=12, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sd_bl_size', full_name='dfu.init.sd_bl_size', index=6,
      number=13, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='app_size', full_name='dfu.init.app_size', index=7,
      number=14, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='hash_type', full_name='dfu.init.hash_type', index=8,
      number=5, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='hash', full_name='dfu.init.hash', index=9,
      number=6, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='signature_type', full_name='dfu.init.signature_type', index=10,
      number=7, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='signatyre', full_name='dfu.init.signatyre', index=11,
      number=8, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_INIT_SD_BL_SIZE_T, ],
  enum_types=[
    _INIT_FW_TYPE_T,
    _INIT_HASH_TYPE_T,
    _INIT_SIGNATURE_TYPE_T,
  ],
  options=None,
  is_extendable=True,
  extension_ranges=[(9, 11), ],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='sizes', full_name='dfu.init.sizes',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=142,
  serialized_end=762,
)

_COMMAND.fields_by_name['op_code'].enum_type = _COMMAND_OP_CODE_T
_COMMAND.fields_by_name['init_packet'].message_type = _INIT
_COMMAND_OP_CODE_T.containing_type = _COMMAND
_INIT_SD_BL_SIZE_T.containing_type = _INIT
_INIT.fields_by_name['type'].enum_type = _INIT_FW_TYPE_T
_INIT.fields_by_name['sd_bl_size'].message_type = _INIT_SD_BL_SIZE_T
_INIT.fields_by_name['hash_type'].enum_type = _INIT_HASH_TYPE_T
_INIT.fields_by_name['signature_type'].enum_type = _INIT_SIGNATURE_TYPE_T
_INIT_FW_TYPE_T.containing_type = _INIT
_INIT_HASH_TYPE_T.containing_type = _INIT
_INIT_SIGNATURE_TYPE_T.containing_type = _INIT
_INIT.oneofs_by_name['sizes'].fields.append(
  _INIT.fields_by_name['sd_size'])
_INIT.fields_by_name['sd_size'].containing_oneof = _INIT.oneofs_by_name['sizes']
_INIT.oneofs_by_name['sizes'].fields.append(
  _INIT.fields_by_name['bl_size'])
_INIT.fields_by_name['bl_size'].containing_oneof = _INIT.oneofs_by_name['sizes']
_INIT.oneofs_by_name['sizes'].fields.append(
  _INIT.fields_by_name['sd_bl_size'])
_INIT.fields_by_name['sd_bl_size'].containing_oneof = _INIT.oneofs_by_name['sizes']
_INIT.oneofs_by_name['sizes'].fields.append(
  _INIT.fields_by_name['app_size'])
_INIT.fields_by_name['app_size'].containing_oneof = _INIT.oneofs_by_name['sizes']
DESCRIPTOR.message_types_by_name['command'] = _COMMAND
DESCRIPTOR.message_types_by_name['init'] = _INIT

command = _reflection.GeneratedProtocolMessageType('command', (_message.Message,), dict(
  DESCRIPTOR = _COMMAND,
  __module__ = 'dfu_init_pb2'
  # @@protoc_insertion_point(class_scope:dfu.command)
  ))
_sym_db.RegisterMessage(command)

init = _reflection.GeneratedProtocolMessageType('init', (_message.Message,), dict(

  sd_bl_size_t = _reflection.GeneratedProtocolMessageType('sd_bl_size_t', (_message.Message,), dict(
    DESCRIPTOR = _INIT_SD_BL_SIZE_T,
    __module__ = 'dfu_init_pb2'
    # @@protoc_insertion_point(class_scope:dfu.init.sd_bl_size_t)
    ))
  ,
  DESCRIPTOR = _INIT,
  __module__ = 'dfu_init_pb2'
  # @@protoc_insertion_point(class_scope:dfu.init)
  ))
_sym_db.RegisterMessage(init)
_sym_db.RegisterMessage(init.sd_bl_size_t)


_INIT.fields_by_name['sd_req'].has_options = True
_INIT.fields_by_name['sd_req']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\020\001'))
# @@protoc_insertion_point(module_scope)
