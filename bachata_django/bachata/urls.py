from django.urls import path
from .views import SignUp
from . import views

urlpatterns = [
    path('', views.event_list, name='event_list'),
    path('events/<int:pk>', views.event_detail, name='event_detail'),
    path('events/new', views.event_create, name='event_create'),
    path('events/<int:pk>/edit', views.event_edit, name='event_edit'),
    path('events/<int:pk>/delete', views.event_delete, name='event_delete'),
    path('accounts/signup/', views.SignUp.as_view(), name='signup'),

]