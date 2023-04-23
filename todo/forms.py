from django.forms import ModelForm
from .models import Todo
from django.forms import ModelForm, ImageField
from .models import Todo, MediaFile

class TodoForm(ModelForm):
    image = ImageField(required=False)

    class Meta:
        model = Todo
        fields = ['title', 'memo', 'important']

