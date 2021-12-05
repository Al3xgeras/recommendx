from django.urls import path
from .views import (ReviewListView, ReviewDetailView, 
                    ReviewCreateView, ReviewUpdateView,
                    ReviewDeleteView, TopReviewsListView,
                    LatestReviewsListView, UserReviewListView, 
                    LikeView, AddCommentView, CategoryView, searchResultsView)
from . import views

urlpatterns = [
    path('', ReviewListView.as_view(), name = 'homepage'),
    path('user/<str:username>', UserReviewListView.as_view(), name = 'user-reviews'),
    path('top_reviews/', TopReviewsListView.as_view(), name = 'top-reviews'),
    path('latest_reviews/', LatestReviewsListView.as_view(), name = 'latest-reviews'),
    path('review/<int:pk>/', ReviewDetailView.as_view(), name = 'review-detail'),
    path('review/new/', ReviewCreateView.as_view(), name = 'review-create'),
    path('review/<int:pk>/update/', ReviewUpdateView.as_view(), name = 'review-update'),
    path('review/<int:pk>/delete/', ReviewDeleteView.as_view(), name = 'review-delete'),
    path('like/<int:pk>/', LikeView, name = 'like-review'),
    path('review/<int:pk>/comment', AddCommentView.as_view(), name = 'add-comment'),
    path('category/<str:cat>/', CategoryView, name='category'),
    path('search_results/', searchResultsView, name='search-results'),
]
