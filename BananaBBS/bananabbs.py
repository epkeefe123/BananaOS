import socket
import threading

messages = []

def handle_client(conn, addr):
    print(f"[CONNECTED] {addr}")
    conn.sendall(b"BananaBBS Server Ready\r\n")
    
    try:
        while True:
            data = conn.recv(1024)
            if not data:
                break

            msg = data.decode(errors='ignore').strip()
            print(f"[{addr}] {msg}")

            if msg.startswith("HELLO"):
                conn.sendall(b"Hello BananaOS User!\r\n")
            elif msg.startswith("READ"):
                if messages:
                    for m in messages:
                        conn.sendall(f"{m}\r\n".encode())
                else:
                    conn.sendall(b"No messages.\r\n")
            elif msg.startswith("POST"):
                content = msg[5:].strip()
                if content:
                    messages.append(content)
                    conn.sendall(b"Message received!\r\n")
                else:
                    conn.sendall(b"Empty message ignored.\r\n")
            elif msg.startswith("BYE"):
                conn.sendall(b"Goodbye!\r\n")
                break
            else:
                conn.sendall(b"Unknown command.\r\n")
    except Exception as e:
        print(f"[ERROR] {e}")
    finally:
        conn.close()
        print(f"[DISCONNECTED] {addr}")

def start_server(host='0.0.0.0', port=2525):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.bind((host, port))
        server.listen(5)
        print(f"BananaBBS Server listening on port {port}...")

        while True:
            conn, addr = server.accept()
            thread = threading.Thread(target=handle_client, args=(conn, addr))
            thread.start()

if __name__ == "__main__":
    start_server()
