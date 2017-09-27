#include <stdio.h>
#include <fcntl.h>
#include <time.h>

#define ENC_MSK 0b00111111	// used to convert char to 6-bit-valid char
#define ENC_TMP 0b01000000	// honestly just makes the ouput file look cooler

int main(int argc, char* argv[]){
	// timing the execution
	clock_t begin = clock();
	// check to see the command was entered correctly
	if(argc != 3){
        fprintf(stderr, "usage: enc.exe <input filename> <output filename>\n");
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
    // read 18 chars into rd_buf, then convert the 3, 8 bit chars into 
    // 4, 6 bit chars (with 0b01 left padding), 6 times (i.e. 18 chars)
    char rd_buf[18];
    while(read(fd_in, rd_buf, 18) > 0){
    	// zero out wr_buf
    	char wr_buf[24] = {0};
    	for(int i = 0; i < 6; i++){
    		// convert three chars to one 24-bit int
    		int buf_bin = (((((rd_buf[0 + 3 * i]) << 8) + 
    						   rd_buf[1 + 3 * i]) << 8) + 
    						   rd_buf[2 + 3 * i]);
    		// zero out rd_buf (in case we get to end of file we have 0's in remaining indices)
    		rd_buf[0 + 3 * i] = 0; rd_buf[1 + 3 * i] = 0; rd_buf[2 + 3 * i] = 0;
    		// append each 6-bit char to wr_buf
    		wr_buf[0 + 4 * i] = (ENC_TMP | (ENC_MSK & (buf_bin >> 18)));
    		wr_buf[1 + 4 * i] = (ENC_TMP | (ENC_MSK & (buf_bin >> 12)));
    		wr_buf[2 + 4 * i] = (ENC_TMP | (ENC_MSK & (buf_bin >> 6)));
    		wr_buf[3 + 4 * i] = (ENC_TMP | (ENC_MSK & buf_bin));
    	}
    	// write wr_buf to output file, return 1 on error
    	if(write(fd_out, wr_buf, 24) != 24){
    		fprintf(stderr, "error writing to file\n");
    		close(fd_in); close(fd_out);
    		return 1;
    	}
    }
    clock_t end = clock();
    double exec_time = ((double)(end-begin))/CLOCKS_PER_SEC;
    printf("%f sec\n", exec_time);
}