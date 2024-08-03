from django.urls import path
from . import views
urlpatterns = [
    path('income/',views.listIncome),
    # path('about/',views.about)
]