from django.urls import path

from . import views

urlpatterns = [
	path('',views.index,name='index'),
	path('maintain',views.maintain,name='maintain'),
	path('addmentor',views.addmentor,name='addmentor'),
	path('notifyleaders',views.notifyleaders,name='notifyleaders'),
]