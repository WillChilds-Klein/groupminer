# test.py

import requests
import json
import uuid


def main():
    ''' each request is a test case...kinda
    '''
    test_sep = ('--------------------------------------------------\n' +
               'TEST %s\n' +
               '=======\n')
    test_end = '--------------------------------------------------'
    tests = []

    instance_host = 'localhost'
    instance_port = 8080
    instance_endpoint = '/mailbox'
    instance_url = ('http://' + instance_host + ':' + str(instance_port) + 
                                instance_endpoint)

    # init test data variables
    # test_uuid = str(uuid.uuid4())
    test_uuid = 'dfb3d8ee-6ec0-491b-9e79-6511205cd7cc'
    test_coin = 'BTC'
    test_time = 12314121235
    test_score = 0.9
    test_host = 'localhost'
    test_port = 9090

    test1 = {
        'type': 'vote',
        'data': {
            'coin_id': test_coin,
            'time': test_time,
            'score': test_score,
            'uuid': test_uuid
        },
        'sender': {
            'host': test_host,
            'port': test_port,
        }
    }
    tests.append(test1)

    test2 = {
        'type': 'vote_request',
        'data': {
            'coin_id': test_coin,
            'time': test_time,
            'uuid': test_uuid
        },
        'sender': {
            'host': test_host,
            'port': test_port,
        }
    }
    tests.append(test2)

    test3 = {
        'type': 'opinion_request',
        'data': {
            'uuid': test_uuid
        },
        'sender': {
            'host': test_host,
            'port': test_port,
        }
    }
    tests.append(test3)


    test4 = {
        'type':'none',
        'data':{
            'uuid': test_uuid
        },
        'sender': {
            'host': test_host,
            'port': test_port,
        }
    }
    tests.append(test4)

    i = 0
    for test in tests:
        print test_sep % i
        nice_data = json.dumps(test, indent=2, separators=(',', ':'))
        print 'REQUEST: %s' % nice_data

        r = requests.post(url=instance_url, json=test)
        try:
            r_json = r.json()
            print ('RESPONSE: %s' % json.dumps(r_json, indent=2,
                                                       separators=(',', ':')))
        except:
            "RESPONSE: invalid response to test: %s" % str(test)
        i += 1
    print test_end

if __name__ == '__main__':
    main()
