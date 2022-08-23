from django.urls import path
from blog import views

urlpatterns = [
	path('', views.IndexView.as_view(), name='index_view'),
]
