from django.shortcuts import redirect, render
from django.core.exceptions import ObjectDoesNotExist



from .forms.plat_form import PlatForm
from .models.plats_model import PlatModel

# Create your views here.


def list_plat(request):
    plats = PlatModel.objects.all()
    plats_count = PlatModel.objects.all().count()

    context = {
        'plats': plats,
        'number_plat' : plats_count
    }
    return render(request, 'plats/plats.html', context)

def add_plat(request):
    plat_form = PlatForm()
    
    if request.method == 'POST':
        plat_form = PlatForm(request.POST)
        if plat_form.is_valid():
            plat_form.save()
            return redirect('plat:list_plat') 
        
    context = {
        'title': 'Ajouter un plat',
        'form': plat_form
    }
    return render(request, 'plats/forms.html',context)

def update_plat(request, id):
    context = {
        "title": 'Modifier un Plat'
    }
    try:
        plat = PlatModel.objects.get(id=id)
    except ObjectDoesNotExist:
        print(f"Plat does not exist !!")
        return redirect('plat:list_plat')
    
    if request.method == 'POST':
        plat_form = PlatForm(data=request.POST, instance=plat)
        if plat_form.is_valid():
            plat_form.save()
            return redirect('plat:list_plat')
    plat_form = PlatForm(instance=plat)
    context["form"] = plat_form

    return render(request, 'plats/forms.html', context)

def delete_plat(request, id):
    try:
        plat = PlatModel.objects.get(id=id)
    except ObjectDoesNotExist:
        print(f"Plat does not exist !!")
        return redirect('plat:list_plat')
    
    plat.delete()
    return redirect('plat:list_plat')

def search_plat(request):
    name_search = request.GET.get('name')
    results = []

    if name_search:
        results = PlatModel.objects.filter(name__icontains=name_search) 

    context = {
        'results': results,
        'query': name_search
    }
    return render(request, 'plats/plats.html', context)
