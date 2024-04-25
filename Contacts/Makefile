CC = gcc
CFLAGS = -Wall -g

all: hash

hash: hash.o hash_helper.o
	$(CC) $(CFLAGS) -o hash hash.o hash_helper.o

hash.o: hash.c hash_helper.h
	$(CC) $(CFLAGS) -c hash.c

hash_helper.o: hash_helper.c hash_helper.h
	$(CC) $(CFLAGS) -c hash_helper.c

clean:
	rm -f *.o hash