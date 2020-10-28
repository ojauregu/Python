from schema_registry.client import SchemaRegistryClient, schema

client = SchemaRegistryClient(url="http://127.0.0.1:8081")

deployment_schema = {
    "type": "record",
    "namespace": "com.pruebas.AVRO",
    "name": "usuario",
    "fields": [
        {"name": "idusuarios", "type": "int"},
        {"name": "nombre", "type": "string"},
        {"name": "puesto", "type": "string"},
        {"name": "sitio", "type": "string"},
    ],
}

avro_schema = schema.AvroSchema(deployment_schema)

schema_id = client.register("test-deployment", avro_schema)

