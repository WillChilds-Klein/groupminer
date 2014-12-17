import uuid
import click
import os
import envoy
import urllib2
import sys
import requests
import json

EXECUTABLE = 'run.sh'
LOCALADDR = "127.0.0.1"

sys.path.insert(0, os.path.abspath('..'))


class Topology:

    def __init__(self):
        self.nodes = []

topo = Topology()


class LaunchException(Exception):

    def __init__(self, msg):
        self.msg = msg


class Node:

    def __init__(self, ip, uuid, port):
        self.ip = str(ip)
        self.uuid = str(uuid)
        self.port = str(port)
        self.logfile = "logs/node-" + self.port + ".log"

    def __repr__(self):
        return '<IP: %s, UUID: %s, PORT: %s>' % (self.ip, self.uuid, self.port)

    def launch(self):
        try:
            os.system("python src/main.py -p %s -u %s >%s &" %
                      (self.port, self.uuid, self.logfile))
        except Exception as e:
            print e

    def ping(self):
        endpoint = 'http://%s:%s/ping' % (self.ip, self.port)
        msg = {'hello':'world'}

        print endpoint

        success = False

        try:
            r = requests.post(url=endpoint, data=json.dumps(msg))
            r.json()
            json.dumps(r.json(), indent=4, separators=(',', ':'))
            print 'Ping Successful'
            success = True

        except requests.exceptions.ConnectionError:
            print 'Failed to make ping connection'
        except ValueError:
            print 'Warning! Ping failed!'
            print r
            success = False

        return success


def pingall():
    for node in topo.nodes:
        retries = 0
        print 'Attempting to ping %s' % node
        while(not node.ping() and retries < 5):
            print 'Error, ping vailed to %s' % node
            retries += 1

def launch(n, startp):
    print 'Launching cluster with n nodes'

    nodes = []
    for nodei in range(n):
        uuidval = str(uuid.uuid1())
        port = startp + nodei

        print 'Attempting create newnode(%s, %s, %s)' % (LOCALADDR, uuidval, port)
        newnode = Node(LOCALADDR, uuidval, port)

        print 'Attempting launch %s' % newnode
        try:
            newnode.launch()
            print 'Launch successful; no exceptions.'
        except LaunchException as e:
            print 'Launch failed: %s' % e.msg

        topo.nodes.append(newnode)

    print 'Attempting to ping all nodes'
    pingall()

def sanitydebug():
    print '-' * 35 + ' Debug:'
    print '\t Cur dir: %s' % os.path.realpath(os.path.curdir)
    print '-' * 35


@click.command()
@click.option('--n', default=1, help='Number of nodes')
@click.option('--p', default=59873, help='Starting port number')
def main(n, p):

    sanitydebug()
    launch(n, p)

if __name__ == '__main__':
    print
    main()
