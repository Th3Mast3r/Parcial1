from django.urls import path    #que entre adjango-urls y de alli importamos los path
from . import views     #importamos las vistas  

app_name = 'main' #variable que ponemos nombre de nuestra app

urlpatterns = [ #aqui se ven todas las secciones de la pagina web
    path('',views.IndexView.as_view(), name="home"),    #path base, se pone vacio (inicio='') xq lo manda a la pag principal
    path('contact/', views.ContactView.as_view(), name="contact"),  #de aqui en + de mas path
    path('blog/', views.BlogView.as_view(), name="blogs"),
    path('blog/<slug:slug>', views.BlogDetailView.as_view(), name="blog"),
    path('blog-create/', views.BlogAddInfo.as_view(), name="blog-create"),  #de aqui en + de mas path
    path('review/', views.ReviewView.as_view(), name="reviews"),
    path('review/<slug:slug>', views.ReviewDetailView.as_view(), name="review"),
    path('review-create/', views.ReviewAddInfo.as_view(), name="review-create"),  #de aqui en + de mas path
    path('register/', views.registerPage, name="register"),
	path('login/', views.loginPage, name="login"),
	path('logout/', views.logoutUser, name="logout"),
]

#slug=(importante)es para no repetir a si mismo(automatiza el url poniendo numero a los proyecto que vayan en portafolio (vainancq.com/portfolio/1 o 2 o 3 etc...))
#cuando hay varios proyectos, y queremos que se desplieguen, lo hara de forma automatica (slug)