# groupthink.py

# Global context object

import uuid

class StartupError(Exception):
    ''' Error occurred when starting node (context object).
    '''
    def __init__(self, message):
        self.message = message


class Groupthink:

    def __init__(self, *args, **kwargs):
        self.server = None
        self.receiver = None
        self.history = None
        self.prediction = None
        self.opinion = None
        self.handlers = {}

        try:
            clargs = kwargs['clargs']
        except KeyError:
            print 'oh noes! no clargs passed to Groupthink object on init!'
            clargs = None

        self.port = clargs['port']
        if not clargs['uuid_str'] == None:
            self.uuid = uuid.UUID(clargs['uuid_str'])
        else:
            self.uuid = uuid.uuid4()
        self.reload = clargs['reload']

    def run(self):
        ''' start the server
        '''
        print 'port: %s' % self.port
        print 'uuid: %s' % self.uuid
        print 'reload: %s\n' % self.reload

        ready = (self.server)
        if not ready:
            raise StartupError("Starting groupthink prematurely (server?)")

        self.server.run()

    def process_event(self, event, *args, **kwargs):
        print 'Processing event %s' % event
        self.call_handlers(event, *args, **kwargs)

    def register_event(self, event):
        if event not in self.handlers.keys():
            self.handlers[event] = []
        else:
            print 'WARNING: Registering event "%s" more than once.' % event

    def call_handlers(self, event, *args, **kwargs):
        for handler in self.handlers[event]:
            handler(*args, **kwargs)

    def register_handler(self, event, callback):
        if event not in self.handlers.keys():
            print ('Warning: Registering handler "%s" on unknown event "%s".' 
                    % (callback, event))
            self.register_event(event)

        self.handlers[event].append(callback)

    def attach_server(self, server):
        if self.server:
            raise StartupError("Trying to attach second server.")

        server.attach_groupthink(self)
        self.server = server

    def attach_receiver(self, receiver):
        if self.receiver:
            raise StartupError("Trying to attach second receiver.")

        receiver.attach_groupthink(self)
        self.receiver = receiver

    def attach_history(self, history):
        if self.history:
            raise StartupError("Trying to attach second history.")

        history.attach_groupthink(self)
        self.history = history

    def attach_prediction(self, prediction):
        if self.prediction:
            raise StartupError("Trying to attach second prediction.")

        prediction.attach_groupthink(self)
        self.prediction = prediction

    def attach_opinion(self, opinion):
        if self.opinion:
            raise StartupError("Trying to attach second opinion.")

        opinion.attach_groupthink(self)
        self.opinion = opinion


def create_groupthink(clargs=None):
    groupthink = Groupthink(clargs=clargs)
    return groupthink
