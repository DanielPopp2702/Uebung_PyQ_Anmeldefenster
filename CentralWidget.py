from PyQt6.QtCore import pyqtSlot  # Importiert pyqtSlot zur Kennzeichnung von Methoden, die auf Signale reagieren
from PyQt6.QtWidgets import QWidget, QLineEdit, QGridLayout, QTextBrowser, QLabel, \
    QPushButton  # Importiert die benötigten GUI-Elemente


class CentralWidget(QWidget):
    """
    Das Haupt-Widget, das ein 3-Faktor-Authentifizierungsformular (Benutzername, Kennwort, Token) implementiert.
    Es erbt von QWidget.
    """

    def __init__(self, parent=None):
        # Ruft den Konstruktor der Basisklasse QWidget auf
        super(CentralWidget, self).__init__(parent)

        # Erstellt ein QGridLayout für die gitterbasierte Anordnung der Widgets
        layout = QGridLayout()

        # --- 1. Zugangsdaten-Definition ---

        # Menge (Set) der gültigen Benutzernamen (Groß-/Kleinschreibung beachtet)
        self.__set_user = {"Dani", "Fabi", "Tobi", "Kobe", "Jojo"}
        # Liste der gültigen Kennwörter
        self.__list_password = ["dani1", "fabi2", "tobi3", "kobe4", "jojo5"]
        # Wörterbuch (Dict) zur Zuordnung von Kennwort zu gültigem Token (Token ist abhängig vom PWD)
        self.__dict_token = {
            "dani1": "0F0F",
            "fabi2": "FF00",
            "tobi3": "0FFF",
            "kobe4": "F00F",
            "jojo5": "00FF"
        }

        # --- 2. Eingabefelder (QLineEdit) ---

        # Eingabefeld für den Benutzernamen
        self.__benutzername = QLineEdit()
        # Setzt eine Eingabemaske: >A (erster Buchstabe muss Großbuchstabe sein), 3*<a (danach folgen drei Kleinbuchstaben)
        self.__benutzername.setInputMask(">A" + 3 * "<a")
        # Begrenzt die maximale Länge auf 4 Zeichen
        self.__benutzername.setMaxLength(4)

        # Eingabefeld für das Kennwort
        self.__kennwort = QLineEdit()
        # Begrenzt die maximale Länge auf 8 Zeichen
        self.__kennwort.setMaxLength(8)
        # Verbirgt die Eingabe durch Punkte (Passwort-Modus)
        self.__kennwort.setEchoMode(QLineEdit.EchoMode.Password)

        # Eingabefeld für den Token
        self.__token = QLineEdit()
        # Setzt eine Eingabemaske: 4 * H (4 Hexadezimalziffern, A-F, 0-9)
        self.__token.setInputMask(4 * "H")
        # Begrenzt die maximale Länge auf 4 Zeichen
        self.__token.setMaxLength(4)

        # --- 3. Steuerelemente und Textausgabe ---

        # Button für den Login-Vorgang
        self.__login = QPushButton("Login")
        # Verbindet das released-Signal (nach Klick) mit der Logik-Methode check_login
        self.__login.released.connect(self.check_login)

        # Button zum Abbrechen/Löschen der Eingabefelder
        self.__abbruch = QPushButton("Abbruch")
        # Verbindet das released-Signal mit der Lösch-Methode abort
        self.__abbruch.released.connect(self.abort)

        # TextBrowser zur Anzeige der Login-Ergebnisse/Meldungen
        self.__text_browser = QTextBrowser()

        # --- 4. Layout-Anordnung (QGridLayout) ---

        # Fügt das Label "Benutzername:" in Zeile 0, Spalte 0 hinzu (nimmt 2 Spalten ein)
        layout.addWidget(QLabel("Benutzername:"), 0, 0, 1, 2)
        # Fügt das Eingabefeld in Zeile 1, Spalte 0 hinzu (nimmt 2 Spalten ein)
        layout.addWidget(self.__benutzername, 1, 0, 1, 2)

        # Fügt das Label "Kennwort:" in Zeile 2, Spalte 0 hinzu (nimmt 2 Spalten ein)
        layout.addWidget(QLabel("Kennwort:"), 2, 0, 1, 2)
        # Fügt das Kennwortfeld in Zeile 3, Spalte 0 hinzu (nimmt 2 Spalten ein)
        layout.addWidget(self.__kennwort, 3, 0, 1, 2)

        # Fügt das Label "Token:" in Zeile 4, Spalte 0 hinzu (nimmt 2 Spalten ein)
        layout.addWidget(QLabel("Token:"), 4, 0, 1, 2)
        # Fügt das Tokenfeld in Zeile 5, Spalte 0 hinzu (nimmt 2 Spalten ein)
        layout.addWidget(self.__token, 5, 0, 1, 2)

        # Fügt den Login-Button in Zeile 6, Spalte 0 hinzu
        layout.addWidget(self.__login, 6, 0)
        # Fügt den Abbruch-Button in Zeile 6, Spalte 1 hinzu
        layout.addWidget(self.__abbruch, 6, 1)

        # Fügt das Label "Ergebnis:" in Zeile 0, Spalte 2 hinzu (separater Bereich)
        layout.addWidget(QLabel("Ergebnis:"), 0, 2)
        # Fügt den TextBrowser in Zeile 1, Spalte 2 hinzu (nimmt 6 Zeilen ein)
        layout.addWidget(self.__text_browser, 1, 2, 6, 1)

        # Setzt das erstellte Layout als Haupt-Layout für das Widget
        self.setLayout(layout)

    # --- 5. Logik-Methoden (Slots) ---

    @pyqtSlot()
    def check_login(self):
        """Überprüft Benutzername, Kennwort und Token zur Authentifizierung."""
        # Löscht vorherige Meldungen im TextBrowser
        self.__text_browser.clear()

        # Liest die aktuellen Eingabewerte aus den Feldern
        user = self.__benutzername.text()
        pwd = self.__kennwort.text()
        token = self.__token.text()

        # Statusvariable: True, solange alle Checks erfolgreich sind
        status = True

        # --- Benutzername-Prüfung ---
        # Prüft, ob der eingegebene Benutzername in der Liste der gültigen User ist
        if user in self.__set_user:
            self.__text_browser.append("Benutzername korrekt")
        else:
            self.__text_browser.append("Eingabe Benutzername falsch.")
            status = False  # Setzt Status auf False

        # --- Kennwort-Prüfung ---
        # Prüft, ob das eingegebene Kennwort in der Liste der gültigen Kennwörter ist
        if pwd in self.__list_password:
            self.__text_browser.append("Kennwort korrekt")
        else:
            self.__text_browser.append("Eingabe Kennwort falsch.")
            status = False

        # --- Token-Prüfung ---
        # 1. Prüft, ob das Kennwort überhaupt einen zugeordneten Token hat (als Schlüssel im Dict)
        if pwd in self.__dict_token:
            # 2. Wenn ja, prüft, ob der eingegebene Token mit dem gespeicherten Token übereinstimmt
            if self.__dict_token[pwd] == token:
                self.__text_browser.append("Token korrekt")
            else:
                self.__text_browser.append("Eingabe Token falsch.")
                status = False  # Token falsch
        else:
            # Wenn das Kennwort nicht einmal im Token-Dict gefunden wird, ist die Kombination falsch
            self.__text_browser.append("Eingabe Token falsch.")
            status = False  # Kennwort/Token-Kombination falsch

        # --- Ergebnis-Ausgabe ---
        # Wenn alle Prüfungen erfolgreich waren (status ist noch True)
        if status:
            self.__text_browser.append("Login erfolgreich.")

    @pyqtSlot()
    def abort(self):
        """Löscht den Inhalt aller Eingabefelder und des Ergebnis-Browsers."""
        # Löscht den Text im Benutzernamen-Feld
        self.__benutzername.clear()
        # Löscht den Text im Kennwort-Feld
        self.__kennwort.clear()
        # Löscht den Text im Token-Feld
        self.__token.clear()
        # Löscht den Inhalt des Ergebnis-Browsers
        self.__text_browser.clear()




