from django import forms
from .models import *


class weworkForm(forms.ModelForm):
    class Meta:
        model = tbWework
        fields = ['wework', 'weworkQuantAndares','weworkAndares','weworkCondominio','weworkSdai','clienteCidade']
        widgets ={
            'wework': forms.TextInput(attrs={'class': 'form-control'}),
            'weworkQuantAndares': forms.TextInput(attrs={'class': 'form-control'}),
            'weworkAndares': forms.TextInput(attrs={'class': 'form-control'}),
            'weworkCondominio': forms.TextInput(attrs={'class': 'form-control'}),
            'weworkSdai': forms.Select(attrs={'class': 'form-control'}),
            'clienteCidade': forms.Select(attrs={'class': 'form-control'}),
        }

class SapForm(forms.ModelForm):
    class Meta:
        model = tbSapScirp
        fields = ['quadroSap', 'gerenciadora', 'statusSap','quantidadeControladoras','quadroIluminacao','atualizacao', 'observacoesSap']
