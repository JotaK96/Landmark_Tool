import sys
from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QApplication
from PyQt5.QtGui import QIcon

class MainWin(QMainWindow):

    def __init__(self):

        super().__init__()
        self.initUI()

    def initUI(self):

        openAct = QAction('&New Project...',self)
        openAct.setShortcut('Ctrl+O')
        openAct.setStatusTip('Create a new project')
        openAct.triggered.connect(qApp.quit)

        LoadAct = QAction('&Load Project',self)
        LoadAct.setShortcut('Ctrl+L')
        LoadAct.setStatusTip('Load a previously saved project')
        LoadAct.triggered.connect(qApp.quit)

        exitAct = QAction(QIcon('4209225.svg'),'&Exit',self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.setStatusTip('Exit application')
        exitAct.triggered.connect(qApp.quit)

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(openAct)
        fileMenu.addAction(LoadAct)
        fileMenu.addAction(exitAct)

        self.setGeometry(300,300,300,200)
        self.setWindowTitle('Landmark Tool')
        self.show()

def main():

    app = QApplication(sys.argv)
    ex = MainWin()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
