If you’re only expecting 1–3 state changes per minute, it’s perfectly reasonable to store each update directly in the database (the “Update on Each Change” approach). The overhead of a few writes per minute is negligible for most modern databases, and you won’t need a specialized caching or buffering layer.

Why a Direct Update is Fine
- Low Frequency: Even 3 updates/minute is only ~180 updates/hour, which is trivial for PostgreSQL.
- Simple Logic: You can use Receiver.objects.update_or_create(...) each time your sensor handshake reports a new state. No need for complex scheduling or a separate in-memory store.
- Immediate Consistency: As soon as the sensor updates, your database reflects the latest state (no delay from a periodic sync).

Sample Pseudocode
```python

def update_sensor_state(sensor_data):
    sensor, _ = Sensor.objects.update_or_create(
        ip=sensor_data["ip"],
        port=sensor_data["port"],
        defaults={
            "driver_name": sensor_data["driver_name"],
            "user_has_access": sensor_data["user_has_access"],
            "location": Point(sensor_data["longitude"], sensor_data["latitude"], srid=4326)
        }
    )

    # Then update each receiver
    for r in sensor_data["receivers"]:
        Receiver.objects.update_or_create(
            sensor=sensor,
            receiver_id=r["id"],
            defaults={
                "name": r["name"]["value"],
                "state": r["state"],
                "type": r["type"],
            }
        )
```
1. Sensor is either created if it doesn’t exist (unique IP+port) or updated if it already does.
2. Receivers for that sensor are also upserted based on receiver_id.
3. Since the data changes only a few times per minute, this approach is efficient, keeps your code simpler, and ensures your database is always up to date.


### compailing .proto files
```sh
python -m grpc_tools.protoc -I skudra\GrpcProtos --python_out=skudra\GrpcProtos --grpc_python_out=skudra\GrpcProtos .\skudra\GrpcProtos\welcome.proto
```