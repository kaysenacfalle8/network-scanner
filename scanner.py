import socket
import argparse

def scan_port(ip, port):

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(1)

    result = sock.connect_ex((ip, port))

    if result == 0:
        return True
    else:
        return False
    

def scan_target(ip):

    print(f"\nScanning target {ip}\n")

    for port in range(1, 1025):

        if scan_port(ip, port):
            print(f"Port {port} is OPEN")


def main():

    parser = argparse.ArgumentParser(description="Simple Network Port Scanner")
    parser.add_argument("target", help="IP address to scan")

    args = parser.parse_args()

    scan_target(args.target)

if __name__ == "__main__":
    main()