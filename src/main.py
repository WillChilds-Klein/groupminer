#!/usr/bin/env python

# main.py
# Main application loop for groupthink

import argparse
import uuid

import groupthink
import http_server
import receiver
import history
import prediction
import opinion
import mailer

def main():
    ''' Launch all the objects, attaching them to each other.
        Parse cmd line args and set them to groupthink's nasmespace.
    '''

    description = ('Welcome to Groupthink, a decentralized, reputation-based' +
                   'content recommendation system.')
    portHelp = 'Specify instance port'
    hostnameHelp = 'Specify hostname or IPv4 address of instance'
    uuidHelp = 'Specify instance uuid'
    debugHelp = ('Run in debug mode for hot-swapping code on save during' +
                 'development')

    print 'Parsing command line arguments.'

    parser = argparse.ArgumentParser(description=description)
    parser.add_argument('-p', '--port', action="store", dest="port", 
                            default=8080, type=int, help=portHelp)
    parser.add_argument('--hostname', action='store', dest='hostname',
                            default='localhost', help=hostnameHelp)
    parser.add_argument('-u', '--uuid', action="store", dest="uuid_str", 
                            default=None, type=str, help=uuidHelp)
    parser.add_argument('-reload', '--reload-enabled', action="store_true", 
        dest="reload", default=False, help=debugHelp)

    clargs = vars(parser.parse_args())


    print 'Launching groupthink.'

    print '\t Creating groupthink object.'
    g = groupthink.create_groupthink(clargs=clargs)

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

    print '\t Creating mailer object.'
    m = mailer.create_mailer()

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

    print '\t Attaching mailer to groupthink.'
    g.attach_mailer(m)

    print 'Done initializing groupthink.\n'

    cmd = 'curl -H "Content-Type: application/json" -d'
    cmd += ' {"somedata":"miles"}'
    cmd += ' http://localhost:8080/mailbox'

    print 'Try this command to test:\n'
    print '\t' + cmd

    print '\nOk, running server...\n'

    g.run()


if __name__ == '__main__':
    main()
