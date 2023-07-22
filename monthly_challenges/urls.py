from django.urls import path

from . import views

urlpatterns = [
    path('', views.challenges_list),
    path('<int:month>', views.challenges_by_number),
    path("<str:month>", views.challenges, name="challenges_by_name"),
]
