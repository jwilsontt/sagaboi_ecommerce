from django.conf.urls import url

from .views import (ProductListView,
                            # product_list_view,
                            # ProductDetailView,
                            ProductDetailSlugView,
                            # product_detail_view,
                            # ProductFeaturedListView,
                            # ProductFeaturedDetailView
                            )

# from .views import home_page, about_page, contact_page, login_page, register_page

urlpatterns = [
    url(r'^$', ProductListView.as_view(), name='list'),
    url(r'^(?P<slug>[\w-]+)/$', ProductDetailSlugView.as_view(), name='detail'),
]
