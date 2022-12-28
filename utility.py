import csv
import os
import sys

year_length = 5

def clean_match_data() :
    try :
        inp = open(os.path.join(sys.path[0], "data\\EPL_Set.csv"), "r", encoding="utf-8")
        out = open(os.path.join(sys.path[0], "data\\EPL_Set_Cleaned.csv"), "w", encoding="utf-8", newline="")

        writer = csv.writer(out)

        for row in csv.reader(inp) :
            writer.writerow([row[1], convert_team_name(row[2]), convert_team_name(row[3]), row[4], row[5], row[6]])

    except IOError as err :
        print("IO Error Number", err.errno, "[", err.strerror, "]")
            
def convert_team_name(name) :
    if name == "Birmingham" :
        return "Birmingham City"
    elif name == "Blackburn" :
        return "Blackburn Rovers"
    elif name == "Bolton" :
        return "Bolton Wanderers"
    elif name == "Bradford" :
        return "Bradford City"
    elif name == "Brighton" :
        return "Brighton & Hove Albion"
    elif name == "Cardiff" :
        return "Cardiff City"
    elif name == "Charlton" :
        return "Charlton Athletic"
    elif name == "Coventry" :
        return "Coventry City"
    elif name == "Derby" :
        return "Derby County"
    elif name == "Huddersfield" :
        return "Huddersfield Town"
    elif name == "Hull" :
        return "Hull City"
    elif name == "Ipswich" :
        return "Ipswich Town"
    elif name == "Leeds" :
        return "Leeds United"
    elif name == "Leicester" :
        return "Leicester City"
    elif name == "Man City" :
        return "Manchester City"
    elif name == "Man United" :
        return "Manchester United"
    elif name == "Middlesboro" :
        return "Middlesbrough"
    elif name == "Newcastle" :
        return "Newcastle United"
    elif name == "Norwich" :
        return "Norwich City"
    elif name == "Nott'm Forest" :
        return "Nottingham Forest"
    elif name == "Oldham" :
        return "Oldham Athletic"
    elif name == "QPR" :
        return "Queen Park Rangers"
    elif name == "Sheffield" :
        return "Sheffield United"
    elif name == "Stoke" :
        return "Stoke City"
    elif name == "Swansea" :
        return "Swansea City"
    elif name == "Swindon" :
        return "Swindon Town"
    elif name == "Tottenham" :
        return "Tottenham Hotspur"
    elif name == "West Brom" :
        return "West Bromwich Albion"
    elif name == "West Ham" :
        return "West Ham United"
    elif name == "Wigan" :
        return "Wigan Athletic"
    elif name == "Wimbledon" :
        return "AFC Wimbledon"
    elif name == "Wolves" :
        return "Wolverhampton Wanderers"
    else :
        return name

def generate_data_for_calculation(home_team, away_team, year) :
    
    try :
        inp = open(os.path.join(sys.path[0], "data\\EPL_Set_Cleaned.csv"), "r", encoding="utf-8")
        out = open(os.path.join(sys.path[0], "data\\Data_For_Claculation.csv"), "w", encoding="utf-8", newline ="")

        writer = csv.writer(out)

        #writing header for csv
        writer.writerow(["Date", "HomeTeam", "AwayTeam", "Season", "FTHG", "FTAG", "FTR"])

        #read the first line(header) to avoid error
        next(inp)

        for row in csv.reader(inp) :
            season = get_season(row[0])

            if row[1] == home_team and row[2] == away_team :
                if int(year) - int(get_year(row[0])) <= year_length :
                    writer.writerow([row[0], row[1], row[2], season, row[3], row[4], row[5]])
            
            if row[1] == away_team and row[2] == home_team :
                if int(year) - int(get_year(row[0])) <= year_length :
                    writer.writerow([row[0], row[1], row[2], season, row[3], row[4], row[5]])
                    
    except IOError as err :
        print("IO Error Number", err.errno, "[", err.strerror, "]")

def get_year(date) :
    length = len(date)
    slash = 0

    for idx in range(0, length):
        if date[idx] == "/" :
            slash += 1

        if slash == 2:
            # this is the year
            if length - idx - 1 == 4 :
                #format yyyy
                return date[idx + 1 :]
            
            else :
                #format yy
                if int(date[idx + 1 : ]) < 80:
                    return "20" + date[idx + 1 : ]
                else :
                    return "19" + date[idx + 1 : ]

def get_season(date) :
    first_slash = 0
    second_slash = 0
    length = len(date)
    month = ""

    for idx in range(0, length) :
        if date[idx] == "/" :
            if first_slash == 0 :
                first_slash = idx
            else :
                second_slash = idx

    month = date[first_slash + 1 : second_slash]

    if int(month) >= 3 and int(month) < 6 :
        return "Spring"
    if int(month) >= 6 and int(month) < 9 :
        return "Summer"
    elif int(month) >= 9 and int(month) < 12 :
        return "Autumn"
    else :
        return "Winter"

def count_data():
    try :
        inp = open(os.path.join(sys.path[0], "data\\Data_For_Claculation.csv"), "r", encoding="utf-8")

        reader = csv.reader(inp)
        return len(list(reader)) - 1
        
    except IOError as err :
        print("IO Error Number", err.errno, "[", err.strerror, "]")

# def count_prior_probability():
def count_prior_probability(home_team):
    win = 0
    draw = 0
    lose = 0
    result = []

    try :
        inp = open(os.path.join(sys.path[0], "data\\Data_For_Claculation.csv"), "r", encoding="utf-8")

        #read the first line(header) to avoid error
        next(inp)

        for row in csv.reader(inp):
            # if row[6] == "H" :
            if (row[6] == "H" and row[1] == home_team) or (row[6] == "A" and row[2]== home_team) :
                win += 1
            elif row[6] == "D" :
                draw  += 1
            else :
                lose += 1
        
        result.append(win)
        result.append(draw)
        result.append(lose)

        return result
    except IOError as err :
        print("IO Error Number", err.errno, "[", err.strerror, "]")

def count_likelihood_place(home_team, is_counting_home_team):
    win = 0
    draw = 0
    lose = 0
    result = []

    try :
        inp = open(os.path.join(sys.path[0], "data\\Data_For_Claculation.csv"), "r", encoding="utf-8")

        #read the first line(header) to avoid error
        next(inp)
        
        for row in csv.reader(inp):
            if is_counting_home_team :
                #counting when the home team input is have a match in their home stadium
                if row[6] == "H" and  row[1] == home_team :
                    win += 1
                elif row[6] == "D" and row[1] == home_team :
                    draw  += 1
                elif row[6] == "A" and row[1] == home_team:
                    lose += 1
            else :
                #counting when the home team input is have a match in their away team stadium
                if row[6] == "A" and  row[2] == home_team :
                    win += 1
                elif row[6] == "D" and row[2] == home_team :
                    draw  += 1
                elif row[6] == "H" and row[2] == home_team :
                    lose += 1
        
        result.append(win)
        result.append(draw)
        result.append(lose)

        return result
    except IOError as err :
        print("IO Error Number", err.errno, "[", err.strerror, "]")

def count_likelihood_season(the_season):
    win = 0
    draw = 0
    lose = 0
    result = []

    try :
        inp = open(os.path.join(sys.path[0], "data\\Data_For_Claculation.csv"), "r", encoding="utf-8")

        #read the first line(header) to avoid error
        next(inp)
        
        for row in csv.reader(inp):
            if row[6] == "H" and  row[3] == the_season :
                win += 1
            elif row[6] == "D" and row[3] == the_season :
                draw  += 1
            elif row[6] == "A" and row[3] == the_season :
                lose += 1
        
        result.append(win)
        result.append(draw)
        result.append(lose)

        return result
    except IOError as err :
        print("IO Error Number", err.errno, "[", err.strerror, "]")

def get_team_list() :
    return ["Arsenal", "Aston Villa", "Bournemouth", "Brighton & Hove Albion",
            "Burnley", "Chelsea", "Crystal Palace", "Everton", "Leicester City",
            "Liverpool", "Manchester City", "Manchester United", "Newcastle United",
            "Norwich City", "Sheffield United", "Southampton", "Tottenham Hotspur",
            "Watford", "West Ham United", "Wolverhampton Wanderers"]

def get_image_path(team) :
    return os.path.join(sys.path[0], "data\\image\\", team + ".PNG")

def set_year_length(new_year):
    global year_length
    year_length = new_year

def split_list(the_list, delimiter):
    head = 0
    tail = 0
    result = []

    length = len(the_list[0])

    for i in range(0, length) :
        if the_list[0][i] == delimiter :
            tail = i
            result.append(the_list[0][head : tail])
            head = i + 1

    result.append(the_list[0][length-1 : length])
    return result
        