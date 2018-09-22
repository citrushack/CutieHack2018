from django.db import models
from django.contrib.auth.models import ( #to use emails as id instead of username, we have to extend the user model
    BaseUserManager, AbstractBaseUser
)
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here. 
# modified https://docs.djangoproject.com/en/2.1/topics/auth/customizing/#specifying-custom-user-model
class MyUserManager(BaseUserManager):
    def create_user(self, email, password=None): #date_of_birth,
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            #date_of_birth=date_of_birth,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password): #date_of_birth,
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            password=password,
            #date_of_birth=date_of_birth,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    #date_of_birth = models.DateField()
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [] #'date_of_birth'

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return False

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return False

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin

class Profile(models.Model):
    user = models.OneToOneField(MyUser, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    age = models.CharField(max_length=30,null=True, blank=True) # change to age
    school = models.CharField(max_length=100, blank=True)
    major = models.CharField(max_length=30, blank=True)
    #appStatus = Pending default
    #need to check what is missing from here
    #email_confirmed = models.BooleanField(default=False)
    phoneNumber = models.CharField(max_length=12, blank=True)
    genderOptions = (("a", "male"), ('b', 'female'), ("c", "Other"), ("d", "Prefer not to disclose"), )
    Gender = models.CharField(max_length=30, choices=genderOptions, default="")
    raceOptions = (('a', 'White'), ('b','Black or African American'), ('c', 'Native American'), ('d', 'Asian'), ('e','Native Hawaiian or other Pacific Islander'), ('f','Latino or Latin American'), ('g','Other'), ('h', 'Two or more races'), ('i', 'Prefer not to disclose'), )
    Race = models.CharField(max_length=30, choices=raceOptions, default="")
    studyOptions = (
      ("a", "1st Year"),
      ("b", "2nd Year"),
      ("c", "3rd Year"),
      ("d", "4th Year"),
      ("e", "5th Year or beyond"),
      ("f", "Prefer not to disclose"),
      )
    LevelofStudy = models.CharField(max_length=30, choices=studyOptions, default="")
    yearOptions = (
      ("a", "2019"),
      ("b", "2020"),
      ("c", "2021"),
      ("d", "2022"),
      ("e", "2023"),
      ("f", "2024"),
      ("g", "2025"),
      )
    gradYear = models.CharField(max_length=30, choices=yearOptions, default="")
    dietRestrictions = models.CharField(max_length=100, default="")
    Resume = models.FileField(default="")
    conductBox = models.BooleanField(default=False)
    shareBox = models.BooleanField(default=False)
    meme = models.CharField(max_length=200, default="")


#might be better to have signal codes somewhere else 
@receiver(post_save, sender=MyUser)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
