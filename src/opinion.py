# opinion.py

import requests
import bottle

class Opinion:

    ''' manages histories of peers' votes.
    '''

    def __init__(self):
        self.groupthink = None
        self.vote_history = {}

    def attach_groupthink(self, groupthink):
        ''' Attach to a Groupthink instance, and register event handlers.
        '''
        self.groupthink = groupthink

    def process_request(self, data):
        print 'got process_request in opinion.py!!'

    
def create_opinion():
    opinion = Opinion()
    return opinion