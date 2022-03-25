from django.urls import path
from . import views

app_name = 'api'


urlpatterns = [
    path('register/', views.Register.as_view(), name='api-register'),
    path('login/', views.Login.as_view(), name='api-login'),
    path('logout/', views.Logout.as_view(), name='logout'),
    path('productView/<uuid:product_id>', views.ProductView.as_view(), name='product-view'),
    path('meeting/', views.JoinMeet.as_view(), name='join-meeting'),
    path('bloodDonation/', views.Blood_Donation.as_view(), name='blood-donation'),
]
