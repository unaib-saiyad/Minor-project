from django.urls import path
from . import views

app_name = 'website'

urlpatterns = [
    path('', views.Index.as_view(), name='dashboard'),
    path('medicine_order/', views.MedicineOrder.as_view(), name='medicine_order'),
    path('blood_donation/', views.BloodDonation.as_view(), name='blood_donation'),
    path('doctor_appointment/', views.DoctorAppointment.as_view(), name='doctor_appointment'),
    path('register/', views.Register.as_view(), name='register'),
    path('login/', views.Login.as_view(), name='login'),
    path('forgot_password/', views.ForgotPassword.as_view(), name='forgot_password'),
    path('product_view/<uuid:product_id>', views.ProductView.as_view(), name='product_view'),
]
