import json

from utils.page_utils import PageUtils


class BaseScreenAction:

    def __init__(self, driver):
        self.driver = driver
        self.pu = PageUtils(driver)
        self.auth_locators = json.loads(open('../locators_Json/auth.conf', 'r').read())
        #self.reg_locators = json.loads(open('../locators_Json/example.conf', 'r').read())