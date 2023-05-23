import sys
from Riot_API_Testing import getPlayerInfo
from functools import partial

#from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QLabel, QWidget, QMainWindow, QHBoxLayout, QLineEdit, QPushButton,QVBoxLayout
from PyQt6.QtGui import QPixmap

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
        label = QLabel(self)
        pMap = QPixmap("download.png")
        pMap = pMap.scaled(75, 75)
        label.setPixmap(pMap)
        label.setFixedSize(75, 75)
        label.move(240, 5)
        self.topBar.addWidget(label)
        txt = QLabel("<h1>TheBoys.gg!</h1>")
        txt.setFixedHeight(75)
        txt.move(365, 0)
        self.topBar.addWidget(txt)
        self.search = QLineEdit()
        f = self.search.font()
        f.setPointSize(18)
        self.search.setFont(f)
        self.search.setPlaceholderText("Enter Summoner Name")
        self.search.setFixedSize(300 , 75)
        self.search.move(550, 5)
        self.topBar.addWidget(self.search)
        self.searchButton = QPushButton("Search")
        self.searchButton.setFixedSize(200, 75)
        self.searchButton.move(860, 5)
        f = self.searchButton.font()
        f.setPointSize(18)
        self.searchButton.setFont(f)
        self.topBar.addWidget(self.searchButton)
        self.generalLayout.addChildLayout(self.topBar)

    def generatePlayerInfo(self, name):
        data = getPlayerInfo(name)

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