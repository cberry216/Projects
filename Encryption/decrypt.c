#include <stdio.h>
#include <fcntl.h>
#include <time.h>

#define DEC_MSK 0b00111111	// used to extract six bits of each input character
#define WRT_MSK 255			// 0b11111111, use to get 8-bit char without arithmetic right shift
#define E_EOF 0

int main(int argc, char* argv[]){
	// timing the execution
	clock_t begin = clock();
	// check to see the command was entered correctly
	if(argc != 3){
		fprintf(stderr, "usage: dec.exe <input filename> <output filename>\n");
		return 1;
	}
	// define our file descriptors, fd_in for reading in and
    // fd_out for writing
	int fd_in, fd_out;
	// open the read file, return 1 on error
	if((fd_in = open(argv[1], O_RDONLY, 0644)) < 0){
		fprintf(stderr, "file '%s' could not be opened\n", argv[1]);
		return 1;
	}
	// open the write file, return 1 on error
	if((fd_out = open(argv[2], O_CREAT | O_WRONLY | O_TRUNC, 0644)) < 0){
		fprintf(stderr, "could not open file '%s'\n", argv[2]);
		return 1;
	}
	// read 24 chars into rd_buf, then converts the 4, 6-bit chars into 
    // 3, 8 bit chars (removing the 0b01 left padding) 6 times (i.e. 24 chars)
	char rd_buf[24];
	while(read(fd_in, rd_buf, 24) > 0){
		char wr_buf[18] = {0}; // write buffer to append each 8-bit char to
		int i;
		char len = 0; // length to write to file so we don't write too much to file
		// convert 4 6-bit chars to 3 8-bit chars.
		for(i = 0; i < 6; i++){
			// convert 4 chars to one 24-bit int
			int bin_buf = (((((((rd_buf[0 + 4 * i] & DEC_MSK) << 6) + 
								(rd_buf[1 + 4 * i] & DEC_MSK)) << 6) + 
								(rd_buf[2 + 4 * i] & DEC_MSK)) << 6) + 
								(rd_buf[3 + 4 * i] & DEC_MSK));
			// append each 8-bit char to wr_buf
			char x;
			if((x = (WRT_MSK & (bin_buf >> 16))) == E_EOF)
				break; //if we encounter 0 (E_EOF), break and write to file
			// add first 8-bit char to wr_buf and inc len
			wr_buf[0 + 3 * i] = x; len++;
			if((x = (WRT_MSK & (bin_buf >> 8))) == E_EOF)
				break;//if we encounter 0 (E_EOF), break and write to file
			// add second 8-bit char to wr_buf and inc len
			wr_buf[1 + 3 * i] = x; len++;
			if((x = (WRT_MSK & bin_buf)) == E_EOF)
				break;//if we encounter 0 (E_EOF), break and write to file
			// add third 8-bit char to wr_buf and inc len
			wr_buf[2 + 3 * i] = x; len++;
		}
		// write wr_buf to output file, return 1 on error
		if(write(fd_out, wr_buf, len) != len){
			fprintf(stderr, "could not write '%s' to dec_file.txt\n", wr_buf);
			return 1;
		}
	}
	clock_t end = clock();
	// timing the execution
    double exec_time = ((double)(end-begin))/CLOCKS_PER_SEC;
    printf("%f sec\n", exec_time);
}