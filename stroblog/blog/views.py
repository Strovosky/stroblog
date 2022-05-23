from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Posts

# Create your views here.

#def home(request):
#    user1_posts = User.objects.get(id=1).posts_set.all()
#    return render(request, "blog/home.html", {"posts": user1_posts})

# This is a list class view.
class PostListView(ListView):
    # NAMING CONVENTION
    # template_name = <app>/<model>_<viewtype>.html     example: "blog/posts_list.html"
    # context_object_name = "object_list"
    # ordering = ["-date_created"]   Organizes the iterations from newest to oldest.
    
    # First, you need to pass the model of the objects you'll be using.
    # If you stuck to the naming conventions, this is all you had to do then.
    model = Posts

    # If you didn't stick to the convention, you can use these to specify the info. 
    # Tell the view what the name of the template is.
    template_name: str = "blog/home.html"

    # The context object (dictionary) that we will pass to the template.
    # This is the object the ListView will look for to iterate it.
    context_object_name = "posts" # This is what we named it in the template.

    # In which order we want the posts to appear.
    ordering = ["-date_created"]

class PostDetailView(DetailView):
    # Conventions for DetailView
    # template_name = <app>/<model>_<viewtype>.html     example: "blog/posts_detail.html"
    # context_object_name = "object"
    model = Posts

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Posts
    # Conventions for DetailView
    # template_name = <app>/<model>_form.html     example: "blog/posts_form.html"

    # CreateView will provide a form to pass the info to create, we need to tell CreateView what...
    # fields the form will use to create the post.
    # We won't pass date_created since that'll be automatic.
    fields = ['title', 'content']

    def form_valid(self, form):
        # Pass the current user as the author before you validate the form.
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    # In this case, you don't need to create a HTML TEMPLATE for this view cuz...
    # it will be using the same POSTS_FORM.HTML template we already used for PostCreateView.
    model = Posts
    fields = ["title", "content"]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

        # This could also be done in a one-liner like this...
        #return True if post.author == self.request.user else False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Posts

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
    
    success_url = "/"



def about_us(request):
    return render(request, "blog/about_us.html", {})

def my_account(request):
    return render(request, "blog/my_account.html", {})
