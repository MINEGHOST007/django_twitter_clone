from typing import Any, Dict
from django.shortcuts import render,get_object_or_404
from django.views.generic import ListView, DetailView , CreateView, UpdateView, DeleteView
from .models import Message,choices_list,Comment
from django.urls import reverse_lazy ,reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db import models


# Create your views here.
# def home(request):
#     return render(request,'index.html',{})


class HomeView(ListView):
    model = Message
    template_name = 'index.html'
    ordering=['-id']


class ArticleView(DetailView):
    model = Message
    template_name = 'article_details.html'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        stuff = get_object_or_404(Message, id = self.kwargs['pk'])
        context = super(ArticleView , self).get_context_data(**kwargs)
        total_likes = stuff.total_likes()
        context["total_likes"] = total_likes
        liked = False
        booked = False
        if stuff.like.filter(id = self.request.user.id).exists():
            liked = True
        if stuff.book.filter(id = self.request.user.id).exists():
            booked = True
        context["booked"] = booked
        context["liked"] = liked
        return context


class AddView(CreateView):
    model= Message
    template_name= 'addpost.html'
    fields= ['author','title','body','categories','image']

class CommentView(CreateView):
    model= Comment
    template_name= 'addcomment.html'
    fields = '__all__'
    success_url = reverse_lazy('home')

    def get_context_data(self,**kwargs):
        context = super(CreateView , self).get_context_data(**kwargs)
        context['pk'] = self.kwargs['pk']
        return context

class EditView(UpdateView):
    model= Message
    template_name= 'update.html'
    fields= ['title','body','categories','image']

class RemoveView(DeleteView):
    model = Message
    template_name = 'delete.html'
    success_url = reverse_lazy('home')

def CategoryView(request,cats):
    category_posts = Message.objects.filter(categories = cats)
    return render(request, 'categories.html', {'cats': cats , 'category_posts': category_posts , 'choices': choices_list})

@login_required
def LikeView(request,pk):
    post = get_object_or_404(Message, id = pk)
    liked =False
    if post.like.filter(id = request.user.id).exists():
        post.like.remove(request.user)
        liked = False
    else:
        post.like.add(request.user) 
        liked= True
    return HttpResponseRedirect(reverse('detail_view', args=[str(pk)]))

@login_required
def BookView(request,pk):
    post = get_object_or_404(Message, id = pk)
    if post.book.filter(id = request.user.id).exists():
        post.book.remove(request.user)
    else:
        post.book.add(request.user)
    return HttpResponseRedirect(reverse('detail_view', args=[str(pk)]))

# def BookView(request,cats):
#     category_posts = Message.objects.filter(book = cats)
#     return render(request, 'bookmarks.html', {'cats': cats , 'category_posts': category_posts , 'choices': bchoices_list})

def BookView2(request,pk):
    bookmark_posts = Message.objects.filter(book = pk)
    return render(request, 'bookmarks.html',{'id': pk , 'bookmark_posts':bookmark_posts })

def ProfileView(request,pk):
    bookmark_posts = Message.objects.filter(author = pk)
    user = get_object_or_404(User, id=pk)
    bluffs = bookmark_posts.count()
    return render(request, 'profile.html',{'id': pk , 'bookmark_posts':bookmark_posts , 'bluffs': bluffs , 'userr' : user })

