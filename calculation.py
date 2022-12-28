import utility as utils
#define the corresponding data in empty list and empty number
laplace_estimator = False
data_amount = 0
prior_probability = []
likelihood_place_home = []
likelihood_place_away = []
likelihood_season_spring = []
likelihood_season_summer = []
likelihood_season_autumn = []
likelihood_season_winter = []
the_season = []
win_probability = 0.0
draw_probability = 0.0
lose_probability = 0.0


#the method
def generate_all_data(home, season):
    global data_amount 
    data_amount = utils.count_data()
    
    global prior_probability 
    # prior_probability = utils.count_prior_probability()
    prior_probability = utils.count_prior_probability(home)
    print('prior_probability before laplace estimator: ', prior_probability)
    
    global likelihood_place_home 
    likelihood_place_home = utils.count_likelihood_place(home, True)
    print('likelihood_place_home before laplace estimator: ', likelihood_place_home)
    
    global likelihood_place_away
    likelihood_place_away = utils.count_likelihood_place(home, False)
    print('likelihood_place_away before laplace estimator: ', likelihood_place_away)
    
    global likelihood_season_spring 
    likelihood_season_spring = utils.count_likelihood_season("Spring")
    print('likelihood_season_spring before laplace estimator: ', likelihood_season_spring)
    
    global likelihood_season_summer
    likelihood_season_summer = utils.count_likelihood_season("Summer")
    print('likelihood_season_summer before laplace estimator: ', likelihood_season_summer)
    
    global likelihood_season_autumn 
    likelihood_season_autumn = utils.count_likelihood_season("Autumn")
    print('likelihood_season_autumn before laplace estimator: ', likelihood_season_autumn)
    
    global likelihood_season_winter
    likelihood_season_winter = utils.count_likelihood_season("Winter")
    print('likelihood_season_winter before laplace estimator: ', likelihood_season_winter)

def laplace_estimator_is_estimator_needed() :
    if 0 in prior_probability :
        return True
    if 0 in likelihood_place_home :
        return True
    if 0 in likelihood_place_away :
        return True
    if 0 in likelihood_season_spring :
        return True
    if 0 in likelihood_season_summer :
        return True
    if 0 in likelihood_season_autumn :
        return True
    if 0 in likelihood_season_winter :
        return True

def do_laplace_estimator() :
    global laplace_estimator
    laplace_estimator = True

    global prior_probability
    prior_probability = [x + 1 for x in prior_probability]

    global likelihood_place_home
    likelihood_place_home = [x + 1 for x in likelihood_place_home]
    
    global likelihood_place_away
    likelihood_place_away = [x + 1 for x in likelihood_place_away]

    global likelihood_season_spring
    likelihood_season_spring = [x + 1 for x in likelihood_season_spring]

    global likelihood_season_summer
    likelihood_season_summer = [x + 1 for x in likelihood_season_summer]

    global likelihood_season_autumn
    likelihood_season_autumn = [x + 1 for x in likelihood_season_autumn]

    global likelihood_season_winter
    likelihood_season_winter = [x + 1 for x in likelihood_season_winter]

def test() :
    if (laplace_estimator):
        print('prior_probability after laplace estimator: ', prior_probability)
        print('likelihood_place_home after laplace estimator: ', likelihood_place_home)
        print('likelihood_place_away after laplace estimator: ', likelihood_place_away)
        print('likelihood_season_spring after laplace estimator: ', likelihood_season_spring)
        print('likelihood_season_summer after laplace estimator: ', likelihood_season_summer)
        print('likelihood_season_autumn after laplace estimator: ', likelihood_season_autumn)
        print('likelihood_season_winter after laplace estimator: ', likelihood_season_winter)

    print('win_probability: ', win_probability)
    print('draw_probability: ', draw_probability)
    print('lose_probability: ', lose_probability)

def get_likelihood_season_data(season) :
    if season == "Spring" :
        return likelihood_season_spring
    elif season == "Summer" :
        return likelihood_season_summer
    elif season == "Autumn" :
        return likelihood_season_autumn
    else :
        return likelihood_season_winter

def calculate_win_probability(home_team, away_team, season) :
    global win_probability

    if laplace_estimator :
        print('laplace estimator')
        win_probability = prior_probability[0] / (data_amount + 3) * \
                          likelihood_place_home[0] / (prior_probability[0] + 1) * \
                          get_likelihood_season_data(season)[0] / (prior_probability[0] + 3)
    else :
        print('not laplace estimator')
        win_probability = prior_probability[0] / data_amount * \
                          likelihood_place_home[0] / prior_probability[0] * \
                          get_likelihood_season_data(season)[0] / prior_probability[0]

def calculate_draw_probability(home_team, away_team, season) :
    global draw_probability

    if laplace_estimator :
        draw_probability = prior_probability[1] / (data_amount + 3) * \
                          likelihood_place_home[1] / (prior_probability[1] + 1) * \
                          get_likelihood_season_data(season)[1] / (prior_probability[1] + 3)
    else :
        draw_probability = prior_probability[1] / data_amount * \
                          likelihood_place_home[1] / prior_probability[1] * \
                          get_likelihood_season_data(season)[1] / prior_probability[1]

def calculate_lose_probability(home_team, away_team, season) :
    global lose_probability

    if laplace_estimator :
        lose_probability = prior_probability[2] / (data_amount + 3) * \
                          likelihood_place_home[2] / (prior_probability[2] + 1) * \
                          get_likelihood_season_data(season)[2] / (prior_probability[2] + 3)
    else :
        lose_probability = prior_probability[2] / data_amount * \
                          likelihood_place_home[2] / prior_probability[2] * \
                          get_likelihood_season_data(season)[2] / prior_probability[2]

def calculate_result() :
    divisor = win_probability + \
              draw_probability + \
                  lose_probability
    
    print ('divisor', divisor)
    
    win_percentage = (win_probability / divisor) * 100
    draw_percentage = (draw_probability / divisor) * 100
    lose_percentage = (lose_probability / divisor) * 100

    result = []
    result.append("{:.2f}".format(win_percentage))
    result.append("{:.2f}".format(draw_percentage))
    result.append("{:.2f}".format(lose_percentage))

    return result

def calculate(home, away, season) :
    generate_all_data(home, season)

    if laplace_estimator_is_estimator_needed() :
        'need laplace estimator'
        do_laplace_estimator()

    calculate_win_probability(home, away, season)
    calculate_draw_probability(home, away, season)
    calculate_lose_probability(home, away, season)

    test()

    return calculate_result()
