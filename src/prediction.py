# prediction.py

import requests
import bottle

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

    def process_request(self, data):
        print 'got process_request in prediction.py!!'

        # Return successfully to the user
        return bottle.HTTPResponse(status=200,
                                   body='[{"status": "success"},\
                                          {"class": "prediction"},\
                                          {"method": "process_request"')

    
def create_prediction():
    prediction = Prediction()
    return prediction