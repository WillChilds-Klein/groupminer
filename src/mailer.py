# mailer.py

from pprint import pprint
import uuid
import bottle
import requests
import json

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

    def map_uuid(self, *args, **kwargs):
        try:
            message = kwargs['json_data']
        except KeyError:
            print 'uh oh! no json_data in message!'
        else:
            if 'uuid' not in message['data']:
                pass # of type none, TODO: move uuid into sender field!
            else:
                remote_uuid = message['data']['uuid']
                remote_info = (message['sender']['host'],
                               message['sender']['port'])

                self.uuid_map[remote_uuid] = remote_info
                print 'mapped %s to %s' % (remote_uuid,remote_info)

    def send_data(self, data, remote_uuid, endpoint='/mailbox'):
        ''' send data via http to 
        '''
        print 'uuid of recipient %s' % remote_uuid

        if remote_uuid not in self.uuid_map:
            raise UnkownHost("don't have host/port info for %s in uuid_map!" 
                            % remote_uuid)
        else:
            remote_host = self.uuid_map[remote_uuid][0]
            remote_port = self.uuid_map[remote_uuid][1]

            url = ('http://' + remote_host + ':' + str(remote_port) + endpoint)
            print 'url: ' + url

            payload_data = json.dumps(data, indent=4, separators=(',', ':'))
            headers = {'content-type': 'application/json'}

            requests.post(url=url, data=payload_data, headers=headers)
            print 'sent %s\n TO\n %s' % (payload_data, url)

def create_mailer():
    mailer = Mailer()
    return mailer