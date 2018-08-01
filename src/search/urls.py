from django.conf.urls import url

from .views import (
                    SearchProductView,
                    )

# from .views import home_page, about_page, contact_page, login_page, register_page

urlpatterns = [
    url(r'^$', SearchProductView.as_view(), name='query'),
]
