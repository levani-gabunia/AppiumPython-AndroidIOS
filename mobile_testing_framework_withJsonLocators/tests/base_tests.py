import pytest
from utils.page_utils import PageUtils
from actions.login_actions import LoginActions

@pytest.mark.usefixtures('setup')
class BaseTests:

    @pytest.fixture
    def init(self):
        driver = self.driver
        self.pu = PageUtils(driver)
        self.login_actions = LoginActions(driver)