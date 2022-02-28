from django.urls import path
from apiRest import views
urlpatterns = [
    path('listar/', views.helloapiView.as_view()),
]