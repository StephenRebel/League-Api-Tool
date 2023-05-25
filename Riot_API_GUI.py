import sys
import time
from Riot_API_Testing import getPlayerInfo
from functools import partial

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QLabel, QWidget, QMainWindow, QHBoxLayout, QLineEdit, QPushButton, QVBoxLayout, QGridLayout
from PyQt6.QtGui import QPixmap, QFont

class PyLeagueWindow(QMainWindow):

    FONT1 = QFont("Times New Roman", 24)

    def __init__(self):
        super().__init__()
        self.setWindowTitle("TheBoys.gg")
        self.setFixedSize(1280, 720)
        self.generalLayout = QVBoxLayout()
        centralWidget = QWidget(self)
        centralWidget.setLayout(self.generalLayout)
        self.setCentralWidget(centralWidget)
        self.generateTopBar()     

    def generateTopBar(self):
        self.topBar = QHBoxLayout()
        self.topBar.setContentsMargins(210, 5, 210, 0)
        self.topBar.setSpacing(20)
        self.label = QLabel(self)
        self.pMap = QPixmap("download.png")
        self.pMap = self.pMap.scaled(75, 75)
        self.label.setPixmap(self.pMap)
        self.label.setFixedSize(75, 75)
        self.topBar.addWidget(self.label)
        self.txt = QLabel("<h1>TheBoys.gg!</h1>")
        self.txt.setFixedHeight(75)
        self.topBar.addWidget(self.txt)
        self.search = QLineEdit()
        f = self.search.font()
        f.setPointSize(18)
        self.search.setFont(f)
        self.search.setPlaceholderText("Enter Summoner Name")
        self.search.setFixedSize(300 , 75)
        self.topBar.addWidget(self.search)
        self.searchButton = QPushButton("Search")
        self.searchButton.setFixedSize(200, 75)
        f = self.searchButton.font()
        f.setPointSize(18)
        self.searchButton.setFont(f)
        self.topBar.addWidget(self.searchButton)
        self.generalLayout.addLayout(self.topBar)

    #HAVE LAYOUT ALWAYS EXIST AND ONLY DISPLAY IT ONCE SEARCG IS CLICKED FIRST AND THEN JUST ALWAYS CHANGE THE VALUES
    def generatePlayerInfo(self, name):
        data = getPlayerInfo(name)

        #WILL BREAK FOR MISSING DATA ACCOUNT FOR IN getPlayerInfo FUCNTION
        self.displayPlate = QGridLayout()
        self.displayPlate.setContentsMargins(10, 10, 10, 10)
        self.displayPlate.setSpacing(20)
        self.summonerDisplay = QVBoxLayout()
        self.nameDisplay = QLabel(str(data[0]))
        self.nameDisplay.setFont(QFont("Impact", 34))
        self.lvlDisplay = QLabel("Summoner Level: " + str(data[1]))
        self.lvlDisplay.setText("test")
        self.lvlDisplay.setFont(QFont("Impact", 28))
        self.summonerDisplay.addWidget(self.nameDisplay)
        self.summonerDisplay.addWidget(self.lvlDisplay)
        self.TXTRANKEDS = QLabel("Ranked Solo/Duo")
        self.TXTRANKEDS.setFont(QFont("Times New Roman", 28))
        self.TXTRANKEDF = QLabel("Ranked Flex")
        self.TXTRANKEDF.setFont(QFont("Times New Roman", 28))

        self.rankSRanks = QVBoxLayout()
        self.rankSRank = QLabel("Rank: " + str(data[2][0]))
        self.rankSRank.setFont(self.FONT1)
        self.rankSLP = QLabel("LP: " + str(data[5][0]))
        self.rankSLP.setFont(self.FONT1)
        self.rankSRanks.addWidget(self.rankSRank)
        self.rankSRanks.addWidget(self.rankSLP)

        self.gameSStats = QVBoxLayout()
        self.gameSWinrate = QLabel("Winrate: %" + str(round(data[3][0] / (data[3][0] + data[4][0]), 2)))
        self.gameSWinrate.setFont(self.FONT1)
        self.gameSPlayed = QLabel("Games Played: " + str(data[3][0] + data[4][0]))
        self.gameSPlayed.setFont(self.FONT1)
        self.gameSWinLoss = QLabel("Wins: " + str(data[3][0]) + " / Losses: " + str(data[4][0]))
        self.gameSWinLoss.setFont(self.FONT1)
        self.gameSStats.addWidget(self.gameSWinrate)
        self.gameSStats.addWidget(self.gameSPlayed)
        self.gameSStats.addWidget(self.gameSWinLoss)

        #SECTION WILLL BREAK RIGHT NOW FOR USERS WITHOUT FLEX DATA
        self.rankFRanks = QVBoxLayout()
        self.rankFRank = QLabel("Rank: " + str(data[2][1]))
        self.rankFRank.setFont(self.FONT1)
        self.rankFLP = QLabel("LP: " + str(data[5][1]))
        self.rankFLP.setFont(self.FONT1)
        self.rankFRanks.addWidget(self.rankFRank)
        self.rankFRanks.addWidget(self.rankFLP)

        self.gameFStats = QVBoxLayout()
        self.gameFWinrate = QLabel("Winrate: %" + str(round(data[3][1] / (data[3][1] + data[4][1]), 2)))
        self.gameFWinrate.setFont(self.FONT1)
        self.gameFPlayed = QLabel("Games Played: " + str(data[3][1] + data[4][1]))
        self.gameFPlayed.setFont(self.FONT1)
        self.gameFWinLoss = QLabel("Wins: " + str(data[3][1]) + " / Losses: " + str(data[4][1]))
        self.gameFWinLoss.setFont(self.FONT1)
        self.gameFStats.addWidget(self.gameFWinrate)
        self.gameFStats.addWidget(self.gameFPlayed)
        self.gameFStats.addWidget(self.gameFWinLoss)

        self.displayPlate.addLayout(self.summonerDisplay, 0, 0, Qt.AlignmentFlag.AlignCenter)
        self.displayPlate.addWidget(self.TXTRANKEDS, 1, 0, Qt.AlignmentFlag.AlignCenter)
        self.displayPlate.addLayout(self.rankSRanks, 1, 1, Qt.AlignmentFlag.AlignCenter)
        self.displayPlate.addLayout(self.gameSStats, 1, 2, Qt.AlignmentFlag.AlignCenter)
        self.displayPlate.addWidget(self.TXTRANKEDF, 2, 0, Qt.AlignmentFlag.AlignCenter)
        self.displayPlate.addLayout(self.rankFRanks, 2, 1, Qt.AlignmentFlag.AlignCenter)
        self.displayPlate.addLayout(self.gameFStats, 2, 2, Qt.AlignmentFlag.AlignCenter)

        self.generalLayout.addLayout(self.displayPlate)

        """
        self.namePlate = QHBoxLayout()
        self.summonerLabel = QLabel(data[0])
        self.summonerLabel.setFont(QFont("Impact", 28))
        self.namePlate.addWidget(self.summonerLabel)
        self.generalLayout.addLayout(self.namePlate)
        time.sleep(3)
        self.namePlate.widget(self.summonerLabel)
        self.generalLayout.removeItem(self.namePlate)
        """
    


class LeagueApp:

    def __init__(self, model, view):
        self.leagueApi = model
        self.leagueView = view
        self.connectButton()

    def connectButton(self):
        self.leagueView.searchButton.clicked.connect(lambda: self.leagueView.generatePlayerInfo(self.leagueView.search.text()))
        self.leagueView.search.returnPressed.connect(lambda: self.leagueView.generatePlayerInfo(self.leagueView.search.text()))



def main():
    leagueApp = QApplication(sys.argv)
    leagueWindow = PyLeagueWindow()
    leagueWindow.show()
    LeagueApp(model="fill", view=leagueWindow)
    sys.exit(leagueApp.exec())

if __name__ == "__main__":
    main()