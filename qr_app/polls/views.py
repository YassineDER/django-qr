import base64
from io import BytesIO
from django.http import FileResponse, HttpResponse
from django.shortcuts import redirect, render
import qrcode
from .models import Produit
from .forms import ProductForm


def index(request):
    return render(request, 'index.html')


def create_product(request):
    if request.method == 'POST': 
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            img = generate_qr(request, Produit.objects.last().id)
            img_data_url = "data:image/png;base64," + base64.b64encode(img).decode()
            return render(request, 'confirmation.html', {'QR': img_data_url})            
    else:
        form = ProductForm()
    return render(request, 'new_produit.html', {'form': form})


def delete_product(request, id):
    if request.method == 'GET':
        produit = Produit.objects.get(id=id)
        produit.delete()
        return redirect('get_produits')
    return HttpResponse("Method not allowed", status=405)

def all(request):
    if request.method == 'GET':
        produits = Produit.objects.all()
        return render(request, 'produits.html', {'produits': produits})


def one(request, id):
    if request.method == 'GET':
        produit = Produit.objects.get(id=id)
        return render(request, 'produit.html', {'produit': produit})


def oneBy_qrcode(request, id):
    if request.method == 'GET':
        # Check if the product exists
        if not Produit.objects.filter(id=id).exists():
            return HttpResponse("Product not found", status=404)
    
        img = generate_qr(request, id)
        response = HttpResponse(img, content_type='image/png')
        response['Content-Disposition'] = 'attachment; filename="qrcode.png"'
        return response

def generate_qr(req, id):
    qr = qrcode.QRCode( version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10, border=4)
    url = req.get_host() + "/get/" + str(id)
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    response = BytesIO()
    img.save(response, "PNG")
    return response.getvalue()