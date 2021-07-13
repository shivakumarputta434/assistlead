from django.urls import path
from .import views

urlpatterns=[
    path('home/',views.home,name='home'),
    path('CompanyData/', views.CompanyData.as_view(), name='CompanyData'),
    path('CompanyData/<int:id>', views.CompanyData.as_view(), name='CompanyData'),

    path('company/', views.Company_Data.as_view(), name='Company'),
    path('company/<int:id>', views.Company_Data.as_view(), name='single_company'),

    path('profile/', views.Profile_Data.as_view(), name='Profile'),
    path('profile/<int:id>', views.Profile_Data.as_view(), name='single_profile'),

]