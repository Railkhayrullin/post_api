from django.core.management.base import BaseCommand
from django.contrib.auth.models import User


class Command(BaseCommand):
    """Команда для создания тестового суперпользователя"""
    def handle(self, *args, **options):
        User.objects.create_superuser(username='test_admin', email='test_admin@gmail.com', password='test_admin')
        print('Admin account create.')
