from django.shortcuts import render, HttpResponse
from .models import Short, Category
# Create your views here.
def homepage(request):
    return render(request,"home.html")

def contacts(request):
    return HttpResponse("Наши контакты!")

def about_us(request):
    return HttpResponse("Информация о нас!")

def shorts(request):
    context={}
    short=Short.objects.all()
    context['shorts'] = short
    return render(request,"shorts.html",context)

def short_info(request,id):
    context={}
    context['short'] = Short.objects.get(id=id)
    return render(request,"short.html",context)

def Categories(request):
    context={}
    context['categories']=Category.objects.all()
    return render(request,"categories.html",context)

def Category_info(request,id):
    context={}
    context['category']=Category.objects.get(id=id)
    return render(request,"category.html",context)

# def video(request,id):
#     return Short.objects.video.get(id=id)