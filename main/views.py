from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render, redirect
from django.conf.urls import handler404, handler500
from .forms import ContactForm, ProjectPostForm

def superuser_required(user):
    return user.is_superuser

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'aboutme.html')

def contact(request):
    form = ContactForm()

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            print(f"Name: {name} n\ Email: {email} n\ Message: {message}")

            return redirect('success_contact_form')
        else:
            form = ContactForm()
    return render(request, 'contact.html', {'form': form})

def success_contact_form(request):
    return render(request, 'success_contact_form')

def blog(request):
    return render(request, 'blog.html')

def project(request):
    return render(request, 'project.html')

def test(request):
    return render(request, 'test.html')

@user_passes_test(superuser_required, login_url='something_wrong')
def post(request):
    form = ProjectPostForm(request.POST, request.FILES)
    return render(request, 'project-post.html')


def custom_404_view(request, exception):
    return(request, '404.html', status==404)


def custom_400_view(request, exception):
    return render(request, '400.html', status=400)

def custom_500_view(request):
    return render(request, '500.html', status=500)

