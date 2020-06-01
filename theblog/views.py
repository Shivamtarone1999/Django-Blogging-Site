from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import *
from .forms import PostForm,EditForm
from django.urls import reverse_lazy ,reverse
from django.http import HttpResponseRedirect
# Create your views here.

"""def home(request):
    context = {}
    return render(request,'home.html',context)"""

class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    #ordering = ['-id']    
    ordering = ['-post_date']

    def get_context_data(self,*args,**kwargs):
        cat_menu = Category.objects.all()
        context = super(HomeView,self).get_context_data(*args,**kwargs)
        context["cat_menu"] = cat_menu
        return context



class ArticleDetailView(DetailView): 
    model = Post
    template_name = 'postDetails.html'
    def get_context_data(self,*args,**kwargs):
        cat_menu = Category.objects.all()
        context = super(ArticleDetailView,self).get_context_data(*args,**kwargs)
        
        stuff = get_object_or_404(Post,id=self.kwargs['pk'])
        total_likes = stuff.total_likes()
        
        liked = False
        if stuff.likes.filter(id=self.request.user.id).exists():
            liked = True
        
        context["cat_menu"] = cat_menu
        context["total_likes"] = total_likes
        context["likes"] = liked
        return context 

   

class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'Add_Post.html'
    #fields = '__all__' 
    #fields = ('title','title_tag','body')

    def get_context_data(self,*args,**kwargs):
        cat_menu = Category.objects.all()
        context = super(AddPostView,self).get_context_data(*args,**kwargs)
        context["cat_menu"] = cat_menu
        return context
   


def CategoryListView(request):
    
    cat_menu_list = Category.objects.all()
    return render(request,'categories_list.html',{'cat_menu_list':cat_menu_list})
    



def CategoryView(request,cats):
    category_posts = Post.objects.filter(category = cats.replace('-',' '))
    context = {'cats':cats.title().replace('-',' '),'category_posts':category_posts}
    return render(request,'categories.html',context)
    

class AddCategoryView(CreateView):
    model = Category
    #form_class = PostForm
    template_name = 'Add_Category.html'
    fields = '__all__' 
    #fields = ('title','title_tag','body')

    def get_context_data(self,*args,**kwargs):
        cat_menu = Category.objects.all()
        context = super(AddCategoryView,self).get_context_data(*args,**kwargs)
        context["cat_menu"] = cat_menu
        return context



class UpdatePostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'editPost.html'
    #fields = ['title','title_tag','body']

    def get_context_data(self,*args,**kwargs):
        cat_menu = Category.objects.all()
        context = super(UpdatePostView,self).get_context_data(*args,**kwargs)
        context["cat_menu"] = cat_menu
        return context


class DeletePostView(DeleteView):
    model = Post
    template_name = 'deletePost.html'
    success_url = reverse_lazy('home')

    def get_context_data(self,*args,**kwargs):
        cat_menu = Category.objects.all()
        context = super(DeleteView,self).get_context_data(*args,**kwargs)
        context["cat_menu"] = cat_menu
        return context


def LikeView(request,pk):
    post = get_object_or_404(Post,id=request.POST.get('post_id'))
    
    liked = False

    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True

    return HttpResponseRedirect(reverse('postDetail',args=[str(pk)]))