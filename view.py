from django.shortcuts import render, get_object_or_404, redirect
from .models import Advertisement
from .forms import AdvertisementForm


def edit_advertisement(request, advertisement_id):
    advertisement = get_object_or_404(Advertisement, id=advertisement_id)

    if request.method == 'POST':
        form = AdvertisementForm(request.POST, instance=advertisement)
        if form.is_valid():
            form.save()
            return redirect('advertisements_list')  # Перенаправление после успешного сохранения
    else:
        form = AdvertisementForm(instance=advertisement)

    return render(request, 'edit_advertisement.html', {'form': form})