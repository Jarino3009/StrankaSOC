from django.shortcuts import render, HttpResponse, redirect
from . models import *
from .forms import TemaForm

def vypis_tem(request):
    temy = Tema.objects.all().order_by("dostupnost")
    return render(request, "soc/index.html", {"temy":temy})

def vypis_temy(request, tema):
    tema = Tema.objects.get(id=tema)
    return render(request, "soc/detail.html", {"tema":tema})

def vypis_ucitela(request, ucitel):
    ucitel = Ucitel.objects.get(id=ucitel)
    temy = Tema.objects.filter(konzultant=ucitel)
    return render(request, "soc/detail.html", {"ucitel":ucitel, "temy":temy})

def vypis_studenta(request, student):
    student = Student.objects.get(id=student)
    temy = Tema.objects.filter(student=student)
    return render(request, "soc/detail.html", {"student":student, "temy":temy})

def statistics(request):
    cakajuce = Tema.objects.filter(dostupnost=2).count()
    volne = Tema.objects.filter(dostupnost=1).count()
    schvalene = Tema.objects.filter(dostupnost=3).count()
    
    pocet_tem = Tema.objects.count()
    pocet_ucitelov = Ucitel.objects.count() 
    pocet_studentov = Student.objects.count()
    return render(request, "soc/statistics.html", {"cakajuce":cakajuce, "volne":volne, "schvalene":schvalene, "pocet_tem":pocet_tem, "pocet_ucitelov":pocet_ucitelov, "pocet_studentov":pocet_studentov})

def pridat_temu(request):
    if request.method == 'POST':
        form = TemaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pridat_temu')
    else:
        form = TemaForm()
    
    return render(request, 'soc/pridat_temu.html', {'form': form})

def tema_list(request):
    temy = Tema.objects.all()

    odbory = Odbor.objects.all()
    ucitelia = Ucitel.objects.all()
    dostupnosti = Dostupnost.objects.all()

    odbor_id = request.GET.get('odbor')
    if odbor_id:
        temy = temy.filter(odbor_id=odbor_id)

    konzultant_id = request.GET.get('konzultant')
    if konzultant_id:
        temy = temy.filter(konzultant_id=konzultant_id)

    dostupnost_id = request.GET.get('dostupnost')
    if dostupnost_id:
        temy = temy.filter(dostupnost_id=dostupnost_id)

    context = {
        'temy': temy,
        'odbory': odbory,
        'ucitelia': ucitelia,
        'dostupnosti': dostupnosti,
    }
    return render(request, 'soc/index.html', context)