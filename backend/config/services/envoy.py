import platform
import yaml
import json
import subprocess
from pathlib import Path
from django.conf import settings
from ..models import Sensor, EnvoyConfigLog
import docker

class EnvoyConfigManager:
    # Change this path according to your project structure
    ENVOY_CONFIG_PATH = Path(settings.BASE_DIR).parent / 'etc' / 'envoy' / 'envoy.yaml'
    CONTAINER_NAME = 'envoy_proxy'
    IS_WINDOWS = platform.system().lower() == 'windows'
    
    @classmethod
    def generate_config(cls):
        """Generate Envoy configuration based on current sensors"""
        sensors = Sensor.objects.all()
        
        config = {
            'static_resources': {
                'listeners': [
                    {
                        'name': 'grpc_web_listener',
                        'address': {
                            'socket_address': {'address': '0.0.0.0', 'port_value': 9090}
                        },
                        'filter_chains': [
                            {
                                'filters': [
                                    {
                                        'name': 'envoy.filters.network.http_connection_manager',
                                        'typed_config': {
                                            '@type': 'type.googleapis.com/envoy.extensions.filters.network.http_connection_manager.v3.HttpConnectionManager',
                                            'stat_prefix': 'grpc_json_transcoder',
                                            'codec_type': 'auto',
                                            'stream_idle_timeout': '0s',
                                            'access_log': [
                                                {
                                                    'name': 'envoy.access_loggers.stdout',
                                                    'typed_config': {
                                                        '@type': 'type.googleapis.com/envoy.extensions.access_loggers.stream.v3.StdoutAccessLog',
                                                        'log_format': {
                                                            'text_format_source': {
                                                                'inline_string': '[%START_TIME%] %REQ(:METHOD)% %REQ(X-ENVOY-ORIGINAL-PATH?:PATH)% %PROTOCOL% %RESPONSE_CODE% %RESPONSE_FLAGS% %BYTES_RECEIVED% %BYTES_SENT% %DURATION% %RESP(X-ENVOY-UPSTREAM-SERVICE-TIME)% "%REQ(X-FORWARDED-FOR)%" "%REQ(USER-AGENT)%" "%REQ(X-REQUEST-ID)%" "%REQ(:AUTHORITY)%" "%UPSTREAM_HOST%" %UPSTREAM_CLUSTER% %UPSTREAM_LOCAL_ADDRESS% %DOWNSTREAM_LOCAL_ADDRESS% %DOWNSTREAM_REMOTE_ADDRESS% %REQUESTED_SERVER_NAME% %ROUTE_NAME%\n'
                                                            }
                                                        }
                                                    }
                                                }
                                            ],
                                            'route_config': {
                                                'name': 'local_route',
                                                'virtual_hosts': [
                                                    {
                                                        'name': 'local_service',
                                                        'domains': ['*'],
                                                        'typed_per_filter_config': {
                                                            'envoy.filters.http.cors': {
                                                                '@type': 'type.googleapis.com/envoy.extensions.filters.http.cors.v3.CorsPolicy',
                                                                'allow_methods': 'GET, PUT, DELETE, POST, OPTIONS',
                                                                'allow_headers': 'keep-alive,user-agent,cache-control,content-type,content-transfer-encoding,x-accept-content-transfer-encoding,x-accept-response-streaming,x-user-agent,x-grpc-web,grpc-timeout,x-device-id,x-device-ip,x-device-port,authorization,accept,origin,sec-fetch-site,sec-fetch-mode,sec-fetch-dest,referer,device-port,device-ip,token',
                                                                'allow_origin_string_match': [
                                                                    {'safe_regex': {'google_re2': {}, 'regex': '.*'}}
                                                                ],
                                                                'allow_credentials': True,
                                                                'max_age': '1728000'
                                                            }
                                                        },
                                                        'routes': []
                                                    }
                                                ]
                                            },
                                            'http_filters': [
                                                {
                                                    'name': 'envoy.filters.http.cors',
                                                    'typed_config': {
                                                        '@type': 'type.googleapis.com/envoy.extensions.filters.http.cors.v3.Cors'
                                                    }
                                                },
                                                {
                                                    'name': 'envoy.filters.http.grpc_json_transcoder',
                                                    'typed_config': {
                                                        '@type': 'type.googleapis.com/envoy.extensions.filters.http.grpc_json_transcoder.v3.GrpcJsonTranscoder',
                                                        'proto_descriptor': '/etc/envoy/test_proto.pb',
                                                        'services': [
                                                            'welcome_grpc.WelcomeGrpc',
                                                            'simple_mode_grpc.SimpleModeGrpc',
                                                            'advanced_mode_grpc.AdvancedModeGrpc'
                                                        ],
                                                        'print_options': {
                                                            'add_whitespace': True,
                                                            'always_print_primitive_fields': True,
                                                            'always_print_enums_as_ints': False,
                                                            'preserve_proto_field_names': True
                                                        },
                                                        'match_incoming_request_route': True,
                                                        'ignore_unknown_query_parameters': True,
                                                        'auto_mapping': True,
                                                        'convert_grpc_status': True
                                                    }
                                                },
                                                {
                                                    'name': 'envoy.filters.http.grpc_web',
                                                    'typed_config': {
                                                        '@type': 'type.googleapis.com/envoy.extensions.filters.http.grpc_web.v3.GrpcWeb'
                                                    }
                                                },
                                                {
                                                    'name': 'envoy.filters.http.router',
                                                    'typed_config': {
                                                        '@type': 'type.googleapis.com/envoy.extensions.filters.http.router.v3.Router'
                                                    }
                                                }
                                            ]
                                        }
                                    }
                                ]
                            }
                        ]
                    }
                ],
                'clusters': []
            },
            'admin': {
                'access_log_path': '/dev/stdout',
                'address': {
                    'socket_address': {'address': '0.0.0.0', 'port_value': 9901}
                }
            }
        }

        # Add test service cluster first
        test_cluster = {
            'name': 'test_service_cluster',
            'connect_timeout': '1s',
            'type': 'strict_dns',
            'lb_policy': 'round_robin',
            'http2_protocol_options': {},
            'load_assignment': {
                'cluster_name': 'test_service_cluster',
                'endpoints': [{
                    'lb_endpoints': [{
                        'endpoint': {
                            'address': {
                                'socket_address': {
                                    'address': '10.0.222.39',
                                    'port_value': 19010
                                }
                            }
                        }
                    }]
                }]
            }
        }
        config['static_resources']['clusters'].append(test_cluster)

        # Add catch-all preflight route first
        routes = [{
            'name': 'preflight_catch_all',
            'match': {
                'prefix': '/',
                'headers': [{
                    'name': ':method',
                    'string_match': {'exact': 'OPTIONS'}
                }]
            },
            'route': {
                'cluster': 'test_service_cluster',
                'timeout': '0s',
                'idle_timeout': '0s'
            }
        }]

        # Add test service route
        routes.append({
            'name': 'test_service_route',
            'match': {
                'path': '/v1/testcall',
                'headers': [{
                    'name': ':method',
                    'string_match': {'exact': 'GET'}
                }]
            },
            'route': {
                'cluster': 'test_service_cluster',
                'timeout': '30s'
            }
        })

        # Add device-specific routes and clusters
        for sensor in sensors:
            device_id = f"device{sensor.id}"

            # Add cluster configuration
            cluster = {
                'name': f"{device_id}_cluster",
                'connect_timeout': '1s',
                'type': 'strict_dns',
                'lb_policy': 'round_robin',
                'http2_protocol_options': {},
                'load_assignment': {
                    'cluster_name': f"{device_id}_cluster",
                    'endpoints': [{
                        'lb_endpoints': [{
                            'endpoint': {
                                'address': {
                                    'socket_address': {
                                        'address': sensor.ip,
                                        'port_value': sensor.port
                                    }
                                }
                            }
                        }]
                    }]
                }
            }
            config['static_resources']['clusters'].append(cluster)

            # Add handshake route
            routes.append({
                'name': f"{device_id}_handshake",
                'match': {
                    'path': '/api/v1/handshake',
                    'headers': [
                        {
                            'name': ':method',
                            'string_match': {'exact': 'POST'}
                        },
                        {
                            'name': 'x-device-id',
                            'string_match': {'exact': device_id}
                        }
                    ]
                },
                'route': {
                    'cluster': f"{device_id}_cluster",
                    'timeout': '30s'
                }
            })

            # Add streaming route
            routes.append({
                'name': f"{device_id}_stream",
                'match': {
                    'path': '/api/v1/receivers/stream',
                    'query_parameters': [
                        {
                            'name': 'deviceId',
                            'string_match': {'exact': device_id}
                        }
                    ]
                },
                'response_headers_to_add': [
                    {'header': {'key': 'Content-Type', 'value': 'text/event-stream'}},
                    {'header': {'key': 'Transfer-Encoding', 'value': 'chunked'}},
                    {'header': {'key': 'Cache-Control', 'value': 'no-cache'}},
                    {'header': {'key': 'Connection', 'value': 'keep-alive'}}
                ],
                'route': {
                    'cluster': f"{device_id}_cluster",
                    'timeout': '0s',
                    'idle_timeout': '0s'
                }
            })

        # Update routes in config
        config['static_resources']['listeners'][0]['filter_chains'][0]['filters'][0]['typed_config']['route_config']['virtual_hosts'][0]['routes'] = routes

        return config
    
    @classmethod
    def validate_config(cls, config):
        """Validate Envoy configuration"""
        try:
            # Write config to temporary file
            temp_path = cls.ENVOY_CONFIG_PATH.parent / 'temp_envoy.yaml'
            with open(temp_path, 'w') as f:
                yaml.dump(config, f)

            # Run Envoy with --mode validate
            result = subprocess.run(
                ['envoy', '--mode', 'validate', '-c', str(temp_path)],
                capture_output=True,
                text=True
            )

            # Clean up
            temp_path.unlink()

            if result.returncode == 0:
                return True, "Configuration validated successfully"
            return False, result.stderr

        except Exception as e:
            return False, str(e)

    @classmethod
    def restart_container(cls):
        """Restart Envoy container with error handling"""
        try:
            client = docker.from_env(timeout=30)
            container = client.containers.get(cls.CONTAINER_NAME)
            container.restart(timeout=30)
            return True, "Container restarted successfully"
        except docker.errors.NotFound:
            return False, f"Container {cls.CONTAINER_NAME} not found"
        except docker.errors.APIError as e:
            return False, f"Docker API error: {str(e)}"
        except Exception as e:
            return False, f"Failed to restart container: {str(e)}"

    @classmethod
    def update_config(cls, config, triggered_by_sensor=None):
        """Update Envoy configuration and restart container"""
        # Skip validation on Windows
        if cls.IS_WINDOWS:
            is_valid, message = True, "Validation skipped in Windows environment"
        else:
            is_valid, message = cls.validate_config(config)
        
        log = EnvoyConfigLog.objects.create(
            status=EnvoyConfigLog.VALIDATED if is_valid else EnvoyConfigLog.FAILED,
            message=message,
            config_snapshot=config,
            triggered_by_sensor=triggered_by_sensor
        )

        if not is_valid:
            return False, message

        try:
            # Write new config
            with open(cls.ENVOY_CONFIG_PATH, 'w') as f:
                yaml.dump(config, f)

            # Restart container (both Windows and Linux)
            success, restart_message = cls.restart_container()
            
            if success:
                success_message = f"Configuration updated and {restart_message}"
                log.status = EnvoyConfigLog.SUCCESS
                log.message += f"\n{success_message}"
                log.save()
                return True, success_message
            else:
                error_msg = f"Config updated but container restart failed: {restart_message}"
                log.status = EnvoyConfigLog.FAILED
                log.message += f"\n{error_msg}"
                log.save()
                return False, error_msg

        except Exception as e:
            error_msg = f"Failed to update configuration: {str(e)}"
            log.status = EnvoyConfigLog.FAILED
            log.message += f"\n{error_msg}"
            log.save()
            return False, error_msg