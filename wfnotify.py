try:
    # Imports required for GUI application.
    import sys
    from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QGroupBox, QVBoxLayout, QTextEdit
    from PyQt5.QtCore import pyqtSlot
    from PyQt5.QtGui import QIcon
    # For contacting Warframe API.
    import requests
    # Partial removed. No longer used.
except ImportError:
    print("Failed to import required packages.")


class App(QWidget):

    # Init Inheriting functions from parent.
    def __init__(self):
        self.endpoint_list = ["https://api.warframestat.us/pc/cetusCycle", "https://api.warframestat.us/pc/alerts",
                              "https://api.warframestat.us/pc/fissures", "https://api.warframestat.us/pc/sortie"]
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowIcon(QIcon("my_logo.png"))
        self.setWindowTitle("wfnotify")
        self.setGeometry(10, 10, 500, 200)

        # Adding groupbox (returned from h_layout() to window.)
        window_layout = QVBoxLayout()
        window_layout.addWidget(self.h_layout())

        # Adding Text box.
        self.text_box = QTextEdit()
        window_layout.addWidget(self.text_box)

        # Set Layout.
        self.setLayout(window_layout)

        # Show the window upon execution.
        self.show()

    def h_layout(self):
        # Groupbox object.
        groupbox = QGroupBox("Select an option: ")
        # Variable holding Horisontal box layout.
        h_box = QHBoxLayout()

        # Defining widgets are appending them to the Horisontal box layout.
        button_worldstate = QPushButton("Check Cetuscycle", self)
        button_worldstate.clicked.connect(lambda: self.cetus_text(
            self.get_request(self.endpoint_list[0])))
        h_box.addWidget(button_worldstate)

        button_alerts = QPushButton("Check Alerts", self)
        button_alerts.clicked.connect(lambda: self.alert_text(
            self.get_request(self.endpoint_list[1])))
        h_box.addWidget(button_alerts)

        button_fissures = QPushButton("Check Fissures", self)
        button_fissures.clicked.connect(lambda: self.fissures_text(
            self.get_request(self.endpoint_list[2])))
        h_box.addWidget(button_fissures)

        button_sortie = QPushButton("Check Sortie", self)
        button_sortie.clicked.connect(lambda: self.sortie_text(
            self.get_request(self.endpoint_list[3])))
        h_box.addWidget(button_sortie)

        # Adding the horisontal box layout to the groupbox object and returning
        # groupbox to addWidget() in init_ui().
        groupbox.setLayout(h_box)
        return groupbox

    # Decorator for good practice denoting method as a PyQt5 slot.
    @pyqtSlot()
    def get_request(self, endpoint):
        try:
            request = requests.get(endpoint)
            if ((request.status_code) == (requests.codes.ok)):
                return request.json()
            else:
                request.raise_for_status()
        except requests.exceptions.TooManyRedirects:
            self.text_box.setText(
                "Request exceeded the acceptable number of redirects.")
        except requests.exceptions.Timeout:
            self.text_box.setText("Request timed out.")
        except requests.exceptions.HTTPError as err:
            self.text_box.setText(f"The following HTTPError occured {err}")

    @pyqtSlot()
    def cetus_text(self, json_resp):
        try:
            short_string = json_resp["shortString"]
            isday = json_resp["isDay"]
            if ((isday) == (True)):
                self.text_box.setText(
                    f"It's currently day with {short_string}")
            else:
                self.text_box.setText(
                    f"It's currently night with {short_string}")
        except KeyError as err:
            self.text_box.setText(f"The following KeyError occured {err}")

    @pyqtSlot()
    def alert_text(self, json_resp):
        try:
            # Clear Text box before start of func.
            self.text_box.setText("")
            # Collect relevant data and store in respective variables.
            for num, alerts in enumerate(json_resp, 1):
                mission_location = alerts["mission"]["node"]
                mission_type = alerts["mission"]["type"]
                eta = alerts["eta"]
                max_enemy_lvl = alerts["mission"]["maxEnemyLevel"]
                faction = alerts["mission"]["faction"]
                reward = alerts["mission"]["reward"]["asString"]
                format_str = f"""{num}.
    Location: {mission_location}
    Type: {mission_type}
    ETA: {eta}
    Enemy Lvl: {max_enemy_lvl}
    Faction: {faction}
    Reward: {reward} \n"""
                self.text_box.append(format_str)
        except KeyError as err:
            self.text_box.setText(f"The following KeyError occured {err}")

    @pyqtSlot()
    def fissures_text(self, json_resp):
        try:
            # Clear Text box before start of func.
            self.text_box.setText("")
            # Collect relevant data and store in respective variables.
            for num, fissures in enumerate(json_resp, 1):
                mission_location = fissures["node"]
                mission_type = fissures["missionType"]
                eta = fissures["eta"]
                tier = fissures["tier"]
                faction = fissures["enemy"]
                format_str = f"""{num}.
    Location: {mission_location}
    Type: {mission_type}
    ETA: {eta}
    Tier: {tier}
    Faction: {faction} \n"""
                self.text_box.append(format_str)
        except KeyError as err:
            self.text_box.setText(f"The following KeyError occured {err}")

    @pyqtSlot()
    def sortie_text(self, json_resp):
        try:
            # Clear Text box before start of func.
            self.text_box.setText("")
            # Collect relevant data and store in respective variables.
            eta = json_resp["eta"]
            faction = json_resp["faction"]
            for num, missions in enumerate(json_resp["variants"], 1):
                mission_location = missions["node"]
                mission_type = missions["missionType"]
                modifier = missions["modifier"]
                format_str = f"""{num}.
    Location: {mission_location}
    Type: {mission_type}
    ETA: {eta}
    Modifier: {modifier}
    Faction: {faction} \n"""
                self.text_box.append(format_str)
        except KeyError as err:
            self.text_box.setText(f"The following KeyError occured {err}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
