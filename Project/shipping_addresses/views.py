from django.shortcuts import render
from .forms import ShippingAddressForm
from .models import ShippingAddress
from django.views.generic import ListView


class ShippingAddressListView(ListView):
    model = ShippingAddress
    template_name = 'shipping_addresses/shipping_addresses.html'

    def get_queryset(self):
        return ShippingAddress.objects.filter(user=self.request.user).order_by('-default')


def create(request):
    form = ShippingAddressForm()
    return render(request, 'shipping_addresses/create.html', {'form': form})
