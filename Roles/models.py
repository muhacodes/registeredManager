from django.db import models

# Create your models here.

class Role(models.Model):

    TYPE_CHOICES = (
        ('contact', 'Contact'),
        ('permanent', 'Permanent'),
        # Add more choices here if needed
    )

    title                           = models.CharField(max_length=250)
    location                        = models.CharField(max_length=250)
    salary                          = models.DecimalField(decimal_places=2,  max_digits=10)
    about                           = models.TextField()
    role_type                       = models.CharField(choices=TYPE_CHOICES, max_length=10)
    info                            = models.TextField()
    created_at                      = models.DateField()    

    def __str__(self):
        return self.title