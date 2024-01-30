import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QWidget, 
                            QPushButton, 
                            QLabel,
                            QApplication,
                            QHBoxLayout
                            )

from my_widget import MyLittleWidget
from my_other_widget import MyCounterWidget



class MyCompositeWidget(QWidget):
    def __init__(self)-> None:
        super().__init__()

        self.state=True
        
        self.button_widget = MyLittleWidget()
        self.counter_widget = MyCounterWidget()
                
        self.my_layout = QHBoxLayout()
        self.my_layout.addWidget(self.button_widget)
        self.my_layout.addWidget(self.counter_widget)
        
        self.button_widget.custom_signal.connect(self.counter_widget.increment_counter)        
        
        self.setLayout(self.my_layout)
        
        self.show() 

if __name__ =="__main__":
    app = QApplication(sys.argv)
    window = MyCompositeWidget()
    
    app.exec()