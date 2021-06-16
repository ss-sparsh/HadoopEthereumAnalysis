from mrjob.job import MRJob

class PartB(MRJob):

    def mapper(self,_,line):
        try:
            if (len(line.split('\t'))==2):
                fields = line.split('\t')
                join_key = fields[0].strip('"\"\\\"')
                join_val = int(fields[1])
                yield (join_key,(join_val,1))

            elif(len(line.split(','))==5):
                fields = line.split(',')
                join_key = fields[0].strip('"\"\\\"')
                join_val = fields[3]
                yield (join_key, (join_val, 2))

        except:
            pass


    def reducer(self,company,val):
        years = []
        sector = 0

        if(val[1]==1):
            sector = val[0]
        elif(val[1]==2):
            years.append(val[0])

        if sector> 0 and len(years) != 0:
            yield (company,sector)

if __name__=='__main__':
    PartB.run()