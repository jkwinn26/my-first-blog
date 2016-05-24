"""
 esat url definitions
"""
from django.conf.urls import patterns, include, url
from . import views

urlpatterns = patterns('',
    url(r'^$', views.esat_index, name='esat_index'),
    url(r'^employee/new$', views.employee_new, name='esat_add_emp'),
    url(r'^employee/list/$', views.employee_list, name='esat_emp_list'),
    url(r'^employee/(?P<pk>[0-9]+)/edit/$', views.employee_edit, name='esat_edit_emp'),
    #url(r'^employee/(?P<pk>[0-9]+)/terminate/$', views.terminate_employee, name='esat_term_emp'),
    #url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
    #url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
)
