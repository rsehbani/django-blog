from django.shortcuts import render

from django.views.generic import ListView, CreateView, UpdateView, DetailView
from django.urls import reverse

from posts.models import BlogPost

class BlogHome(ListView):
    model = BlogPost
    context_object_name = "posts"

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.is_authenticated:
            return queryset

        return queryset.filter(published=True)

class BlogPostCreate(CreateView):
    model = BlogPost
    template_name = 'posts/blogpost_form.html'
    fields = ['title', 'content', ]
"""
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect

def original_view(request):
    # line below is an example of how you SHOULD NOT hardcode a URL
    # return HttpResponseRedirect('/another-url/')
    reversed_url = reverse('named-url')  # /another-url/
    return HttpResponseRedirect(reversed_url)

    
def another_view(request):
    content = '<p>dummy content</p>'
    return HttpResponse(content)

"""


class BlogPostEdit(UpdateView):
    model = BlogPost
    template_name = 'posts/blogpost_edit.html'
    fields = ['title', 'content', 'published', ]

class BlogPostDetail(DetailView):
    model = BlogPost
    context_object_name = "post"

from django.urls import reverse_lazy
from django.views.generic import DeleteView

class BlogPostDelete(DeleteView):
    model = BlogPost
    success_url = reverse_lazy("posts:home")