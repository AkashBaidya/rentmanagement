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

from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from rentmanagement import views

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
from rentmanagement.views import agreement_detail_view

from rentmanagement.views import rent_input_view
from rentmanagement.views import rent_detail_view
from rentmanagement.views import advance_input_view
from rentmanagement.views import advance_detail_view
from rentmanagement.views import security_input_view
from rentmanagement.views import security_detail_view

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('accounts/', include('django.contrib.auth.urls')),
    # url(r'^login/$', auth_views.login, {'template_name': 'agreement/login.html'}, name='login'),
    url( r'^login/$',auth_views.LoginView.as_view(template_name="agreement/login.html"), name="login"),
    path('dashboard/',dashboard_view,name='dashboard_view'),
    path('sites_input_view/',sites_input_view,name='sites_input_view'),
    path('sites/',sites_view,name='sites_view'),
    path('person_input/',person_input_view,name='person_input_view'),
    path('person/',person_view,name='person_view'),
    path('property_input/',property_input_view,name='property_input_view'),
    path('property/',properties_view,name='properties_view'),
    path('agreement/',agreement_input_view,name='agreement_input_view'),
    path('agreement_result/',agreement_view,name='agreement_view'),
    url(r'^agreement/?(?P<pk>[^/]+)/$', agreement_detail_view, name="agreement_detail_view"),
    url(r'^rents/?(?P<ag>[^/]+)/$', rent_detail_view, name="rent_detail_view"),
    path('rent_input_view/',rent_input_view,name='rent_input_view'),
    url(r'^securities/?(?P<ag>[^/]+)/$', security_detail_view, name="rent_security_view"),
    path('security_input_view/',security_input_view,name='security_input_view'),
    url(r'^advancepayments/?(?P<ag>[^/]+)/$', advance_detail_view, name="advance_detail_view"),
    path('advance_input_view/',advance_input_view,name='advance_input_view'),
    path('success/', views.success, name='success'),
    url( r'^logout/$',auth_views.LogoutView.as_view(template_name="agreement/login.html"), name="logout"),


    # path('accounts/', include('django.contrib.auth.urls')),
]
