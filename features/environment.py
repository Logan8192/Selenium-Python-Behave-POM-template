import os
from pathlib import Path
from selenium import webdriver


def before_scenario(context, scenario):
    # Obtaining the driver name set by the user.
    driver_name = context.config.userdata.get("driver")

    # Starting the chosen driver.
    if driver_name == "FIREFOX_LINUX":
        context.driver = webdriver.Firefox(
            executable_path=str(Path(os.path.dirname(__file__)).parent / "drivers/linux/geckodriver"))
    elif driver_name == "CHROME_LINUX":
        context.driver = webdriver.Chrome(
            executable_path=str(Path(os.path.dirname(__file__)).parent / "drivers/linux/chromedriver"))
    elif driver_name == "OPERA_LINUX":
        context.driver = webdriver.Opera(
            executable_path=str(Path(os.path.dirname(__file__)).parent / "drivers/linux/operadriver"))
    else:
        raise ValueError("An incorrect driver name was set. Please set a valid driver name.")
    context.driver.maximize_window()
    context.driver.get("https://duckduckgo.com")


def after_scenario(context, scenario):
    context.driver.quit()
