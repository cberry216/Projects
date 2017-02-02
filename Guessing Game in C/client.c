#include "csapp.h"

void get_resp(char *buffer);

int main(int argc, char **argv){
	int clientfd, port;
	char *host, buf[SENDANS];

	int wrong = 1;

	if(argc != 3){
		error(1, 0, "usage: ./client <hostname> <port>");
		return 1;
	}

	host = argv[1];
	port = atoi(argv[2]);

	clientfd = Open_clientfd(host, port);

	//FILE *file = Fdopen(clientfd, "+a");

	while(wrong){
		printf("Guess the number: ");
		get_resp(buf);
		send(clientfd, buf, strlen(buf), 0);
		//clear_buf(buf);
		ssize_t n = recv(clientfd, buf, strlen(buf), 0);
		//printf("Recieved %ld bytes.\n", n);
		if(buf[0] == 'a'){
			printf("Incorrect answer\n");
		}
		else{
			wrong = 0;
			printf("Correct answer\n");
		}
	}

	Close(clientfd);

	return 0;
}

void get_resp(char *buffer){
	int c, i;
	for(i = 0; i < SENDANS-1 && (c = getchar()) != '\n'; i++){
		buffer[i] = c;
	}
	for(; i < SENDANS; i++){
		buffer[i] = '\0';
	}
}