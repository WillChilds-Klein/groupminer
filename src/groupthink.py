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
        self.uuid = uuid.uuid4()

    def run(self):
        ready = (self.server)
        if not ready:
            raise StartupError("Starting groupthink prematurely (server?)")

        self.server.run()

    def process_message(message):
        ''' process incoming message
        '''
        msgtype = message["type"]

        if msgtype == "vote":
            history.add_score(message["data"])
        elif msgtype == "opinion":
            pass # this type is only used for external auditing.
        elif msgtype == "vote_request":
            prediction.process_request(message["data"])
        elif msgtype == "opinion_request":
            opinion.process_request(message["data"])
        else:
            pass # TODO: raise bad mesage error

    def register_event(self, event):
        if event not in self.handlers.keys():
            self.handlers[event] = []
        else:
            print 'WARNING: Registering event "%s" more than once.' % event

    def register_handler(self, event, callback):
        if event not in self.handlers.keys():
            print 'Warning: Registering handler "%s" on unknown event "%s".' \
                % (callback, event)
            self.register_event(event)

        self.handlers[event].append(callback)

    def process_event(self, event, *args, **kwargs):
        print 'Processing event %s' % event
        self.call_handlers(event, *args, **kwargs)

    def call_handlers(self, event, *args, **kwargs):
        for handler in self.handlers[event]:
            handler(*args, **kwargs)

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



def create_groupthink():
    groupthink = Groupthink()
    return groupthink
