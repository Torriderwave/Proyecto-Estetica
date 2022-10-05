from dataclasses import fields
from socket import fromshare
from django import forms
from .models import Cliente,Mascota,Citas,Producto



class ClienteForm(forms.ModelForm):
    class Meta:
        model=Cliente
        fields='__all__'

class MascotaForm(forms.ModelForm):
    class Meta:
        model=Mascota
        fields='__all__'


class CitaForm(forms.ModelForm):
    class Meta:
        model=Citas
        fields='__all__'


class ProdcutoForm(forms.ModelForm):
    class Meta:
        model=Producto
        fields='__all__'
