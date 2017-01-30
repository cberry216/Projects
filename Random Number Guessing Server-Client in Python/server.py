import socket
import threading
import sys

def echo(connect, cli_addr):
	thread_id = threading.current_thread().ident
	print("(%d) Connected to %s on port %s\n" % (thread_id, str(cli_addr[0]), str(cli_addr[1])))
	send_msg = "Type: "
	connect.send(send_msg.encode())
	print("(%d) Sending %d bytes to %s on port %s" % (thread_id, sys.getsizeof(send_msg),str(cli_addr[0]), str(cli_addr[1])))
	recv_msg = connect.recv(100)
	print("(%d) Recieved %d bytes from %s on port %s" % (thread_id, sys.getsizeof(recv_msg),str(cli_addr[0]), str(cli_addr[1])))
	send_msg = recv_msg.decode().upper()
	connect.send(send_msg.encode())
	print("(%d) Sending %d bytes to %s on port %s" % (thread_id, sys.getsizeof(send_msg),str(cli_addr[0]), str(cli_addr[1])))

def main():

	server_name = input("Enter server name: ")
	server_port = int(input("Enter port number: "))

	server_address = (server_name, server_port)

	server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	server_socket.bind(server_address)

	server_socket.listen(10)
	while(True):
		try:
			print("waiting for connection...\n")
			server_thread = threading.Thread(target=echo, args=(server_socket.accept()))
			server_thread.start()
		except:
			exc = sys.exc_info();
			exc_type = exc[0]
			exc_value = exc[1]
			print("Error: %s\n%s" % (str(exc_type), str(exc_value)))

main()