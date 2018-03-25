from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings

from web.views import HomeView, ContactView, LoginSignupView, \
CategoriesView, LoginView, UserSignup, MarketView, FishDetailsView, PayView

urlpatterns = [

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^market/$', MarketView.as_view(), name='market'),
    url(r'^contact/$', ContactView.as_view(), name='contact'),
    url(r'^login_signup/$', LoginSignupView.as_view(), name='index'),
    url(r'^categories/$', CategoriesView.as_view(),name='categories'),
    url(r'^pay/$', PayView.as_view(),name='pay'),
    url(r'^login/$', LoginView.as_view(),name='login'),
    url(r'^signup/$', UserSignup.as_view(),name='signup'),
    url(r'^logout/$', 'web.views.logout_view', name='logout'),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
       {'document_root': settings.MEDIA_ROOT, }),
    url(r'^fish/details/(?P<fish_id>\d+)/$', FishDetailsView.as_view(), name='fish_details'),
]