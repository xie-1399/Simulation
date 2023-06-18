#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

//get os error form the errno
void unix_error(char *msg){
    fprintf(stderr,"%s:%s\n",msg, strerror(errno));
    exit(EXIT_SUCCESS);
}

int main(){
    write(1,"hello world\n",13);
//    char str[] = "hello world";
//    fwrite(str,sizeof(char),sizeof(char),1);
    exit(EXIT_SUCCESS);
}


