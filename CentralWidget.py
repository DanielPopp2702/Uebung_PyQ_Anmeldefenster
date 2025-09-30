from PyQt6.QtCore import pyqtSlot
from PyQt6.QtWidgets import QWidget, QLineEdit, QGridLayout, QTextBrowser, QLabel, QPushButton

class CentralWidget(QWidget):
    def __init__(self, parent=None):
        super(CentralWidget, self).__init__(parent)

        layout = QGridLayout()


        self.__set_user = {"Dani", "Fabi", "Tobi", "Kobe", "Jojo"}
        self.__list_password = ["dani1", "fabi2", "tobi3", "kobe4", "jojo5"]
        self.__dict_token = {
            "dani1": "0F0F",
            "fabi2": "FF00",
            "tobi3": "0FFF",
            "kobe4": "F00F",
            "jojo5": "00FF"
        }


        self.__benutzername = QLineEdit()
        self.__benutzername.setInputMask(">A" + 3*"<a")
        self.__benutzername.setMaxLength(4)

        self.__kennwort = QLineEdit()
        self.__kennwort.setMaxLength(8)
        self.__kennwort.setEchoMode(QLineEdit.EchoMode.Password)

        self.__token = QLineEdit()
        self.__token.setInputMask(4 * "H")
        self.__token.setMaxLength(4)

        self.__login = QPushButton("Login")
        self.__login.released.connect(self.check_login)

        self.__abbruch = QPushButton("Abbruch")
        self.__abbruch.released.connect(self.abort)

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

    @pyqtSlot()
    def check_login(self):
        self.__text_browser.clear()

        user = self.__benutzername.text()
        pwd = self.__kennwort.text()
        token = self.__token.text()

        status = True


        if user in self.__set_user:
            self.__text_browser.append("Benutzername korrekt")
        else:
            self.__text_browser.append("Eingabe Benutzername falsch.")
            status = False


        if pwd in self.__list_password:
            self.__text_browser.append("Kennwort korrekt")
        else:
            self.__text_browser.append("Eingabe Kennwort falsch.")
            status = False


        if pwd in self.__dict_token:
            if self.__dict_token[pwd] == token:
                self.__text_browser.append("Token korrekt")
            else:
                self.__text_browser.append("Eingabe Token falsch.")
                status = False
        else:
            self.__text_browser.append("Eingabe Token falsch.")
            status = False


        if status:
            self.__text_browser.append("Login erfolgreich.")

    @pyqtSlot()
    def abort(self):
        self.__benutzername.clear()
        self.__kennwort.clear()
        self.__token.clear()
        self.__text_browser.clear()




