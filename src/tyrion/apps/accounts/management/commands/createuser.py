from django.core.mail import send_mail
from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from django.contrib.auth.models import UserManager, User
from django.contrib.sites.models import Site
from django.template.loader import render_to_string

from userena.models import UserenaSignup
from userena.utils import get_protocol
from userena import settings as userena_settings
from userena import signals as userena_signals

import hashlib
import random
import sys

class Command(BaseCommand):
    args = '<email1> <email2> ...'
    help = 'Creates a new user with the given email'

    def handle(self, *args, **options):
        for email in args:
            if User.objects.filter(email__iexact=email):
                sys.stderr.write("User with email %s already exists. Skipping.\n" % email)
                continue

            while True:
                username = hashlib.sha1(email).hexdigest()[:16]
                try:
                    User.objects.get(username__iexact=username)
                except User.DoesNotExist: break

            # create user
            new_user = UserenaSignup.objects.create_user(username,
                                                         email,
                                                         hashlib.sha1(str(random.random())).hexdigest(),
                                                         active=False,
                                                         send_email=False)

            # send activation email
            context = {'user': new_user,
                'without_usernames': userena_settings.USERENA_WITHOUT_USERNAMES,
                'protocol': get_protocol(),
                'activation_days': userena_settings.USERENA_ACTIVATION_DAYS,
                'activation_key': new_user.userena_signup.activation_key,
                'site': Site.objects.get_current()}

            subject = render_to_string('emails/activation_subject.txt', context)
            subject = ''.join(subject.splitlines())

            body = render_to_string('emails/activation_body.txt', context)

            send_mail(subject,
                body,
                settings.DEFAULT_FROM_EMAIL,
                [new_user.email,])

            self.stdout.write("Created user for %s\n" % email)
