from django.shortcuts import redirect, render
from django.core.exceptions import ObjectDoesNotExist



from .forms.menu_form import MenuForm
from .models.menu_models import MenuModel

# Create your views here.


def list_menu(request):
    menus = MenuModel.objects.all()
    menu_count = MenuModel.objects.all().count()
    context = {
        'menus': menus,
        'number' : menu_count,
    }
    return render(request, 'menu/menus.html', context)

def add_menu(request):
    menu_form = MenuForm()
    
    if request.method == 'POST':
        menu_form = MenuForm(request.POST)
        if menu_form.is_valid():
            menu_form.save()
            return redirect('menu:list_menu')
        
    context = {
        'title': 'Ajouter un menu',
        'form': menu_form
    }
    return render(request, 'menu/forms.html',context)

def update_menu(request, id):
    context = {
        "title": 'Modifier un Menu'
    }
    try:
        menu = MenuModel.objects.get(id=id)
    except ObjectDoesNotExist:
        print(f"Menu does not exist !!")
        return redirect('menu:list_menu')
    
    if request.method == 'POST':
        menu_form = MenuForm(data=request.POST, instance=menu)
        if menu_form.is_valid():
            menu_form.save()
            return redirect('menu:list_menu')
    menu_form = MenuForm(instance=menu)
    context["form"] = menu_form

    return render(request, 'menu/forms.html', context)

def delete_menu(request, id):
    try:
        menu = MenuModel.objects.get(id=id)
    except ObjectDoesNotExist:
        print(f"Menu does not exist !!")
        return redirect('menu:list_menu')
    
    menu.delete()
    return redirect('menu:list_menu')

def search_menu(request):
    name_search = request.GET.get('name')
    results = []

    if name_search:
        results = MenuModel.objects.filter(name__icontains=name_search) 

    context = {
        'results': results,
        'query': name_search
    }
    return render(request, 'menu/menus.html', context)