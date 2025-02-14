from django import forms
from django.core.validators import validate_email
from .models import Contact, ProjectPost, TypeOfPost


"""
for my future update
"""

class ContactForm(forms.Form):
    class Meta:
        model = Contact
        field = ['name', 'email', 'description']
        email = forms.EmailField(validators=[validate_email], widget=forms.EmailInput(attrs={'autocomplete': 'off'}))

class ProjectPostForm(forms.Form):
    class Meta:
        modal = ProjectPost
        field = ['type_of_project', 'title', 'image', 'description']
        type_of_post = forms.ModelChoiceField(
            queryset=TypeOfPost.objects.all(),
            empty_label="Select a post type",
            label="Project",
            widget=forms.Select(attrs={'class': 'form-control'})
        )