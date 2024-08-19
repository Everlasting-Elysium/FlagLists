from . import models
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
# Create your views here.
def home_page(request):
    if request.method == 'POST':
        new_item_text = request.POST.get('item_text')
        models.Item.objects.create(text=new_item_text)
        return redirect("/")
    else:
        new_item_text = ''

    items = models.Item.objects.all()
    return render(request, 'home.html', {'items': items})