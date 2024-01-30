import sys

from PyQt5.QtCore import Qt 
from PyQt5.QtWidgets import (QWidget, 
                            QPushButton, 
                            QLabel,
                            QApplication,
                            QVBoxLayout
                            )



class MyCounterWidget(QWidget):
    def __init__(self)-> None:
        super().__init__()

        self.count=0       
        
        self.my_label = QLabel(f"Count {self.count} ")
                
        self.my_layout = QVBoxLayout()
        self.my_layout.addWidget(self.my_label)


        self.setLayout(self.my_layout)
        
        self.show() 
    
    def increment_counter(self):
        self.count+=1
        self.my_label.setText(f"Count {self.count}")

if __name__ =="__main__":
    app = QApplication(sys.argv)
    window = MyCounterWidget()
    
    app.exec()