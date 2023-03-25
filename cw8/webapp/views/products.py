from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView
from webapp.forms import ProductForm
from webapp.models import Product


class ProductCreateView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    template_name = 'product_create.html'
    model = Product
    form_class = ProductForm
    success_message = 'Статья создана'

    def get_success_url(self):
        return reverse('product_detail', kwargs={'pk': self.object.pk})


class ProductDetailView(DetailView):
    model = Product
    template_name = 'product.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product = self.object
        reviews = product.reviews.all()
        context['reviews'] = reviews
        return context


class ProductUpdateView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    template_name = 'product_update.html'
    form_class = ProductForm
    model = Product
    success_message = 'Статья обновлена'

    def get_success_url(self):
        return reverse('product_detail', kwargs={'pk': self.object.pk})


class ProductDeleteView(SuccessMessageMixin, LoginRequiredMixin, DeleteView):
    template_name = 'product_confirm_delete.html'
    model = Product
    success_url = reverse_lazy('index')
    success_message = 'Статья удалена'







