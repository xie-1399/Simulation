// about how to control the process(P513)
#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>
#include <sys/wait.h>
#include <sys/types.h>
#include <time.h>

#define N 10

int usefork(){
    pid_t pid;
    int x = 1;

    pid = fork();
    if (pid == 0){
        printf("child: x = %d\n",++x);
        exit(EXIT_SUCCESS);
    }

    printf("parent:x = %d\n",--x);
    exit(EXIT_SUCCESS);
}

int forkprob0(){
    printf("-------------forkprob0---------------\n");
    int x = 1;
    if(fork() == 0){
        printf("p1: x = %d\n",++x);
    }
    printf("p2:x = %d\n",--x);
    exit(EXIT_SUCCESS);
}

//4 hello
int forkprob1(){
    printf("-------------forkprob1---------------\n");
    fork();
    fork();
    printf("hello\n");
    exit(EXIT_SUCCESS);
}

int waitprob0(){ //if b starts -> bacc
    printf("-------------waitprob0---------------\n");
    fflush(stdout);
    if(fork() == 0){
        printf("a");
        fflush(stdout);
    }
    else{
        printf("b");
        fflush(stdout);
        waitpid(-1,NULL,0);
    }
    printf("c");
    fflush(stdout);
    exit(EXIT_SUCCESS);
}

int waitprob1(){
    printf("-------------waitprob1---------------\n");
    int status,i;
    pid_t pid;
    for(i = 0 ; i < N ; i++){
        if((pid = fork()) == 0){
            exit(100 + i);
        }
    }

    while((pid = waitpid(-1,&status,0)) > 0){ //No Order because of -1
        printf("child %d\n",pid);
    }
    printf("finish wait\n");
    exit(EXIT_SUCCESS);
}

void sleepprob0(int secs){
    clock_t start,end;
    int cpu_time;
    start = clock();
    int sleepsec = sleep(secs);
    if(sleepsec == 0){
        end = clock();
        cpu_time = end - start;
        printf("selpt for %d of %d secs\n",secs,cpu_time);
    }
};

int main(){
    //exit really exits the process
    //usefork();
    //forkprob1();
    //waitprob0();
    //waitprob1();
    sleepprob0(10);

}