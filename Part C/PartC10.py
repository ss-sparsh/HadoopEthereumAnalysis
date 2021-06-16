from mrjob.job import MRJob

class PartC(MRJob):

    def mapper(self,_,line):
        try:
            fields = line.split('\t')
            if len(fields) == 2:
                add = fields[0]
                agg = float(fields[1])
                yield (None,(add, agg))
        except:
            pass

    def combiner(self, key, val):
        sorted_values = sorted(val,reverse=True, key=lambda tup:tup[1])

        i=0
        for v in sorted_values:
            yield ("Top",v)
            i += 1
            if i >= 10:
                break

    def reducer(self,key,val):
        sorted_values = sorted(val, reverse=True, key=lambda tup: tup[1])

        i = 0
        for v in sorted_values:
            yield ("{}-{}".format(v[0], v[1]))
            i+=1
            if i>=10:
                break


if __name__=='__main__':
    PartC.run()