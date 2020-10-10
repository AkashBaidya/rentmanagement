"""rentmanagement URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.conf.urls import url
from django.contrib.auth import views

from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView

from django.contrib.auth import views as auth_views
from rentmanagement.views import dashboard_view
from django.contrib.auth.views import LogoutView
from rentmanagement.views import sites_input_view
from rentmanagement.views import person_input_view
from rentmanagement.views import property_input_view
from rentmanagement.views import agreement_input_view
from rentmanagement.views import agreement_view
from rentmanagement.views import sites_view
from rentmanagement.views import properties_view
from rentmanagement.views import person_view
from rentmanagement.views import error_view
from rentmanagement.views import agreement_detail_view
from rentmanagement.views import agreement_detail_view_activate

from rentmanagement.views import rent_input_view
from rentmanagement.views import rent_input_view_new
from rentmanagement.views import rent_delete_view
from rentmanagement.views import rent_delete_view_new
from rentmanagement.views import advance_delete_view
from rentmanagement.views import advance_delete_view_new
from rentmanagement.views import adv_input_view_new
from rentmanagement.views import rent_detail_view
from rentmanagement.views import advance_input_view
from rentmanagement.views import advance_detail_view
from rentmanagement.views import security_input_view
from rentmanagement.views import security_detail_view
from rentmanagement.views import sites_edit_view
from rentmanagement.views import person_edit_view
from rentmanagement.views import agreement_detail_view_agrm
from rentmanagement.views import agreement_edit_view

from rentmanagement.views import agreement_activated_view

from rentmanagement.views import update_agreement_status_view
from rentmanagement.views import update_agreement_status_new_view

from rentmanagement.views import autocomplete_div_view
from rentmanagement.views import autocomplete_postcode_view

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('accounts/login/', auth_views.LoginView.as_view(template_name="agreement/login.html"), name='login'),
    # path('accounts/', include('django.contrib.auth.urls')),
    # url(r'^login/$', auth_views.login, {'template_name': 'agreement/login.html'}, name='login'),
    url( r'^login/$',auth_views.LoginView.as_view(template_name="agreement/login.html"), name="login"),
    path('accounts/profile/',dashboard_view,name='dashboard_view'),
    path('sites_input_view/',sites_input_view,name='sites_input_view'),
    url(r'^sites_edit_view/?(?P<id>[^/]+)/$', sites_edit_view, name="sites_edit_view"),
    url(r'^person_edit_view/?(?P<id>[^/]+)/$', person_edit_view, name="person_edit_view"),
    url(r'^rent_delete_view/?(?P<id>[^/]+)/$', rent_delete_view, name="rent_delete_view"),
    url(r'^rent_delete_view_new/?(?P<id>[^/]+)/$', rent_delete_view_new, name="rent_delete_view_new"),
    url(r'^advance_delete_view/?(?P<id>[^/]+)/$', advance_delete_view, name="advance_delete_view"),
    url(r'^advance_delete_view_new/?(?P<id>[^/]+)/$', advance_delete_view_new, name="advance_delete_view_new"),
    path('sites/',sites_view,name='sites_view'),
    path('update_agr_status/<id>/',update_agreement_status_view,name='update_agreement_status_view'),
    path('update_agr_status_new/<id>/',update_agreement_status_new_view,name='update_agreement_status_new_view'),
    path('person_input/',person_input_view,name='person_input_view'),
    path('person/',person_view,name='person_view'),
    path('error/',error_view,name='error_view'),
    path('property_input/',property_input_view,name='property_input_view'),
    path('property/',properties_view,name='properties_view'),
    path('agreement/',agreement_input_view,name='agreement_input_view'),
    url(r'^agreement_edit/?(?P<id>[^/]+)/$', agreement_edit_view, name="agreement_edit_view"),
    # path('agreement_edit/',agreement_edit_view,name='agreement_edit_view'),
    path('agreement_result/',agreement_view,name='agreement_view'),
    path('agreement_final_result/',agreement_activated_view,name='agreement_activated_view'),
    url(r'^agreement/?(?P<pk>[^/]+)/$', agreement_detail_view, name="agreement_detail_view"),
    url(r'^agreement_detail_activate/?(?P<pk>[^/]+)/$', agreement_detail_view_activate, name="agreement_detail_view_activate"),
    url(r'^agreement_rent/(?P<pk>\d+)/$', agreement_detail_view_agrm, name="agreement_detail_view_agrm"),
    url(r'^rents/?(?P<ag>[^/]+)/$', rent_detail_view, name="rent_detail_view"),
    url(r'^rent_input_view_new/?(?P<id>[^/]+)/$', rent_input_view_new, name="rent_input_view_new"),
    url(r'^adv_input_view_new/?(?P<id>[^/]+)/$', adv_input_view_new, name="adv_input_view_new"),
    path('rent_input_view/',rent_input_view,name='rent_input_view'),
    url(r'^securities/?(?P<ag>[^/]+)/$', security_detail_view, name="rent_security_view"),
    path('security_input_view/',security_input_view,name='security_input_view'),
    url(r'^advancepayments/?(?P<ag>[^/]+)/$', advance_detail_view, name="advance_detail_view"),
    path('advance_input_view/',advance_input_view,name='advance_input_view'),
    # path('success/', views.success, name='success'),
    url(r'^autocomplete_div_view/', autocomplete_div_view,name='autocomplete_div_view'),
    url(r'^autocomplete_postcode_view/', autocomplete_postcode_view,name='autocomplete_postcode_view'),
    url( r'^logout/$',auth_views.LogoutView.as_view(), {'next_page': '/'},name="logout"),
    # url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name='logout'),


    # path('accounts/', include('django.contrib.auth.urls')),
]
