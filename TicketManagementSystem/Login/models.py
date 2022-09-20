from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your models here.

class Profile(models.Model):
    id = models.UUIDField(primary_key=True,editable=False,default=uuid.uuid4)
    ps_number = models.IntegerField( unique=True)
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    def __str__(self):
        return str(self.ps_number)

    # class Meta:
    #     abstract = True