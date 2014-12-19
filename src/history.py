# history.py

import uuid
from pprint import pprint
import bottle
import json

class History:

    ''' manages histories of peers' votes.
    '''

    def __init__(self):
        self.groupthink = None
        self.vote_history = {}

    def attach_groupthink(self, groupthink):
        ''' Attach to a Groupthink instance, and register event handlers.
        '''
        self.groupthink = groupthink
        self.groupthink.register_handler(event='/vote_recieved',
                                         callback=self.process_vote)

    def process_vote(self, data):
        ''' parse vote payload from message and add vote data to internal 
            datastructures. 
        '''
        print 'process_vote: adding vote data to history:'
        print "%s" % json.dumps(data, indent=2, separators=(',', ':'))

        coin_id = str(data['coin_id'])
        time = int(data['time'])
        node_uuid = uuid.UUID(data['uuid'])
        score = float(data['score'])
        
        self.vote_history[coin_id, time] = (node_uuid, score)


def create_history():
    history = History()
    return history