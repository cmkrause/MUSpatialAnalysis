from ez.Stats import *

def raceContigencyAnalysis(race):
    collegesFC = "C:\\NHGIS\\CollegeScorecard.gdb\\Points2013_REGION_2"
    hotspotsFC = "C:\\NHGIS\\HotSpots.gdb\\%s_REGION_2" % race

    rowQueries = ["Gi_Bin >= 1", "Gi_Bin <= -1"]
    columnQueries = ["CONTROL = 1 or CONTROL = 2", "CONTROL = 3"]

    rowNames = ["Hot Spots", "Cold Spots"]
    columnNames = ["Public or Private Non-Profit", "Private For-Profit"]

    contigencyTable2FC(collegesFC, hotspotsFC, columnQueries, rowQueries, columnNames, rowNames, display = False, outputFile = "C:\\NHGIS\\%s.csv" % race)



if __name__ == "__main__":

    from ez.Timer import *
    import multiprocessing as mp

    timer = ezTimer()

    races = ["CM1AA", "CM1AB", "CM1AC", "CM1AD", "CM1AE", "CM1AF", "CM1AG"]
##    raceContigencyAnalysis(races[0])
    pool = mp.Pool()
    for race in races:
        pool.apply_async(raceContigencyAnalysis, args = (race, ))
    pool.close()
    pool.join()

    timer.report()
