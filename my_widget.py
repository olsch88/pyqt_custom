import sys

from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtWidgets import (QWidget, 
                            QPushButton, 
                            QLabel,
                            QApplication,
                            QVBoxLayout
                            )



class MyLittleWidget(QWidget):
    custom_signal=pyqtSignal()
    
    def __init__(self)-> None:
        super().__init__()

        self.state=True
        
        self.my_label = QLabel("On")
        self.my_button = QPushButton("Click me!")
                
        self.my_layout = QVBoxLayout()
        self.my_layout.addWidget(self.my_label)
        self.my_layout.addWidget(self.my_button)
        
        self.my_button.clicked.connect(self.switch_state)        
        
        self.setLayout(self.my_layout)
        
        self.show() 
    
    def switch_state(self):
        self.custom_signal.emit()
        if self.state:
            self.state = False
            self.my_label.setText("Off")
        else:
            self.state = True
            self.my_label.setText("On")

if __name__ =="__main__":
    app = QApplication(sys.argv)
    window = MyLittleWidget()
    
    app.exec()