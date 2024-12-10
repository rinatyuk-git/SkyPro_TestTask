from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    """ Creation of users """
    def handle(self, *args, **kwargs):
        user_list = [
            {'email': 'user1@mail.com',
             'password': 'User1_1resU',
             'phone': '+36524895247',
             'city': 'Berlin'},
            {'email': 'user2@mail.com',
             'password': 'User2_2resU',
             'phone': '+985412575',
             'city': 'Milano'},
            {'email': 'user3@mail.com',
             'password': 'User3_3resU',
             'phone': '+12584966477',
             'city': 'Orlando'},
        ]
        users_for_create = []
        for item in user_list:
            users_for_create.append(
                User(**item)
            )
        User.objects.bulk_create(users_for_create)
