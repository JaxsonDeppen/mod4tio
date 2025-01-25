from django.shortcuts import render
from .models import Product

# Create your views here.
def index(request):
    list = Product.objects.all()
    context = {
        "list": list,
    }
    return render(request, "coolapp/index.html", context)