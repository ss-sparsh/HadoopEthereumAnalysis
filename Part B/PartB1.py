from mrjob.job import MRJob
import time

class PartB(MRJob):

    def mapper(self,_,line):
        try:
            fields = line.split(',')
            val = float(fields[3])
            if len(fields) == 7:
                add = fields[2]
                yield (add, val)
                #yield ((date.tm_mon,date.tm_year),val)


        except:
            pass

    def combiner(self,key,val):
        yield (key,(sum(val)))

    def reducer(self,key,val):
        yield (key, sum(val))

if __name__=='__main__':
    PartB.run()