from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path('c/<str:constituency>', views.constituency, name='constituency'),
    path('postcode/', views.postcode, name='postcode')
]
