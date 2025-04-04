import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel
from PyQt6.QtCore import Qt

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        
        # Main Variables
        self.current_inputs = "Make calculations by interact with buttons"
        self.previous_char_type = "none"
        self.current_error = ""

        # Setup Window
        self.setGeometry(1000 , 300, 260, 410)
        self.setWindowTitle("Calculator")
        self.setStyleSheet("background-color: #AAAAAA;" )

        # Setup General App
        self.init()

    def init(self):

        # TOP
        self.show_inputs = QLabel(f"{self.current_inputs}", parent=self)
        self.show_inputs.setGeometry(10, 20, 240, 50)
        self.show_inputs.setStyleSheet("background-color: lightgray; border: 1px solid black;")
        self.show_inputs.setAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)

        # Row 1
        self.button1a = QPushButton("C", parent=self)
        self.button1a.setGeometry(10, 100, 60, 60) # Element 1
        self.button1a.setStyleSheet("background-color: lightgray")
        self.button1a.clicked.connect(lambda: self.add_char_in_calculator("C"))

        self.button2a = QPushButton("0", parent=self)
        self.button2a.setGeometry(70, 100, 60, 60) # Element 2
        self.button2a.setStyleSheet("background-color: gray")
        self.button2a.clicked.connect(lambda: self.add_char_in_calculator("0"))

        self.button3a = QPushButton("/", parent=self)
        self.button3a.setGeometry(130, 100, 60, 60) # Element 3
        self.button3a.setStyleSheet("background-color: lightgray")
        self.button3a.clicked.connect(lambda: self.add_char_in_calculator("/"))

        self.button4a = QPushButton("⋆", parent=self)
        self.button4a.setGeometry(190, 100, 60, 60) # Element 4
        self.button4a.setStyleSheet("background-color: lightgray")
        self.button4a.clicked.connect(lambda: self.add_char_in_calculator("*"))

        # Row 2
        self.button1b = QPushButton("1", parent=self)
        self.button1b.setGeometry(10, 160, 60, 60) # Element 1
        self.button1b.setStyleSheet("background-color: gray")
        self.button1b.clicked.connect(lambda: self.add_char_in_calculator("1"))

        self.button2b = QPushButton("2", parent=self)
        self.button2b.setGeometry(70, 160, 60, 60) # Element 2
        self.button2b.setStyleSheet("background-color: gray")
        self.button2b.clicked.connect(lambda: self.add_char_in_calculator("2"))

        self.button3b = QPushButton("3", parent=self)
        self.button3b.setGeometry(130, 160, 60, 60) # Element 3
        self.button3b.setStyleSheet("background-color: gray")
        self.button3b.clicked.connect(lambda: self.add_char_in_calculator("3"))

        self.button4b = QPushButton("-", parent=self)
        self.button4b.setGeometry(190, 160, 60, 60) # Element 4
        self.button4b.setStyleSheet("background-color: lightgray")
        self.button4b.clicked.connect(lambda: self.add_char_in_calculator("-"))

        # Row 3
        self.button1c = QPushButton("4", parent=self)
        self.button1c.setGeometry(10, 220, 60, 60) # Element 1
        self.button1c.setStyleSheet("background-color: gray")
        self.button1c.clicked.connect(lambda: self.add_char_in_calculator("4"))

        self.button2c = QPushButton("5", parent=self)
        self.button2c.setGeometry(70, 220, 60, 60) # Element 2
        self.button2c.setStyleSheet("background-color: gray")
        self.button2c.clicked.connect(lambda: self.add_char_in_calculator("5"))

        self.button3c = QPushButton("6", parent=self)
        self.button3c.setGeometry(130, 220, 60, 60) # Element 3
        self.button3c.setStyleSheet("background-color: gray")
        self.button3c.clicked.connect(lambda: self.add_char_in_calculator("6"))

        self.button4c = QPushButton("+", parent=self)
        self.button4c.setGeometry(190, 220, 60, 60) # Element 4
        self.button4c.setStyleSheet("background-color: lightgray")
        self.button4c.clicked.connect(lambda: self.add_char_in_calculator("+"))

        # Row 4
        self.button1d = QPushButton("7", parent=self)
        self.button1d.setGeometry(10, 280, 60, 60) # Element 1
        self.button1d.setStyleSheet("background-color: gray")
        self.button1d.clicked.connect(lambda: self.add_char_in_calculator("7"))

        self.button2d = QPushButton("8", parent=self)
        self.button2d.setGeometry(70, 280, 60, 60) # Element 2
        self.button2d.setStyleSheet("background-color: gray")
        self.button2d.clicked.connect(lambda: self.add_char_in_calculator("8"))

        self.button3d = QPushButton("9", parent=self)
        self.button3d.setGeometry(130, 280, 60, 60) # Element 3
        self.button3d.setStyleSheet("background-color: gray")
        self.button3d.clicked.connect(lambda: self.add_char_in_calculator("9"))

        self.button4d = QPushButton("=", parent=self)
        self.button4d.setGeometry(190, 280, 60, 60) # Element 4
        self.button4d.setStyleSheet("background-color: lightgray")
        self.button4d.clicked.connect(lambda: self.add_char_in_calculator("="))

        # Row 5
        self.button1e = QPushButton(".", parent=self)
        self.button1e.setGeometry(10, 340, 60, 60)
        self.button1e.setStyleSheet("background-color: gray")
        self.button1e.clicked.connect(lambda: self.add_char_in_calculator("."))

    def add_char_in_calculator(self, char):
        if self.previous_char_type in ["number","operator1"]:
            if char == "+":
                self.current_inputs = str(self.current_inputs) + "+"
                self.show_inputs.setText(f"{self.current_inputs}")
                self.previous_char_type = "operator"
            elif char == "-":
                self.current_inputs = str(self.current_inputs) + "-"
                self.show_inputs.setText(f"{self.current_inputs}")
                self.previous_char_type = "operator"
            elif char == "*":
                self.current_inputs = str(self.current_inputs) + "*"
                self.show_inputs.setText(f"{self.current_inputs}")
                self.previous_char_type = "operator"
            elif char == "/":
                self.current_inputs = str(self.current_inputs) + "/"
                self.show_inputs.setText(f"{self.current_inputs}")
                self.previous_char_type = "operator"
            elif char == "=":
                try:
                    self.current_inputs = eval(str(self.current_inputs))
                    decimals, decimal_part, integer_part = self.count_decimals(self.current_inputs)
                    self.show_inputs.setText(f"{int(self.current_inputs)}")

                    if decimals >= 1 and not '000' in decimal_part and len(integer_part) <= 3:
                        self.show_inputs.setText(f"{self.current_inputs:.8f}")
                    elif decimals >= 1 and not '000' in decimal_part and len(integer_part) == 4:
                        self.show_inputs.setText(f"{self.current_inputs:.7f}")
                    elif decimals >= 1 and not '000' in decimal_part and len(integer_part) == 5:
                        self.show_inputs.setText(f"{self.current_inputs:.6f}")
                    elif decimals >= 1 and not '000' in decimal_part and len(integer_part) == 6:
                        self.show_inputs.setText(f"{self.current_inputs:.5f}")
                    elif decimals >= 1 and not '000' in decimal_part and len(integer_part) == 7:
                        self.show_inputs.setText(f"{self.current_inputs:.4f}")
                    elif decimals >= 1 and not '000' in decimal_part and len(integer_part) == 8:
                        self.show_inputs.setText(f"{self.current_inputs:.3f}")
                    elif decimals >= 1 and not '000' in decimal_part and len(integer_part) == 9:
                        self.show_inputs.setText(f"{self.current_inputs:.2f}")
                    else:
                        self.show_inputs.setText(f"{self.current_inputs:.1f}")  

                except Exception as e:
                    self.current_error = e
                    self.current_inputs = f"{e}"
                    self.show_inputs.setText(f"{self.current_inputs}")
                    print(self.current_error)
                    self.show_inputs.setStyleSheet("font-size: 10px; background-color: lightgray; border: 1px solid black")
                
                self.previous_char_type = "operator1"
                

        if self.previous_char_type in ["number","none","operator","function","dot"]:
            if self.current_inputs in ["Make calculations by interact with buttons", str(self.current_error)]:
                self.current_inputs = ""
            
            self.show_inputs.setStyleSheet("font-size: 33px; background-color: lightgray; border: 1px solid black")

            if char == "0":
                self.current_inputs = str(self.current_inputs) + "0"
                self.show_inputs.setText(f"{self.current_inputs}")
                self.previous_char_type = "number" 
            elif char == "1":
                self.current_inputs = str(self.current_inputs) + "1"
                self.show_inputs.setText(f"{self.current_inputs}")
                self.previous_char_type = "number"
            elif char == "2":
                self.current_inputs = str(self.current_inputs) + "2"
                self.show_inputs.setText(f"{self.current_inputs}")
                self.previous_char_type = "number"
            elif char == "3":
                self.current_inputs = str(self.current_inputs) + "3"
                self.show_inputs.setText(f"{self.current_inputs}")
                self.previous_char_type = "number"
            elif char == "4":
                self.current_inputs = str(self.current_inputs) + "4"
                self.show_inputs.setText(f"{self.current_inputs}")
                self.previous_char_type = "number"
            elif char == "5":
                self.current_inputs = str(self.current_inputs) + "5"
                self.show_inputs.setText(f"{self.current_inputs}")
                self.previous_char_type = "number"
            elif char == "6":
                self.current_inputs = str(self.current_inputs) + "6"
                self.show_inputs.setText(f"{self.current_inputs}")
                self.previous_char_type = "number"
            elif char == "7":
                self.current_inputs = str(self.current_inputs) + "7"
                self.show_inputs.setText(f"{self.current_inputs}")
                self.previous_char_type = "number"
            elif char == "8":
                self.current_inputs = str(self.current_inputs) + "8"
                self.show_inputs.setText(f"{self.current_inputs}")
                self.previous_char_type = "number"
            elif char == "9":
                self.current_inputs = str(self.current_inputs) + "9"
                self.show_inputs.setText(f"{self.current_inputs}")
                self.previous_char_type = "number"
        
        if self.previous_char_type in ["operator","operator1","number","function","dot"]:
            if char == "C":
                self.current_inputs = ""
                self.show_inputs.setText(f"{self.current_inputs}")
                self.previous_char_type = "function"
        
        if self.previous_char_type in ["number"]:
            if char == ".":
                self.current_inputs = str(self.current_inputs) + "."
                self.show_inputs.setText(f"{self.current_inputs}")
                self.previous_char_type = "dot"
    
    def count_decimals(self, number):
        number_str = str(number)
        if '.' in number_str:
            integer_part, decimal_part = number_str.split(".")

            return len(decimal_part), decimal_part, integer_part
        else:
            return 0, 0, 0
        
app = QApplication(sys.argv)

window = MyApp()
window.show()

sys.exit(app.exec())