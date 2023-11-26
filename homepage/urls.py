from django.urls import path
from .import views
from django.views.decorators.csrf import csrf_exempt
from .views import LogoutView

urlpatterns = [
    path('', views.index, name='homepage'),
    path('login/', views.custom_login, name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('adding/', views.add_stuff, name='adding'),
    path('stuff/<int:pk>/', views.stuff_detail, name='stuff_detail'),
    path('stuff-delete/<int:pk>/', views.delete_stuff, name='delete'),
    path('stuff-edit/<int:pk>/', views.stuff_edit, name='stuff_edit'),
]
