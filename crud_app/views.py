from django.shortcuts import render, redirect
from .models import Item

def item_list(request):
    items = Item.objects.all()
    return render(request, 'crud_app/item_list.html', {'items': items})

def item_create(request):
    if request.method == 'POST':
        name = request.POST['name']
        description = request.POST['description']
        Item.objects.create(name=name, description=description)
        return redirect('item_list')
    return render(request, 'crud_app/item_form.html')

def item_update(request, pk):
    item = Item.objects.get(id=pk)
    if request.method == 'POST':
        item.name = request.POST['name']
        item.description = request.POST['description']
        item.save()
        return redirect('item_list')
    return render(request, 'crud_app/item_form.html', {'item': item})

def item_delete(request, pk):
    item = Item.objects.get(id=pk)
    item.delete()
    return redirect('item_list')
