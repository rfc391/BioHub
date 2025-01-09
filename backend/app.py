from flask import Flask, request, jsonify
import grpc
from generated.sample_pb2 import User
from generated.sample_pb2_grpc import UserServiceStub
from concurrent import futures
from grpc import server

# Flask app setup
app = Flask(__name__)

# gRPC client setup
def get_grpc_stub():
    channel = grpc.insecure_channel('localhost:50051')
    return UserServiceStub(channel)

@app.route('/get-user', methods=['GET'])
def get_user():
    user_id = request.args.get('id')
    if not user_id:
        return jsonify({'error': 'User ID is required'}), 400

    try:
        stub = get_grpc_stub()
        response = stub.GetUser(User(id=user_id))
        return jsonify({'id': response.id, 'name': response.name, 'email': response.email})
    except grpc.RpcError as e:
        return jsonify({'error': f'{e.code()} - {e.details()}'}), 500

@app.route('/')
def serve_dashboard():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>BioHub Dashboard</title>
    </head>
    <body>
        <h1>BioHub User Dashboard</h1>
        <form id="user-form">
            <label for="user-id">Enter User ID:</label>
            <input type="text" id="user-id" name="user-id" required>
            <button type="submit">Fetch User</button>
        </form>
        <div id="user-data">
            <h2>User Details</h2>
            <pre id="user-output"></pre>
        </div>
        <script>
            document.getElementById('user-form').addEventListener('submit', async function(e) {
                e.preventDefault();
                const userId = document.getElementById('user-id').value;

                // Fetch user data from the backend API
                try {
                    const response = await fetch(`/get-user?id=${userId}`);
                    const data = await response.json();
                    document.getElementById('user-output').textContent = JSON.stringify(data, null, 2);
                } catch (error) {
                    document.getElementById('user-output').textContent = `Error: ${error.message}`;
                }
            });
        </script>
    </body>
    </html>
    """

# gRPC server setup for testing
def start_grpc_server():
    grpc_server = server(futures.ThreadPoolExecutor(max_workers=10))
    from generated.sample_pb2_grpc import add_UserServiceServicer_to_server
    from immudb.client import ImmudbClient

    class UserServiceImplementation:
        def __init__(self):
            self.immudb_client = ImmudbClient()
            self.immudb_client.login("immudb", "immudb")

        def GetUser(self, request, context):
            user_data = self.immudb_client.get(request.id.encode())
            if user_data:
                return User(id=request.id, name=user_data["name"].decode(), email=user_data["email"].decode())
            else:
                context.set_code(grpc.StatusCode.NOT_FOUND)
                context.set_details("User not found")
                return User()

    add_UserServiceServicer_to_server(UserServiceImplementation(), grpc_server)
    grpc_server.add_insecure_port('[::]:50051')
    grpc_server.start()
    print("gRPC Server running on port 50051")
    grpc_server.wait_for_termination()

if __name__ == "__main__":
    import threading

    # Run gRPC server in a separate thread
    grpc_thread = threading.Thread(target=start_grpc_server, daemon=True)
    grpc_thread.start()

    # Start Flask app
    app.run(host="0.0.0.0", port=5000)
