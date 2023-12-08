import sys
from PyQt6.QtWidgets import QApplication, QLabel, QWidget

# AApplication deals with the command-line commands
# In this example the command-line will not be used, hence the empty list
app = QApplication([])

# App GUI
window = QWidget()
window.setWindowTitle("PyQt App")
window.setGeometry(100, 100, 280, 80)
helloMsg = QLabel("<h1>Hello, World!</h1>", parent=window)
helloMsg.move(60, 15)

# Display the window
window.show()

# Run the application loop
sys.exit(app.exec())

