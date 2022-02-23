"""
    Created By  : itsparser
    Created On  : 26/01/22
"""

from selenium import webdriver

capabilities = {
    "browserName": "chrome",
    "browserVersion": "96.0",
    "selenoid:options": {
        "enableVNC": True,
        "enableVideo": False
    }
}

driver = webdriver.Remote(
    command_executor="http://localhost:4444/wd/hub",
    desired_capabilities=capabilities)

driver.get("http://www.google.com")
