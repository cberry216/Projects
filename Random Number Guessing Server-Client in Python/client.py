import socket
import sys

def main():
	client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	host_name = input("Enter host name: ")
	host_port = int(input("Enter port number: "))

	host_address = (host_name, host_port)

	try:
		client_socket.connect(host_address)
	except:
		exc = sys.exc_info()
		exc_value = exc[1]
		exc_type  = exc[0]
		if exc_type == socket.gaierror:
			print("Error: Address name may be incorrect.\n%s\n" % str(exc_value))
		if exc_type == socket.error:
			print("Error: Port may be incorrect.\n%s\n" % str(exc_value))
		else:
			print("Error: %s\n%s\n" % (str(exc_type), str(exc_value)))

	recv_msg = client_socket.recv(100)
	send_msg = input(recv_msg.decode())
	client_socket.send(send_msg.encode())
	recv_msg = client_socket.recv(100)
	print(recv_msg.decode())

main()