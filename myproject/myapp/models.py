from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profile_pics',
                              default='profile_pics/default.jpeg')

    def __str__(self):
        return f'{self.user.username} Profile'


class UserBio(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    f_name = models.CharField(max_length=50)
    l_name = models.CharField(max_length=50)
    dob = models.CharField(max_length=10)
    phone = models.CharField(max_length=14)
    gender = models.CharField(max_length=10)
    country = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.user.username} Bio'


class UserPost(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.TextField(max_length=100)
    image = models.ImageField(upload_to='users_post', default=None)

    def __str__(self):
        return f'{self.user.username} Post'


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, created, **kwargs):
    if created:
        UserBio.objects.create(user=instance)
