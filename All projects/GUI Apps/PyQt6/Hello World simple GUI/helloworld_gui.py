import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel

app = QApplication(sys.argv) # Without this, nothing works

window = QWidget() # The window where will apperar the "Hello, World!" text(label)
window.setGeometry(100, 100, 200, 50) # x, y, width, height

text =  QLabel("<h1>Hello, World!</h1>", parent=window) # The "Hello, World!" text(label)
text.move(20, 10) # Move the "Hello, World!" text(label) at x, y coordonates in the window

# Show the window AND run the main loop of GUI whats help the GUI to stay opened
window.show()
sys.exit(app.exec())