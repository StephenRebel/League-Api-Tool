import sys
from Riot_API_Testing import getPlayerInfo

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QLabel, QWidget, QMainWindow, QHBoxLayout, QLineEdit, QPushButton, QVBoxLayout, QGridLayout, QMessageBox
from PyQt6.QtGui import QPixmap, QFont

class PyLeagueWindow(QMainWindow):

    FONT1 = QFont("Times New Roman", 24)

    def __init__(self):
        super(PyLeagueWindow, self).__init__()
        self.setWindowTitle("TheBoys.gg")
        self.setFixedSize(1280, 720)
        self.generalLayout = QVBoxLayout()
        centralWidget = QWidget(self)
        centralWidget.setLayout(self.generalLayout)
        self.setCentralWidget(centralWidget)
        self.generateTopBar()   
        self.generatePlayerInfo()  

    def generateTopBar(self):
        self.topBar = QHBoxLayout()
        self.topBar.setContentsMargins(210, 5, 210, 0)
        self.topBar.setSpacing(20)
        self.label = QLabel(self)
        self.pMap = QPixmap("icon.png")
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

    def generatePlayerInfo(self):
        self.displayPlate = QGridLayout()
        self.displayPlate.setContentsMargins(10, 10, 10, 10)
        self.displayPlate.setSpacing(20)
        self.summonerDisplay = QVBoxLayout()
        self.nameDisplay = QLabel()
        self.nameDisplay.setFont(QFont("Impact", 34))
        self.lvlDisplay = QLabel()
        self.lvlDisplay.setFont(QFont("Impact", 28))
        self.TXTRANKEDS = QLabel("Ranked Solo/Duo")
        self.TXTRANKEDF = QLabel("Ranked Flex")
        self.TXTRANKEDS.setFont(QFont("Times New Roman", 28))
        self.TXTRANKEDF.setFont(QFont("Times New Roman", 28))
        self.summonerDisplay.addWidget(self.nameDisplay)
        self.summonerDisplay.addWidget(self.lvlDisplay)
        self.rankSRanks = QVBoxLayout()
        self.rankSRank = QLabel()
        self.rankSRank.setFont(self.FONT1)
        self.rankSLP = QLabel()
        self.rankSLP.setFont(self.FONT1)
        self.rankSRanks.addWidget(self.rankSRank)
        self.rankSRanks.addWidget(self.rankSLP)
        self.gameSStats = QVBoxLayout()
        self.gameSWinrate = QLabel()
        self.gameSWinrate.setFont(self.FONT1)
        self.gameSPlayed = QLabel()
        self.gameSPlayed.setFont(self.FONT1)
        self.gameSWinLoss = QLabel()
        self.gameSWinLoss.setFont(self.FONT1)
        self.gameSStats.addWidget(self.gameSWinrate)
        self.gameSStats.addWidget(self.gameSPlayed)
        self.gameSStats.addWidget(self.gameSWinLoss)
        self.rankFRanks = QVBoxLayout()
        self.rankFRank = QLabel()
        self.rankFRank.setFont(self.FONT1)
        self.rankFLP = QLabel()
        self.rankFLP.setFont(self.FONT1)
        self.rankFRanks.addWidget(self.rankFRank)
        self.rankFRanks.addWidget(self.rankFLP)
        self.gameFStats = QVBoxLayout()
        self.gameFWinrate = QLabel()
        self.gameFWinrate.setFont(self.FONT1)
        self.gameFPlayed = QLabel()
        self.gameFPlayed.setFont(self.FONT1)
        self.gameFWinLoss = QLabel()
        self.gameFWinLoss.setFont(self.FONT1)
        self.gameFStats.addWidget(self.gameFWinrate)
        self.gameFStats.addWidget(self.gameFPlayed)
        self.gameFStats.addWidget(self.gameFWinLoss)

        self.summonerPfp = QLabel(self)
        self.summonerPfpPmap = QPixmap()

        self.displayPlate.addWidget(self.summonerPfp, 0, 0, Qt.AlignmentFlag.AlignCenter)
        self.displayPlate.addLayout(self.summonerDisplay, 0, 1, Qt.AlignmentFlag.AlignCenter)
        self.displayPlate.addWidget(self.TXTRANKEDS, 1, 0, Qt.AlignmentFlag.AlignCenter)
        self.displayPlate.addLayout(self.rankSRanks, 1, 1, Qt.AlignmentFlag.AlignCenter)
        self.displayPlate.addLayout(self.gameSStats, 1, 2, Qt.AlignmentFlag.AlignCenter)
        self.displayPlate.addWidget(self.TXTRANKEDF, 2, 0, Qt.AlignmentFlag.AlignCenter)
        self.displayPlate.addLayout(self.rankFRanks, 2, 1, Qt.AlignmentFlag.AlignCenter)
        self.displayPlate.addLayout(self.gameFStats, 2, 2, Qt.AlignmentFlag.AlignCenter)

        self.count = 0

    def updatePlayerInfo(self, name):
        data = getPlayerInfo(name)

        self.nameDisplay.setText(str(data[0]))
        self.lvlDisplay.setText("Summoner Level: " + str(data[1]))

        self.rankSRank.setText("Rank: " + str(data[2][0]))
        self.rankSLP.setText("LP: " + str(data[5][0]))

        self.gameSWinrate.setText("Winrate: %" + str(data[7][0]))
        self.gameSPlayed.setText("Games Played: " + str(data[6][0]))
        self.gameSWinLoss.setText("Wins: " + str(data[3][0]) + " / Losses: " + str(data[4][0]))

        self.rankFRank.setText("Rank: " + str(data[2][1]))
        self.rankFLP.setText("LP: " + str(data[5][1]))

        self.gameFWinrate.setText("Winrate: %" + str(data[7][1]))
        self.gameFPlayed.setText("Games Played: " + str(data[6][1]))
        self.gameFWinLoss.setText("Wins: " + str(data[3][1]) + " / Losses: " + str(data[4][1]))

        try:
            self.summonerPfpPmap.loadFromData(data[8])

        except TypeError:
            self.summonerPfpPmap.load("blank.png")
        
        finally:
            self.summonerPfpPmap = self.summonerPfpPmap.scaled(125, 125)
            self.summonerPfp.setPixmap(self.summonerPfpPmap)

        if self.count < 1:
            self.generalLayout.addLayout(self.displayPlate)
        
        self.count += 1
        
        if name.lower() == "moldycroc":
            dlg = QMessageBox(self)
            dlg.setWindowTitle("Summoner Tips")
            dlg.setText("You spend to much on skins")
            dlg.exec()
        elif name.lower() == "hamouzy":
            dlg = QMessageBox(self)
            dlg.setWindowTitle("Summoner Tips")
            dlg.setText("Try playing anything other than Jinx")
            dlg.exec()
        elif name.lower() == "magentahk":
            dlg = QMessageBox(self)
            dlg.setWindowTitle("Summoner Tips")
            dlg.setText("Teemo is not that good")
            dlg.exec()
        elif name.lower() == "deaddeimos":
            dlg = QMessageBox(self)
            dlg.setWindowTitle("Summoner Tips")
            dlg.setText("Idk he plays Nunu?")
            dlg.exec()
        elif name.lower() == "misticmuslim":
            dlg = QMessageBox(self)
            dlg.setWindowTitle("Summoner Tips")
            dlg.setText("Cracked on Vex, keep going")
            dlg.exec()
        elif name.lower() == "xxdaddysharkxx":
            dlg = QMessageBox(self)
            dlg.setWindowTitle("Summoner Tips")
            dlg.setText("Hmm this guy is fishyxx")
            dlg.exec()
        elif name.lower() == "dahhhrius":
            dlg = QMessageBox(self)
            dlg.setWindowTitle("Summoner Tips")
            dlg.setText("He plays this game?")
            dlg.exec()
        elif name.lower() == "sabr22":
            dlg = QMessageBox(self)
            dlg.setWindowTitle("Summoner Tips")
            dlg.setText("This guy is carried trash")
            dlg.exec()
        


class LeagueApp:

    def __init__(self, model, view):
        self.leagueApi = model
        self.leagueView = view
        self.connectButton()

    def connectButton(self):
        self.leagueView.searchButton.clicked.connect(lambda: self.leagueView.updatePlayerInfo(self.leagueView.search.text()))
        self.leagueView.search.returnPressed.connect(lambda: self.leagueView.updatePlayerInfo(self.leagueView.search.text()))



def main():
    leagueApp = QApplication(sys.argv)
    leagueWindow = PyLeagueWindow()
    leagueWindow.show()
    LeagueApp(model="fill", view=leagueWindow)
    sys.exit(leagueApp.exec())

if __name__ == "__main__":
    main()