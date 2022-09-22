
from re import T
from django.shortcuts import render,redirect
from django.shortcuts import render
from django.shortcuts import render,HttpResponse,redirect
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from Tickets.models import Ticket, Category, SubCategory
from django.shortcuts import render, redirect
from Login.models import Profile
from json import dumps


# Create your views here.


# def dashboard(request):
#     return render(request,"dashboard.html")


class all_tickets(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'alltickets.html'


    def get(self, request):
        # queryset = Ticket.objects.all().values()#[::-1][:10]
        queryset = Ticket.objects.all()[::-1]
        # profile = Profile.objects.get(id=id)
        status_set_processingandclosed = Ticket.ticket_status[1:] #Ticket.objects.filter(status=True).all()
        status_set_closed = Ticket.ticket_status[2:]
        print(status_set_processingandclosed)
        print(status_set_closed)
        # print(queryset[0].status)
        # for x in status_set:
        #     print(x[0])
        return render(request,'alltickets.html',{'list': queryset,'statusprocessingandclosed':status_set_processingandclosed,'statusclosed':status_set_closed})

    def post(self,request,id):
        ticket = Ticket.objects.get(id=id)
        changed_status = request.POST['changedstatus']
        print(ticket.status)
        Ticket.objects.filter(id=id).update(status=changed_status)
        print('changed_status')
        # return render(request,'alltickets.html',{'id': id})
        return redirect('/alltickets')

class dashboard(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'dashboard.html'


    def get(self, request):
        queryset = Ticket.objects.all().values()[::-1][:10]
        status_set = Ticket.objects.all().values('status')
        print(status_set)
        number = {'raised':0,'processing':0,'closed':0}
        for y in status_set:
            if y['status'] == 'raised':
                number['raised'] += 1
            elif y['status'] == 'processing':
                number['processing'] += 1
            elif y['status'] == 'closed':
                number['closed'] += 1
        print(number)
        # for x in status_set:
        #     print(x)
        return render(request,'dashboard.html',{'list': queryset,'value_count':number})

