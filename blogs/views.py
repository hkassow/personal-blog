from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views import generic
from .models import Post

from rest_framework import viewsets
from .serializer import PostSerializer
# Create your views here.


# def HomeView(request):
#     return render(request, 'blogs/home.html')


# class DetailView(generic.DetailView):
#     model = Post
#     template_name ='blogs/detail.html'

class PostView(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()

from email.message import EmailMessage
import smtplib, ssl
import environ
env = environ.Env()
environ.Env.read_env()

def emailFunction(request):
    result = 'email function called'

    # creating message content 
    msg = EmailMessage()
    msg['Subject'] = 'test subject'
    msg['From'] = env('email_from')
    msg['To'] = 'hunterkassow@protonmail.com'
    msg.set_content('test_content')
    
    print(msg)
    # connecting to gmail server and sending message
    context=ssl.create_default_context()
    with smtplib.SMTP('smtp.gmail.com', port=587) as smtp:
    
        smtp.starttls(context=context)
        smtp.ehlo()
        smtp.login(msg['From'], env('email_pass'))
        smtp.send_message(msg)
        smtp.quit()

    

    return HttpResponse(result)