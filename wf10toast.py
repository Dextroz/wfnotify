try:
    from win10toast import ToastNotifier
    import requests
    import time
except ImportError:
    print("Failed to import required modules.")


def get_request(endpoint):
    try:
        resp = requests.get(endpoint)
        if ((resp.status_code) == (requests.codes.ok)):
            return resp.json()
        else:
            resp.raise_for_status()
    except requests.exceptions.TooManyRedirects:
        print("Request exceeded the acceptable number of redirects.")
    except requests.exceptions.Timeout:
        print("Request timed out.")
    except requests.exceptions.HTTPError as err:
        print(f"The following HTTPError occured {err}")


def fetch_alerts(json_resp):
    try:
        # Collect relevant data and store in respective variables.
        for num, alerts in enumerate(json_resp):
            mission_location = alerts["mission"]["node"]
            mission_type = alerts["mission"]["type"]
            eta = alerts["eta"]
            max_enemy_lvl = alerts["mission"]["maxEnemyLevel"]
            faction = alerts["mission"]["faction"]
            reward = alerts["mission"]["reward"]["asString"]
            mission_title = f"Alert: {mission_type} at {mission_location}"
            mission_info = f"""ETA: {eta}
Enemy Lvl: {max_enemy_lvl}
Faction: {faction}
Reward: {reward}"""
            create_noti(mission_title, mission_info)
    except KeyError as err:
        print(f"The following KeyError occured {err}")


def create_noti(mission_title, mission_info):
    toaster = ToastNotifier()
    toaster.show_toast(title=mission_title, msg=mission_info, icon_path="./my_logo.ico",
                       duration=15, threaded=True)
    while toaster.notification_active():
        time.sleep(0.1)


fetch_alerts(get_request("https://api.warframestat.us/pc/alerts"))
