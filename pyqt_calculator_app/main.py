import sys
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, 
                             QVBoxLayout, QLabel, QSpinBox, QPushButton,
                             QGridLayout)
from PyQt6.QtGui import QPalette, QColor
from PyQt6.QtCore import Qt

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("Volume Calculator App")

        main_layout = QVBoxLayout()

        ### Title stuff! ################################################
        # Title label
        title_label = QLabel("Volume Calculator")
        
        # Title font
        h1_font = title_label.font()
        h1_font.setPointSize(30)
        title_label.setFont(h1_font)

        ### Pane stuff! #################################################
        # Top pane widgets
        top_pane = QVBoxLayout()
        length_label = QLabel("Length =")
        length_spinbox = QSpinBox()
        height_label = QLabel("Height =")
        height_spinbox = QSpinBox()
        width_label = QLabel("Width =")
        width_spinbox = QSpinBox()

        # Bottom pane widgets
        bottom_pane = QVBoxLayout()
        submit_button = QPushButton("Calculate")
        submit_button.setFixedSize(150, 70)
        bottom_pane.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        results_label = QLabel()

        ### Add widgets and layouts #####################################
        # Add top pane widgets
        top_pane.addWidget(title_label)
        top_pane.addWidget(length_label)
        top_pane.addWidget(length_spinbox)
        top_pane.addWidget(height_label)
        top_pane.addWidget(height_spinbox)
        top_pane.addWidget(width_label)
        top_pane.addWidget(width_spinbox)

        # Add bottom pane widgets
        bottom_pane.addWidget(submit_button)
        bottom_pane.addWidget(results_label)

        # Add aspects to main layout
        main_layout.addLayout(top_pane)
        main_layout.addLayout(bottom_pane)


        widget = QWidget()
        widget.setLayout(main_layout)
        self.setCentralWidget(widget)



app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()