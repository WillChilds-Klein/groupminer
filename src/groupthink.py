# groupthink.py

# Global context object


class StartupError(Exception):

    ''' Error occurred when starting node (context object).
    '''

    def __init__(self, message):
        self.message = message


class Groupthink:

    def __init__(self, *args, **kwargs):
        self.server = None
        self.receiver = None
        self.handlers = {}

    def run(self):
        ready = (self.server)
        if not ready:
            raise StartupError("Starting groupthink prematurely (server?)")

        self.server.run()

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


def create_groupthink():
    groupthink = Groupthink()
    return groupthink
