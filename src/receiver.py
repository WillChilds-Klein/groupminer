# receiver.py
# Responsible for handling incoming messages


class Receiver:

    ''' Handles incoming messages.
    '''

    def __init__(self):
        self.groupthink = None

    def attach_groupthink(self, groupthink):
        ''' Attach to a Groupthink instance, and register event handlers.
        '''
        self.groupthink = groupthink
        self.groupthink.register_handler(event='/mailbox',
                                         callback=self.message_received)

    def message_received(self, *args, **kwargs):
        ''' This function will be called when the '/mailbox' event happens,
            and it expects to have a 'data' argument in **kwargs. This should
            be a valid JSON object (otherwise the user would have gotten an
            error).
        '''
        try:
            msgdata = kwargs['data']
        except KeyError:
            msgdata = None

        print 'Receiver got message:'

        from pprint import pprint
        pprint(msgdata)


def create_receiver():
    receiver = Receiver()
    return receiver
