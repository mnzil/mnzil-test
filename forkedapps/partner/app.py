from django.conf.urls import url, include

from oscar.core.application import Application
from oscar.core.loading import get_class


class BasePartnerApplication(Application):
    name = 'partner'
    partner_list_view = get_class('partner.views', 'PartnerList')
    partner_view = get_class('partner.views', 'PartnerView')
    
    def get_urls(self):
        urlpatterns = super(BasePartnerApplication, self).get_urls()
        urlpatterns += [
           url(r'^$', self.partner_list_view.as_view(), name='partner_list'),
           url(r'^(?P<pk>\d+)/$',
                self.partner_view.as_view(), name='partner_detail'),
    ]
        return self.post_process_urls(urlpatterns)


application = BasePartnerApplication()

