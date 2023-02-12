from django.urls import path
from .views import add_student_view,show_view,update_view,delete_view




urlpatterns = [
    path('av/',add_student_view,name='add_url'),
    path('sv/',show_view,name='show_url'),
    path('up/<int:pk>/',update_view,name='update_url'),
    path('dl/<int:pk>/',delete_view,name='delete_url')
]