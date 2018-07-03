try:
    # Imports required for GUI application.
    import sys
    from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QGroupBox, QVBoxLayout
    from PyQt5.QtCore import pyqtSlot
    # For contacting Warframe API.
    import requests
    # Partial used to pass additional args into function for button.
    # See: https://docs.python.org/3/library/functools.html#functools.partial
    from functools import partial
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
        self.setWindowTitle("Warframe Notifier")
        self.setGeometry(10, 10, 320, 100)

        # Adding groupbox (returned from h_layout() to window.)
        window_layout = QVBoxLayout()
        window_layout.addWidget(self.h_layout())
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
        button_worldstate.clicked.connect(
            partial(self.get_request, endpoint=self.endpoint_list[0]))
        h_box.addWidget(button_worldstate)

        button_alerts = QPushButton("Check Alerts", self)
        button_alerts.clicked.connect(
            partial(self.get_request, endpoint=self.endpoint_list[1]))
        h_box.addWidget(button_alerts)

        button_fissures = QPushButton("Check Fissures", self)
        button_fissures.clicked.connect(
            partial(self.get_request, endpoint=self.endpoint_list[2]))
        h_box.addWidget(button_fissures)

        button_sortie = QPushButton("Check Sortie", self)
        button_sortie.clicked.connect(
            partial(self.get_request, endpoint=self.endpoint_list[3]))
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
                print(request.json())
            else:
                request.raise_for_status()
        except requests.exceptions.TooManyRedirects:
            print("Request exceeded the acceptable number of redirects.")
        except requests.exceptions.Timeout:
            print("Request timed out.")
        except requests.exceptions.HTTPError as err:
            print(f"The following HTTPError occured {err}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
