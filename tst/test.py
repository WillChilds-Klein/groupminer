# test.py

import requests
import json
import uuid


def main():
    ''' each request is a test case...kinda
    '''

    linesep = '--------------------------------------------------\n\n'
    endpoint = 'http://127.0.0.1:8080/mailbox'
    tests = []

    # init test data variables
    # test_uuid = str(uuid.uuid4())
    test_uuid = 'dfb3d8ee-6ec0-491b-9e79-6511205cd7cc'
    test_coin = 'BTC'
    test_time = 12314121235
    test_score = 0.9

    test1 = {'type': 'vote', 'data': {'uuid': test_uuid,
                                      'coin_id': test_coin,
                                      'time': test_time,
                                      'score': 0.9}}
    tests.append(test1)

    test2 = {'type': 'vote_request', 'data': {'uuid': test_uuid}}
    tests.append(test2)

    test3 = {'type': 'opinion_request', 'data': {'uuid': test_uuid}}
    tests.append(test3)

    print linesep
    i = 0
    for test in tests:

        data = json.dumps(test, indent=4,
                          separators=(',', ':'))
        print 'TEST %s DATA: %s' % (i, data) + '\n\n'

        r = requests.post(url=endpoint, data=data)

        try:
            r_json = r.json()
            print 'RESPONSE: %s' % json.dumps(r_json, indent=4,
                                              separators=(',', ':'))
        except:
            "TEST: invalid response to test: %s" % str(test)

        print linesep
        i += 1


if __name__ == '__main__':
    main()
