import re

from django.core.cache import cache

from django_auth_ldap.backend import LDAPBackend


class CustomLDAPBackend(LDAPBackend):
    default_settings = {
        "LOGIN_COUNTER_KEY": "CUSTOM_LDAP_LOGIN_ATTEMPT_COUNT",
        "LOGIN_ATTEMPT_LIMIT": 50,
        "RESET_TIME": 30 * 60,
        "USERNAME_REGEX": r"^.*$",
    }

    def authenticate_ldap_user(self, ldap_user, password):
        if self.exceeded_login_attempt_limit():
            # Or you can raise a 403 if you do not want
            # to continue checking other auth backends
            print("Login attempts exceeded.")
            return None
        self.increment_login_attempt_count()
        user = ldap_user.authenticate(password)
        if user and self.username_matches_regex(user.username):
            self.send_sms(user.username)
        return user

    @property
    def login_attempt_count(self):
        return cache.get_or_set(
            self.settings.LOGIN_COUNTER_KEY, 0, self.settings.RESET_TIME
        )

    def increment_login_attempt_count(self):
        try:
            cache.incr(self.settings.LOGIN_COUNTER_KEY)
        except ValueError:
            cache.set(self.settings.LOGIN_COUNTER_KEY, 1, self.settings.RESET_TIME)

    def exceeded_login_attempt_limit(self):
        return self.login_attempt_count >= self.settings.LOGIN_ATTEMPT_LIMIT

    def username_matches_regex(self, username):
        return re.match(self.settings.USERNAME_REGEX, username)

    def send_sms(self, username):
        # Implement your SMS logic here
        print("SMS sent!")