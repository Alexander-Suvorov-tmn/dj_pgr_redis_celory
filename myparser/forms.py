from .models import *
from django.forms import ModelForm


class WelderForm(ModelForm):

    class Meta:
        # Название модели на основе
        # которой создается форма
        model = Welder
        # Включаем все поля с модели в форму
        fields = '__all__'