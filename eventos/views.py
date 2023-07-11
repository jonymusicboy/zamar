from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import Page

# Create your views here.
def pages(request):
    pages = get_list_or_404(Page)
    return render(request, 'eventos/pages.html', {'pages':pages})

def page(request, page_id, page_slug):
    page = get_object_or_404(Page, id=page_id)
    return render(request, 'eventos/page.html', {'page':page})