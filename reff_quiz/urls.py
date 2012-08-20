from django.conf.urls import patterns, include, url
from django.contrib.auth.views import password_reset, password_reset_done, password_change, password_change_done
from django.views.generic.simple import direct_to_template

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'reff_quiz.views.index', name='index'),
    # url(r'^reff_quiz/', include('reff_quiz.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^', direct_to_template, {'template': 'index.html'}),
    url(r'^', include('registration.backends.default.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('',
    url(r'^profile/$', direct_to_template, {'template': 'registration/profile.html'}),
    url(r'^password_reset/$', password_reset, {'template_name': 'registration/password_reset.html'}),
    url(r'^password_reset_done/$', password_reset_done, {'template_name': 'registration/password_reset_done.html'}),
    url(r'^password_change/$', password_change, {'template_name': 'registration/password_change.html'}),
    url(r'^password_change_done/$', password_change_done, {'template_name': 'registration/password_change_done.html'}),
)
