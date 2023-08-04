from django.urls import path
from . import views

urlpatterns = [
    path("", view= views.IndexClass.as_view(), name='index'),
    path("form", view=views.ReviewView.as_view(), name='reviewform'),
    path("thank-you", view=views.ReviewListView.as_view(), name="reviews")
]
