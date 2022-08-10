from django.shortcuts import render, redirect
import uuid
from .models import URL
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html')

def create(request):
    if request.method == 'POST':
        link = request.POST['link']
        uid = str(uuid.uuid4())[:5]
        new_url = URL(link=link, uuid=uid)
        new_url.save()
        return HttpResponse(uid)

def fetch(request, pk):
    url = URL.objects.get(uuid=pk)
    link = url.link
    pre = link[:8]
    if pre != 'https://':
        link = 'https://' + link
    return redirect(link) 