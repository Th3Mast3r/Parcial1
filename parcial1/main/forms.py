from django import forms #llama a forms
from .models import Blogs, Contact, Reviews #tener el punto pegado/por si acaso

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class ContactForm(forms.ModelForm):
    #charfield es string
    name = forms.CharField(max_length=100, required=True, #el true en lo necesario de ingresar algo
        widget=forms.TextInput(attrs={ #lo que vas a escribir es un textinput
            'placeholder': '*Full name..', #placerholder = indicacion del full name que se borra cuando lo seleccionas, a la derecha se pone lo que se quiere ver
             }))
    # se complementa por @ y .com
    email = forms.EmailField(max_length=254, required=True, 
        widget=forms.TextInput(attrs={
            'placeholder': '*Email..',
            }))
    message = forms.CharField(max_length=1000, required=True,
        widget=forms.Textarea(attrs={
            'placeholder': '*Message..',
            'row': 6, #numero de filas en la ventana de texto (mensaje)
            }))
    #clase meta que indica quien va a recibir la informacion
    class Meta:
        model = Contact
        fields = ('name', 'email', 'message',) #al final de cada parametro se pone , por identificador

class BlogForm(forms.ModelForm):

    author = forms.CharField(max_length=200, required=True, #el true en lo necesario de ingresar algo
        widget=forms.TextInput(attrs={ #lo que vas a escribir es un textinput
            'placeholder': '*Author name..', #placerholder = indicacion del full name que se borra cuando lo seleccionas, a la derecha se pone lo que se quiere ver
             }))
    name = forms.CharField(max_length=200, required=True, #el true en lo necesario de ingresar algo
        widget=forms.TextInput(attrs={ #lo que vas a escribir es un textinput
            'placeholder': '*Full name..', #placerholder = indicacion del full name que se borra cuando lo seleccionas, a la derecha se pone lo que se quiere ver
             }))
    description = forms.CharField(max_length=500, required=True, #el true en lo necesario de ingresar algo
        widget=forms.TextInput(attrs={ #lo que vas a escribir es un textinput
            'placeholder': '*Description..', #placerholder = indicacion del full name que se borra cuando lo seleccionas, a la derecha se pone lo que se quiere ver
             }))
    body = forms.CharField(max_length=1000, required=True, #el true en lo necesario de ingresar algo
        widget=forms.Textarea(attrs={ #lo que vas a escribir es un textinput
            'placeholder': '*Info Blog..', #placerholder = indicacion del full name que se borra cuando lo seleccionas, a la derecha se pone lo que se quiere ver
             }))
    image = forms.ImageField()

    class Meta:
        model = Blogs
        fields = ('author','name', 'description', 'body', 'image',) 

class ReviewForm(forms.ModelForm):

    author = forms.CharField(max_length=200, required=True, #el true en lo necesario de ingresar algo
        widget=forms.TextInput(attrs={ #lo que vas a escribir es un textinput
            'placeholder': '*Author name..', #placerholder = indicacion del full name que se borra cuando lo seleccionas, a la derecha se pone lo que se quiere ver
             }))
    title = forms.CharField(max_length=200, required=True, #el true en lo necesario de ingresar algo
        widget=forms.TextInput(attrs={ #lo que vas a escribir es un textinput
            'placeholder': '*Title of Review...', #placerholder = indicacion del full name que se borra cuando lo seleccionas, a la derecha se pone lo que se quiere ver
             }))
    description = forms.CharField(max_length=500, required=True, #el true en lo necesario de ingresar algo
        widget=forms.TextInput(attrs={ #lo que vas a escribir es un textinput
            'placeholder': '*Description..', #placerholder = indicacion del full name que se borra cuando lo seleccionas, a la derecha se pone lo que se quiere ver
             }))
    body = forms.CharField(max_length=1000, required=True, #el true en lo necesario de ingresar algo
        widget=forms.Textarea(attrs={ #lo que vas a escribir es un textinput
            'placeholder': '*Review part...', #placerholder = indicacion del full name que se borra cuando lo seleccionas, a la derecha se pone lo que se quiere ver
             }))
    image = forms.ImageField()

    class Meta:
        model = Reviews
        fields = ('author','title', 'description', 'body', 'image',) 

class CreateUserForm(UserCreationForm): #form para loggin, despues pasamos a views
    class Meta: #en que tabla se va a guardar
        model = User
        fields = ['username', 'email', 'password1', 'password2']