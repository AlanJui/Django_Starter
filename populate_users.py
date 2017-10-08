import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_01.settings')

import django
django.setup()

from first_app.models import User
from faker import Faker

fakeGen = Faker()

def populate(N=5):

    for entry in range(N):
        fake_name = fakeGen.name().split()
        fake_first_name = fake_name[0]
        fake_last_name = fake_name[1]
        fake_email = fakeGen.email()

        # New entry
        user = User.objects.get_or_create(
            first_name = fake_first_name,
            last_name = fake_last_name,
            email = fake_email
        )[0]

if __name__ == '__main__':
    print('Populating starting......')
    populate(20)
    print('Populating complete!')