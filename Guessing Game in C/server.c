#include "csapp.h"

int main(int argc, char **argv){
	int listfd, connfd, port, cli_ans, wrong;
	socklen_t clientlen;
	struct sockaddr_in clientaddr;
	struct hostent *hp;
	char *haddrp, buf[SENDANS];
	unsigned short client_port;

	int rand_num;

	wrong = 1;

	if(argc != 2){
		error(1, 0, "usage: ./server <port>");
		return 1;
	}

	port = atoi(argv[1]);

	listfd = Open_listenfd(port);

	while(1){
		clientlen = sizeof(clientaddr);
		connfd = Accept(listfd, (SA *)&clientaddr, &clientlen);

		hp = gethostbyaddr((const char*)&clientaddr.sin_addr.s_addr, 
							sizeof(clientaddr.sin_addr.s_addr), AF_INET);
		haddrp = inet_ntoa(clientaddr.sin_addr);
		client_port = ntohs(clientaddr.sin_port);
		printf("client connected to %s (%s), port %u\n", hp->h_name, haddrp, client_port);

		srand((int)clock());
		rand_num = (rand() + 1) % 10;
		//printf("rand_num = %d\n", rand_num);

		do{
			ssize_t n = recv(connfd, buf, strlen(buf), 0);
			printf("Recieved %ld bytes.\n", n);

			cli_ans = atoi(buf);
			if(cli_ans == rand_num){
				printf("Client guessed correct answer: %d\n", rand_num);
				wrong = 0;
				//clear_buf(buf);
				buf[0] = 'z';
				buf[1] = '\0';
				send(connfd, buf, strlen(buf), 0);
			}
			else{
				printf("Client did not guess correct answer: %d\n", cli_ans);
				//clear_buf(buf);
				buf[0] = 'a';
				buf[1] = '\0';
				send(connfd, buf, strlen(buf), 0);
			}
		}
		while(wrong);

		Close(connfd);
		printf("Connection closed\n");
	}

	Close(listfd);

	exit(0);
}