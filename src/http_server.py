# http_server.py
# Server object handles HTTP communication.
# Endpoints object sets which URL's to listen to requests

import bottle
import json
import pprint
import socket

class MessageError(Exception):
    ''' Error caused by bad incoming message.
    '''
    def __init__(self, message):
        self.message = message

class Server:

    ''' Responsible for serving all HTTP requests and returning responses.
        Currently (and for forseeable future), HTTP server is just a wrapper
        around a JSON message receive path. All messages from any peer should
        go to the /mailbox URL, as a POST request, containing a valid JSON obj.
    '''

    def __init__(self):
        self.app = None
        self.reload = None

    def attach_groupthink(self, groupthink):
        ''' Attach to a Groupthink insance and register event handlers.
            Cannot run server until attached to groupthink.
        '''
        self.groupthink = groupthink

        self.register_events()
        self.build_routes()

    def register_events(self):
        ''' Register each possible event with the groupthink instance.
        '''
        self.groupthink.register_event('/mailbox')
        self.groupthink.register_event('/vote_recieved')
        self.groupthink.register_event('/vote_requested')
        self.groupthink.register_event('/opinion_requested')
        self.groupthink.register_event('/send')

    def build_routes(self):
        ''' Tell bottle which routes to listen to.
        '''
        @bottle.post('/mailbox')
        def mailbox():
            ''' All vote submission messages from peers go to /mailbox.
                Because HTTP is a simple wrapper, this method just starts the
                event chain for the /mailbox event.
            '''
            try:
                json_data = bottle.request.json
            except:
                print 'invalid message! request body: %s' % bottle.request.body
                bottle.abort(code=400, text='Invalid JSON.')

            print ('raw JSON: %s' % json.dumps(json_data, indent=2, 
                                               separators=(',', ':')))

            for key in ['type','data','sender']:
                if key not in json_data:
                    raise MessageError('invalid message! not all keys present!')

            # Start the event chain
            self.groupthink.process_event('/mailbox', json_data=json_data)

            # Return successfully to the user
            return bottle.HTTPResponse(status=200,
                                       body='{"status": "success"}')

        @bottle.post('/ping')
        def ping():
            return bottle.HTTPResponse(status=200,
                                       body='{"status": "success"}')

    def run(self, **kwargs):
        try:
            self.app = bottle.run(reloader=self.groupthink.reload,
                                  port=self.groupthink.port,
                                  **kwargs)
        except socket.error as e:
            print 'Socket error: %s' % e



def create_server():
    ''' Factory method for Server objects. Used by main()
    '''
    server = Server()

    return server
