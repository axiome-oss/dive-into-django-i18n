
from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.i18n import i18n_patterns

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
]

urlpatterns += i18n_patterns(
    url(r'^test$', 'your_package.views.test', name='test'),
    url(r'^user/([0-9]+)$', 'your_package.views.user'),
)
