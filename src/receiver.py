# receiver.py
# Responsible for handling incoming messages

import pprint

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
            message = kwargs['data']
        except KeyError:
            message = None

        # print 'Receiver got message:'
        # pprint.pprint(message)

        if not message == None:
            self.groupthink.process_message(message)


def create_receiver():
    receiver = Receiver()
    return receiver
