

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