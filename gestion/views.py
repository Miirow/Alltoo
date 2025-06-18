from django.shortcuts import render, redirect, get_object_or_404
from .models import Produit, Facture
from django.core.paginator import Paginator
from .forms import ProduitForm

from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa

def facture_pdf(request, pk):
    facture = get_object_or_404(Facture, pk=pk)
    template_path = 'gestion/facture_pdf.html'
    context = {'facture': facture}
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'filename="facture_{facture.id}.pdf"'
    template = get_template(template_path)
    html = template.render(context)
    pisa_status = pisa.CreatePDF(html, dest=response)
    if pisa_status.err:
        return HttpResponse('Erreur lors de la génération du PDF', status=500)
    return response


def liste_produits(request):
    produits = Produit.objects.all()
    paginator = Paginator(produits, 5)
    page = request.GET.get('page')
    produits = paginator.get_page(page)
    return render(request, 'gestion/liste.html', {'produits': produits})

def produit_create(request):
    form = ProduitForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('liste_produits')
    return render(request, 'gestion/produit_form.html', {'form': form})

def produit_update(request, pk):
    produit = get_object_or_404(Produit, pk=pk)
    form = ProduitForm(request.POST or None, instance=produit)
    if form.is_valid():
        form.save()
        return redirect('liste_produits')
    return render(request, 'gestion/produit_form.html', {'form': form})

def produit_delete(request, pk):
    produit = get_object_or_404(Produit, pk=pk)
    if request.method == 'POST':
        produit.delete()
        return redirect('liste_produits')
    return render(request, 'gestion/produit_confirm_delete.html', {'produit': produit})

def creer_facture(request):
    if request.method == 'POST':
        ids = request.POST.getlist('produits')
        client = request.POST.get('client', '')
        facture = Facture.objects.create(client=client)
        facture.produits.set(ids)
        return redirect('facture_detail', pk=facture.pk)
    produits = Produit.objects.all()
    return render(request, 'gestion/creer_facture.html', {'produits': produits})

def facture_detail(request, pk):
    facture = get_object_or_404(Facture, pk=pk)
    return render(request, 'gestion/facture_detail.html', {'facture': facture})

def facture_delete(request, pk):
    facture = get_object_or_404(Facture, pk=pk)
    if request.method == 'POST':
        facture.delete()
        return redirect('liste_produits')
    return render(request, 'gestion/facture_confirm_delete.html', {'facture': facture})

def liste_factures(request):
    factures = Facture.objects.all().order_by('-date')
    return render(request, 'gestion/liste_factures.html', {'factures': factures})

def facture_delete(request, pk):
    facture = get_object_or_404(Facture, pk=pk)
    if request.method == 'POST':
        facture.delete()
        return redirect('liste_factures')
    return render(request, 'gestion/facture_confirm_delete.html', {'facture': facture})
