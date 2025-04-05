from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from wagtail.admin import urls as wagtailadmin_urls
from wagtail.documents import urls as wagtaildocs_urls
from wagtail import urls as wagtail_urls

from django.conf.urls.i18n import i18n_patterns

urlpatterns = [

    path('cms/', include(wagtailadmin_urls)),
    path('documents/', include(wagtaildocs_urls)),
    path('admin/', admin.site.urls),
    path("base/", include("base.urls")),
    path("events/", include("events.urls")),
    # path("locations/", include("locations.urls")),
    path("jobs/", include("jobs.urls")),
]

# translations
urlpatterns += i18n_patterns(
    path("", include(wagtail_urls)),
    prefix_default_language=False,
)

urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
