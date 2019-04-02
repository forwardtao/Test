from django.shortcuts import render
from .models import Article,Category,Banner,Tui

# Create your views here.
from django.http import  HttpResponse

def index(request):
    # 添加两个变量，并赋值
    tui = Article.objects.filter(tui__id=1)[:3]
    allarticle = Article.objects.all().order_by('-id')
    allcategory = Category.objects.all()
    banner = Banner.objects.filter(is_active=True)[0:4]
    context = {
        'allarticle': allarticle,
        'allcategory': allcategory,
        'banner': banner,
        'tui': tui,
    }
    return render(request, 'tliublog/index.html', context)