from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from lost.forms import LostPersonModelForm, LostItemModelForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def lost(request):
    lost_person = Person.objects.filter(person='L').all()
    lost_item = Item.objects.filter(category='L').all()
    search = request.GET.get('q')
    if search:
        lost_person = Person.objects.filter(
            Q(status__icontains=search) |
            Q(name__icontains=search) |
            Q(father_name__icontains=search) |
            Q(mother_name__icontains=search) |
            Q(age__icontains=search) |
            Q(location__icontains=search) |
            Q(phone_number__icontains=search) |
            Q(identification_mark__icontains=search) |
            Q(secret_information__icontains=search)
        )

        lost_item = Item.objects.filter(
            Q(status__icontains=search) |
            Q(name__icontains=search) |
            Q(category__icontains=search) |
            Q(location__icontains=search) |
            Q(phone_number__icontains=search) |
            Q(identification_mark__icontains=search) |
            Q(secret_information__icontains=search)
        )
    context = {
        'lost_person': lost_person,
        'lost_item': lost_item
    }
    return render(request, 'lost.html', context)
