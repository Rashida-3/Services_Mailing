from django.shortcuts import render
# from django.http import HttpResponse
from django.core.mail import send_mail



# Create your views here.

def index(request):
    return render(request,'index.html')


def homepage(request):
    send_mail(
    "Testing Mail",
    "thanky for showing intrest !.",
    "rashidamcc123@gmail.com",
    ["rashidaansari0123@gmail.com"],
    fail_silently=False,
)