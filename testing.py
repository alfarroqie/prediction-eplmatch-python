import utility as utils
import calculation as calculation
import os
import sys
import csv

for idx in [6, 7] :
    utils.set_year_length(idx)

    try :    
        inp = open(os.path.join(sys.path[0], "result\\Test_Data.csv"), "r", encoding="utf-8")
        out = open(os.path.join(sys.path[0], "result\\Testing_"+ str(idx) +"_Years.csv"), "w", encoding="utf-8", newline ="")

        writer = csv.writer(out)

        #writing header for csv
        writer.writerow(["Matchday", "Date", "HomeTeam", "AwayTeam", "HomeWin", "Draw", "HomeLose", "ActualResult"])

        #read the header
        next(inp)

        for x in csv.reader(inp) :
            row = utils.split_list(x, ";")

            home_team = row[2]
            away_team = row[3]
            date = row[1]
            season = utils.get_season(row[1])

            utils.generate_data_for_calculation(home_team, away_team, utils.get_year(date))

            result = calculation.calculate(home_team, away_team, season)

            writer.writerow([row[0], date, home_team, away_team, result[0]+"%", result[1]+"%", result[2]+"%", row[4]])


    except IOError as err :
        print("IO Error Number", err.errno, "[", err.strerror, "]")