from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("user_account.urls")),
    path("api/", include("categories.urls")),
    path("api/", include("products.urls")),
    path("api/", include("home_page_display.urls")),

]


if settings.DEBUG: 
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
