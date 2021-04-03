import sys
from PyQt5.QtWidgets import (QWidget, QCheckBox, QPushButton, QLineEdit, QLabel, QApplication, QGridLayout)

class nProjectWin(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):


        ## Labels for titles
        pathLbl = QLabel('Path')
        optionsLbl = QLabel("Options")

        #landmLbl = QLabel('Landmarks')
        #boxLbl = QLabel('Bounding Box')
        #sizeLbl = QLabel('Picture Resize')

        ## Text Boxes
        pathEdit = QLineEdit()
        landmarkEdit = QLineEdit()
        boundingEdit = QLineEdit()
        widthEdit = QLineEdit()
        heightEdit = QLineEdit()


        ## Check Boxes
            ##Landmark
        landmarkCheck = QCheckBox('Landmarks')
        landmarkCheck.toggle()
            ## Bounding Box
        boundingCheck = QCheckBox('Bounding Boxes?')
        boundingCheck.toggle()
            ##Picture Resize
        sizeCheck = QCheckBox('Resize Pictures?')
        sizeCheck.toggle()



        ##Buttons
            ## File Button
        pathButton = QPushButton("...")

            ##Bottom Buttons
        helpButton = QPushButton("Help")
        defaultButton = QPushButton("Default")
        acceptButton = QPushButton("Accept")
        cancelButton = QPushButton("Cancel")

            ##Link Button
        linkButton = QPushButton("X")
        linkButton.setCheckable(True)


        ## Grid Setup
        grid = QGridLayout()
        grid.setSpacing(12)

            ## Path
        grid.addWidget(pathLbl,1,0)
        grid.addWidget(pathEdit,1,1,1,2)
        grid.addWidget(pathButton,1,3)

            ## Options title
        grid.addWidget(optionsLbl,2,0)

            ## Landmark
        grid.addWidget(landmarkCheck,3,0)
        grid.addWidget(landmarkEdit,3,1)

            ## Bounding Box
        grid.addWidget(boundingCheck,4,0)
        grid.addWidget(boundingEdit,4,1)

            ## Picture Resize
        grid.addWidget(sizeCheck,5,0)
        grid.addWidget(widthEdit,5,1)
        grid.addWidget(linkButton,5,2)
        grid.addWidget(heightEdit,5,3)


            ## Action Buttons
        grid.addWidget(helpButton,6,0)
        grid.addWidget(defaultButton,6,1)
        grid.addWidget(acceptButton,6,2)
        grid.addWidget(cancelButton,6,3)


        self.setLayout(grid)
                        ## X,Y,width,height
        self.setGeometry(400,400,400,169)
        self.setWindowTitle("New Project")
        self.show()

def main():
    app = QApplication(sys.argv)
    ex = nProjectWin()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
