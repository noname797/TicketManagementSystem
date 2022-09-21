from django.shortcuts import render,HttpResponse,redirect
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from Tickets.models import Ticket, Category, SubCategory
from Login.models import Profile

# Create your views here.
class raiseReq(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'raiseReq.html'
    
    def get(self, request, id):
        categ = Category.objects.all()
        profile = Profile.objects.get(id=id)
        #name = profile.name
        #ps_no = profile.ps_number
        sub = {}
        for i in categ:
            sub_categ = SubCategory.objects.all().filter(category=i)
            sub[i] = sub_categ
        print(sub)
        return render(request,"raiseReq.html",{'id':id, 'categ':sub, 'profile':profile})


class create_ticket(APIView):
    enderer_classes = [TemplateHTMLRenderer]
    template_name = 'raiseReq.html'
    
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
        queryset = Ticket.objects.all().filter(user_id=id)
        print(queryset)
        return render(request,"history.html",{'list': queryset, 'id':id})