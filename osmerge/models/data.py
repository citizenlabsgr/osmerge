import csv


class Data(object):

    FILENAME = 'osmerge.csv'

    HEADER_ID = '_id'
    HEADER_SHOW = '_show'
    HEADER = [HEADER_ID, HEADER_SHOW]

    @classmethod
    def generate_example(cls):
        with open(cls.FILENAME, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(cls.HEADER)
