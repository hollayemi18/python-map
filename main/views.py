from django.shortcuts import render, redirect
from .models import Address
from .forms import StoreData


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
    user = Address.objects.get(id=1)

    return render(request, "show.html", {'user': user})
