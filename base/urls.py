from django.urls import path
from .views import register, login, StudentView
urlpatterns = [
    
    path('register/', register ),
    path('login/', login ),
    path('Student/', StudentView.as_view({'get':'list','post':'create'}) ),
    path('Student/<int:pk>/', StudentView.as_view({'get':'retrieve','put':'update', 'delete':'destroy'}) )
    
]