from django.shortcuts import render


def about(request):

    return render(request,'songlab/about.html')

def index(request):

    return render(request,'songlab/index.html')

def contact(request):

    return  render(request,'songlab/contact.html')

def services(request):

    return render(request,'songlab/services.html')