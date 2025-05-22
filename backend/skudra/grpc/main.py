import grpc
from skudra.GrpcProtos import welcome_pb2 as welcome, welcome_pb2_grpc as welcome_grpc
from skudra.GrpcProtos import common_pb2
from skudra.GrpcProtos import advanced_mode_grpc_pb2 as advanced, advanced_mode_grpc_pb2_grpc as advanced_grpc

from decimal import Decimal
import sys
sys.path.insert(0, 'C:\\Users\\ilmarsl\\Development\\SKUDRA WEB\\SKUDRA WEB\\backend\\skudra\\GrpcProtos')

from google.protobuf.json_format import MessageToDict

def firstInit(obj):
    """
    Performs the handshake and returns a dict with sensor data.
    """
    handshake_data = handshake(
        username=False,
        password=False,
        server_token=False,
        is_guest_user=False,
        ip=obj.ip,
        port=obj.port
    )
    return build_sensor_fields(MessageToDict(handshake_data))

def build_sensor_fields(handshake_dict):
    """
    Extract relevant fields from the handshake dict and return them in a Python dict.
    """
    sensor_fields = {}
    if 'error' in handshake_dict and handshake_dict['error']:
        sensor_fields['state'] = handshake_dict.get('code', 'ERROR')
    else:
        sensor_fields['state'] = handshake_dict.get('status', 'READY')
        sensor_fields['driver_name'] = handshake_dict.get('driverName', '')
        sensor_fields['user_has_access'] = handshake_dict.get('user_has_access', False)
        sensor_fields['frontendToken'] = handshake_dict.get('frontendToken', False)
        sensor_fields['analysisCredentials'] = handshake_dict.get('analysisCredentials', {})
        sensor_fields['receivers'] = handshake_dict.get('receivers', [])
        sensor_fields['longitude'] = get_decimal_from_decimal_value(handshake_dict.get('longitude'))
        sensor_fields['latitude'] = get_decimal_from_decimal_value(handshake_dict.get('latitude'))
    return sensor_fields

def get_decimal_from_decimal_value(decimal_value):
    print("_______________________________________________________________", decimal_value)
    if not decimal_value:
        return 0
    if 'units' not in decimal_value or 'nanos' not in decimal_value:
        return 0
    return Decimal(decimal_value['units']) + (Decimal(decimal_value['nanos']) / Decimal(10**9))

def update_regular_sensor_states(ip, port):
    """
    Updates the states of regular sensors.
    """
    handshake_data = handshake(
        username=False,
        password=False,
        server_token=False,
        is_guest_user=False,
        ip=ip,
        port=port
    )
    return build_state_update(MessageToDict(handshake_data))

def build_state_update(handshake_dict):
    """
    Extract relevant fields from the handshake dict and return them in a Python dict.
    """
    sensor_fields = {}
    if 'error' in handshake_dict and handshake_dict['error']:
        sensor_fields['state'] = handshake_dict.get('code', 'ERROR')
    else:
        sensor_fields['state'] = handshake_dict.get('status', 'READY')
        # sensor_fields['driver_name'] = handshake_dict.get('driverName', '')
        # sensor_fields['analysisCredentials'] = handshake_dict.get('analysisCredentials', {})
        sensor_fields['receivers'] = handshake_dict.get('receivers', [])
    return sensor_fields

def handshake(username, password, server_token, is_guest_user, ip, port):
    channel = grpc.insecure_channel(f'{ip}:{port}')
    # stub = welcome_grpc.WelcomeGrpcStub(channel)
    stub = advanced_grpc.AdvancedModeGrpcStub(channel)
    
    if username and password:
        request = advanced.AdvancedModeHandshakeRequest(
            username=advanced.StringValue(value=username),
            password=advanced.StringValue(value=password)
        )
    elif server_token:
        request = advanced.AdvancedModeHandshakeRequest(
            server_token=advanced.StringValue(value=server_token)
        )
    else:
        request = advanced.AdvancedModeHandshakeRequest()
        
    try:
        response = stub.AdvancedModeHandshake(request)
    except grpc.RpcError as e:
        error_msg = str(e)
        error_code = e.code().name if hasattr(e, 'code') else "UNKNOWN"
        error_response = common_pb2.ErrorResponse(
            error=True,
            message=error_msg,
            code=error_code
        )
        return error_response
    return response
