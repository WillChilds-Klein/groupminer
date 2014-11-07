# http_server.py
# Server object handles HTTP communication.
# Endpoints object sets which URL's to listen to requests

import bottle
import json


class Server:

    ''' Responsible for serving all HTTP requests and returning responses.
        Currently (and for forseeable future), HTTP server is just a wrapper
        around a JSON message receive path. All messages from any peer should
        go to the /mailbox URL, as a POST request, containing a valid JSON obj.
    '''

    def __init__(self):
        self.app = None

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

    def build_routes(self):
        ''' Tell bottle which routes to listen to. '''

        @bottle.route('/mailbox', method='POST')
        def mailbox():
            ''' All messages from peers go to /mailbox.
                Because HTTP is a simple wrapper, this method just starts the
                event chain for the /mailbox event.
            '''
            try:
                data = json.loads(bottle.request.body.read())
            except:
                bottle.abort(code=400, text='Invalid JSON.')

            # Start the event chain
            self.groupthink.process_event('/mailbox', data=data)

            # Return successfully to the user
            return bottle.HTTPResponse(status=200,
                                       body='{"status": "success"}')

    def run(self, **kwargs):
        self.app = bottle.run(**kwargs)


def create_server():
    ''' Factory method for Server objects. Used by main()'''
    server = Server()

    return server