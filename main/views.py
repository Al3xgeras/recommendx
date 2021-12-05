from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views.generic import (ListView, DetailView, 
                                CreateView, UpdateView, 
                                DeleteView)
from .models import Review, Category, Comment
from .forms import ReviewCreateForm, AddCommentForm

choises = Category.objects.all().values_list('name', 'name')

"""
def homepage(request):
    top_reviews = Review.objects.all().order_by('-rating')
    latest_reviews = Review.objects.all().order_by('-date')
    return render(request, 'main/index.html', {'top_reviews':top_reviews, 
                                            'latest_reviews':latest_reviews})
"""

class ReviewListView(ListView):
    model = Review
    template_name = 'main/index.html'
    context_object_name = 'top_reviews'
    ordering = ['-rating']

    def get_context_data(self, *args, **kwargs):
        context = super(ReviewListView, self).get_context_data(*args, **kwargs)
        context['latest_reviews'] = Review.objects.all().order_by('-date')
        return context 

class UserReviewListView(ListView):
    model = Review
    template_name = 'main/user_reviews.html'
    context_object_name = 'reviews'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Review.objects.filter(publisher=user).order_by('-date')

class TopReviewsListView(ListView):
    model = Review
    template_name = 'main/top_reviews.html'
    context_object_name = 'top_reviews'
    ordering = ['-rating']
    paginate_by = 5

class LatestReviewsListView(ListView):
    model = Review
    template_name = 'main/latest_reviews.html'
    context_object_name = 'latest_reviews'
    ordering = ['-date']
    paginate_by = 5

def CategoryView(request, cat):
    category_reviews = Review.objects.filter(category__iexact=cat.replace('-', ' '))
    context = {'cat':cat.title().replace('-', ' '), 'category_reviews':category_reviews}
    return render(request, template_name='main/category.html', context=context)

class ReviewDetailView(DetailView):
    model = Review
    template_name = 'main/review_detail.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ReviewDetailView, self).get_context_data()
        review = get_object_or_404(Review, id=self.kwargs['pk'])
        total_likes = review.total_likes()
        context['total_likes'] = total_likes
        return context

class ReviewCreateView(LoginRequiredMixin, CreateView):
    model = Review
    form_class = ReviewCreateForm
    template_name = 'main/review_form.html'

    def form_valid(self, form):
        form.instance.publisher = self.request.user
        return super().form_valid(form)

class AddCommentView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = AddCommentForm
    template_name = 'main/add_comment.html'

    def form_valid(self, form):
        form.instance.name = self.request.user
        form.instance.review_id = self.kwargs['pk']
        return super().form_valid(form)
    
    def get_success_url(self):
          review_id = self.kwargs['pk']
          return reverse_lazy('review-detail', kwargs={'pk': review_id})


class ReviewUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Review
    form_class = ReviewCreateForm

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

def LikeView(request, pk):
    review = get_object_or_404(Review, id=request.POST.get('review_id'))
    review.likes.add(request.user)
    return HttpResponseRedirect(reverse('review-detail', args=[str(pk)]))