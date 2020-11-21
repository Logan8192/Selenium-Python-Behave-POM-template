# Python-Selenium-Behave-PyHamCrest 
Web automation testing framework using the page object model pattern with Python, Selenium and the behavior-driven development tool Behave.

## Install Requirements:
Once the virtual environment for the repository is created and activated, run this command to download the project 
requirements: 
``` 
pip3 install -r requirements.txt 
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