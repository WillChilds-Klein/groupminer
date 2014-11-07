CC=gcc
CFLAGS=-Wall -std=c99 -g -pedantic

all: groupthink

groupthink: src/*.py
	ln run.sh Groupthink
	chmod +x Groupthink

run:
	./Groupthink

clean:
	$(RM) Groupthink src/*.pyc
