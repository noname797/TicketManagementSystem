from rest_framework import serializers

from Tickets.models import Category,SubCategory, Ticket
from Login.models import Profile

class UserSerializer(serializers.ModelSerializer):
   class Meta:
       model = Profile
       fields = ('ps_number', 'name', 'email')


class TicketSerializer(serializers.ModelSerializer):
   class Meta:
       model = Ticket
       fields = ('status','category','subCategory','description','issue_date')


class CategorySerializer(serializers.ModelSerializer):
   class Meta:
       model = Category
       fields = ('category')

class SubcatSerializer(serializers.ModelSerializer):
   class Meta:
       model = SubCategory
       fields = ('subcategory')


