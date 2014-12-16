#!/usr/bin/env python

# main.py
# Main application loop for groupthink

import groupthink
import http_server
import receiver
import history
import prediction
import opinion


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

    print '\t Creating history object.'
    h = history.create_history()

    print '\t Creating prediction object.'
    p = prediction.create_prediction()

    print '\t Creating opinion object.'
    o = opinion.create_opinion()

    print '\t Attaching server to groupthink.'
    g.attach_server(s)

    print '\t Attaching receiver to groupthink.'
    g.attach_receiver(r)

    print '\t Attaching history to groupthink.'
    g.attach_history(h)

    print '\t Attaching prediction to groupthink.'
    g.attach_prediction(p)

    print '\t Attaching opinion to groupthink.'
    g.attach_opinion(o)

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
