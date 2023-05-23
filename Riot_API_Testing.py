import requests

KEY = "RGAPI-68bb0bf6-0811-4d37-a142-dfb1a749f7de"

def getApiUrl(URL, key, arg) :
    return URL + arg + "?api_key=" + key

def getPlayerInfo(name):

    apiRequest = getApiUrl("https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/", KEY, name)

    info = requests.get(apiRequest).json()

    playerID = info["id"]
    playerLvl = info["summonerLevel"]
    playerName = info["name"]

    print(f"Name: {playerName}, Player Level: {playerLvl}, Player ID: {playerID}")

    apiRequest = getApiUrl("https://na1.api.riotgames.com/lol/league/v4/entries/by-summoner/", KEY, playerID)

    info = requests .get(apiRequest).json()

    playerRank  = []
    playerWinrate = []
    playerLP = []

    for i in range(len(info)):
        playerRank.append(info[i]["tier"] + ": " + info[i]["rank"])
        playerWinrate.append(round(info[i]["wins"] / (info[i]["wins"] + info[i]["losses"]), 2))
        playerLP.append(info[i]["leaguePoints"])

    print(f"Ranks: {playerRank}, Winrates: {playerWinrate}, LP: {playerLP}")

    return [playerName, playerLvl, playerRank, playerLP, playerWinrate]