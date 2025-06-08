import socket

HOST = '0.0.0.0'
PORT = 8080

def handle_request(request):
    if request.startswith('GET /api/hello'):
        body = '{"message": "Hello, world!"}'
        response = (
            "HTTP/1.1 200 OK\r\n"
            "Content-Type: application/json\r\n"
            f"Content-Length: {len(body)}\r\n"
            "\r\n"
            f"{body}"
        )
    elif request.startswith('GET /static/'):
        path = request.split(' ')[1].lstrip('/')
        try:
            with open(path, 'rb') as f:
                content = f.read()
            mime = 'text/html' if path.endswith('.html') else 'text/plain'
            response = (
                "HTTP/1.1 200 OK\r\n"
                f"Content-Type: {mime}\r\n"
                f"Content-Length: {len(content)}\r\n"
                "\r\n"
            ).encode() + content
        except FileNotFoundError:
            body = "<h1>404 Not Found</h1>"
            response = (
                "HTTP/1.1 404 Not Found\r\n"
                "Content-Type: text/html\r\n"
                f"Content-Length: {len(body)}\r\n"
                "\r\n"
                f"{body}"
            )
    else:
        body = "<h1>404 Not Found</h1>"
        response = (
            "HTTP/1.1 404 Not Found\r\n"
            "Content-Type: text/html\r\n"
            f"Content-Length: {len(body)}\r\n"
            "\r\n"
            f"{body}"
        )
    return response

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(5)
    print(f"Server running on http://{HOST}:{PORT}")
    while True:
        conn, addr = s.accept()
        with conn:
            request = conn.recv(1024).decode()
            if not request:
                continue
            print(f"Request from {addr}:\n{request}")
            response = handle_request(request)
            if isinstance(response, str):
                response = response.encode()
            conn.sendall(response)
