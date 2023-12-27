from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import News
from .forms import NewsForm

# Create your views here.
def index(request):
    context = News.objects.all()
    return render(request, "newsletter/homepage.html", {"context": context})

def info(request,id):
    context = News.objects.get(id=id)
    return render(request,"newsletter/info.html",{"context": context})

def update(request,id):
    news = News.objects.get(id=id)
    form = NewsForm(request.POST or None, request.FILES,instance=news)
    if form.is_valid():
        form.save()
        return redirect('/')


    #pending

    return render(request, "newsletter/update.html",{"form":form})

def delete(request,id):
    if request.method == "POST":
        obj = News.objects.get(id=id)
        News.delete(obj)
        return redirect('/')

    return render(request,"newsletter/delete.html")

def detail(request):
    if request.method == "POST":
        username = request.POST.get("username")
        title = request.POST.get("title")
        description = request.POST.get("description")
        image = request.FILES["image"]
        date = request.POST.get("date")
        print(username)
        obj = News(username=username,title = title, description= description, image=image, date=date)
        obj.save()

        return redirect('/')

    return render(request,"newsletter/details.html")