from django.conf.urls import include, url
from django.contrib import admin

from web.views import HomeView, ContactView, LoginSignupView, CategoriesView, LoginView, UserSignup

urlpatterns = [

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^contact/$', ContactView.as_view(), name='contact'),
    url(r'^login_signup/$', LoginSignupView.as_view(), name='index'),
    url(r'^categories/$', CategoriesView.as_view(),name='categories'),
    url(r'^login/$', LoginView.as_view(),name='login'),
    url(r'^signup/$', UserSignup.as_view(),name='signup'),
    url(r'^logout/$', 'web.views.logout_view', name='logout')
]