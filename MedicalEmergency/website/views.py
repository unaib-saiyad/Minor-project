from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView
from api.models import *


# Create your views here.

class Index(TemplateView):
    template_name = "index.html"


class MedicineOrder(TemplateView):
    template_name = "medicine_order.html"

    def get_context_data(self, **kwargs):
        context = super(MedicineOrder, self).get_context_data(**kwargs)
        context['products'] = []
        context['slides'] = []
        categories = ProductCategory.objects.all()
        for count, item in enumerate(categories):
            context['products'].append(Product.objects.filter(category=item))
            context['slides'].append(range(1, int(len(context['products'][count]) / 4) + 1))
        return context


class BloodDonation(TemplateView):
    template_name = 'blood_donation.html'


class DoctorAppointment(TemplateView):
    template_name = 'doctors_appointment.html'


class Register(TemplateView):
    template_name = 'register.html'


class Login(TemplateView):
    template_name = 'login.html'


class ForgotPassword(TemplateView):
    template_name = 'forgot-password.html'


class ProductView(TemplateView):
    template_name = 'product-view.html'
