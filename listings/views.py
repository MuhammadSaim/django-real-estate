from django.shortcuts import render, get_object_or_404
from .models import Listing
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .choices import *


# Create your views here.
def listings(request):
    listings = Listing.objects.all()
    paginator = Paginator(listings, 3);
    page_number = request.GET.get('page')
    listings = paginator.get_page(page_number)
    context = {
        'listings': listings,
    }
    return render(request, "listings/listings.html", context)


def listing(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)
    context = {
        'listing': listing
    }
    return render(request, "listings/listing.html", context)


def search(request):
    listings = Listing.objects.order_by("-list_date")

    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            listings = Listing.objects.filter(description__icontains=keywords)

    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            listings = Listing.objects.filter(city__iexact=city)

    if 'state' in request.GET:
        state = request.GET['state']
        if state:
            listings = Listing.objects.filter(state__iexact=state)

    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms:
            listings = Listing.objects.filter(bedrooms__lte=bedrooms)

    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            listings = Listing.objects.filter(price__lte=price)

    context = {
        'bedrooms': bedrooms_choices,
        'prices': price_choices,
        'states': state_choices,
        'listings': listings,
        'form_values': request.GET
    }
    return render(request, "listings/search.html", context)





