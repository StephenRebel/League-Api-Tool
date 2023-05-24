import sys
import time
from Riot_API_Testing import getPlayerInfo
from functools import partial

#from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QLabel, QWidget, QMainWindow, QHBoxLayout, QLineEdit, QPushButton,QVBoxLayout
from PyQt6.QtGui import QPixmap, QFont

class PyLeagueWindow(QMainWindow):
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
        #self.label.move(240, 5)
        self.topBar.addWidget(self.label)
        self.txt = QLabel("<h1>TheBoys.gg!</h1>")
        self.txt.setFixedHeight(75)
        #self.txt.move(365, 0)
        self.topBar.addWidget(self.txt)
        self.search = QLineEdit()
        f = self.search.font()
        f.setPointSize(18)
        self.search.setFont(f)
        self.search.setPlaceholderText("Enter Summoner Name")
        self.search.setFixedSize(300 , 75)
        #self.search.move(550, 5)
        self.topBar.addWidget(self.search)
        self.searchButton = QPushButton("Search")
        self.searchButton.setFixedSize(200, 75)
        #self.searchButton.move(860, 5)
        f = self.searchButton.font()
        f.setPointSize(18)
        self.searchButton.setFont(f)
        self.topBar.addWidget(self.searchButton)
        self.generalLayout.addLayout(self.topBar)
        self.show()

    #USE GRID LAYOUT TO PUT THING IN (I THINK)
    #CAN USE TRY EXCEPT FINAL TO DELETE PREVIOUS LAYOUT IF IT EXISTS THEN ALWAYS MAKE NEW ONE
    def generatePlayerInfo(self, name):
        data = getPlayerInfo(name)
        self.namePlate = QHBoxLayout()
        self.summonerLabel = QLabel(data[0])
        self.summonerLabel.setFont(QFont("Sans Serif 10", 28))
        #self.summonerLabel.move(200, 150)
        self.namePlate.addWidget(self.summonerLabel)
        self.generalLayout.addLayout(self.namePlate)
        #time.sleep(3)
        self.namePlate.removeWidget(self.summonerLabel)
        self.generalLayout.removeItem(self.namePlate)
    


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
    #leagueWindow.show()
    LeagueApp(model="fill", view=leagueWindow)
    sys.exit(leagueApp.exec())

if __name__ == "__main__":
    main()