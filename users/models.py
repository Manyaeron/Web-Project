from django.db import models
from django.core.validators import RegexValidator


class UserProfile(models.Model):    
    
    POSITIONS = (
    (0, "Choose an option"),
    (1, "Technical Head ACM"),
    (2, "Technical Head ACM-W"),
    (3, "Webmaster ACM"),
    (4, "Webmaster ACM-W"),
    (5, "Events Head ACM"),
    (6, "Events Head ACM-W"),
    (7, "PR Head ACM"),
    (8, "PR Head ACM-W"),
    (9, "Design Head ACM"),
    (10, "Design Head ACM-W"),
    (11, "Editorial Head ACM"),
    (12, "Editorial Head ACM-W")    
    )
 
    name = models.CharField(max_length=35)
   # last_name = models.CharField(max_length=35)
    position = models.IntegerField( choices=POSITIONS, default= 0)
    email = models.CharField(max_length=50, )
    contact_number = models.CharField(max_length=10, validators=[RegexValidator(regex='^.{10}$', message='Enter a 10 digit mobile number', code='nomatch')], )
    whatsapp_number = models.CharField(max_length=10, validators=[RegexValidator(regex='^.{10}$', message='Enter a 10 digit mobile number', code='nomatch')], )
  

    
    def __str__(self):
        return self.name
    