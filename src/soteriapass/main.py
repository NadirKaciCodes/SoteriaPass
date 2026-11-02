import sys 
from PySide6.QtWidgets import QApplication, QLabel 

# Database import
from soteriapass.storage.database import initialise_database

def main():
    initialise_database()

    app = QApplication(sys.argv)

    window = QLabel("Welcome to SoteriaPass")
    window.setWindowTitle("SoteriaPass")
    window.resize(400, 200)
    window.show()

    sys.exit(app.exec())

if __name__ == "__main__":
    main()

