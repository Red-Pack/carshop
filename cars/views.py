from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from django.http import JsonResponse
from .forms import CarFilterForm
from .models import Car, CarModel

def load_models(request):
    brand_id = request.GET.get('brand')
    models = CarModel.objects.filter(brand_id=brand_id).order_by('name')
    models_list = list(models.values('id', 'name'))
    return JsonResponse(models_list, safe=False)

def car_list(request):
    form = CarFilterForm(request.GET or None)
    qs = Car.objects.all()  # Исходный QuerySet

    if form.is_valid():
        brand = form.cleaned_data.get('brand')
        if brand:
            qs = qs.filter(model__brand=brand)

        model = form.cleaned_data.get('model')
        if model:
            qs = qs.filter(model=model)

        year_from = form.cleaned_data.get('year_from')
        if year_from:
            qs = qs.filter(year__gte=year_from)

        year_to = form.cleaned_data.get('year_to')
        if year_to:
            qs = qs.filter(year__lte=year_to)

        transmission = form.cleaned_data.get('transmission')
        if transmission:
            qs = qs.filter(transmission=transmission)

        engine = form.cleaned_data.get('engine')
        if engine:
            qs = qs.filter(engine=engine)

        drive = form.cleaned_data.get('drive')
        if drive:
            qs = qs.filter(drive=drive)

        has_photo = form.cleaned_data.get('has_photo')
        if has_photo:
            qs = qs.filter(images__isnull=False).distinct()

    # Сортируем QuerySet для стабильной пагинации
    qs = qs.order_by('id')

    # Пагинация (например, 2 машины на страницу для теста)
    paginator = Paginator(qs, 5)
    page = request.GET.get('page')
    try:
        cars = paginator.page(page)
    except PageNotAnInteger:
        cars = paginator.page(1)
    except EmptyPage:
        cars = paginator.page(paginator.num_pages)

    # Копируем GET-параметры и удаляем 'page'
    params = request.GET.copy()
    if 'page' in params:
        del params['page']

    context = {
        'form': form,
        'cars': cars,
        'query': params.urlencode()  # Передаём оставшиеся параметры
    }
    return render(request, 'cars/car_list.html', context)

