from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'users'
# import user signal in the ready function

    def ready(self):
        import users.signals
