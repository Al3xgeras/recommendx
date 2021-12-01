from django import forms
from .models import Review, Category
#queryset
choices = Category.objects.all().values_list('name', 'name')

choice_list = []
for choice in choices:
    choice_list.append(choice)

class ReviewCreateForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('title', 'category', 'content')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(choices=choices, attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'})
        }