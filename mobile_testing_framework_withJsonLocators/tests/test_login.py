from tests.base_tests import BaseTests
from settings import TEST_DATA
import allure


@allure.epic("Extra Mobile App")
@allure.feature("01 - Sign In")
@allure.story("01 - Login with correct and incorrect credentials")
class TestLogin(BaseTests):

    @allure.title("01 -  login with correct Credentials")
    def test_login(self, init):
        self.login_actions.login_steps(email=TEST_DATA['login']['email'], password=TEST_DATA['login']['password'])
        assert self.login_actions.get_profile_name() == "ID - 273316"

    @allure.title("02 -  login Out")
    def test_login_logOut(self, init):
        self.login_actions.login_steps_logOut()
        assert self.login_actions.get_logout_text() == "ავტორიზაცია"

    @allure.title("03 -  login with incorrect Credentials")
    def test_login_invalidData(self, init):
        self.login_actions.login_steps_invalid("ragaca@ragac.ra", "ragaca@ragac.ra")
        assert self.login_actions.get_errMsg_text() == "მომხმარებლის პაროლი ან იმეილი არასწორია"
        self.login_actions.close_warning()

    @allure.title("04 -  login without password")
    def test_login_noPassword(self, init):
        self.login_actions.login_steps_noPassword("ragaca@ragac.ra")
        assert self.login_actions.get_valid_text() == "სავალდებულო ველი"

    @allure.title("05 -  login without username")
    def test_login_noUsername(self, init):
        self.login_actions.login_steps_noUsername("password")
        assert self.login_actions.get_valid_text() == "სავალდებულო ველი"

    @allure.title("06 -  login with incorrect username")
    def test_login_invalidUsername(self, init):
        self.login_actions.login_steps_invalid("ragaca@ragac.ra", password=TEST_DATA['login']['password'])
        assert self.login_actions.get_errMsg_text() == "მომხმარებლის პაროლი ან იმეილი არასწორია"
        self.login_actions.close_warning()

    @allure.title("07 -  login with incorrect password")
    def test_login_invalidPassword(self, init):
        self.login_actions.login_steps_invalid(email=TEST_DATA['login']['email'], password="Rame12sd")
        assert self.login_actions.get_errMsg_text() == "მომხმარებლის პაროლი ან იმეილი არასწორია"
        self.login_actions.close_warning()

    @allure.title("08 -  login with incorrect Format")
    def test_login_invalidFormat(self, init):
        self.login_actions.login_steps_invalid("invalidFormatUSR", "a")
        assert self.login_actions.get_valid_text() == "არავალიდური ფორმატი"
        assert self.login_actions.get_valid_text() == "არავალიდური ფორმატი"

    @allure.title("09 -  login with incorrect Format username")
    def test_login_invalidFormatUsername(self, init):
        self.login_actions.login_steps_invalid("invalidFormatUSR", password=TEST_DATA['login']['password'])
        assert self.login_actions.get_valid_text() == "არავალიდური ფორმატი"

    @allure.title("10 -  login with incorrect Format password")
    def test_login_invalidFormatPassword(self, init):
        self.login_actions.login_steps_invalid(email=TEST_DATA['login']['email'], password="a")
        assert self.login_actions.get_valid_text() == "არავალიდური ფორმატი"

    @allure.title("11 - check password eye open/close")
    def test_login_eye(self, init):
        self.login_actions.login_steps_eyeOpen("satesto")
        assert self.login_actions.get_password_input() == "satesto"
        self.login_actions.login_steps_closeEye()
