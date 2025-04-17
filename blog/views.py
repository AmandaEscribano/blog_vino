from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .models import Blog
from django.contrib.auth.decorators import login_required
from .forms import BlogForm
from django.contrib import messages


# Página principal
def home(request):
    return render(request, 'blog/home.html')


# Vista de "Acerca de"
def about(request):
    return render(request, 'blog/about.html')


# Listado de blogs
def blog_list(request):
    blogs = Blog.objects.all()  # Ya ordenados por Meta.ordering
    return render(request, 'blog/blog_list.html', {'blogs': blogs})


# Detalle de un blog individual
def blog_detail(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    return render(request, 'blog/blog_detail.html', {'blog': blog})


# Página de prueba genérica
def pages_view(request):
    return render(request, 'blog/pages.html')


# Registro de usuario + login automático
def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Login automático
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'blog/signup.html', {'form': form})

@login_required
def create_blog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.author = request.user
            blog.save()
            return redirect('blog_list')
    else:
        form = BlogForm()
    return render(request, 'blog/create_blog.html', {'form': form})

@login_required
def edit_blog(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    if blog.author != request.user:
        messages.error(request, "No tenés permiso para editar este post.")
        return redirect('blog_list')

    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            form.save()
            messages.success(request, "Blog actualizado con éxito.")
            return redirect('blog_detail', pk=pk)
    else:
        form = BlogForm(instance=blog)
    return render(request, 'blog/edit_blog.html', {'form': form})


@login_required
def delete_blog(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    if blog.author != request.user:
        messages.error(request, "No tenés permiso para eliminar este post.")
        return redirect('blog_list')

    if request.method == 'POST':
        blog.delete()
        messages.success(request, "Post eliminado.")
        return redirect('blog_list')
    return render(request, 'blog/delete_blog.html', {'blog': blog})