from mrjob.job import MRJob
import time

class PartA(MRJob):

    def mapper(self,_,line):
        try:
            fields = line.split(',')
            if len(fields) == 9:
                size = float(fields[4])
                miner = fields[2]
                yield (fields[2], size)
        except:
            pass

    def combiner(self,key,val):
        yield (key,sum(val))

    def reducer(self,key,val):
        yield (key,sum(val))


if __name__=='__main__':
    PartA.run()