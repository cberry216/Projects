CC = gcc
CFLAGS = -Wall -pthread

all: server client

server: server.o csapp.o
	$(CC) $(CFLAGS) server.o csapp.o -o server

client: client.o csapp.o
	$(CC) $(CFLAGS) client.o csapp.o -o client

client.o: client.c
	$(CC) $(CFLAGS) client.c -c

server.o: server.c
	$(CC) $(CFLAGS) server.c -c

csapp.o: csapp.c csapp.h
	$(CC) $(CLFAGS) csapp.c -c

clean:
	rm -f server server.o csapp.o client client.o
