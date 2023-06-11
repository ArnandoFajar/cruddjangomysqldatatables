from django.shortcuts import render, redirect
from mahasiswa_app.forms import MahasiswaForm
from mahasiswa_app.models import Mahasiswa

# Create your views here.


def index(request):
    mahasiswas = Mahasiswa.objects.all()
    return render(request, "index.html", {'mahasiswas': mahasiswas})


def add(request):
    if request.method == "POST":
        form = MahasiswaForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/')
            except:
                pass
    else:
        form = MahasiswaForm()
    return render(request, "add.html", {'form': form})


def edit(request, id):
    mahasiswa = Mahasiswa.objects.get(id=id)
    return render(request, 'edit.html', {'mahasiswa': mahasiswa})


def update(request, id):
    mahasiswa = Mahasiswa.objects.get(id=id)
    form = MahasiswaForm(request.POST, instance=mahasiswa)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'edit.html', {'mahasiswa': mahasiswa})


def delete(request, id):
    mahasiswa = Mahasiswa.objects.get(id=id)
    mahasiswa.delete()
    return redirect("/")
