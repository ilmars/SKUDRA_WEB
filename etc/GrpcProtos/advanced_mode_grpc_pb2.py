# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: advanced_mode_grpc.proto
# Protobuf Python Version: 5.29.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    29,
    0,
    '',
    'advanced_mode_grpc.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
import decimal_value_pb2 as decimal__value__pb2
import shared_architecture_pb2 as shared__architecture__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x18\x61\x64vanced_mode_grpc.proto\x12\x12\x61\x64vanced_mode_grpc\x1a\x1cgoogle/api/annotations.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a\x13\x64\x65\x63imal_value.proto\x1a\x19shared_architecture.proto\"\x99\x01\n\x1c\x41\x64vancedModeHandshakeRequest\x12.\n\x08username\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x32\n\x0cserver_token\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x15\n\ris_guest_user\x18\x03 \x01(\x08\"\x95\x02\n\x1a\x41\x64vancedModeHandshakeReply\x12.\n\tlongitude\x18\x01 \x01(\x0b\x32\x1b.decimal_value.DecimalValue\x12-\n\x08latitude\x18\x02 \x01(\x0b\x32\x1b.decimal_value.DecimalValue\x12\x17\n\x0fuser_has_access\x18\x03 \x01(\x08\x12\x13\n\x0b\x64river_name\x18\x04 \x01(\t\x12\x34\n\x0e\x66rontend_token\x18\x05 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x34\n\treceivers\x18\x06 \x03(\x0b\x32!.shared_architecture.ReceiverInfo\"\xc3\x01\n\x0eRecordingReply\x12\x14\n\x0cis_measuring\x18\x01 \x01(\x08\x12U\n!updated_direct_measurement_config\x18\x02 \x01(\x0b\x32*.shared_architecture.MeasurementConfigGrpc\x12\x44\n\x10updated_schedule\x18\x03 \x01(\x0b\x32*.shared_architecture.MeasuringScheduleGrpc\"q\n\x10RecordingRequest\x12\x36\n\x10measurement_name\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12%\n\x1dis_enable_recording_requested\x18\x02 \x01(\x08\",\n\x16\x43onnectReceiverRequest\x12\x12\n\nreceiverId\x18\x01 \x01(\x05\"\xf2\x01\n\x18ReceiverCapabilitiesGrpc\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x19\n\x11\x64irection_finding\x18\x04 \x01(\x08\x12\x0b\n\x03itu\x18\x05 \x01(\x08\x12\x31\n\x0b\x64\x66_com_port\x18\x07 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x1b\n\x13is_rotator_attached\x18\x08 \x01(\x08\x12\x15\n\rpanorama_scan\x18\t \x01(\x08\x12\x1f\n\x17geographical_details_id\x18\n \x01(\x05\x12\x1a\n\x12receiver_access_id\x18\r \x01(\x05\"\xed\x04\n\x14\x43onnectReceiverReply\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x13\n\x0breceiver_id\x18\x02 \x01(\x05\x12\x37\n\x11\x64\x65vice_idn_string\x18\x03 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x36\n\x0c\x64\x65vice_state\x18\x04 \x01(\x0e\x32 .shared_architecture.DeviceState\x12\x36\n\x0b\x64\x65vice_info\x18\x05 \x01(\x0b\x32!.shared_architecture.ReceiverInfo\x12\x1b\n\x13measuring_is_active\x18\x06 \x01(\x08\x12K\n\x15receiver_capabilities\x18\x07 \x01(\x0b\x32,.advanced_mode_grpc.ReceiverCapabilitiesGrpc\x12:\n\x0c\x61ntenna_list\x18\x08 \x01(\x0b\x32$.advanced_mode_grpc.AntennaListReply\x12P\n\x1clast_used_measuring_schedule\x18\t \x01(\x0b\x32*.shared_architecture.MeasuringScheduleGrpc\x12P\n\x1clast_used_measurement_config\x18\n \x01(\x0b\x32*.shared_architecture.MeasurementConfigGrpc\x12<\n\rreceiver_mode\x18\x0b \x01(\x0e\x32%.shared_architecture.ReceiverModeGrpc\"\x9d\x01\n\x0fUserInformation\x12\x15\n\ris_guest_user\x18\x01 \x01(\x08\x12.\n\x08username\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12.\n\x08password\x18\x03 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x13\n\x0bremember_me\x18\x04 \x01(\x08\"\x8d\x01\n\x15PossibleSettingValues\x12\x45\n\x06values\x18\x01 \x03(\x0b\x32\x35.advanced_mode_grpc.PossibleSettingValues.ValuesEntry\x1a-\n\x0bValuesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\x14\n\x12\x41llSettingsRequest\"\x88\x03\n\x10\x41llSettingsReply\x12\x44\n\x08settings\x18\x01 \x03(\x0b\x32\x32.advanced_mode_grpc.AllSettingsReply.SettingsEntry\x12`\n\x17possible_setting_values\x18\x02 \x03(\x0b\x32?.advanced_mode_grpc.AllSettingsReply.PossibleSettingValuesEntry\x12\x32\n\rrequested_key\x18\x03 \x01(\x0b\x32\x1b.google.protobuf.Int32Value\x1a/\n\rSettingsEntry\x12\x0b\n\x03key\x18\x01 \x01(\x05\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1ag\n\x1aPossibleSettingValuesEntry\x12\x0b\n\x03key\x18\x01 \x01(\x05\x12\x38\n\x05value\x18\x02 \x01(\x0b\x32).advanced_mode_grpc.PossibleSettingValues:\x02\x38\x01\"g\n\x1c\x43hangeReceiverSettingRequest\x12\x12\n\nsettingKey\x18\x01 \x01(\x05\x12\x33\n\rsetting_value\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.StringValue\"\xab\x01\n\x10\x41ntennaListReply\x12?\n\x10\x61ntenna_accesses\x18\x01 \x03(\x0b\x32%.advanced_mode_grpc.AntennaAccessGrpc\x12\x39\n\x14\x63onnected_antenna_id\x18\x02 \x01(\x0b\x32\x1b.google.protobuf.Int32Value\x12\x1b\n\x13is_rotator_attached\x18\x03 \x01(\x08\"\xf1\x01\n\x11\x41ntennaAccessGrpc\x12\n\n\x02id\x18\x01 \x01(\x05\x12*\n\x04name\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12:\n\x0cpolarization\x18\x03 \x01(\x0e\x32$.advanced_mode_grpc.PolarizationGrpc\x12\x33\n\rmin_frequency\x18\x04 \x01(\x0b\x32\x1c.google.protobuf.DoubleValue\x12\x33\n\rmax_frequency\x18\x05 \x01(\x0b\x32\x1c.google.protobuf.DoubleValue\"G\n\x14SwitchAntennaRequest\x12/\n\nantenna_id\x18\x01 \x01(\x0b\x32\x1b.google.protobuf.Int32Value\"\xd1\x02\n\x12ReceiverAccessGrpc\x12\n\n\x02id\x18\x01 \x01(\x05\x12*\n\x04name\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x30\n\nip_address\x18\x03 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x10\n\x08url_port\x18\x04 \x01(\x05\x12K\n\x15receiver_capabilities\x18\x05 \x01(\x0b\x32,.advanced_mode_grpc.ReceiverCapabilitiesGrpc\x12\x38\n\x0ereceiver_state\x18\x06 \x01(\x0e\x32 .shared_architecture.DeviceState\x12\x38\n\rreceiver_type\x18\x07 \x01(\x0e\x32!.shared_architecture.ReceiverType\"\xc1\x03\n&NewSimpleModePresetCreationRequestGrpc\x12\x34\n\x0eminFrequencyHz\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.DoubleValue\x12\x34\n\x0emaxFrequencyHz\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.DoubleValue\x12\x44\n\x0e\x62\x61ndwidth_type\x18\x03 \x01(\x0e\x32,.shared_architecture.SimpleModeBandwidthType\x12\x44\n\x0emeasuring_mode\x18\x04 \x01(\x0e\x32,.shared_architecture.SimpleModeMeasuringMode\x12P\n\x14\x61ntenna_polarization\x18\x05 \x01(\x0e\x32\x32.shared_architecture.SimpleModeAntennaPolarization\x12M\n\x12\x61ntennaAttenuation\x18\x06 \x01(\x0e\x32\x31.shared_architecture.SimpleModeAntennaAttenuation\"\xc9\x04\n\x13MeasuringPresetGrpc\x12\n\n\x02id\x18\x01 \x01(\x05\x12*\n\x04name\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12.\n\ncreated_at\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x30\n\x0clast_used_at\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12 \n\x18is_created_automatically\x18\x05 \x01(\x08\x12\x46\n\x12measurement_config\x18\x06 \x01(\x0b\x32*.shared_architecture.MeasurementConfigGrpc\x12=\n\x0e\x61ntenna_access\x18\x07 \x01(\x0b\x32%.advanced_mode_grpc.AntennaAccessGrpc\x12?\n\x0freceiver_access\x18\x08 \x01(\x0b\x32&.advanced_mode_grpc.ReceiverAccessGrpc\x12\x34\n\x0ename_with_date\x18\t \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12G\n\x08settings\x18\n \x03(\x0b\x32\x35.advanced_mode_grpc.MeasuringPresetGrpc.SettingsEntry\x1a/\n\rSettingsEntry\x12\x0b\n\x03key\x18\x01 \x01(\x05\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"]\n\x18MeasuringPresetListReply\x12\x41\n\x10MeasuringPresets\x18\x01 \x03(\x0b\x32\'.advanced_mode_grpc.MeasuringPresetGrpc\"N\n\x17\x43hangeDeviceModeRequest\x12\x33\n\x04mode\x18\x01 \x01(\x0e\x32%.shared_architecture.ReceiverModeGrpc\"]\n\x15\x43hangeDeviceModeReply\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x33\n\rerror_message\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.StringValue\"C\n\x14ScpiExecutionRequest\x12+\n\x05query\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.StringValue\"S\n\x12ScpiExecutionReply\x12,\n\x06\x61nswer\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x0f\n\x07success\x18\x02 \x01(\x08\"h\n\x1eStartScheduledMeasuringRequest\x12\x46\n\x12measuring_schedule\x18\x01 \x01(\x0b\x32*.shared_architecture.MeasuringScheduleGrpc\"e\n\x1bStartDirectMeasuringRequest\x12\x46\n\x12measurement_config\x18\x01 \x01(\x0b\x32*.shared_architecture.MeasurementConfigGrpc\"B\n\x12StopMeasuringReply\x12,\n\x06reason\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.StringValue\"J\n\x0eRotorAngleGrpc\x12\r\n\x05\x61ngle\x18\x01 \x01(\x05\x12\x15\n\rrotor_enabled\x18\x02 \x01(\x08\x12\x12\n\nis_invalid\x18\x03 \x01(\x08\"\xb9\x01\n\x14RotatorAlignmentGrpc\x12\x33\n\x07\x61zimuth\x18\x01 \x01(\x0b\x32\".advanced_mode_grpc.RotorAngleGrpc\x12\x38\n\x0cpolarization\x18\x02 \x01(\x0b\x32\".advanced_mode_grpc.RotorAngleGrpc\x12\x32\n\x06height\x18\x03 \x01(\x0b\x32\".advanced_mode_grpc.RotorAngleGrpc\"\xb9\x03\n\x13\x41lignmentLimitsGrpc\x12\x37\n\x0bmin_azimuth\x18\x01 \x01(\x0b\x32\".advanced_mode_grpc.RotorAngleGrpc\x12\x37\n\x0bmax_azimuth\x18\x02 \x01(\x0b\x32\".advanced_mode_grpc.RotorAngleGrpc\x12<\n\x10min_polarization\x18\x03 \x01(\x0b\x32\".advanced_mode_grpc.RotorAngleGrpc\x12<\n\x10max_polarization\x18\x04 \x01(\x0b\x32\".advanced_mode_grpc.RotorAngleGrpc\x12\x36\n\nmin_height\x18\x05 \x01(\x0b\x32\".advanced_mode_grpc.RotorAngleGrpc\x12\x36\n\nmax_height\x18\x06 \x01(\x0b\x32\".advanced_mode_grpc.RotorAngleGrpc\x12\x19\n\x11\x64\x65vice_recognized\x18\x07 \x01(\x08\x12)\n\x03Idn\x18\x08 \x01(\x0b\x32\x1c.google.protobuf.StringValue\"^\n\x17RotatorAlignmentRequest\x12\x43\n\x11rotator_alignment\x18\x01 \x01(\x0b\x32(.advanced_mode_grpc.RotatorAlignmentGrpc\"\x9f\x01\n\x15RotatorAlignmentReply\x12\x43\n\x11rotator_alignment\x18\x01 \x01(\x0b\x32(.advanced_mode_grpc.RotatorAlignmentGrpc\x12\x41\n\x10\x61lignment_limits\x18\x02 \x01(\x0b\x32\'.advanced_mode_grpc.AlignmentLimitsGrpc\"\x91\x01\n\x1bStoreMeasuringPresetRequest\x12*\n\x04name\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x46\n\x12measurement_config\x18\x02 \x01(\x0b\x32*.shared_architecture.MeasurementConfigGrpc\"*\n\x1c\x44\x65leteMeasuringPresetRequest\x12\n\n\x02id\x18\x01 \x01(\x05\"\xa2\x01\n\x1cUpdateMeasuringPresetRequest\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x46\n\x12measurement_config\x18\x02 \x01(\x0b\x32*.shared_architecture.MeasurementConfigGrpc\x12.\n\x08new_name\x18\x03 \x01(\x0b\x32\x1c.google.protobuf.StringValue\"(\n\x11RemoteModeRequest\x12\x13\n\x0bremote_mode\x18\x01 \x01(\x08\"&\n\x0fRemoteModeReply\x12\x13\n\x0bremote_mode\x18\x01 \x01(\x08\":\n\x1b\x41pplyMeasuringPresetRequest\x12\x1b\n\x13measuring_preset_id\x18\x01 \x01(\x05\"\xed\x01\n\x19\x41pplyMeasuringPresetReply\x12:\n\x0c\x61ll_settings\x18\x01 \x01(\x0b\x32$.advanced_mode_grpc.AllSettingsReply\x12\x39\n\x14\x63onnected_antenna_id\x18\x02 \x01(\x0b\x32\x1b.google.protobuf.Int32Value\x12\x1b\n\x13is_rotator_attached\x18\x03 \x01(\x08\x12<\n\rreceiver_mode\x18\x04 \x01(\x0e\x32%.shared_architecture.ReceiverModeGrpc*K\n\x10PolarizationGrpc\x12\x0c\n\x08Vertical\x10\x00\x12\x0e\n\nHorizontal\x10\x01\x12\x19\n\x15VerticalAndHorizontal\x10\x02\x32\xf3\x15\n\x10\x41\x64vancedModeGrpc\x12\xb8\x01\n\x15\x41\x64vancedModeHandshake\x12\x30.advanced_mode_grpc.AdvancedModeHandshakeRequest\x1a..advanced_mode_grpc.AdvancedModeHandshakeReply\"=\x82\xd3\xe4\x93\x02\x37\"\x11/api/v1/handshake:\x01*Z\x1f\"\x1a/api/v1/advanced/handshake:\x01*\x12l\n\x14ReplyConnectReceiver\x12*.advanced_mode_grpc.ConnectReceiverRequest\x1a(.advanced_mode_grpc.ConnectReceiverReply\x12^\n\x12StreamMeasurements\x12\x16.google.protobuf.Empty\x1a..shared_architecture.MeasurementStreamDataGrpc0\x01\x12J\n\x18ReplyEnableLivestreaming\x12\x16.google.protobuf.Empty\x1a\x16.google.protobuf.Empty\x12K\n\x19ReplyDisableLivestreaming\x12\x16.google.protobuf.Empty\x1a\x16.google.protobuf.Empty\x12\x62\n\x12RequestAllSettings\x12&.advanced_mode_grpc.AllSettingsRequest\x1a$.advanced_mode_grpc.AllSettingsReply\x12x\n\x1eRequestToChangeReceiverSetting\x12\x30.advanced_mode_grpc.ChangeReceiverSettingRequest\x1a$.advanced_mode_grpc.AllSettingsReply\x12R\n\x12RequestAntennaList\x12\x16.google.protobuf.Empty\x1a$.advanced_mode_grpc.AntennaListReply\x12\x66\n\x14RequestChangeAntenna\x12(.advanced_mode_grpc.SwitchAntennaRequest\x1a$.advanced_mode_grpc.AntennaListReply\x12\x62\n\x1aRequestMeasuringPresetList\x12\x16.google.protobuf.Empty\x1a,.advanced_mode_grpc.MeasuringPresetListReply\x12q\n\x17RequestChangeDeviceMode\x12+.advanced_mode_grpc.ChangeDeviceModeRequest\x1a).advanced_mode_grpc.ChangeDeviceModeReply\x12h\n\x14RequestScpiExecution\x12(.advanced_mode_grpc.ScpiExecutionRequest\x1a&.advanced_mode_grpc.ScpiExecutionReply\x12l\n\x1eRequestStartScheduledMeasuring\x12\x32.advanced_mode_grpc.StartScheduledMeasuringRequest\x1a\x16.google.protobuf.Empty\x12\x66\n\x1bRequestStartDirectMeasuring\x12/.advanced_mode_grpc.StartDirectMeasuringRequest\x1a\x16.google.protobuf.Empty\x12V\n\x14RequestStopMeasuring\x12\x16.google.protobuf.Empty\x1a&.advanced_mode_grpc.StopMeasuringReply\x12\x45\n\x13RequestPresetDevice\x12\x16.google.protobuf.Empty\x1a\x16.google.protobuf.Empty\x12q\n\x17RequestRotatorAlignment\x12+.advanced_mode_grpc.RotatorAlignmentRequest\x1a).advanced_mode_grpc.RotatorAlignmentReply\x12\x44\n\x12RequestRotatorStop\x12\x16.google.protobuf.Empty\x1a\x16.google.protobuf.Empty\x12|\n\x1bRequestStoreMeasuringPreset\x12/.advanced_mode_grpc.StoreMeasuringPresetRequest\x1a,.advanced_mode_grpc.MeasuringPresetListReply\x12h\n\x1cRequestDeleteMeasuringPreset\x12\x30.advanced_mode_grpc.DeleteMeasuringPresetRequest\x1a\x16.google.protobuf.Empty\x12~\n\x1cRequestUpdateMeasuringPreset\x12\x30.advanced_mode_grpc.UpdateMeasuringPresetRequest\x1a,.advanced_mode_grpc.MeasuringPresetListReply\x12R\n\x11RequestRemoteMode\x12%.advanced_mode_grpc.RemoteModeRequest\x1a\x16.google.protobuf.Empty\x12}\n\x1bRequestApplyMeasuringPreset\x12/.advanced_mode_grpc.ApplyMeasuringPresetRequest\x1a-.advanced_mode_grpc.ApplyMeasuringPresetReply\x12\\\n\x10RequestRecording\x12$.advanced_mode_grpc.RecordingRequest\x1a\".advanced_mode_grpc.RecordingReply\x12\x43\n\x11RequestDisconnect\x12\x16.google.protobuf.Empty\x1a\x16.google.protobuf.Empty\x12\\\n\x17RequestCurrentAlignment\x12\x16.google.protobuf.Empty\x1a).advanced_mode_grpc.RotatorAlignmentReply\x12x\n\"RequestNewSimpleModePresetCreation\x12:.advanced_mode_grpc.NewSimpleModePresetCreationRequestGrpc\x1a\x16.google.protobuf.EmptyB\x13\xaa\x02\x10VASES.GrpcProtosb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'advanced_mode_grpc_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\252\002\020VASES.GrpcProtos'
  _globals['_POSSIBLESETTINGVALUES_VALUESENTRY']._loaded_options = None
  _globals['_POSSIBLESETTINGVALUES_VALUESENTRY']._serialized_options = b'8\001'
  _globals['_ALLSETTINGSREPLY_SETTINGSENTRY']._loaded_options = None
  _globals['_ALLSETTINGSREPLY_SETTINGSENTRY']._serialized_options = b'8\001'
  _globals['_ALLSETTINGSREPLY_POSSIBLESETTINGVALUESENTRY']._loaded_options = None
  _globals['_ALLSETTINGSREPLY_POSSIBLESETTINGVALUESENTRY']._serialized_options = b'8\001'
  _globals['_MEASURINGPRESETGRPC_SETTINGSENTRY']._loaded_options = None
  _globals['_MEASURINGPRESETGRPC_SETTINGSENTRY']._serialized_options = b'8\001'
  _globals['_ADVANCEDMODEGRPC'].methods_by_name['AdvancedModeHandshake']._loaded_options = None
  _globals['_ADVANCEDMODEGRPC'].methods_by_name['AdvancedModeHandshake']._serialized_options = b'\202\323\344\223\0027\"\021/api/v1/handshake:\001*Z\037\"\032/api/v1/advanced/handshake:\001*'
  _globals['_POLARIZATIONGRPC']._serialized_start=6987
  _globals['_POLARIZATIONGRPC']._serialized_end=7062
  _globals['_ADVANCEDMODEHANDSHAKEREQUEST']._serialized_start=221
  _globals['_ADVANCEDMODEHANDSHAKEREQUEST']._serialized_end=374
  _globals['_ADVANCEDMODEHANDSHAKEREPLY']._serialized_start=377
  _globals['_ADVANCEDMODEHANDSHAKEREPLY']._serialized_end=654
  _globals['_RECORDINGREPLY']._serialized_start=657
  _globals['_RECORDINGREPLY']._serialized_end=852
  _globals['_RECORDINGREQUEST']._serialized_start=854
  _globals['_RECORDINGREQUEST']._serialized_end=967
  _globals['_CONNECTRECEIVERREQUEST']._serialized_start=969
  _globals['_CONNECTRECEIVERREQUEST']._serialized_end=1013
  _globals['_RECEIVERCAPABILITIESGRPC']._serialized_start=1016
  _globals['_RECEIVERCAPABILITIESGRPC']._serialized_end=1258
  _globals['_CONNECTRECEIVERREPLY']._serialized_start=1261
  _globals['_CONNECTRECEIVERREPLY']._serialized_end=1882
  _globals['_USERINFORMATION']._serialized_start=1885
  _globals['_USERINFORMATION']._serialized_end=2042
  _globals['_POSSIBLESETTINGVALUES']._serialized_start=2045
  _globals['_POSSIBLESETTINGVALUES']._serialized_end=2186
  _globals['_POSSIBLESETTINGVALUES_VALUESENTRY']._serialized_start=2141
  _globals['_POSSIBLESETTINGVALUES_VALUESENTRY']._serialized_end=2186
  _globals['_ALLSETTINGSREQUEST']._serialized_start=2188
  _globals['_ALLSETTINGSREQUEST']._serialized_end=2208
  _globals['_ALLSETTINGSREPLY']._serialized_start=2211
  _globals['_ALLSETTINGSREPLY']._serialized_end=2603
  _globals['_ALLSETTINGSREPLY_SETTINGSENTRY']._serialized_start=2451
  _globals['_ALLSETTINGSREPLY_SETTINGSENTRY']._serialized_end=2498
  _globals['_ALLSETTINGSREPLY_POSSIBLESETTINGVALUESENTRY']._serialized_start=2500
  _globals['_ALLSETTINGSREPLY_POSSIBLESETTINGVALUESENTRY']._serialized_end=2603
  _globals['_CHANGERECEIVERSETTINGREQUEST']._serialized_start=2605
  _globals['_CHANGERECEIVERSETTINGREQUEST']._serialized_end=2708
  _globals['_ANTENNALISTREPLY']._serialized_start=2711
  _globals['_ANTENNALISTREPLY']._serialized_end=2882
  _globals['_ANTENNAACCESSGRPC']._serialized_start=2885
  _globals['_ANTENNAACCESSGRPC']._serialized_end=3126
  _globals['_SWITCHANTENNAREQUEST']._serialized_start=3128
  _globals['_SWITCHANTENNAREQUEST']._serialized_end=3199
  _globals['_RECEIVERACCESSGRPC']._serialized_start=3202
  _globals['_RECEIVERACCESSGRPC']._serialized_end=3539
  _globals['_NEWSIMPLEMODEPRESETCREATIONREQUESTGRPC']._serialized_start=3542
  _globals['_NEWSIMPLEMODEPRESETCREATIONREQUESTGRPC']._serialized_end=3991
  _globals['_MEASURINGPRESETGRPC']._serialized_start=3994
  _globals['_MEASURINGPRESETGRPC']._serialized_end=4579
  _globals['_MEASURINGPRESETGRPC_SETTINGSENTRY']._serialized_start=2451
  _globals['_MEASURINGPRESETGRPC_SETTINGSENTRY']._serialized_end=2498
  _globals['_MEASURINGPRESETLISTREPLY']._serialized_start=4581
  _globals['_MEASURINGPRESETLISTREPLY']._serialized_end=4674
  _globals['_CHANGEDEVICEMODEREQUEST']._serialized_start=4676
  _globals['_CHANGEDEVICEMODEREQUEST']._serialized_end=4754
  _globals['_CHANGEDEVICEMODEREPLY']._serialized_start=4756
  _globals['_CHANGEDEVICEMODEREPLY']._serialized_end=4849
  _globals['_SCPIEXECUTIONREQUEST']._serialized_start=4851
  _globals['_SCPIEXECUTIONREQUEST']._serialized_end=4918
  _globals['_SCPIEXECUTIONREPLY']._serialized_start=4920
  _globals['_SCPIEXECUTIONREPLY']._serialized_end=5003
  _globals['_STARTSCHEDULEDMEASURINGREQUEST']._serialized_start=5005
  _globals['_STARTSCHEDULEDMEASURINGREQUEST']._serialized_end=5109
  _globals['_STARTDIRECTMEASURINGREQUEST']._serialized_start=5111
  _globals['_STARTDIRECTMEASURINGREQUEST']._serialized_end=5212
  _globals['_STOPMEASURINGREPLY']._serialized_start=5214
  _globals['_STOPMEASURINGREPLY']._serialized_end=5280
  _globals['_ROTORANGLEGRPC']._serialized_start=5282
  _globals['_ROTORANGLEGRPC']._serialized_end=5356
  _globals['_ROTATORALIGNMENTGRPC']._serialized_start=5359
  _globals['_ROTATORALIGNMENTGRPC']._serialized_end=5544
  _globals['_ALIGNMENTLIMITSGRPC']._serialized_start=5547
  _globals['_ALIGNMENTLIMITSGRPC']._serialized_end=5988
  _globals['_ROTATORALIGNMENTREQUEST']._serialized_start=5990
  _globals['_ROTATORALIGNMENTREQUEST']._serialized_end=6084
  _globals['_ROTATORALIGNMENTREPLY']._serialized_start=6087
  _globals['_ROTATORALIGNMENTREPLY']._serialized_end=6246
  _globals['_STOREMEASURINGPRESETREQUEST']._serialized_start=6249
  _globals['_STOREMEASURINGPRESETREQUEST']._serialized_end=6394
  _globals['_DELETEMEASURINGPRESETREQUEST']._serialized_start=6396
  _globals['_DELETEMEASURINGPRESETREQUEST']._serialized_end=6438
  _globals['_UPDATEMEASURINGPRESETREQUEST']._serialized_start=6441
  _globals['_UPDATEMEASURINGPRESETREQUEST']._serialized_end=6603
  _globals['_REMOTEMODEREQUEST']._serialized_start=6605
  _globals['_REMOTEMODEREQUEST']._serialized_end=6645
  _globals['_REMOTEMODEREPLY']._serialized_start=6647
  _globals['_REMOTEMODEREPLY']._serialized_end=6685
  _globals['_APPLYMEASURINGPRESETREQUEST']._serialized_start=6687
  _globals['_APPLYMEASURINGPRESETREQUEST']._serialized_end=6745
  _globals['_APPLYMEASURINGPRESETREPLY']._serialized_start=6748
  _globals['_APPLYMEASURINGPRESETREPLY']._serialized_end=6985
  _globals['_ADVANCEDMODEGRPC']._serialized_start=7065
  _globals['_ADVANCEDMODEGRPC']._serialized_end=9868
# @@protoc_insertion_point(module_scope)
