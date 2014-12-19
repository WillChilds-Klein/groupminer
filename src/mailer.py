# mailer.py

from pprint import pprint
import uuid
import bottle
import requests
import json

class UnknownUUID(Exception):
    ''' Error caused by bad incoming message.
    '''
    def __init__(self, message):
        self.message = message

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
                                         callback=self.send_message)
        self.groupthink.register_handler(event='/mailbox',
                                         callback=self.map_uuid)

    def map_uuid(self, *args, **kwargs):
        try:
            message = kwargs['json_data']
        except KeyError:
            print 'uh oh! no json_data in message!'
        else:
            if 'uuid' not in message['data']:
                print 'tried to map_uuid, but no uuid in message data!!'
                pass # probably of type none
            else:
                remote_uuid = message['data']['uuid']
                remote_info = (message['sender']['host'],
                               message['sender']['port'])

                self.uuid_map[remote_uuid] = remote_info
                print 'mapped %s to %s' % (remote_uuid,remote_info)

    def send_message(self, type, data, remote_uuid, endpoint='/mailbox'):
        ''' send data via http to remote_uuid's hostname/port
        '''
        if remote_uuid not in self.uuid_map:
            raise UnknownUUID("don't have host/port info for %s in uuid_map!" 
                            % remote_uuid)

        sender = {
            'host': self.groupthink.hostname, 
            'port': self.groupthink.port
        }

        message = {
            'type': type,
            'data': data,
            'sender': sender
        }

        remote_host = self.uuid_map[remote_uuid][0]
        remote_port = self.uuid_map[remote_uuid][1]
        url = ('http://' + remote_host + ':' + str(remote_port) + endpoint)

        requests.post(url=url, json=message)
        print 'POSTED %s TO %s' % (json.dumps(message, indent=2, 
                                                      separators=(',', ':')), 
                                     url)

def create_mailer():
    mailer = Mailer()
    return mailer