from django.http import HttpResponse
from django.template import loader

from django.shortcuts import render

from aurora_application.models import IMG

# Create your views here.
def index(request):
    # template = loader.get_template('templates/aurora_main.html')
    return render(request, 'aurora_main.html')


def upload(request):
    # if request.method == 'POST':
    #     img = IMG(img_url=request.FILES.get('img'))
    #     img.save()
    return render(request, 'upload.html')

def show(request):
    new_img = IMG(img=request.FILES.get('img'))
    new_img.save()
    content = {
        'aaa': new_img,
    }
    return render(request, 'show.html', content)

def contact(request):
    return render(request, "contact.html")