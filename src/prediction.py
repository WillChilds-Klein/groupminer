# prediction.py

import requests
import bottle
from pprint import pprint

class Prediction:

    ''' manages histories of peers' votes.
    '''

    def __init__(self):
        self.groupthink = None
        self.vote_history = {}

    def attach_groupthink(self, groupthink):
        ''' Attach to a Groupthink instance, and register event handlers.
        '''
        self.groupthink = groupthink
        self.groupthink.register_handler(event='/vote_requested',
                                         callback=self.process_request)

    def process_request(self, data):
        print 'got process_request in prediction.py!!'

        print 'data:'
        pprint(data, indent=1)

    
def create_prediction():
    prediction = Prediction()
    return prediction