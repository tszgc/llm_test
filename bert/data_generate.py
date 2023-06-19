import math
import csv

targetFile = './data_sequence_sin.tsv'


def generateFineTuneData():
    with open(targetFile, 'wt') as data_file:
        tsv_writer = csv.writer(data_file, delimiter='\t')
        for i in range(0, 180):
            tsv_writer.writerow(['sin(' + str(i) + ')', math.sin(math.radians(i))])


if __name__ == '__main__':
    generateFineTuneData()
    # print(math.sin(90))
