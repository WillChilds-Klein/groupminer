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
	pkill -f main.py
	rm logs/*
	$(RM) Groupthink src/*.pyc
