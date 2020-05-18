from django.shortcuts import render

from django.db import models

from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect

from django.template import loader
from django.http import HttpResponse
from agreement.forms import SiteForm
from agreement.forms import PersonForm
from agreement.forms import PropertyForm
from agreement.forms import AgreementForm
from agreement.forms import RentlineForm
from agreement.forms import SecuritylineForm
from agreement.forms import AdvancePaymentlineForm

from agreement.models import Agreement
from agreement.models import Rentline
from agreement.models import Site
from agreement.models import Person
from agreement.models import Properties
from django.shortcuts import get_object_or_404


# Create your views here.
def dashboard_view(request):
    return render(request, 'agreement/dashboard.html')
def sites_input_view(request):
    form = SiteForm(request.POST or None)
    if form.is_valid():
        form.save()
    return render(request, 'agreement/sites.html', {'form': form})
def person_input_view(request):
    form = PersonForm(request.POST or None)
    if form.is_valid():
        form.save()
    return render(request, 'agreement/person.html', {'form': form})
def property_input_view(request):
    form = PropertyForm(request.POST or None)
    if form.is_valid():
        form.save()
    return render(request, 'agreement/property.html', {'form': form})
def rent_input_view(request):
    form = RentlineForm(request.POST or None)
    if form.is_valid():
        form.save()
    return render(request, 'agreement/rent.html', {'form': form})
def security_input_view(request):
    form = SecuritylineForm(request.POST or None)
    if form.is_valid():
        form.save()
    return render(request, 'agreement/Security.html', {'form': form})
def advance_input_view(request):
    form = AdvancePaymentlineForm(request.POST or None)
    if form.is_valid():
        form.save()
        # return redirect('success')
        # return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    return render(request, 'agreement/advance.html', {'form': form})

def success(request):
    return HttpResponse("File successfully uploaded")

def agreement_input_view(request):
    form = AgreementForm(request.POST or None)
    if form.is_valid():
        form.save()
    return render(request, 'agreement/agreement.html', {'form': form})
def sites_view(request):
    all_sites = Site.objects.all()
    return render(request, 'agreement/sites_result.html', {'all_sites': all_sites})
def rent_detail_view(request):

    rent= Agreement.objects.all().select_related('rentline').values()
    # rent= Rentline.objects.all().select_related('agreement_ref').values()
    return render(request, 'agreement/rent_detail.html', context={'rent': rent})


def rent_detail_view(request,ag):

    e = Agreement.objects.get(id=ag)

    #working
    # e = Agreement.objects.get()
    rent=e.rentline.all()
#working
    # rent= Agreement.objects.all().prefetch_related('rentline')

    # Agreement.objects.raw('SELECT agreement.* from agreement LEFT OUTER JOIN '
    #              '"foo" ON (auth_user.id = foo.id AND '


    # print(rent)
    # agreement = get_object_or_404(Agreement,id=pk)
    # users = User.objects.get(id=pk).prefetch_related('item_set')
    # agreement=agreement.rent
    return render(request, 'agreement/rent_detail.html', context={'rent': rent})
def security_detail_view(request,ag):
    # agreement = get_object_or_404(Agreement,id=pk)
    e = Agreement.objects.get(id=ag)
    rent=e.securityline.all()
    # users = User.objects.get(id=pk).prefetch_related('item_set')
    # agreement=agreement.rent
    return render(request, 'agreement/security_detail.html', context={'rent': rent})
def advance_detail_view(request,ag):
    # agreement = get_object_or_404(Agreement,id=pk)
    e = Agreement.objects.get(id=ag)
    rent=e.advanceline.all()
    # users = User.objects.get(id=pk).prefetch_related('item_set')
    # agreement=agreement.rent
    return render(request, 'agreement/advance_detail.html', context={'rent': rent})

def agreement_view(request):
    all_agreement = Agreement.objects.all()
    return render(request, 'agreement/agreement_result.html', {'all_agreement': all_agreement})
def agreement_detail_view(request,pk):
    # agreement = get_object_or_404(Agreement,id=pk)
    agreement=Agreement.objects.prefetch_related('rentline').get(id=pk)
    # users = User.objects.get(id=pk).prefetch_related('item_set')
    # agreement=agreement.rent
    return render(request, 'agreement/agreement_detail.html', context={'agreement': agreement})


def properties_view(request):
    all_properties = Properties.objects.all()
    return render(request, 'agreement/property_results.html', {'all_properties': all_properties})

def person_view(request):
    all_person = Person.objects.all()
    return render(request, 'agreement/person_result.html', {'all_person': all_person})
    # if request.method == 'POST':
    #     form = SiteForm(request.POST)
    #     if form.is_valid():
    #         pass
    #
    #         # u = form.save()
    #         # users = Site.objects.all()
    #         #
    #         # return render(request, 'display.html', {'users': users})
    #
    #
    #
    # else:
    #     form_class = SiteForm
    #
    # return render(request, 'sites.html', {
    #     'form': form_class,
    # })
