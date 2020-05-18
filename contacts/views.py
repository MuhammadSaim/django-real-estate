from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact


# Create your views here.
def contact(request):
    if request.method == 'POST':
        user_id = request.POST['user_id']
        realtor_email = request.POST['realtor_email']
        listing_id = request.POST['listing_id']
        listing = request.POST['listing']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']

        if request.user.is_authenticated:
            user_id = request.user.id
            has_connected = Contact.objects.all().filter(listing_id=listing_id, user_id=user_id)
            if has_connected:
                messages.error(request, "You have already made an inquiry for this listing")
                return redirect("/listings/" + listing_id)


        contact = Contact(user_id=user_id, listing_id=listing_id, listing=listing, name=name, email=email, phone=phone, message=message)
        contact.save()

        messages.success(request, "Your request is submitted successfully realtor will get you soon.")
        return redirect("/listings/"+listing_id)


