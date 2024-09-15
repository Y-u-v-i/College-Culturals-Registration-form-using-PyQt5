import sys 
from PyQt5.QtWidgets import QMainWindow,QApplication,QLineEdit,QPushButton,QLabel,QRadioButton,QButtonGroup
from PyQt5.QtGui import QFont 

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700,300,500,500)
        self.line=QLineEdit(self)
        Topic=QLabel("Culturals Registration form",self)
        Topic.setFont(QFont("Arial",15))
        Topic.setGeometry(120,0,500,40)
        self.button=QPushButton("Submit",self)
        Name=QLabel("Enter Your Name:",self)
        Name.setFont(QFont("Arial",15))
        Name.setGeometry(10,60,200,40)
        Age=QLabel("Enter Your Age:",self)
        Age.setFont(QFont("Arial",15))
        Age.setGeometry(10,120,200,40)
        self.Event1=QLabel("Event Selection:",self)
        self.Event1.setStyleSheet("font-size: 25px;"
                             "font-family: Arial;")
        self.Event=QRadioButton("Technical",self)
        self.Event.setStyleSheet("font-size: 25px;"
                            "font-family: Arial;")
        self.Event2=QRadioButton("Non-Technical",self)
        self.Event2.setStyleSheet("font-size: 25px;"
                            "font-family: Arial;")
        self.Event.setGeometry(240,190,200,40)
        self.Event2.setGeometry(240,220,200,40)
        self.Event1.setGeometry(10,190,230,40)
        Address=QLabel("College Name:",self)
        Address.setFont(QFont("Arial",15))
        Address.setGeometry(10,280,230,40)
        self.line1=QLineEdit(self)
        self.line2=QLineEdit(self)
        self.Payment=QLabel("Payment Mode:",self)
        self.Payment.setFont(QFont("Arial",15))
        self.Payment.setGeometry(10,340,230,40)
        self.Payment1=QLabel("(1 Entry-Rs.200/-)",self)
        self.Payment1.setFont(QFont("Arial",15))
        self.Payment1.setGeometry(10,372,230,40)
        self.Event3=QRadioButton("UPI/Gpay",self)
        self.Event4=QRadioButton("Cash",self)
        self.Event3.setStyleSheet("font-size: 25px;"
                            "font-family: Arial;")
        self.Event4.setStyleSheet("font-size: 25px;"
                            "font-family: Arial;")
        self.Event3.setGeometry(230,340,200,40)
        self.Event4.setGeometry(230,370,200,40)
        self.group1=QButtonGroup(self)
        self.group2=QButtonGroup(self)
        self.initUI()
    def initUI(self):
        self.line2.setGeometry(190,280,300,40)
        self.line.setGeometry(230,60,200,40)
        self.line1.setGeometry(230,120,200,40)
        self.button.setGeometry(180,430,100,40)
        self.line.setStyleSheet("font-size: 20px;"
                                "font-family: Arial;")
        self.line1.setStyleSheet("font-size: 20px;"
                                "font-family: Arial;")
        self.line2.setStyleSheet("font-size: 20px;"
                                "font-family: Arial;")
        self.button.setStyleSheet("font-size: 20px;"
                                  "font-family: Arial")
        self.button.clicked.connect(self.button_clicked)
        self.Event.toggled.connect(self.button_clicked)
        self.Event2.toggled.connect(self.button_clicked)
        self.Event3.toggled.connect(self.button_clicked)
        self.Event4.toggled.connect(self.button_clicked)
        
        self.group1.addButton(self.Event)
        self.group1.addButton(self.Event2)
        self.group2.addButton(self.Event3)
        self.group2.addButton(self.Event4)

    def button_clicked(self):
        print(self.line.text())
        print(self.line1.text())
        print(self.line2.text())
        
        selector = self.sender()
        if selector.isChecked():
            print(f"{selector.text()}")

if __name__=='__main__':
    app=QApplication(sys.argv)
    window=MainWindow()
    window.show()
    sys.exit(app.exec_())
