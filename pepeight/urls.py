from django.conf.urls import include, url
from django.contrib import admin
import debug_toolbar

from hettinger.views import Pep8View

urlpatterns = [
    url(r'^$', Pep8View.as_view(), name="home"),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^__debug__/', include(debug_toolbar.urls)),
]
