import sys
from threading import Timer
import time
from PyQt4 import QtGui, QtCore



class Window(QtGui.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(50, 50, 500, 300)
        self.setWindowTitle("Tea Timer")
        self.setWindowIcon(QtGui.QIcon('clock.png'))
        QtGui.QApplication.setStyle("plastique")

        extractAction = QtGui.QAction("&Leave", self)
        extractAction.setShortcut("Cmd+Q")
        extractAction.setStatusTip("Leave the app")
        extractAction.triggered.connect(self.close_application)

        extractAction2 = QtGui.QAction("&Edit Timer", self)
        extractAction2.setShortcut("Cmd+,")
        extractAction2.setStatusTip("Edit Preferences")
        extractAction2.triggered.connect(self.preferences)

        self.statusBar()

        mainMenu = self.menuBar()

        # mainMenu.setNativeMenuBar(False) this option add the menu bar to the window to be able to use words like "exit"

        menu1 = mainMenu.addMenu('&Menu')

        menu1.addAction(extractAction)
        menu1.addAction(extractAction2)

        self.home()
        self.raise_()

    def home(self):
        btn = QtGui.QPushButton("Quit", self)
        teabtn = QtGui.QPushButton("Tea", self)
        coffeebtn = QtGui.QPushButton("Coffee", self)
        btn.clicked.connect(self.close_application)
        # btn.clicked.connect(QtCore.QCoreApplication.instance().quit)
        teabtn.clicked.connect(self.tea)
        coffeebtn.clicked.connect(self.coffee)
        btn.resize(70, 30)
        btn.move(370, 230)
        teabtn.move(50, 50)
        coffeebtn.move(50, 100)
        self.show()

    def preferences(self):
        pass

    def close_application(self):
        choice = QtGui.QMessageBox.question(self, 'Text example!',
                                            "Are you sure you want to exit?",
                                            QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
        if choice == QtGui.QMessageBox.Yes:
            sys.exit()
        else:
            pass


    def tea(self):
        time.sleep(10)
        reply = QtGui.QMessageBox.information(self, "", "Tea ready!")

    def coffee(self):
        time.sleep(10)
        reply = QtGui.QMessageBox.information(self, "", "Coffee ready!")


def run():
    app = QtGui.QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())


run()
