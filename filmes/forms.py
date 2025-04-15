from django import forms
from filmes.models import Genero, Filme  

class FilmeForm(forms.Form):
    titulo = forms.CharField(max_length=100)
    sinopse = forms.CharField(widget=forms.Textarea)
    duracao = forms.IntegerField()
    ano = forms.IntegerField()
    genero = forms.ModelChoiceField(Genero.objects.all())
    diretor = forms.CharField(max_length=100)  
    atores = forms.CharField(max_length=100)
    poster = forms.ImageField()

    def save(self):       
        filme = Filme(
            titulo=self.cleaned_data['titulo'],
            sinopse=self.cleaned_data['sinopse'],
            duracao=self.cleaned_data['duracao'],
            ano=self.cleaned_data['ano'],
            genero=self.cleaned_data['genero'],
            diretor=self.cleaned_data['diretor'],
            atores=self.cleaned_data['atores'],
            poster=self.cleaned_data['poster']
        )
        filme.save()
        return filme