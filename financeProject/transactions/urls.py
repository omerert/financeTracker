from django.urls import path
from . import views
urlpatterns = [
    path('', views.listTransaction),
    # path('about/',views.about)
]