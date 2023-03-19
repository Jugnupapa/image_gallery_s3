from django.shortcuts import render
from .models import GalleryModel
# Create your views here.
def home(request):
    galleries = GalleryModel.objects.all()

    return render(request, 'home.html', {'galleries': galleries})