#!/usr/bin/env python

# main.py
# Main application loop for groupthink

import groupthink
import http_server
import receiver


def main():
    ''' Launch all the objects, attach them to each other.
    '''

    print 'Launching groupthink.'

    print '\t Creating groupthink object.'
    g = groupthink.create_groupthink()

    print '\t Creating server object.'
    s = http_server.create_server()

    print '\t Creating receiver object.'
    r = receiver.create_receiver()

    print '\t Attaching server to groupthink.'
    g.attach_server(s)

    print '\t Attaching receiver to groupthink.'
    g.attach_receiver(r)

    cmd = 'curl -H "Content-Type: application/json" -d'
    cmd += ' {"somedata":"miles"}'
    cmd += ' http://localhost:8080/mailbox'

    print '\t Starting server.'

    print 'Done initializing groupthink.'

    print 'Try this command to test:\n'
    print '\t' + cmd

    print '\nOk, running server...'
    print
    g.run()


if __name__ == '__main__':
    main()
