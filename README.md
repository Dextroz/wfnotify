# wfnotify
![wfnotify](example.gif)

A PyQt5 app for viewing Warframe API data.

## Disclaimer
* This build of the app is currently under development and is not final.
* I did not create PyQt5. See [Acknowledgments](#acknowledgments)
* Source code for the entire program can be found in [wfnotify.py](wfnotify.py)

## Current Features
  1. Fetch current Cetustime (Check if night or day).
  2. Fetch current alerts data.
  3. Fetch current fissure data.
  4. Fetch current sortie data.

## Dependencies
wfnotify is written in Python 3.

wfnotify requires the following dependencies:
  1. * [PyQt5](https://riverbankcomputing.com/software/pyqt/download5) - A Python application framework.
  2. * [Requests](https://github.com/requests/requests/) - Python HTTP Requests for Humans ✨🍰✨

## Usage
Clone or download the master branch.

Extract and navigate to the zipfile directory and run wfnotify by executing the main entry point file (wfnotify.py):
  ```
  python3 wfnotify.py
  ```

If you don't have python installed then you can run the .exe file which is a packaged version of the application
meaning you can still use the app without a python interpreter installed on you're system.

The .exe is located in:
  ```
  ./dist/wfnotify.exe
  ```

[Virustotal Scan](https://www.virustotal.com/#/file/9012e8806c3f9175b1566fe1fa41af38136d7c3a0b03a9efdf7a0edddf02321a/detection)
**The 5 detections are false positives. Examine the code used at [wfnotify.py](wfnotify.py)**

## Authors -- Contributors

* **Daniel Brennand** - *Author of project* - [Dextroz](https://github.com/Dextroz)

## License

This project is licensed under the GPL-3.0 License - see the [LICENSE](LICENSE) for details.

## Acknowledgments
Riverbank Computing Limited created [PyQt5](https://riverbankcomputing.com/software/pyqt/download5)

Freeze (package) Python programs into stand-alone executables - [pyinstaller](http://www.pyinstaller.org)
