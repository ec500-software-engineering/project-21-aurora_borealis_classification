from django.http import HttpResponse
#上面一行最后删
from django.template import loader

from django.shortcuts import render

# Create your views here.
def index(request):
    # template = loader.get_template('templates/aurora_main.html')
    return render(request, 'aurora_main.html')

def uploadImg(request):
    if request.method == 'POST':
        img = Img(img_url=request.FILES.get('img'))
        img.save()
    return render(request, 'imgUpload.html')

def showImg(request):
    imgs = Img.objects.all()
    context = {
        'imgs' : imgs
    }
    return render(request, 'showImg.html', context)