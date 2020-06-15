import argparse
import os
import sys
from pathlib import Path
from selenium import webdriver


def before_scenario(context, scenario):
    context.driver = webdriver.Firefox(
            executable_path=str(Path(os.path.dirname(__file__)).parent / "drivers/linux/geckodriver"))
    context.driver.maximize_window()
    context.driver.get("https://duckduckgo.com")


def after_scenario(context, scenario):
    context.driver.quit()
