# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: sonic_acl.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import ywrapper_pb2 as ywrapper__pb2
import yext_pb2 as yext__pb2
import enums_pb2 as enums__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='sonic_acl.proto',
  package='openconfig',
  syntax='proto3',
  serialized_options=b'\n\025com.nocsys.openconfig',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0fsonic_acl.proto\x12\nopenconfig\x1a\x0eywrapper.proto\x1a\nyext.proto\x1a\x0b\x65nums.proto\"\xed\x1d\n\x08SonicAcl\x12J\n\x08\x61\x63l_rule\x18\xc3\xf9\xe3\xfe\x01 \x01(\x0b\x32\x1c.openconfig.SonicAcl.AclRuleB\x16\x82\x41\x13/sonic-acl/acl-rule\x12M\n\tacl_table\x18\xc3\xdc\xee\xb9\x01 \x01(\x0b\x32\x1d.openconfig.SonicAcl.AclTableB\x17\x82\x41\x14/sonic-acl/acl-table\x1a\xa8\x16\n\x07\x41\x63lRule\x12l\n\racl_rule_list\x18\xce\xdf\xff\xa5\x01 \x03(\x0b\x32+.openconfig.SonicAcl.AclRule.AclRuleListKeyB$\x82\x41!/sonic-acl/acl-rule/acl-rule-list\x1a\xca\x13\n\x0b\x41\x63lRuleList\x12l\n\x11L4_DST_PORT_RANGE\x18\xbe\xb5\xe6\xd8\x01 \x01(\x0b\x32\x15.ywrapper.StringValueB6\x82\x41\x33/sonic-acl/acl-rule/acl-rule-list/L4_DST_PORT_RANGE\x12P\n\x04\x64scp\x18\xff\xb2\xef\xad\x01 \x01(\x0b\x32\x13.ywrapper.UintValueB)\x82\x41&/sonic-acl/acl-rule/acl-rule-list/dscp\x12V\n\x06\x64st_ip\x18\x96\x8f\xda\xd9\x01 \x01(\x0b\x32\x15.ywrapper.StringValueB+\x82\x41(/sonic-acl/acl-rule/acl-rule-list/dst-ip\x12W\n\x07\x64st_ip6\x18\x9a\x99\xe0: \x01(\x0b\x32\x15.ywrapper.StringValueB,\x82\x41)/sonic-acl/acl-rule/acl-rule-list/dst-ip6\x12^\n\nether_type\x18\xd0\xc6\x95\xc3\x01 \x01(\x0b\x32\x15.ywrapper.StringValueB/\x82\x41,/sonic-acl/acl-rule/acl-rule-list/ether-type\x12Z\n\ticmp_code\x18\xf0\xe1\x92\x83\x01 \x01(\x0b\x32\x13.ywrapper.UintValueB.\x82\x41+/sonic-acl/acl-rule/acl-rule-list/icmp-code\x12Y\n\ticmp_type\x18\xab\xa4\xde\x15 \x01(\x0b\x32\x13.ywrapper.UintValueB.\x82\x41+/sonic-acl/acl-rule/acl-rule-list/icmp-type\x12]\n\x0bicmpv6_code\x18\xaa\x99\xe0> \x01(\x0b\x32\x13.ywrapper.UintValueB0\x82\x41-/sonic-acl/acl-rule/acl-rule-list/icmpv6-code\x12]\n\x0bicmpv6_type\x18\xcd\x91\x95\x17 \x01(\x0b\x32\x13.ywrapper.UintValueB0\x82\x41-/sonic-acl/acl-rule/acl-rule-list/icmpv6-type\x12X\n\x08in_ports\x18\x87\xbe\xd1\xf8\x01 \x03(\x0b\x32\x13.ywrapper.UintValueB-\x82\x41*/sonic-acl/acl-rule/acl-rule-list/in-ports\x12j\n\x10inner_ether_type\x18\xf1\xbe\xea\x9c\x01 \x01(\x0b\x32\x15.ywrapper.StringValueB5\x82\x41\x32/sonic-acl/acl-rule/acl-rule-list/inner-ether-type\x12j\n\x11inner_ip_protocol\x18\xac\x9d\xaa\xbb\x01 \x01(\x0b\x32\x13.ywrapper.UintValueB6\x82\x41\x33/sonic-acl/acl-rule/acl-rule-list/inner-ip-protocol\x12j\n\x11inner_l4_dst_port\x18\xfa\xb3\xd0\xe2\x01 \x01(\x0b\x32\x13.ywrapper.UintValueB6\x82\x41\x33/sonic-acl/acl-rule/acl-rule-list/inner-l4-dst-port\x12i\n\x11inner_l4_src_port\x18\xfb\xe2\xeek \x01(\x0b\x32\x13.ywrapper.UintValueB6\x82\x41\x33/sonic-acl/acl-rule/acl-rule-list/inner-l4-src-port\x12^\n\x0bip_protocol\x18\xb3\xea\x8b\xdb\x01 \x01(\x0b\x32\x13.ywrapper.UintValueB0\x82\x41-/sonic-acl/acl-rule/acl-rule-list/ip-protocol\x12\\\n\x07ip_type\x18\xd3\xe7\xaf\x1e \x01(\x0e\x32\x1a.openconfig.SonicAclIpTypeB,\x82\x41)/sonic-acl/acl-rule/acl-rule-list/ip-type\x12^\n\x0bl4_dst_port\x18\xce\xc3\xad\x8f\x01 \x01(\x0b\x32\x13.ywrapper.UintValueB0\x82\x41-/sonic-acl/acl-rule/acl-rule-list/l4-dst-port\x12]\n\x0bl4_src_port\x18\xfb\xaf\xf5R \x01(\x0b\x32\x13.ywrapper.UintValueB0\x82\x41-/sonic-acl/acl-rule/acl-rule-list/l4-src-port\x12l\n\x11l4_src_port_range\x18\xf7\xe6\xa4\xfa\x01 \x01(\x0b\x32\x15.ywrapper.StringValueB6\x82\x41\x33/sonic-acl/acl-rule/acl-rule-list/l4-src-port-range\x12Z\n\tout_ports\x18\xcc\xb2\xcc\xff\x01 \x03(\x0b\x32\x13.ywrapper.UintValueB.\x82\x41+/sonic-acl/acl-rule/acl-rule-list/out-ports\x12o\n\rpacket_action\x18\xf0\xe4\xfb\xad\x01 \x01(\x0e\x32 .openconfig.SonicAclPacketActionB2\x82\x41//sonic-acl/acl-rule/acl-rule-list/packet-action\x12W\n\x08priority\x18\x9d\xd8\x89\n \x01(\x0b\x32\x13.ywrapper.UintValueB-\x82\x41*/sonic-acl/acl-rule/acl-rule-list/priority\x12V\n\x06src_ip\x18\xd7\xb0\xb1\xbe\x01 \x01(\x0b\x32\x15.ywrapper.StringValueB+\x82\x41(/sonic-acl/acl-rule/acl-rule-list/src-ip\x12X\n\x07src_ip6\x18\x9f\xcc\xc8\x90\x01 \x01(\x0b\x32\x15.ywrapper.StringValueB,\x82\x41)/sonic-acl/acl-rule/acl-rule-list/src_ip6\x12K\n\x02tc\x18\xb2\xfb\xf9q \x01(\x0b\x32\x13.ywrapper.UintValueB\'\x82\x41$/sonic-acl/acl-rule/acl-rule-list/tc\x12\\\n\ttcp_flags\x18\xfc\xbc\xd7\xea\x01 \x01(\x0b\x32\x15.ywrapper.StringValueB.\x82\x41+/sonic-acl/acl-rule/acl-rule-list/tcp-flags\x1a\xe1\x01\n\x0e\x41\x63lRuleListKey\x12K\n\x0e\x61\x63l_table_name\x18\x01 \x01(\tB3\x82\x41\x30/sonic-acl/acl-rule/acl-rule-list/acl-table-name\x12\x41\n\trule_name\x18\x02 \x01(\tB.\x82\x41+/sonic-acl/acl-rule/acl-rule-list/rule-name\x12?\n\racl_rule_list\x18\x03 \x01(\x0b\x32(.openconfig.SonicAcl.AclRule.AclRuleList\x1a\x9a\x06\n\x08\x41\x63lTable\x12q\n\x0e\x61\x63l_table_list\x18\xda\xf9\xa9\xb2\x01 \x03(\x0b\x32-.openconfig.SonicAcl.AclTable.AclTableListKeyB&\x82\x41#/sonic-acl/acl-table/acl-table-list\x1a\xf3\x03\n\x0c\x41\x63lTableList\x12\x62\n\x0bpolicy_desc\x18\xe3\x9f\xae\xfc\x01 \x01(\x0b\x32\x15.ywrapper.StringValueB2\x82\x41//sonic-acl/acl-table/acl-table-list/policy-desc\x12U\n\x05ports\x18\xdf\xdd\xf6Y \x03(\x0b\x32\x15.ywrapper.StringValueB,\x82\x41)/sonic-acl/acl-table/acl-table-list/ports\x12q\n\x05stage\x18\xe5\xe3\x82\x8b\x01 \x01(\x0e\x32\x30.openconfig.SonicAcl.AclTable.AclTableList.StageB,\x82\x41)/sonic-acl/acl-table/acl-table-list/stage\x12_\n\x04type\x18\xc9\x9f\x9d\xc0\x01 \x01(\x0e\x32 .openconfig.SonicAclAclTableTypeB+\x82\x41(/sonic-acl/acl-table/acl-table-list/type\"T\n\x05Stage\x12\x0f\n\x0bSTAGE_UNSET\x10\x00\x12\x1d\n\rSTAGE_INGRESS\x10\x01\x1a\n\x82\x41\x07INGRESS\x12\x1b\n\x0cSTAGE_EGRESS\x10\x02\x1a\t\x82\x41\x06\x45GRESS\x1a\xa4\x01\n\x0f\x41\x63lTableListKey\x12M\n\x0e\x61\x63l_table_name\x18\x01 \x01(\tB5\x82\x41\x32/sonic-acl/acl-table/acl-table-list/acl-table-name\x12\x42\n\x0e\x61\x63l_table_list\x18\x02 \x01(\x0b\x32*.openconfig.SonicAcl.AclTable.AclTableListB\x17\n\x15\x63om.nocsys.openconfigb\x06proto3'
  ,
  dependencies=[ywrapper__pb2.DESCRIPTOR,yext__pb2.DESCRIPTOR,enums__pb2.DESCRIPTOR,])



_SONICACL_ACLTABLE_ACLTABLELIST_STAGE = _descriptor.EnumDescriptor(
  name='Stage',
  full_name='openconfig.SonicAcl.AclTable.AclTableList.Stage',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='STAGE_UNSET', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='STAGE_INGRESS', index=1, number=1,
      serialized_options=b'\202A\007INGRESS',
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='STAGE_EGRESS', index=2, number=2,
      serialized_options=b'\202A\006EGRESS',
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=3643,
  serialized_end=3727,
)
_sym_db.RegisterEnumDescriptor(_SONICACL_ACLTABLE_ACLTABLELIST_STAGE)


_SONICACL_ACLRULE_ACLRULELIST = _descriptor.Descriptor(
  name='AclRuleList',
  full_name='openconfig.SonicAcl.AclRule.AclRuleList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='L4_DST_PORT_RANGE', full_name='openconfig.SonicAcl.AclRule.AclRuleList.L4_DST_PORT_RANGE', index=0,
      number=454662846, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\202A3/sonic-acl/acl-rule/acl-rule-list/L4_DST_PORT_RANGE', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='dscp', full_name='openconfig.SonicAcl.AclRule.AclRuleList.dscp', index=1,
      number=364632447, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\202A&/sonic-acl/acl-rule/acl-rule-list/dscp', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='dst_ip', full_name='openconfig.SonicAcl.AclRule.AclRuleList.dst_ip', index=2,
      number=456558486, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\202A(/sonic-acl/acl-rule/acl-rule-list/dst-ip', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='dst_ip6', full_name='openconfig.SonicAcl.AclRule.AclRuleList.dst_ip6', index=3,
      number=123210906, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\202A)/sonic-acl/acl-rule/acl-rule-list/dst-ip6', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ether_type', full_name='openconfig.SonicAcl.AclRule.AclRuleList.ether_type', index=4,
      number=409297744, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\202A,/sonic-acl/acl-rule/acl-rule-list/ether-type', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='icmp_code', full_name='openconfig.SonicAcl.AclRule.AclRuleList.icmp_code', index=5,
      number=275034352, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\202A+/sonic-acl/acl-rule/acl-rule-list/icmp-code', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='icmp_type', full_name='openconfig.SonicAcl.AclRule.AclRuleList.icmp_type', index=6,
      number=45584939, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\202A+/sonic-acl/acl-rule/acl-rule-list/icmp-type', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='icmpv6_code', full_name='openconfig.SonicAcl.AclRule.AclRuleList.icmpv6_code', index=7,
      number=131599530, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\202A-/sonic-acl/acl-rule/acl-rule-list/icmpv6-code', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='icmpv6_type', full_name='openconfig.SonicAcl.AclRule.AclRuleList.icmpv6_type', index=8,
      number=48580813, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\202A-/sonic-acl/acl-rule/acl-rule-list/icmpv6-type', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='in_ports', full_name='openconfig.SonicAcl.AclRule.AclRuleList.in_ports', index=9,
      number=521428743, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\202A*/sonic-acl/acl-rule/acl-rule-list/in-ports', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='inner_ether_type', full_name='openconfig.SonicAcl.AclRule.AclRuleList.inner_ether_type', index=10,
      number=328900465, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\202A2/sonic-acl/acl-rule/acl-rule-list/inner-ether-type', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='inner_ip_protocol', full_name='openconfig.SonicAcl.AclRule.AclRuleList.inner_ip_protocol', index=11,
      number=392859308, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\202A3/sonic-acl/acl-rule/acl-rule-list/inner-ip-protocol', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='inner_l4_dst_port', full_name='openconfig.SonicAcl.AclRule.AclRuleList.inner_l4_dst_port', index=12,
      number=475273722, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\202A3/sonic-acl/acl-rule/acl-rule-list/inner-l4-dst-port', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='inner_l4_src_port', full_name='openconfig.SonicAcl.AclRule.AclRuleList.inner_l4_src_port', index=13,
      number=226210171, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\202A3/sonic-acl/acl-rule/acl-rule-list/inner-l4-src-port', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ip_protocol', full_name='openconfig.SonicAcl.AclRule.AclRuleList.ip_protocol', index=14,
      number=459470131, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\202A-/sonic-acl/acl-rule/acl-rule-list/ip-protocol', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ip_type', full_name='openconfig.SonicAcl.AclRule.AclRuleList.ip_type', index=15,
      number=63697875, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\202A)/sonic-acl/acl-rule/acl-rule-list/ip-type', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='l4_dst_port', full_name='openconfig.SonicAcl.AclRule.AclRuleList.l4_dst_port', index=16,
      number=300638670, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\202A-/sonic-acl/acl-rule/acl-rule-list/l4-dst-port', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='l4_src_port', full_name='openconfig.SonicAcl.AclRule.AclRuleList.l4_src_port', index=17,
      number=173889531, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\202A-/sonic-acl/acl-rule/acl-rule-list/l4-src-port', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='l4_src_port_range', full_name='openconfig.SonicAcl.AclRule.AclRuleList.l4_src_port_range', index=18,
      number=524890999, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\202A3/sonic-acl/acl-rule/acl-rule-list/l4-src-port-range', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='out_ports', full_name='openconfig.SonicAcl.AclRule.AclRuleList.out_ports', index=19,
      number=536025420, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\202A+/sonic-acl/acl-rule/acl-rule-list/out-ports', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='packet_action', full_name='openconfig.SonicAcl.AclRule.AclRuleList.packet_action', index=20,
      number=364835440, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\202A//sonic-acl/acl-rule/acl-rule-list/packet-action', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='priority', full_name='openconfig.SonicAcl.AclRule.AclRuleList.priority', index=21,
      number=21130269, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\202A*/sonic-acl/acl-rule/acl-rule-list/priority', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='src_ip', full_name='openconfig.SonicAcl.AclRule.AclRuleList.src_ip', index=22,
      number=399267927, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\202A(/sonic-acl/acl-rule/acl-rule-list/src-ip', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='src_ip6', full_name='openconfig.SonicAcl.AclRule.AclRuleList.src_ip6', index=23,
      number=303179295, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\202A)/sonic-acl/acl-rule/acl-rule-list/src_ip6', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='tc', full_name='openconfig.SonicAcl.AclRule.AclRuleList.tc', index=24,
      number=238976434, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\202A$/sonic-acl/acl-rule/acl-rule-list/tc', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='tcp_flags', full_name='openconfig.SonicAcl.AclRule.AclRuleList.tcp_flags', index=25,
      number=492166780, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\202A+/sonic-acl/acl-rule/acl-rule-list/tcp-flags', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_end=2869,
)

_SONICACL_ACLRULE_ACLRULELISTKEY = _descriptor.Descriptor(
  name='AclRuleListKey',
  full_name='openconfig.SonicAcl.AclRule.AclRuleListKey',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='acl_table_name', full_name='openconfig.SonicAcl.AclRule.AclRuleListKey.acl_table_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\202A0/sonic-acl/acl-rule/acl-rule-list/acl-table-name', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='rule_name', full_name='openconfig.SonicAcl.AclRule.AclRuleListKey.rule_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\202A+/sonic-acl/acl-rule/acl-rule-list/rule-name', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='acl_rule_list', full_name='openconfig.SonicAcl.AclRule.AclRuleListKey.acl_rule_list', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=2872,
  serialized_end=3097,
)

_SONICACL_ACLRULE = _descriptor.Descriptor(
  name='AclRule',
  full_name='openconfig.SonicAcl.AclRule',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='acl_rule_list', full_name='openconfig.SonicAcl.AclRule.acl_rule_list', index=0,
      number=348123086, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\202A!/sonic-acl/acl-rule/acl-rule-list', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_SONICACL_ACLRULE_ACLRULELIST, _SONICACL_ACLRULE_ACLRULELISTKEY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=241,
  serialized_end=3097,
)

_SONICACL_ACLTABLE_ACLTABLELIST = _descriptor.Descriptor(
  name='AclTableList',
  full_name='openconfig.SonicAcl.AclTable.AclTableList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='policy_desc', full_name='openconfig.SonicAcl.AclTable.AclTableList.policy_desc', index=0,
      number=529240035, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\202A//sonic-acl/acl-table/acl-table-list/policy-desc', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ports', full_name='openconfig.SonicAcl.AclTable.AclTableList.ports', index=1,
      number=188591839, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\202A)/sonic-acl/acl-table/acl-table-list/ports', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='stage', full_name='openconfig.SonicAcl.AclTable.AclTableList.stage', index=2,
      number=291549669, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\202A)/sonic-acl/acl-table/acl-table-list/stage', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='type', full_name='openconfig.SonicAcl.AclTable.AclTableList.type', index=3,
      number=403132361, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\202A(/sonic-acl/acl-table/acl-table-list/type', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _SONICACL_ACLTABLE_ACLTABLELIST_STAGE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=3228,
  serialized_end=3727,
)

_SONICACL_ACLTABLE_ACLTABLELISTKEY = _descriptor.Descriptor(
  name='AclTableListKey',
  full_name='openconfig.SonicAcl.AclTable.AclTableListKey',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='acl_table_name', full_name='openconfig.SonicAcl.AclTable.AclTableListKey.acl_table_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\202A2/sonic-acl/acl-table/acl-table-list/acl-table-name', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='acl_table_list', full_name='openconfig.SonicAcl.AclTable.AclTableListKey.acl_table_list', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=3730,
  serialized_end=3894,
)

_SONICACL_ACLTABLE = _descriptor.Descriptor(
  name='AclTable',
  full_name='openconfig.SonicAcl.AclTable',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='acl_table_list', full_name='openconfig.SonicAcl.AclTable.acl_table_list', index=0,
      number=373980378, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\202A#/sonic-acl/acl-table/acl-table-list', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_SONICACL_ACLTABLE_ACLTABLELIST, _SONICACL_ACLTABLE_ACLTABLELISTKEY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=3100,
  serialized_end=3894,
)

_SONICACL = _descriptor.Descriptor(
  name='SonicAcl',
  full_name='openconfig.SonicAcl',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='acl_rule', full_name='openconfig.SonicAcl.acl_rule', index=0,
      number=534314179, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\202A\023/sonic-acl/acl-rule', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='acl_table', full_name='openconfig.SonicAcl.acl_table', index=1,
      number=389787203, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\202A\024/sonic-acl/acl-table', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_SONICACL_ACLRULE, _SONICACL_ACLTABLE, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=73,
  serialized_end=3894,
)

_SONICACL_ACLRULE_ACLRULELIST.fields_by_name['L4_DST_PORT_RANGE'].message_type = ywrapper__pb2._STRINGVALUE
_SONICACL_ACLRULE_ACLRULELIST.fields_by_name['dscp'].message_type = ywrapper__pb2._UINTVALUE
_SONICACL_ACLRULE_ACLRULELIST.fields_by_name['dst_ip'].message_type = ywrapper__pb2._STRINGVALUE
_SONICACL_ACLRULE_ACLRULELIST.fields_by_name['dst_ip6'].message_type = ywrapper__pb2._STRINGVALUE
_SONICACL_ACLRULE_ACLRULELIST.fields_by_name['ether_type'].message_type = ywrapper__pb2._STRINGVALUE
_SONICACL_ACLRULE_ACLRULELIST.fields_by_name['icmp_code'].message_type = ywrapper__pb2._UINTVALUE
_SONICACL_ACLRULE_ACLRULELIST.fields_by_name['icmp_type'].message_type = ywrapper__pb2._UINTVALUE
_SONICACL_ACLRULE_ACLRULELIST.fields_by_name['icmpv6_code'].message_type = ywrapper__pb2._UINTVALUE
_SONICACL_ACLRULE_ACLRULELIST.fields_by_name['icmpv6_type'].message_type = ywrapper__pb2._UINTVALUE
_SONICACL_ACLRULE_ACLRULELIST.fields_by_name['in_ports'].message_type = ywrapper__pb2._UINTVALUE
_SONICACL_ACLRULE_ACLRULELIST.fields_by_name['inner_ether_type'].message_type = ywrapper__pb2._STRINGVALUE
_SONICACL_ACLRULE_ACLRULELIST.fields_by_name['inner_ip_protocol'].message_type = ywrapper__pb2._UINTVALUE
_SONICACL_ACLRULE_ACLRULELIST.fields_by_name['inner_l4_dst_port'].message_type = ywrapper__pb2._UINTVALUE
_SONICACL_ACLRULE_ACLRULELIST.fields_by_name['inner_l4_src_port'].message_type = ywrapper__pb2._UINTVALUE
_SONICACL_ACLRULE_ACLRULELIST.fields_by_name['ip_protocol'].message_type = ywrapper__pb2._UINTVALUE
_SONICACL_ACLRULE_ACLRULELIST.fields_by_name['ip_type'].enum_type = enums__pb2._SONICACLIPTYPE
_SONICACL_ACLRULE_ACLRULELIST.fields_by_name['l4_dst_port'].message_type = ywrapper__pb2._UINTVALUE
_SONICACL_ACLRULE_ACLRULELIST.fields_by_name['l4_src_port'].message_type = ywrapper__pb2._UINTVALUE
_SONICACL_ACLRULE_ACLRULELIST.fields_by_name['l4_src_port_range'].message_type = ywrapper__pb2._STRINGVALUE
_SONICACL_ACLRULE_ACLRULELIST.fields_by_name['out_ports'].message_type = ywrapper__pb2._UINTVALUE
_SONICACL_ACLRULE_ACLRULELIST.fields_by_name['packet_action'].enum_type = enums__pb2._SONICACLPACKETACTION
_SONICACL_ACLRULE_ACLRULELIST.fields_by_name['priority'].message_type = ywrapper__pb2._UINTVALUE
_SONICACL_ACLRULE_ACLRULELIST.fields_by_name['src_ip'].message_type = ywrapper__pb2._STRINGVALUE
_SONICACL_ACLRULE_ACLRULELIST.fields_by_name['src_ip6'].message_type = ywrapper__pb2._STRINGVALUE
_SONICACL_ACLRULE_ACLRULELIST.fields_by_name['tc'].message_type = ywrapper__pb2._UINTVALUE
_SONICACL_ACLRULE_ACLRULELIST.fields_by_name['tcp_flags'].message_type = ywrapper__pb2._STRINGVALUE
_SONICACL_ACLRULE_ACLRULELIST.containing_type = _SONICACL_ACLRULE
_SONICACL_ACLRULE_ACLRULELISTKEY.fields_by_name['acl_rule_list'].message_type = _SONICACL_ACLRULE_ACLRULELIST
_SONICACL_ACLRULE_ACLRULELISTKEY.containing_type = _SONICACL_ACLRULE
_SONICACL_ACLRULE.fields_by_name['acl_rule_list'].message_type = _SONICACL_ACLRULE_ACLRULELISTKEY
_SONICACL_ACLRULE.containing_type = _SONICACL
_SONICACL_ACLTABLE_ACLTABLELIST.fields_by_name['policy_desc'].message_type = ywrapper__pb2._STRINGVALUE
_SONICACL_ACLTABLE_ACLTABLELIST.fields_by_name['ports'].message_type = ywrapper__pb2._STRINGVALUE
_SONICACL_ACLTABLE_ACLTABLELIST.fields_by_name['stage'].enum_type = _SONICACL_ACLTABLE_ACLTABLELIST_STAGE
_SONICACL_ACLTABLE_ACLTABLELIST.fields_by_name['type'].enum_type = enums__pb2._SONICACLACLTABLETYPE
_SONICACL_ACLTABLE_ACLTABLELIST.containing_type = _SONICACL_ACLTABLE
_SONICACL_ACLTABLE_ACLTABLELIST_STAGE.containing_type = _SONICACL_ACLTABLE_ACLTABLELIST
_SONICACL_ACLTABLE_ACLTABLELISTKEY.fields_by_name['acl_table_list'].message_type = _SONICACL_ACLTABLE_ACLTABLELIST
_SONICACL_ACLTABLE_ACLTABLELISTKEY.containing_type = _SONICACL_ACLTABLE
_SONICACL_ACLTABLE.fields_by_name['acl_table_list'].message_type = _SONICACL_ACLTABLE_ACLTABLELISTKEY
_SONICACL_ACLTABLE.containing_type = _SONICACL
_SONICACL.fields_by_name['acl_rule'].message_type = _SONICACL_ACLRULE
_SONICACL.fields_by_name['acl_table'].message_type = _SONICACL_ACLTABLE
DESCRIPTOR.message_types_by_name['SonicAcl'] = _SONICACL
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SonicAcl = _reflection.GeneratedProtocolMessageType('SonicAcl', (_message.Message,), {

  'AclRule' : _reflection.GeneratedProtocolMessageType('AclRule', (_message.Message,), {

    'AclRuleList' : _reflection.GeneratedProtocolMessageType('AclRuleList', (_message.Message,), {
      'DESCRIPTOR' : _SONICACL_ACLRULE_ACLRULELIST,
      '__module__' : 'sonic_acl_pb2'
      # @@protoc_insertion_point(class_scope:openconfig.SonicAcl.AclRule.AclRuleList)
      })
    ,

    'AclRuleListKey' : _reflection.GeneratedProtocolMessageType('AclRuleListKey', (_message.Message,), {
      'DESCRIPTOR' : _SONICACL_ACLRULE_ACLRULELISTKEY,
      '__module__' : 'sonic_acl_pb2'
      # @@protoc_insertion_point(class_scope:openconfig.SonicAcl.AclRule.AclRuleListKey)
      })
    ,
    'DESCRIPTOR' : _SONICACL_ACLRULE,
    '__module__' : 'sonic_acl_pb2'
    # @@protoc_insertion_point(class_scope:openconfig.SonicAcl.AclRule)
    })
  ,

  'AclTable' : _reflection.GeneratedProtocolMessageType('AclTable', (_message.Message,), {

    'AclTableList' : _reflection.GeneratedProtocolMessageType('AclTableList', (_message.Message,), {
      'DESCRIPTOR' : _SONICACL_ACLTABLE_ACLTABLELIST,
      '__module__' : 'sonic_acl_pb2'
      # @@protoc_insertion_point(class_scope:openconfig.SonicAcl.AclTable.AclTableList)
      })
    ,

    'AclTableListKey' : _reflection.GeneratedProtocolMessageType('AclTableListKey', (_message.Message,), {
      'DESCRIPTOR' : _SONICACL_ACLTABLE_ACLTABLELISTKEY,
      '__module__' : 'sonic_acl_pb2'
      # @@protoc_insertion_point(class_scope:openconfig.SonicAcl.AclTable.AclTableListKey)
      })
    ,
    'DESCRIPTOR' : _SONICACL_ACLTABLE,
    '__module__' : 'sonic_acl_pb2'
    # @@protoc_insertion_point(class_scope:openconfig.SonicAcl.AclTable)
    })
  ,
  'DESCRIPTOR' : _SONICACL,
  '__module__' : 'sonic_acl_pb2'
  # @@protoc_insertion_point(class_scope:openconfig.SonicAcl)
  })
_sym_db.RegisterMessage(SonicAcl)
_sym_db.RegisterMessage(SonicAcl.AclRule)
_sym_db.RegisterMessage(SonicAcl.AclRule.AclRuleList)
_sym_db.RegisterMessage(SonicAcl.AclRule.AclRuleListKey)
_sym_db.RegisterMessage(SonicAcl.AclTable)
_sym_db.RegisterMessage(SonicAcl.AclTable.AclTableList)
_sym_db.RegisterMessage(SonicAcl.AclTable.AclTableListKey)


DESCRIPTOR._options = None
_SONICACL_ACLRULE_ACLRULELIST.fields_by_name['L4_DST_PORT_RANGE']._options = None
_SONICACL_ACLRULE_ACLRULELIST.fields_by_name['dscp']._options = None
_SONICACL_ACLRULE_ACLRULELIST.fields_by_name['dst_ip']._options = None
_SONICACL_ACLRULE_ACLRULELIST.fields_by_name['dst_ip6']._options = None
_SONICACL_ACLRULE_ACLRULELIST.fields_by_name['ether_type']._options = None
_SONICACL_ACLRULE_ACLRULELIST.fields_by_name['icmp_code']._options = None
_SONICACL_ACLRULE_ACLRULELIST.fields_by_name['icmp_type']._options = None
_SONICACL_ACLRULE_ACLRULELIST.fields_by_name['icmpv6_code']._options = None
_SONICACL_ACLRULE_ACLRULELIST.fields_by_name['icmpv6_type']._options = None
_SONICACL_ACLRULE_ACLRULELIST.fields_by_name['in_ports']._options = None
_SONICACL_ACLRULE_ACLRULELIST.fields_by_name['inner_ether_type']._options = None
_SONICACL_ACLRULE_ACLRULELIST.fields_by_name['inner_ip_protocol']._options = None
_SONICACL_ACLRULE_ACLRULELIST.fields_by_name['inner_l4_dst_port']._options = None
_SONICACL_ACLRULE_ACLRULELIST.fields_by_name['inner_l4_src_port']._options = None
_SONICACL_ACLRULE_ACLRULELIST.fields_by_name['ip_protocol']._options = None
_SONICACL_ACLRULE_ACLRULELIST.fields_by_name['ip_type']._options = None
_SONICACL_ACLRULE_ACLRULELIST.fields_by_name['l4_dst_port']._options = None
_SONICACL_ACLRULE_ACLRULELIST.fields_by_name['l4_src_port']._options = None
_SONICACL_ACLRULE_ACLRULELIST.fields_by_name['l4_src_port_range']._options = None
_SONICACL_ACLRULE_ACLRULELIST.fields_by_name['out_ports']._options = None
_SONICACL_ACLRULE_ACLRULELIST.fields_by_name['packet_action']._options = None
_SONICACL_ACLRULE_ACLRULELIST.fields_by_name['priority']._options = None
_SONICACL_ACLRULE_ACLRULELIST.fields_by_name['src_ip']._options = None
_SONICACL_ACLRULE_ACLRULELIST.fields_by_name['src_ip6']._options = None
_SONICACL_ACLRULE_ACLRULELIST.fields_by_name['tc']._options = None
_SONICACL_ACLRULE_ACLRULELIST.fields_by_name['tcp_flags']._options = None
_SONICACL_ACLRULE_ACLRULELISTKEY.fields_by_name['acl_table_name']._options = None
_SONICACL_ACLRULE_ACLRULELISTKEY.fields_by_name['rule_name']._options = None
_SONICACL_ACLRULE.fields_by_name['acl_rule_list']._options = None
_SONICACL_ACLTABLE_ACLTABLELIST_STAGE.values_by_name["STAGE_INGRESS"]._options = None
_SONICACL_ACLTABLE_ACLTABLELIST_STAGE.values_by_name["STAGE_EGRESS"]._options = None
_SONICACL_ACLTABLE_ACLTABLELIST.fields_by_name['policy_desc']._options = None
_SONICACL_ACLTABLE_ACLTABLELIST.fields_by_name['ports']._options = None
_SONICACL_ACLTABLE_ACLTABLELIST.fields_by_name['stage']._options = None
_SONICACL_ACLTABLE_ACLTABLELIST.fields_by_name['type']._options = None
_SONICACL_ACLTABLE_ACLTABLELISTKEY.fields_by_name['acl_table_name']._options = None
_SONICACL_ACLTABLE.fields_by_name['acl_table_list']._options = None
_SONICACL.fields_by_name['acl_rule']._options = None
_SONICACL.fields_by_name['acl_table']._options = None
# @@protoc_insertion_point(module_scope)
