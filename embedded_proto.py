
# Embedded .proto content for the BioHub project

PROTO_CONTENT = """
syntax = "proto3";

package BioHub;

message SensorData {
  string sensor_id = 1;
  string timestamp = 2;
  double value = 3;
}

message AnalysisResult {
  string analysis_id = 1;
  string status = 2;
  string description = 3;
}
"""

def get_proto_content():
    """Returns the embedded .proto content."""
    return PROTO_CONTENT
    