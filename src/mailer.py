# mailer.py

from pprint import pprint
import uuid
import bottle

class Mailer:

    ''' manages outgoing messages.
    '''

    def __init__(self):
        self.groupthink = None
        self.uuid_map = {}

    def attach_groupthink(self, groupthink):
        ''' Attach to a Groupthink instance, and register event handlers.
        '''
        self.groupthink = groupthink
        self.groupthink.register_handler(event='/send',
                                         callback=self.send_data)
        self.groupthink.register_handler(event='/mailbox',
                                         callback=self.map_uuid)

    def send_data(self, data, remote_uuid, endpoint='/mailbox'):
        ''' send data via http to 
        '''
        if remote_uuid not in uuid_map:
            raise UnkownHost("don't have host/port info for %s in uuid_map!" 
                            % remote_uuid)
        else:
            remote_host = uuid_map[remote_uuid][0]
            remote_port = uuid_map[remote_uuid][1]
            url = 'http://' + remote_host + ':' + remote_port + endpoint

            payload_data = json.dumps(data, indent=4, separators=(',', ':'))
            requests.post(url=endpoint, data=payload_data)

    def map_uuid(self, data):
        try:
            message = kwargs['data']
        except KeyError:
            message = None
        else:
            remote_uuid = message['data']['uuid']
            remote_info = (message['sender']['host'],
                           message['sender'],['port'])
            uuid_map[remote_uuid] = remote_info

            print 'mapped %s to %s' % (remote_uuid,remote_info)