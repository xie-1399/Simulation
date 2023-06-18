CC = gcc
CFLAGS = -Wall

all:writeStd process

program:main.o
	$(CC) ${CFLAGS} -o program main.o

writeStd:writeStd.c
	${CC} ${CFLAGS} -o writeStd writeStd.c

process:process.c
	${CC} ${CFLAGS} -o process process.c

main.o:main.c
	${CC} ${CFLAGS} -c main.c

clean:
	rm -f *.o program writeStd process