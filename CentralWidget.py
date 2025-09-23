from PyQt6.QtWidgets import QWidget, QLineEdit, QGridLayout, QTextEdit, QTextBrowser, QLabel, QPushButton


class CentralWidget(QWidget):
    def __init__(self, parent=None):
        super(CentralWidget, self).__init__(parent)

        layout = QGridLayout()

        self.__benutzername = QLineEdit()
        self.__kennwort = QLineEdit()
        self.__token = QLineEdit()

        self.__login = QPushButton("Login")
        self.__abbruch = QPushButton("Abbruch")

        self.__text_browser = QTextBrowser()

        layout.addWidget(QLabel("Benutzername:"), 0, 0, 1, 2)
        layout.addWidget(self.__benutzername, 1, 0, 1, 2)

        layout.addWidget(QLabel("Kennwort:"), 2, 0, 1, 2)
        layout.addWidget(self.__kennwort, 3, 0, 1, 2)

        layout.addWidget(QLabel("Token:"), 4, 0, 1, 2)
        layout.addWidget(self.__token, 5, 0, 1, 2)

        layout.addWidget(self.__login, 6, 0)
        layout.addWidget(self.__abbruch, 6, 1)

        layout.addWidget(QLabel("Ergebnis:"), 0, 2)
        layout.addWidget(self.__text_browser, 1, 2, 6, 1)

        self.setLayout(layout)
