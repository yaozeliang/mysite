from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'personal_portfolio/home.html',{'title':'Home'})

def about(request):
    return render(request,'personal_portfolio/about.html',{'title':'About'})

def resume(request):
    return render(request,'personal_portfolio/resume.html',{'title':'Resume'})

def gallery(request):
    return render(request,'personal_portfolio/gallery.html',{'title':'Portfolio'})


def article(request):
    return render(request,'personal_portfolio/article.html',{'title':'Article'})


def contact(request):
    return render(request,'personal_portfolio/contact.html',{'title':'Contact'})



