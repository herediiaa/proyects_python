from django.shortcuts import get_object_or_404, render,redirect
from django.views.generic import View,UpdateView
from .models import Blog
from .forms import BlogCreateForm
from django.urls import reverse_lazy

# Create your views here.
class IndexView(View):
    def get(self,request,*args,**kwargs):
        blogPosts = Blog.objects.all()
        print(blogPosts)
        context = {'blogPosts':blogPosts}
        return render(request,'blog/index.html', context)

class BlogDetailView(View):
    def get(self,request,pk,*args,**kwargs):
        blogDetails = Blog.objects.get(pk=pk)
        context={'blog':blogDetails}
        return render(request, 'blog/blogDetail.html',context)
    
class BlogCreateView(View):
    def get(self,request,*args,**kwargs):
        formulario = BlogCreateForm()
        context = {
            'formulario':formulario
        }
        print("fomulario activo")
        return render(request,'blog/createBlogForm.html', context)
    
    def post(self,request,*args, **kwargs):
        if request.method =="POST":
            formulario = BlogCreateForm(request.POST)
            if formulario.is_valid():
                titulo = formulario.cleaned_data.get('titulo')
                autor = formulario.cleaned_data.get('autor')
                contenido = formulario.cleaned_data.get('contenido')    
                p,created = Blog.objects.get_or_create(titulo=titulo,autor=autor,contenido=contenido)
                p.save()
        return redirect('blog:home')


class BlogUpdateView(UpdateView):
    model=Blog
    fields=['titulo','autor','contenido']
    template_name='blog/updateCreateBlog.html'
    
    def get_success_url(self):
        pk = self.kwargs['pk']
        return reverse_lazy('blog:detail', kwargs={'pk':pk})


