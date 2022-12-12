from actions.base_screen_action import BaseScreenAction


class LoginActions(BaseScreenAction):

    def login_steps(self, email, password):
        if self.pu.is_visible(self.pu.get_locator(self.auth_locators, 'Iallert_notification')):
            self.pu.click(self.pu.get_locator(self.auth_locators, 'Iallert_notification'))
        if self.pu.is_visible(self.pu.get_locator(self.auth_locators, 'Iprofile_button')):
            self.pu.click(self.pu.get_locator(self.auth_locators, 'Iprofile_button'))
        self.pu.clear(self.pu.get_locator(self.auth_locators, 'Iemail_input'))
        self.pu.send_keys(self.pu.get_locator(self.auth_locators, 'Iemail_input'), email)
        self.pu.send_keys(self.pu.get_locator(self.auth_locators, 'Ipassword_input'), password)
        self.pu.click(self.pu.get_locator(self.auth_locators, 'Ienter_button'))
        self.pu.click(self.pu.get_locator(self.auth_locators, 'Iclose_easy_auth_button'))

    def login_steps_logOut(self):
        self.pu.click(self.pu.get_locator(self.auth_locators, 'Iprofile_button'))
        self.pu.click(self.pu.get_locator(self.auth_locators, 'Imy_profile_button'))
        self.pu.click(self.pu.get_locator(self.auth_locators, 'Iexit_button'))

    def login_steps_noUsername(self, password):
        self.pu.clear(self.pu.get_locator(self.auth_locators, 'Iemail_input'))
        self.pu.send_keys(self.pu.get_locator(self.auth_locators, 'Ipassword_input'), password)
        self.pu.click(self.pu.get_locator(self.auth_locators, 'Ienter_button'))

    def login_steps_noPassword(self, email):
        self.pu.clear(self.pu.get_locator(self.auth_locators, 'Iemail_input'))
        self.pu.send_keys(self.pu.get_locator(self.auth_locators, 'Iemail_input'), email)
        self.pu.clear(self.pu.get_locator(self.auth_locators, 'Ipassword_input'))
        self.pu.click(self.pu.get_locator(self.auth_locators, 'Ienter_button'))

    def login_steps_invalid(self, email, password):
        self.pu.clear(self.pu.get_locator(self.auth_locators, 'Iemail_input'))
        self.pu.send_keys(self.pu.get_locator(self.auth_locators, 'Iemail_input'), email)
        self.pu.send_keys(self.pu.get_locator(self.auth_locators, 'Ipassword_input'), password)
        self.pu.click(self.pu.get_locator(self.auth_locators, 'Ienter_button'))

    def login_steps_eyeOpen(self, password):
        self.pu.clear(self.pu.get_locator(self.auth_locators, 'Ipassword_input'))
        self.pu.send_keys(self.pu.get_locator(self.auth_locators, 'Ipassword_input'), password)
        self.pu.click(self.pu.get_locator(self.auth_locators, 'eye'))

    def login_steps_closeEye(self):
        self.pu.click(self.pu.get_locator(self.auth_locators, 'close_eye'))

    def get_password_input(self):
        text = self.pu.get_text(self.pu.get_locator(self.auth_locators, 'password_text'))
        return text

    def get_profile_name(self):
        text = self.pu.get_text(self.pu.get_locator(self.auth_locators, 'Iprofile_name'))
        return text

    def get_logout_text(self):
        text = self.pu.get_text(self.pu.get_locator(self.auth_locators, 'Iautorization_icon'))
        return text

    def get_errMsg_text(self):
        text = self.pu.get_text(self.pu.get_locator(self.auth_locators, 'Ierror_message'))
        return text

    def get_valid_text(self):
        text = self.pu.get_text(self.pu.get_locator(self.auth_locators, 'Iprofile_name'))
        return text

    def close_warning(self):
        self.pu.click(self.pu.get_locator(self.auth_locators, 'Iclose_warrning'))
