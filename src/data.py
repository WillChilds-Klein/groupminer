import csv

import datetime


class DataSource:

    ''' Parser for CSV files of format (time, val).
        Currently only for parsing coin difficulty history from blockchain.info
        e.g. :

            ds = DataSource('/groupthinkminer/data/bitcoindifficulty.csv')
            for time, val in ds.tvtuples:
                print time, val
    '''

    def __init__(self, csvfilename):
        ''' csvfilename is absolute path to csc file
        '''
        self.csvfilename = csvfilename
        self.records = []

        self.load()

    @property
    def tvtuples():
        ''' ds.tvtuples is a list of time/value tuples:
                (DATETIME, DIFFICULTY)
        DATETIME is a python datetime object, DIFFICULTY is a float.'''
        return self.records

    def load(self):
        with open(self.csvfilename, 'rb') as csvfile:
            for date, difficulty in csv.reader(csvfile, delimiter=','):
                d = datetime.datetime.strptime(date, "%d/%m/%Y %H:%M:%S")
                self.records.append((d, difficulty))


def examplefunc():
    ds = DataSource('bitcoindifficulty.csv')
    for date, difficulty in ds.tvtuples:
        print date, difficulty
