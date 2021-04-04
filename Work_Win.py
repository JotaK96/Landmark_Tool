# import sys
# from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QApplication
# from PyQt5.QtGui import QIcon


def global_imports(module_name,
                   short_name=None,
                   context_module_name = None):

    if not short_name:
        short_name = module_name
    if not context_module_name:
        globals()[short_name] = __import__(module_name)
    else:
        context_module = __import__(context_module_name,fromlist=[module_name])
        globals()[short_name] = getattr(context_module,module_name)

global_imports('os')
global_imports("sys")
global_imports("QMainWindow",None,"PyQt5.QtWidgets")
global_imports("QAction",None,"PyQt5.QtWidgets")
global_imports("qApp",None,"PyQt5.QtWidgets")
global_imports("QApplication",None,"PyQt5.QtWidgets")
global_imports("QIcon",None,"PyQt5.QtGui")
global_imports("QPixmap",None,"PyQt5.QtGui")




class MainWin(QMainWindow):

    def __init__(self):

        super().__init__()
        self.initUI()


    def initUI(self):

        # This is to create menu options for the File Menu bar
        def menu_creation(title, actions=None):
            fileMenu = menubar.addMenu(title)
            if actions:
                for i in actions:
                    fileMenu.addAction(i)
            else:
                pass
            return fileMenu

        # This creates the options for each menu
        def opt_creation(title, shortcut=None,tip=None,action=None):

            menu_opt = QAction(title,self)
            menu_opt.setShortcut(shortcut)
            menu_opt.setStatusTip(tip)
            return menu_opt


        # This is used to create multiple options
        # variable_name = opt_creation('Title','shortcut','tip',)

        ## File Actions
        openAct = opt_creation('&New Project','Ctrl+O','Create a new project')
        loadAct = opt_creation('&Load Project','Ctrl+L','Load a previously saved project')
        exitAct = opt_creation('&Exit','Ctrl+Q','Exit Application')
        file_actions = [openAct,loadAct,exitAct]



        # FileMenu Bar
        menubar = self.menuBar()

        file = menu_creation('&File',file_actions)
        options = menu_creation('Options')
        help = menu_creation('Help')


        # fileMenu = menubar.addMenu('&File')
        # fileMenu.addAction(openAct)
        # fileMenu.addAction(loadAct)
        # fileMenu.addAction(exitAct)
        # fileMenu.addAction(test)

        # Adding an image
        dirname = os.path.dirname(__file__)
        image = os.path.join(dirname,'image.jpg')
        pixmap = QPixmap(image)

        lbl = QLabel(self)
        lbl.setPixmap(pixmap)


        self.setGeometry(300,300,600,500)
        self.setWindowTitle('Landmark Tool')
        self.show()


def main():

    app = QApplication(sys.argv)
    ex = MainWin()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
