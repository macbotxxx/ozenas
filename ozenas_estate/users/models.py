from django.contrib.auth.models import AbstractUser
from django.db.models import CharField, EmailField
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from django.contrib.auth.base_user import BaseUserManager
from django.db import models
from django.utils import timezone
from helper.common.basemodel import BaseModel
from ozenas_estate.users.managers import UserManager

NULL_AND_BLANK = {'null': True, 'blank': True}



class UserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError(_('The given email must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """Create and save a regular User with the given email and password."""
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))

        return self._create_user(email, password, **extra_fields)




class User(AbstractUser):
    """
    Default custom user model for xploit.
    If adding fields that need to be filled at user signup,
    check forms.SignupForm and forms.SocialSignupForms accordingly.
  
    # Each `User` needs a human-readable unique identifier that we can use to
    # represent the `User` in the UI. We want to index this column in the
    # database to improve lookup performance.
    username = models.CharField(db_index=True, max_length=255, unique=True)

    # We also need a way to contact the user and a way for the user to identify
    # themselves when logging in. Since we need an email address for contacting
    # the user anyways, we will use it for logging in because it is
    # the most common form of login credential at the time of writing.
    email = models.EmailField(db_index=True, unique=True)

    # When a user no longer wishes to use our platform, they may try to delete
    # there account. That's a problem for us because the data we collect is
    # valuable to us and we don't want to delete it. To solve this problem, we
    # will simply offer users a way to deactivate their account.
    # That way they won't show up on the site anymore,
    # but we can still analyze the data.
    is_active = models.BooleanField(default=True)

    # The `is_staff` flag is expected by Django to determine who can and cannot
    # log into the Django admin site. For most users this flag will always be
    # falsed.
    is_staff = models.BooleanField(default=False)
    """

    # First and last name do not cover name patterns around the globe
    name = CharField(_("Name of User"), blank=True, max_length=255)
    first_name = None  # type: ignore
    last_name = None  # type: ignore
    email = models.EmailField(
        max_length=150,
        null=True,
        unique=True,
        verbose_name=_("Email Address"),
        help_text=_("The email address of the customer.")
    )
    username = None  # type: ignore
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()

    created_date = models.DateTimeField(
        default=timezone.now,
        editable=False,
        verbose_name=_('Created'),
        help_text=_(
            """Timestamp when the record was created. The date and time 
            are displayed in the Timezone from where request is made. 
            e.g. 2019-14-29T00:15:09Z for April 29, 2019 0:15:09 UTC"""
        )
    )

    account_key = models.CharField(
        verbose_name=_("Account Key"),
        max_length=150,
        null=True,
        unique=True,
        help_text=_("The stores the account hash key")
    )

    modified_date = models.DateTimeField(
        auto_now=True,
        editable=False,
        verbose_name=_('Updated'),
        **NULL_AND_BLANK,
        help_text=_(
            """Timestamp when the record was modified. The date and 
            time are displayed in the Timezone from where request 
            is made. e.g. 2019-14-29T00:15:09Z for April 29, 2019 0:15:09 UTC
            """)
    )

    def get_absolute_url(self) -> str:
        """Get URL for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("users:detail", kwargs={"pk": self.id})
    
    class Meta:
        ordering = ('-created_date',)
        verbose_name = _("Users Account")
        verbose_name_plural = _("Users Account")



# class UserLogin(BaseModel):
#     """
#     User login logs details refer to the records of user authentication activities within a system or application. These logs capture information such as the date and time of login, the user's identity, the source of the login (IP address or device information), and any relevant events or actions during the login process.

#     Saving user login logs is crucial for several reasons:

#     # Security Monitoring: By keeping track of user logins, administrators can monitor for any unusual or suspicious activities. Unusual login patterns or multiple failed login attempts may indicate a security threat or unauthorized access.

#     # Audit Trails: User login logs provide a comprehensive audit trail, allowing organizations to trace user activities and comply with regulatory requirements. In regulated industries, such as finance or healthcare, maintaining detailed logs is often a legal necessity.

#     # Incident Investigation: In the event of a security incident or a data breach, user login logs can be invaluable for forensic analysis. They help identify the scope of the incident, track down the source, and understand how the unauthorized access occurred.

#     # Compliance: Many industries and organizations are subject to various data protection and privacy regulations. Saving user login logs helps demonstrate compliance with these regulations, as it provides evidence of security measures and accountability.

#     # User Accountability: Login logs can serve as a deterrent against misuse of user accounts. Knowing that their activities are being logged, users are more likely to adhere to security policies, and in the case of malicious activities, individual accountability can be established.

#     # System Health Monitoring: User login logs can also contribute to monitoring the health and performance of the system. Unusual spikes in login attempts or patterns may indicate technical issues or potential denial-of-service attacks.
#     """

#     r
