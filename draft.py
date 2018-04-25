import pandas
import csv
statsFile = pandas.read_excel('stats.xlsx')
print(list(statsFile))
#got data from https://www.basketball-reference.com/leagues/NBA_2017_per_game.html
def BVPalgorithm(pts,rbs,assists,steals,blks,to,mp):
        BVP = (pts + rbs + (assists*1.5) + (steals*2) + (blks*2) - to) * (mp/18.8) 
        #Median minutes played calculated from this print(statsFile["MP"].median())
        return BVP

def writelinetoCSV(line, file):
        #print(line)
        filewriter = csv.writer(file, quoting = csv.QUOTE_NONE, delimiter = ',', quotechar='', lineterminator='\n')
        filewriter.writerow(line)

def applyAlgorithm(file):
   # header = "'Name', 'BVP','Team','Position'"
    #header = header.split(',"')
    #print(header)
    with open('/BVPFantasy.csv','w') as csv_file:

        for row in statsFile.itertuples():
                team = row[5]
                pos = row[3]
                name = row[2]
                pts = ((row[12]*3) + (row[15] * 2) + (row[19] * 1))
                rbs = (row[22] +row[23] + row[24])
                assists = row[25]
                steals = row[26]
                blks = row[27]
                to = row[28]
                mp = row[8]
                BVP = BVPalgorithm(pts,rbs,assists,steals,blks,to,mp)
                IndexofSlash = name.index('\\')
                name = name[:IndexofSlash]
                outputstring = name + "," + str(BVP) + "," + str(team) + ',' + str(pos)
                print(outputstring)
                #writelinetoCSV(outputstring,csv_file)

applyAlgorithm(statsFile)





