from django import forms
from mahasiswa_app.models import Mahasiswa


class MahasiswaForm(forms.ModelForm):
    class Meta:
        model = Mahasiswa
        fields = ['name', 'contact', 'email']
