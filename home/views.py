from django.shortcuts import render, redirect
from django.contrib import messages
from django.views import View
from .models import Profile

class HomeView (View):
    def get(self, request):
        context = {}
        return render(request, 'home//home.html', context=context)
    
    def post(self, request):
        # Extract data
        full_name = request.POST.get('full_name', '')
        company_name = request.POST.get('company', '')
        phone = request.POST.get('phone', '')
        email = request.POST.get('email', '')
        
        # Guardar en base de datos
        profile_entry = Profile(full_name=full_name, company_name=company_name, phone=phone, email=email)
        profile_entry.save()
        
        return redirect('home')