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
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

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
    appStatus = models.CharField(max_length=30, default ="Pending")
    #need to check what is missing from here
    #email_confirmed = models.BooleanField(default=False)
    phoneNumber = models.CharField(max_length=12, blank=True)
    genderOptions = (
      ("Female", "Female"),
      ("Male", "Male"),  
      ("Other", "Other"), 
      ("Prefer not to disclose", "Prefer not to disclose"),
      )
    Gender = models.CharField(max_length=30, choices=genderOptions, blank=True)
    raceOptions = (
      ('Asian', 'Asian'), 
      ('Black or African American','Black or African American'), 
      ('Latino or Latin American','Latino or Latin American'), 
      ('Native American', 'Native American'),  
      ('Native Hawaiian or other Pacific Islander','Native Hawaiian or other Pacific Islander'), 
      ('Other','Other'),
      ('Prefer not to diclose', 'Prefer not to disclose'),
      ('Two or more races', 'Two or more races'), 
      ('White', 'White'), 
      )
    Race = models.CharField(max_length=30, choices=raceOptions, blank=True)
    studyOptions = (
      ("1st Year", "1st Year"),
      ("2nd Year", "2nd Year"),
      ("3rd Year","3rd Year"),
      ("4th Year", "4th Year"),
      ("5th Year or beyond", "5th Year or beyond"),
      ("Prefer not to disclose", "Prefer not to disclose"),
      )
    LevelofStudy = models.CharField(max_length=30, choices=studyOptions, default="")
    yearOptions = (
      ("2019", "2019"),
      ("2020", "2020"),
      ("2021", "2021"),
      ("2022", "2022"),
      ("2023", "2023"),
      ("2024", "2024"),
      ("2025", "2025"),
      )
    gradYear = models.CharField(max_length=30, choices=yearOptions, default="")
    dietRestrictions = models.CharField(max_length=100, default="")
    Resume = models.FileField(default="", upload_to='uploads/')
    conductBox = models.BooleanField(default=False)
    shareBox = models.BooleanField(default=False)
    meme = models.CharField(max_length=200, blank=True)


#might be better to have signal codes somewhere else 
@receiver(post_save, sender=MyUser)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
