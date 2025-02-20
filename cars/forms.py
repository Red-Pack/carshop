from django import forms
from .models import Brand, CarModel, Car

class CarFilterForm(forms.Form):
    brand = forms.ModelChoiceField(
        queryset=Brand.objects.all(),
        required=False,
        label='Марка',
        empty_label='Любая марка'
    )
    model = forms.ModelChoiceField(
        queryset=CarModel.objects.none(),  # Заполним динамически
        required=False,
        label='Модель',
        empty_label='Любая модель'
    )

    year_from = forms.IntegerField(required=False, label='Год от')
    year_to = forms.IntegerField(required=False, label='Год до')

    # Поле КПП (transmission) – используем ваши choices из модели Car
    transmission = forms.ChoiceField(
        choices=[('', 'Любая')] + list(Car.TRANSMISSION_CHOICES),
        required=False,
        label='КПП'
    )

    # Поле топлива (engine)
    engine = forms.ChoiceField(
        choices=[('', 'Любое')] + list(Car.ENGINE_FUEL),
        required=False,
        label='Топливо'
    )

    # Поле привода (drive)
    drive = forms.ChoiceField(
        choices=[('', 'Любой')] + list(Car.DRIVE_CHOICES),
        required=False,
        label='Привод'
    )

    # Поле "С фото"
    has_photo = forms.BooleanField(required=False, label='С фото')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'brand' in self.data and self.data['brand']:
            try:
                brand_id = int(self.data['brand'])
                self.fields['model'].queryset = CarModel.objects.filter(brand_id=brand_id)
                # Если марка выбрана, убираем атрибут disabled (на случай, если форма отправлена повторно)
                self.fields['model'].widget.attrs.pop('disabled', None)
            except (ValueError, TypeError):
                pass
        else:
            # Если марка не выбрана, делаем список моделей неактивным
            self.fields['model'].queryset = CarModel.objects.none()
            self.fields['model'].widget.attrs['disabled'] = 'disabled'

