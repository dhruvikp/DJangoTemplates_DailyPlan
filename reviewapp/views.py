from django.shortcuts import render

from django.views import View
from django.http import HttpResponse, HttpResponseRedirect
from .forms import ReviewForm
from django.views.generic.base import TemplateView
from .models import Review

class IndexClass(View):
    def get(self, request):
        return HttpResponse("This is rview app from index page")


class ReviewView(View):
    def get(self, request):
        form = ReviewForm()
        return render(request, "reviewapp/review.html", {"form": form})
    
    def post(self, request):
        form = ReviewForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect("thank-you")
        
        return render(request, "reviewapp/review.html", {"form": form})

class ReviewListView(TemplateView):
    template_name="reviewapp/thank-you.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        review = Review.objects.all()
        context["review"] = review
        return context
    