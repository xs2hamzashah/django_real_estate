from gettext import install
from urllib import response
from django.shortcuts import redirect, render

from listings.forms import ListingForm
from .models import Listing

# Create your views here.
def listing_list(request):
    listings = Listing.objects.all()
    context = {
        "listings": listings
    }
    return render(request, "listings.html", context)


def listing_retrieve(request, id):
    listing = Listing.objects.get(id=id)
    context = {
        'listing': listing
    }
    return render(request, "listing.html", context)

def listing_create(request):
    form = ListingForm()
    context = {
        'form': form
    }

    if request.method == 'POST':
        form = ListingForm(request.POST, request.FILES) # populating the form
        if form.is_valid():
            form.save()
            return redirect("/")
        return render(request, "listing_create.html", context)
        pass
   
    return render(request, "listing_create.html", context)

def listing_update(request, id):
    listing = Listing.objects.get(id=id)
    form = ListingForm(instance=listing)
   

    if request.method == 'POST':
        form = ListingForm(request.POST, instance=listing, files=request.FILES) # instance know this is updating 
        if form.is_valid():
            form.save()
            return redirect("/")
     
    context = {
        "form": form
    }
    return render(request, "listing_update.html", context)

def listing_delete(request, id):
    listing = Listing.objects.get(id=id)
    listing.delete()
    return redirect('/')