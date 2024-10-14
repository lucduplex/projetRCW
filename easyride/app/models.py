from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    cell = models.CharField(max_length=15)
    address = models.CharField(max_length=255)
    face_id = models.ImageField(upload_to='face_ids/', blank=True, null=True)

    # Ajoute related_name pour éviter les conflits
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_set',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        verbose_name='groups'
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_set',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions'
    )

    REQUIRED_FIELDS = ['email', 'cell']

    def __str__(self):
        return self.username
