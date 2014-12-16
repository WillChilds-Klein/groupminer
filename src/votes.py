# Votes.py

class Votes:

    ''' manages histories of peers' votes.
    '''

    def __init__(self):
        self.groupthink = None
        self.vote_history = {}

    def attach_groupthink(self, groupthink):
        ''' Attach to a Groupthink instance, and register event handlers.
        '''
        self.groupthink = groupthink

    def add_vote(vote):
        ''' Add vote to internal datastructures. This method assumes that
            msgdata is list of form: [node_uuid,coin_id,time,score]
        '''
        node_uuid = vote[0]
        coin_id = vote[1]
        time = vote[2]
        score = vote[3]
        
        self.vote_history[node_uuid][coin_id] = [time,score]