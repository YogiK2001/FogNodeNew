# Trial.py

class fog_node:
    def __init__(self, ip='', host='', tcp=0, udp=0, resp_time=0):
        self.host_name = host
        self.IP_addr = ip
        self.TCP_port = int(tcp)
        self.UDP_port = int(udp)
        self.Queue = []
        self.list_neighbours = []
        self.max_response_time = resp_time
        self.queue_time = 0

    def start_server(self):
        import socket
        s = socket.socket()
        s.bind((self.IP_addr, self.TCP_port))
        print(f"Fog Node server started on {self.IP_addr}:{self.TCP_port}")
        s.listen()
        while True:
            c, addr = s.accept()
            print('Got connection from', addr)
            data = c.recv(1024)
            print('Received from client:', data.decode())
            c.send(b'Thank you for connecting...')
            c.close()