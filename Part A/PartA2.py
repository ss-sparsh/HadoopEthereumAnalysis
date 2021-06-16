from mrjob.job import MRJob
import time

class PartA(MRJob):

    def mapper(self,_,line):
        try:
            fields = line.split(',')
            val = float(fields[3])
            date = time.gmtime(float(fields[6]))
            if len(fields) == 7:
                yield ((date.tm_mon,date.tm_year), (1, val))
                #yield ((date.tm_mon,date.tm_year),val)


        except:
            pass

    def combiner(self,key,val):
        count = 0
        total = 0
        for v in val:
            count+= v[0]
            total+= v[1]

        yield (key,(count,total))

    def reducer(self,key,val):
        count = 0
        total = 0
        for v in val:
            count += v[0]
            total += v[1]

        yield (key, (total,count))

if __name__=='__main__':
    PartA.run()