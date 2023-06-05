import requests
import urllib.request

KEY = "RGAPI-cea38e04-8e39-4d2e-b829-f918d31d1b8d"

def getApiUrl(URL, key, arg) :
    return URL + arg + "?api_key=" + key

def getPlayerInfo(name):

    apiRequest = getApiUrl("https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/", KEY, name)

    info = requests.get(apiRequest).json()

    version = requests.get("https://ddragon.leagueoflegends.com/api/versions.json").json()[0]

    playerRank  = []
    playerLP = []
    playerWins = []
    playerLosses = []
    playerGamesPlayed = []
    playerWinrate = []

    try:
        playerID = info["id"]
        playerLvl = info["summonerLevel"]
        playerName = info["name"]
        playerPfp = urllib.request.urlopen(f"https://ddragon.leagueoflegends.com/cdn/{version}/img/profileicon/{info['profileIconId']}.png").read()
    except:
        playerID = "No Data"
        playerLvl = "No Data"
        playerName = "No Data"
        playerRank  =       ["No Data", "No Data"]
        playerLP =          ["No Data", "No Data"]
        playerWins =        ["No Data", "No Data"]
        playerLosses =      ["No Data", "No Data"]
        playerGamesPlayed = ["No Data", "No Data"]
        playerWinrate =     ["No Data", "No Data"]
        playerPfp = "No Data"

        return [playerName, playerLvl, playerRank, playerWins, playerLosses, playerLP, playerGamesPlayed, playerWinrate, playerPfp]

    apiRequest = getApiUrl("https://na1.api.riotgames.com/lol/league/v4/entries/by-summoner/", KEY, playerID)

    info = requests.get(apiRequest).json()

    for i in range(2):
        try:
            playerRank.append(info[i]["tier"] + ": " + info[i]["rank"])
            playerWins.append(info[i]["wins"])
            playerLosses.append(info[i]["losses"])
            playerLP.append(info[i]["leaguePoints"])
            playerGamesPlayed.append(playerWins[i] + playerLosses[i])
            playerWinrate.append(round((playerWins[i] / playerGamesPlayed[i]) * 100, 2))
        except IndexError:
            playerRank.append("No Data")
            playerWins.append("No Data")
            playerLosses.append("No Data")
            playerLP.append("No Data")
            playerGamesPlayed.append("No Data")
            playerWinrate.append("No Data")

    return [playerName, playerLvl, playerRank, playerWins, playerLosses, playerLP, playerGamesPlayed, playerWinrate, playerPfp]