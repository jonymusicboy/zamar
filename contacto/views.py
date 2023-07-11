from django.shortcuts import render, redirect
from .forms import ContactForm
from .models import ContactMessage

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact_success')
    else:
        form = ContactForm()
    return render(request, 'contacto/contact.html', {'form': form})

def contact_success(request):
    return render(request, 'contacto/success.html')

def mensajes_enviados(request):
    mensajes = ContactMessage.objects.all().order_by('-created_at')
    return render(request, 'contacto/mensajes_enviados.html', {'mensajes': mensajes})
