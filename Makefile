CC=gcc
CFLAGS=-Wall -std=c99 -g -pedantic

all: groupthink

groupthink: src/*.py
	ln run.sh Groupthink
	chmod +x Groupthink

run:
	./Groupthink

launch:
	$(python controllers/launch.py --n 10 --p 54632)

clean:
	$(RM) Groupthink src/*.pyc
	rm logs/*
	pkill -f main.py
