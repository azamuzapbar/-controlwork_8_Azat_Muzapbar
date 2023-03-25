from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from webapp.forms import ReviewForm
from webapp.models import Product, Review


class ReviewCreateView(CreateView):
    template_name = 'review/review_create.html'
    form_class = ReviewForm

    def form_valid(self, form):
        product_pk = self.kwargs['pk']
        author = form.cleaned_data['author']
        text = form.cleaned_data['text']
        rating = form.cleaned_data['rating']
        product = get_object_or_404(Product, pk=product_pk)
        Review.objects.create(product=product, author=author, text=text, rating=rating)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('product_detail', kwargs={'pk': self.kwargs['pk']})

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['product_pk'] = self.kwargs['pk']
        return kwargs


class ReviewUpdateView(LoginRequiredMixin, UpdateView):
    model = Review
    form_class = ReviewForm
    template_name = 'review/review_update.html'
    pk_url_kwarg = 'pk'

    def get_success_url(self):
        return reverse_lazy('product_detail', kwargs={'pk': self.object.product.pk})

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['product_pk'] = self.object.product_id
        return kwargs

    def dispatch(self, request, *args, **kwargs):
        review = get_object_or_404(Review, pk=self.kwargs['pk'])
        if review.author != self.request.user:
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)




class DeleteReview(LoginRequiredMixin, DeleteView):
    model = Review
    template_name = 'review/review_confirm_delete.html'
    success_url = reverse_lazy('product_detail')

    def get_success_url(self):
        return reverse_lazy('product_detail', kwargs={'pk': self.object.product.pk})

    def dispatch(self, request, *args, **kwargs):
        review = self.get_object()
        if review.author != self.request.user:
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)