import warnings
from django.contrib import messages
from django.core.paginator import InvalidPage
from django.utils.http import urlquote
from django.http import HttpResponsePermanentRedirect, Http404
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import DetailView, TemplateView
from django.utils.translation import ugettext_lazy as _

from oscar.core.loading import get_class, get_model
from oscar.apps.catalogue.signals import product_viewed


from django.views.generic.list import ListView
from django.utils import timezone

Partner = get_model('partner', 'partner')


class PartnerList(ListView):

    model = Partner
    template_name = 'partner/list.html'

    def get_context_data(self, **kwargs):
        context = super(PartnerList, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

    
class PartnerView(DetailView):
   
    model = Partner
    template_name = 'partner/detail.html'

   

    def get(self, request, **kwargs):
        """
        Ensures that the correct URL is used before rendering a response
        """
        self.object = partner = self.get_object()

       
        response = super(PartnerView, self).get(request, **kwargs)
        return response

    def get_object(self, queryset=None):
        # Check if self.object is already set to prevent unnecessary DB calls
        if hasattr(self, 'object'):
            return self.object
        else:
            return super(PartnerView, self).get_object(queryset)

