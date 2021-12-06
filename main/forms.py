from django import forms
from .models import Review, Category, Comment
#queryset
choices = Category.objects.all().values_list('name', 'name')

choice_list = []
for choice in choices:
    choice_list.append(choice)

class ReviewCreateForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('title', 'category', 'content', 'images')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(choices=choices, attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
        }

class AddCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)

        widgets = {
            'content': forms.Textarea(attrs={'class': 'form-control'})
        }