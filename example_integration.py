
from google.protobuf.timestamp_pb2 import Timestamp
from data.example_with_timestamp_pb2 import ExampleEntity
from datetime import datetime

# Function to create an ExampleEntity with timestamps
def create_example_entity(entity_id, name):
    entity = ExampleEntity()
    entity.id = entity_id
    entity.name = name
    
    now = datetime.utcnow()
    created_at = Timestamp()
    updated_at = Timestamp()
    
    created_at.FromDatetime(now)
    updated_at.FromDatetime(now)
    
    entity.created_at.CopyFrom(created_at)
    entity.updated_at.CopyFrom(updated_at)
    return entity

# Example usage
if __name__ == "__main__":
    example_entity = create_example_entity("123", "Sample Name")
    print(f"Entity ID: {example_entity.id}")
    print(f"Entity Name: {example_entity.name}")
    print(f"Created At: {example_entity.created_at}")
    print(f"Updated At: {example_entity.updated_at}")
