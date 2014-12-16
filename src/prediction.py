# prediction.py

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

    def process_request(data):
        print 'got process_request in prediction.py!!'

    
def create_prediction():
    prediction = Prediction()
    return prediction