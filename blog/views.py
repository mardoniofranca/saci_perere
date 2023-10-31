# blog/views.py
from django.views.generic.list import ListView

from django.views.generic import DetailView     

from .models import Post

class BlogListView(ListView):
    model = Post
    template_name = 'home.html'


class BlogDetailView(DetailView): # new
    model = Post
    template_name = 'post_detail.html'