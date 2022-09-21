from django.shortcuts import render #backend renderizar lo que va a pasar de la base de datos(parte vital : proyecta tolo lo que hemos hecho), la parte de url, el index (que recibe y que hace)
from django.contrib import messages #aca va a mostrar los datos solicitados que se piden a travez de django
from django.views import generic #importa el generico = forma en que se muestra lo importado
from .forms import BlogForm, ReviewForm,ContactForm,CreateUserForm #, ReviewForm, BlogForm #el conector de backend y frontend (forms)
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout #se importa la autenticacion, login y logout de django
from django.contrib.auth.decorators import login_required	#imporamos el requerimiento de login de django
from django.contrib.auth.forms import UserCreationForm		#importamos el formulario para los usuarios de django
from django.http import HttpResponse						
from django.shortcuts import redirect						#importamos la redireccion para diferentes casos
from django.contrib.auth.mixins import LoginRequiredMixin	#importamos el limitador de acciones para los usuarios no logeados
from .models import ( #importamos todos los datos desde las tablas
	Blogs,
	Reviews,
	)

def registerPage(request): #Funcion registradora de usuario
	if request.user.is_authenticated: 	#decision que verifica si el usuario existe
		return redirect("main:home")	#si existe regresa al home
	else:
		form = CreateUserForm()			#si no existe, empieza el proceso para crear un usuario
		if request.method == 'POST':
			form = CreateUserForm(request.POST)
			if form.is_valid():
				form.save()
				user = form.cleaned_data.get('username')
				messages.success(request, 'Account was created for ' + user)

				return redirect('main:login')
			

		context = {'form':form}
		return render(request, 'main/register.html', context)

def loginPage(request):
	if request.user.is_authenticated:
		return redirect("main:home")
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password =request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				return redirect("main:home")
			else:
				messages.info(request, 'Username OR password is incorrect')

		context = {}
		return render(request, 'main/login.html', context)

def logoutUser(request):
	logout(request)
	return redirect('main:login')

class IndexView(generic.TemplateView):
	template_name = "main/index.html" #asignando la vista

	def get_context_data(self, **kwargs): #funcion q va a obtener la data
		#declaramos las variables donde se va a gaurdar la info
		context = super().get_context_data(**kwargs) #context guardara la informacion de testimonial, certificate, etc.
		reviews = Reviews.objects.filter(is_active=True)#despues de guardar la info en las variables lo guardamos en contexto
		blogs = Blogs.objects.filter(is_active=True)
		
		context["reviews"] = reviews #aqui es donde guarda la info de todo!!!
		context["blogs"] = blogs
		return context #regresamos la info

class ContactView(generic.FormView):
	template_name = "main/contact.html" #asigno la vista que html recibe
	form_class = ContactForm #creado para recibir info
	success_url = "/" #envia al index apenas de se clic
	
	def form_valid(self, form): #
		form.save()	#guarda info en base de datos
		return super().form_valid(form) 
	
class BlogView(generic.ListView): #aca se suben las noticia (blog), aca se ven 10 lineas
	model = Blogs
	template_name = "main/blog.html"
	paginate_by = 10 #para q no se sature, mostrara solo 10 lineas... (no toda la info x si es larga)
	
	def get_queryset(self):
		return super().get_queryset().filter(is_active=True) #retorno de info apenas encuentre todo

class BlogDetailView(generic.DetailView): #aca se encuentra todo (detalles) (despues de clickear la blogview)
	model = Blogs
	template_name = "main/blog-details.html"

class BlogAddInfo(LoginRequiredMixin, generic.FormView):
	login_url = 'main:login'
	redirect_field_name = 'login'
	template_name = "main/blog-create.html" #asigno la vista que html recibe
	form_class = BlogForm #creado para recibir info
	success_url = "/" #envia al index apenas de se clic
	
	def form_valid(self, form): 
		form.save()	#guarda info en base de datos
		messages.success(self.request, 'Thank you. We will be in touch soon.')
		return super().form_valid(form) 

class ReviewView(generic.ListView): #aca se suben las noticia (blog), aca se ven 10 lineas
	model = Reviews
	template_name = "main/review.html"
	paginate_by = 10 #para q no se sature, mostrara solo 10 lineas... (no toda la info x si es larga)
	
	def get_queryset(self):
		return super().get_queryset().filter(is_active=True) #retorno de info apenas encuentre todo

class ReviewDetailView(generic.DetailView): #aca se encuentra todo (detalles) (despues de clickear la blogview)
	model = Reviews
	template_name = "main/review-details.html"

class ReviewAddInfo(LoginRequiredMixin, generic.FormView):
	login_url = 'main:login'
	redirect_field_name = 'login'
	template_name = "main/review-create.html" #asigno la vista que html recibe
	form_class = ReviewForm #creado para recibir info
	success_url = "/" #envia al index apenas de se clic
	
	def form_valid(self, form): 
		form.save()	#guarda info en base de datos
		messages.success(self.request, 'Thank you. We will be in touch soon.')
		return super().form_valid(form) 