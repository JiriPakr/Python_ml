import json
import pandas as pd
from matchrequest import getMatchID

def getMatchData(matches, features):
    data = []
    for i in range(len(matches)):
        if matches[i]['game_mode'] != 22:
            continue

        preds_data = {k: v for k, v in matches[i].items() if k in features}

        for j in range(len(matches[0]['radiant_team'].split(","))):
            hero = 'r_hero' + "% s" % (j + 1)
            preds_data[hero] = matches[i]['dire_team'].split(",")[j]

        for j in range(len(matches[0]['dire_team'].split(","))):
            hero = 'd_hero' + "% s" % (j + 1)
            preds_data[hero] = matches[i]['dire_team'].split(",")[j]    

        data.append(preds_data)
    return data

def getHeroName(id):

    try:
        if not heroid_dict:
            pass
    except:
        with open('heroes.json') as json_file:
            data = json.load(json_file)
            heroes = data['heroes']
            heroid_dict = {}
            for i in range(len(heroes)):
                heroid_dict[data['heroes'][i]['id']]= data['heroes'][i]['name']

    hero_name = ""
    try:
        hero_name = heroid_dict[id]
    except:
        hero_name = "invalid"

    return hero_name

def getHeroId(name):

    try:
        if not heroid_dict:
            pass
    except:
        with open('heroes.json') as json_file:
            data = json.load(json_file)
            heroes = data['heroes']
            heroid_dict = {}
            for i in range(len(heroes)):
                heroid_dict[data['heroes'][i]['id']]= data['heroes'][i]['name']

    hero_id = ""
    try:
        hero_id = list(heroid_dict.keys())[list(heroid_dict.values()).index(name)]
        hero_id = float(hero_id)
    except:
        hero_id = "invalid"

    return hero_id

def getMatchHeroes(match_id):
    try:
        match_data = getMatchID(match_id=match_id)
        data, columns = list(match_data.values()), list(match_data.keys())
        df_mdata = pd.DataFrame([data],columns=columns)
    except:
        return 0
    
    features, heroes_pos_list, match_heroes = ['hero_id', 'player_slot'], [], []

    for i in range(10):
        features_dict = {k: v for k, v in df_mdata.players[0][i].items() if k in features}
        heroes_pos_list.append(list(features_dict.items()))
        match_heroes.append(float(heroes_pos_list[i][1][1]))
    return match_heroes  

def getDataReadyForPrediction(data):

    try:
        test_df = pd.read_csv('train_data.csv')
        test_df.drop(['game_mode'], axis=1)
        X_test= test_df.drop(['game_mode', 'radiant_win','match_id'], axis=1)
    except:
        return 0
    X_columns = X_test.columns
    result_df = pd.DataFrame(columns=X_columns)
    result_df = result_df.append(pd.DataFrame([data], columns=X_columns), ignore_index=True)
    return result_df