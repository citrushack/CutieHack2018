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
    date_of_birth = models.DateField(null=True, blank=True) # change to age
    school = models.CharField(max_length=100, blank=True)
    major = models.CharField(max_length=30, blank=True)
    # Hey Jerry! Thanks!! Write below
    #phone number
    #gender
    #race/ethnicity
    #current level of study
    #expected year of graduation
    #code of conduct boolean
    #data sharing boolean
    #dietary restriction
    #resume
    #link to a meme
    #application status default to Pending

#might be better to have signal codes somewhere else 
@receiver(post_save, sender=MyUser)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
