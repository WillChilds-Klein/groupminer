# receiver.py
# Responsible for handling incoming messages

import pprint


class MessageError(Exception):

    ''' Error caused by bad incoming message.
    '''

    def __init__(self, message):
        self.message = message


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

        request = kwargs['request']

        try:
            message = kwargs['data']
        except KeyError:
            message = None
        else:
            msgtype = message["type"]
            print 'processing message of type: %s' % msgtype

            if msgtype == "vote":
                self.groupthink.process_event('/vote_recieved',
                                              data=message['data'])
            elif msgtype == 'opinion':
                pass  # this type is only used for external auditing.
            elif msgtype == 'vote_request':
                self.groupthink.process_event('/vote_requested',
                                              data=message['data'])
            elif msgtype == 'opinion_request':
                self.groupthink.process_event('/opinion_requested',
                                              data=message['data'])
            else:
                raise MessageError('got bad message!')


def create_receiver():
    receiver = Receiver()
    return receiver
