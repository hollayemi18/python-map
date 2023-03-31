from django.shortcuts import render, redirect
from geopy.geocoders import Nominatim
from .models import Address
from .forms import StoreData

# map function


def user_map(request, id):
    try:
        # getting adress from database
        user = Address.objects.get(id=id)

        stre = user.street
        city = user.city
        # concant adress from the database
        address = f"{user.street}, {user.city}, {user.country} "
        # calling the nominatim server
        geolocator = Nominatim(user_agent="my_application")
        # nominatim working it magic
        location = geolocator.geocode(address)
        lat = location.latitude
        lng = location.longitude
        return render(request, 'user_map.html', {'lat': lat, 'lng': lng, 'user': user, 'street': stre, 'city': city})
    except AttributeError:
        return redirect('/emp')

# just a form to save data


def emp(request):
    if request.method == "POST":
        form = StoreData(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/')
            except:
                pass
    else:
        form = StoreData()
    return render(request, 'index.html', {'form': form})

# rendering of data


def show(request):
    storedata = Address.objects.all()
    return render(request, "show.html", {'storedata': storedata})
