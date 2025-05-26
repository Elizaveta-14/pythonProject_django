from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from blog.models import Blog


class BlogListView(ListView):
    model = Blog

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(publication_attribute=True)


class BlogDetailView(DetailView):
    model = Blog
    template_name = 'blog/blog_detail.html'

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_counter += 1
        self.object.save()
        return self.object


class BlogCreateView(CreateView):
    model = Blog
    fields = ('heading', 'content', 'preview', 'publication_attribute')
    success_url = reverse_lazy('blog:blog_list')


class BlogUpdateView(UpdateView):
    model = Blog
    fields = ('heading', 'content', 'preview', 'publication_attribute')
    success_url = reverse_lazy('blog:blog_detail')

    def get_success_url(self):
        return reverse(viewname='blog:blog_detail', args=[self.kwargs.get('pk')])


class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy('blog:blog_list')
