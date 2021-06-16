from mrjob.job import MRJob
import time

class PartA(MRJob):

    def mapper(self,_,line):
        try:
            fields = line.split(',')
            date  = time.localtime(fields[6])
            if len(fields) == 7:
                yield ((date.tm_mon,date.tm_year),1)

        except:
            pass

    def combiner(self,key,val):
        yield (key,sum(val))

    def reducer(self,key,val):
        yield (key,sum(val))


if __name__=='__main__':
    PartA.run()