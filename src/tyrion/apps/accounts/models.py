from django.contrib.auth.models import User
from django.db import models
from userena.models import UserenaBaseProfile


class UserProfile(UserenaBaseProfile):
    user = models.OneToOneField(User,
                                unique=True,
                                verbose_name="User",
                                related_name='tyrion_profile')
