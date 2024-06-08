from django.shortcuts import render
from django.shortcuts import HttpResponseRedirect
from .forms import ReviewForm
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, FormView, CreateView

from .models import Review


# Create your views here.
# class ReviewView(FormView):
#     form_class = ReviewForm
#     template_name = "reviews/review.html"
#     success_url = "/thank-you"
#
#     def form_valid(self, form):
#         # This method is called when valid form data has been POSTed.
#         # It should return an HttpResponse.
#         form.save()
#         return super().form_valid(form)


class ReviewView(CreateView):
    model = Review
    form_class = ReviewForm
    template_name = "reviews/review.html"
    success_url = "/thank-you"


class ThankYouView(TemplateView):
    template_name = "reviews/thank-you.html"


class ReviewListView(ListView):
    template_name = "reviews/review_list.html"
    model = Review
    context_object_name = "reviews"


class ReviewDetail(DetailView):
    template_name = "reviews/review_detail.html"
    model = Review
