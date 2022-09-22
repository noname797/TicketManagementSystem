from django.shortcuts import render,HttpResponse,redirect
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from Tickets.models import Ticket, Category, SubCategory
from Login.models import Profile
from json import dumps

# Create your views here.
class raiseReq(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'raiseReq.html'
    
    def get(self, request, id):
        categories = Category.objects.all()
        profile = Profile.objects.get(id=id)
        #name = profile.name
        #ps_no = profile.ps_number

        data_dict = {}
        for category in categories:

            sub_categ = SubCategory.objects.all().filter(category=category).values()
            items = []

            for i in sub_categ:
                items.append(i['subcategory'])
            
            data_dict[category.category] = items
            # items = []

            # items.append(str(dict(categories)['category']))

            # data_dict[category] = items
        
        categories = dumps(data_dict)
        

        

        # sub = {}
        # for i in categ:
        #     sub_categ = SubCategory.objects.all().filter(category=i).values()
        #     sub[i] = sub_categ
        # print(sub)

        context = {
            'id':id,
            'categories':categories,
            'profile':profile,
        }
        return render(request,"raiseReq.html",context)
    
    def post(self, request, id):
        category = request.POST['categories']
        sub_category = request.POST['sub_categories']
        description = request.POST['reason'] 
        profile = Profile.objects.get(id=id)
        tic = Ticket(user_id=profile,status='raised',category=category, subCategory=sub_category, description=description)
        tic.save()
        details = Ticket.objects.all().filter(user_id=id)
        return render(request,"history.html",{'id':id, 'list':details})



    



def reset(request):
    return redirect("/")

class user_history(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'history.html'


    def get(self, request, id):
        queryset = Ticket.objects.all().filter(user_id=id).values()
        # print(queryset[0])
        return render(request,"history.html",{'list': queryset, 'id':id})