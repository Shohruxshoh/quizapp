from django.urls import path
from .views import addQuestion, home, registerPage, loginPage, logoutPage, category, category_list

urlpatterns = [
    path('category/', category, name='category'),
    path('category/<slug:slug>/', category_list, name='category-list'),
    path('', home,name='home'),
    path('addQuestion/', addQuestion,name='addQuestion'),
    path('login/', loginPage,name='login'),
    path('logout/', logoutPage,name='logout'),
    path('register/', registerPage,name='register'),
]
