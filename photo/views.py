from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.templatetags.static import static
from .models import Images, Location, Category
from django.db.models.query import QuerySet

def home(request):
    images = Images.objects.all()
    location = Location.objects.all()
    context = {
        "images":images,
        "location":location,
    }
    return render(request, 'home.html', context)

def images(request, images_id):
    try:
        images = Images.objects.get(id = images_id)
    except DoesNotExist:
        raise Http404()
    return render(request,"gall/gallery.html", {"images":images})

def search_image(request):
    if 'images' in request.GET and request.GET['images']:
        search_term = request.GET["images"]
        searched_images = Images.search_by_category(search_term)
        message = f'{search_term}'
        return render(request, 'gall/search.html', {"message":message, "images":searched_images})

    else:
        message = "You haven't searched for any image"
        return render(request, 'gall/search.html', {"message":message})

def display_by_location(request, id):
    queryset = Location.objects.all()
    queryset = Images.objects.filter(location__id=id)
    context = {
        "location":queryset,
        "images":queryset,
    }
    return render(request, "location.html", context)
