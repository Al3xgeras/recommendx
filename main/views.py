from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (ListView, DetailView, 
                                CreateView, UpdateView, 
                                DeleteView)
from .models import Review

def homepage(request):
    top_reviews = Review.objects.all().order_by('-rating')
    latest_reviews = Review.objects.all().order_by('-date')
    return render(request, 'main/index.html', {'top_reviews':top_reviews, 
                                            'latest_reviews':latest_reviews})

class ReviewListView(ListView):
    model = Review
    template_name = 'main/index.html'
    context_object_name = 'top_reviews'
    ordering = ['-rating']
    
    def get_context_data(self, *args, **kwargs):
        context = super(ReviewListView, self).get_context_data(*args, **kwargs)
        context['latest_reviews'] = Review.objects.all().order_by('-date')
        return context 

class ReviewDetailView(DetailView):
    model = Review
    template_name = 'main/review_detail.html'

class ReviewCreateView(LoginRequiredMixin, CreateView):
    model = Review
    fields = ['title', 'content', 'score']

    def form_valid(self, form):
        form.instance.publisher = self.request.user
        return super().form_valid(form)

class ReviewUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Review
    fields = ['title', 'content', 'score']

    def form_valid(self, form):
        form.instance.publisher = self.request.user
        return super().form_valid(form)

    def test_func(self):
        review = self.get_object()
        if self.request.user == review.publisher:
            return True
        return False

class ReviewDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Review
    success_url = '/'
    def test_func(self):
        review = self.get_object()
        if self.request.user == review.publisher:
            return True
        return False