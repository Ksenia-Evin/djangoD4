from django.urls import path  
from p_library.views import main, RegisterView, CreateUserProfile  
from django.urls import reverse_lazy 
from allauth.account.views import login, logout


app_name = 'p_library'  
  
urlpatterns = [  

    path('main/login/', login, name='login'),  
    path('main/logout/', logout, name='logout'),
    path('main/', main, name='main'),  
    path('register/', RegisterView.as_view(  
        template_name='register.html',  
		success_url=reverse_lazy('p_library:profile-create')  
    ), name='register'),  
    path('profile-create/', CreateUserProfile.as_view(), name='profile-create')
]