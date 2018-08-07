from django.conf.urls import include, url

from django.contrib import admin
from django.utils.translation import ugettext_lazy as _


urlpatterns = [
    # Examples:
    # url(r'^$', 'myproject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
]

admin.site.site_header = _("Site Administration")
admin.site.site_title = _("My Site Admin")


admin.site.site_header = "SPINAL CORRECTION SYSTEM"
admin.site.site_title = "SPINAL CORRECTION SYSTEM PORTAL"
admin.site.index_title = "WELCOME TO SPINAL CORRECTION SYSTEM"