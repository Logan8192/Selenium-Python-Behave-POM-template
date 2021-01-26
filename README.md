# Python-Selenium-Behave-PyHamCrest
Web automation testing framework using the page object model pattern with Python, Selenium and the behavior-driven development tool Behave.

## Get Started:

### Create a virtual environment for the project:
```
python3 -m venv venv
```

### Activate virtual environment:
- Linux and MacOS:
```
source venv/bin/activate
```

- Windows:
```
venv\Scripts\activate.bat
```

### Install Requirements:
```
pip install -r requirements.txt
```

## Run Tests:
In order to run all tests, it is only necessary to run the command:
```
behave --define driver="DRIVER NAME"
```

Make sure to add a correct driver name parameter in order to set the browser where the test will be executed
with the following values:

 - Linux:
    - **Chrome**: *CHROME_LINUX*
    - **Firefox**: *FIREFOX_LINUX*
    - **Opera**: *OPERA_LINUX*

- Windows:
    - **Chrome**: *CHROME_WINDOWS*
    - **Edge (Chromium)**: EDGE_CHROMIUM_WINDOWS
    - **Firefox**: *FIREFOX_WINDOWS*
    - **Opera**: *OPERA_WINDOWS*

**Example:**
```
behave --define driver="CHROME_LINUX"
```
