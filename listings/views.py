from django.shortcuts import render, get_object_or_404, redirect
from .models import Listing

def main(request):
    return render(request, 'main.html')

def home(request):
    listings_obj = Listing.objects.all()
    context = {'listings': listings_obj}
    return render(request, 'index.html', context)

def create(request):
    if request.method == "POST":
        title = request.POST.get('title')
        price = request.POST.get('price')
        num_bathrooms = request.POST.get('num_bathrooms')
        num_bedrooms = request.POST.get('num_bedrooms')
        square_foot = request.POST.get('square_foot')
        address = request.POST.get('address')
        image = request.FILES.get('image')
        
        Listing.objects.create(
            title=title,
            price=price,
            num_bathrooms=num_bathrooms,
            num_bedrooms=num_bedrooms,
            square_foot=square_foot,
            address=address,
            image=image
        )
        return redirect('home')
    return render(request, 'create.html')

def edit(request, pk):
    listing = get_object_or_404(Listing, id=pk)
    
    if request.method == "POST":
        listing.title = request.POST.get('title')
        listing.price = request.POST.get('price')
        listing.num_bathrooms = request.POST.get('num_bathrooms')
        listing.num_bedrooms = request.POST.get('num_bedrooms')
        listing.square_foot = request.POST.get('square_foot')
        listing.address = request.POST.get('address')
        if 'image' in request.FILES:
            listing.image = request.FILES['image']
        listing.save()
        return redirect('home')
    
    context = {'listing': listing}
    return render(request, 'update.html', context)

def delete(request, pk):
    listing = get_object_or_404(Listing, id=pk)
    listing.delete()
    return redirect('home')

