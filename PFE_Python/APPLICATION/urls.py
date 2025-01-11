from django.urls import path

from APPLICATION import views

urlpatterns = [
    path('',views.base,name='base'),
     path('inscription/',views.inscription,name='inscription'),
     path('connexion/',views.connexion,name='connexion'),
     path('acceuil/', views.acceuil, name='acceuil'),
      path('deconnexion/', views.deconnexion, name='deconnexion'),
     path('formations/', views.formations, name='formations'),
     path('jeux/', views.jeux, name='jeux'),
     path('formvideo/', views.formvideo, name='formvideo'), 
   
]