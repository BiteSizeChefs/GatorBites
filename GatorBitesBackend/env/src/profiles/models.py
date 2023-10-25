# profiles/models.py
from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from .utils import get_random_code

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(max_length=200, blank=False)

    first_name = models.CharField(max_length=200, blank=True)
    last_name = models.CharField(max_length=200, blank=True)
    location = models.CharField(max_length=200, blank=True)
    bio = models.TextField(default="no bio set", max_length=300)
    avatar = models.ImageField(default='avatar.png', upload_to='avatars/')
    friends = models.ManyToManyField(User, blank=True, related_name='friends')
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True, blank=True)

    def __str__(self):
        return f"{self.user.username}-{self.created.strftime('%d-%m-%Y')}"
    
    def get_email(self):
        return f"{self.user.email}"

    def get_friends(self):
        return self.friends.all()

    def get_friends_no(self):
        return self.friends.all().count()

    def fullName(self):
        return "%s %s" % (self.first_name, self.last_name)

    def get_calendars_no(self):
        return self.calendars.all().count()

    def get_calendars(self):
        return self.calendars.all()

    def save(self, *args, **kwargs):
        ex = False
        if self.first_name and self.last_name:
                to_slug = slugify(str(self.first_name) + " " + str(self.last_name))
                ex = Profile.objects.filter(slug=to_slug).exists()
                while ex:
                    to_slug = slugify(to_slug + " " + str(get_random_code()))
                    ex = Profile.objects.filter(slug=to_slug).exists()
        else:
            to_slug = str(self.user)
        self.slug = to_slug
        super().save(*args, **kwargs)

class Relationship(models.Model):
    class StatusType(models.TextChoices):
        SENT = "sent"
        ACCEPTED = "accepted"
        # DECLINED = "declined"

    sender = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='sender')
    receiver = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='receiver')
    status = models.CharField(max_length=8, choices=StatusType.choices)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.sender}-{self.receiver}-{self.status}"