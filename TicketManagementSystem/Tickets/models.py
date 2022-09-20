from unicodedata import category
from django.db import models
import uuid
from Login.models import Profile
from django.utils.text import slugify
# from .models import Category,SubCategory
# Create your models here.


class Category(models.Model):
    category= models.CharField(max_length=100)
    slug=models.SlugField(unique=True, null=True, blank= True)

    def save(self, *args,**kwargs):
        self.slug =slugify(self.category)
        super(Category, self).save(*args,**kwargs)

    def __str__(self):
        return self.category   


class SubCategory(models.Model):
    subcategory= models.CharField(max_length=100)
    category= models.ForeignKey(Category,related_name='category_sub',on_delete=models.CASCADE)
    slug=models.SlugField(unique=True, null=True, blank= True)

    def save(self, *args,**kwargs):
        self.slug =slugify(self.subcategory)
        super(SubCategory, self).save(*args,**kwargs)

    def __str__(self):
        return self.subcategory +"under" + self.category.category


class Ticket(models.Model):
    ticket_status = [
    ('Raised', 'Raised'),
    ('processing', 'processing'),
    ('closed', 'closed'),
]
    ticket_id = models.UUIDField(primary_key=True,editable=False,default=uuid.uuid4)
    user_id = models.ForeignKey(Profile,related_name='user',on_delete=models.CASCADE)
    status = models.CharField(max_length=100,choices=ticket_status)
    category = models.ForeignKey(Category,related_name='categoryT',on_delete=models.CASCADE) # in case future error arises convert it to char field
    subCategory = models.ForeignKey(SubCategory,related_name='subcategoryT',on_delete=models.CASCADE)
    description = models.TextField()

    def save(self, *args,**kwargs):
        # self.slug =slugify (self.product_name)
        super(Ticket, self).save(*args,**kwargs)

    def __str__(self):
        return str(self.status + " ticket ID:  " + str(self.ticket_id) + " from PS no. :" + str(self.user_id.ps_number))

