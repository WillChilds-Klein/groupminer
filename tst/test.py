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

    test_uuid = uuid.UUID('dfb3d8ee-6ec0-491b-9e79-6511205cd7cc')
    uuid_str = str(test_uuid)
    print uuid_str

    test1 = {'type':'vote','data':{'uuid':uuid_str,     \
                                   'coin_id':'BTC',     \
                                   'time':12314121235,  \
                                   'score':0.9}}
    test2 = {'type':'vote_request','data':{'uuid':uuid_str}}
    test3 = {'type':'opinion_request','data':{'uuid':uuid_str}}

    tests = [test1, test2, test3]

    print linesep
    i = 0
    for test in tests:

        data = json.dumps(test, indent=4, 
                                separators=(',', ':'))
        print 'TEST %s DATA: %s' % (i, data) + '\n\n'

        r = requests.post(url=endpoint, data=data)

        try:
            r_json = r.json()
            print 'RESPONSE: %s' % json.dumps(r_json, indent=4, \
                                                      separators=(',', ':'))
        except:
            "TEST: invalid response to test: %s" % str(test)

        print linesep
        i += 1



if __name__ == '__main__':
    main()