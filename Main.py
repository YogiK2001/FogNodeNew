from Trial import fog_node

def main():
    f1 = fog_node(
        ip="127.0.0.1",  # localhost IP address
        tcp=8000,        # TCP port number
        udp=8001,        # UDP port number
        resp_time=5000   # Max response time in milliseconds
    )

    # Example of calling a method (ensure it's defined in fog_node)
    f1.start_server()
    # Additional code to use the fog_node instance

if __name__ == "__main__":
    main()