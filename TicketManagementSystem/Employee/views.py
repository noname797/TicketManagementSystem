from django.shortcuts import render,HttpResponse,redirect
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from Tickets.models import Ticket

# Create your views here.

def raiseReq(request):
    return render(request,"raiseReq.html")

def reset(request):
    return redirect("/")

class user_history(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'history.html'


    def get(self, request):
        id=1
        #print(Ticket.objects.all())
        queryset = Ticket.objects.all().filter(user_id=id)
        
        #queryset = Ticket.objects.all()
        print(queryset)
        #return Response()
        return render(request,"history.html",{'list': queryset, 'id':id})