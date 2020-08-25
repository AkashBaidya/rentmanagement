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
from agreement.models import AdvancePaymentline
from agreement.models import Site
from agreement.models import Person
from agreement.models import Properties
from django.shortcuts import get_object_or_404

from django.core import validators

from django.db.models import Sum

import numpy as np


# Create your views here.
def dashboard_view(request):
    return render(request, 'agreement/dashboard.html')
def error_view(request):
    return render(request, 'agreement/error.html')
def sites_input_view(request):
    form = SiteForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect(sites_view)
    return render(request, 'agreement/sites.html', {'form': form})
def sites_edit_view(request,id):
    obj=get_object_or_404(Site,id=id)
    form = SiteForm(request.POST or None,instance=obj)
    if form.is_valid():
        form.save()
        return redirect(sites_view)
    else:
        messages.success(request,"Please try again")
    return render(request, 'agreement/sites.html', {'form': form})





def rent_delete_view(request,id):
    # obj=get_object_or_404(Rentline,id=id)
    rent= Rentline.objects.filter(id=id)
    # print(context)
    # form = SiteForm(request.POST or None,instance=obj)
    # if form.is_valid():
    #     form.save()
    #     return redirect(sites_view)
    # else:
    #     messages.success(request,"Please try again")
    return render(request, 'agreement/delete_rent.html',context={'rent':rent})
def rent_delete_view_new(request,id):
    # obj=get_object_or_404(Rentline,id=id)
    rent= Rentline.objects.filter(id=id)
    rent.delete()
    return redirect(agreement_view)

    # print(context)
    # form = SiteForm(request.POST or None,instance=obj)
    # if form.is_valid():
    #     form.save()
    #     return redirect(sites_view)
    # else:
    #     messages.success(request,"Please try again")
    return render(request, 'agreement/delete_rent.html',context={'rent':rent})


def advance_delete_view(request,id):
    # obj=get_object_or_404(Rentline,id=id)
    rent= AdvancePaymentline.objects.filter(id=id)
    # print(context)
    # form = SiteForm(request.POST or None,instance=obj)
    # if form.is_valid():
    #     form.save()
    #     return redirect(sites_view)
    # else:
    #     messages.success(request,"Please try again")
    return render(request, 'agreement/delete_advance.html',context={'rent':rent})
def advance_delete_view_new(request,id):
    # obj=get_object_or_404(Rentline,id=id)
    rent= AdvancePaymentline.objects.filter(id=id)
    rent.delete()
    return redirect(agreement_view)

    # print(context)
    # form = SiteForm(request.POST or None,instance=obj)
    # if form.is_valid():
    #     form.save()
    #     return redirect(sites_view)
    # else:
    #     messages.success(request,"Please try again")
    return render(request, 'agreement/delete_advance.html',context={'rent':rent})

def person_edit_view(request,id):
    obj=get_object_or_404(Person,id=id)
    form = PersonForm(request.POST or None,instance=obj)
    if form.is_valid():
        form.save()
        return redirect(person_view)
    else:
        messages.success(request,"Please try again")
    return render(request, 'agreement/person_update.html', {'form': form})

def agreement_edit_view(request,id):
    obj=get_object_or_404(Agreement,id=id)
    form = AgreementForm(request.POST or None,instance=obj)
    if form.is_valid():
        form.save()
        return redirect(agreement_detail_view)
    else:
        messages.success(request,"Please try again")
    return render(request, 'agreement/agreement.html', {'form': form})
def person_input_view(request):
    form = PersonForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect(person_view)
    return render(request, 'agreement/person.html', {'form': form})

def property_input_view(request):
    form = PropertyForm(request.POST or None)
    print(request.POST)

    # if form.is_valid():
    #     form.save()
    #     return redirect(properties_view)
    #
    size_shop_total=0
    if request.POST:
        if form['site1'].value()=='None':
            site1=0

        else:
            site1=form['site1'].value()
            e1 = Site.objects.get(id=site1)
            size_shop_total=size_shop_total+e1.site_size
        print(form['site1'].value())
        if form['site2'].value()=='':
            site2=0

        else:
            site2=form['site2'].value()
            e2 = Site.objects.get(id=site2)
            size_shop_total=size_shop_total+e2.site_size
        if form['site3'].value()=='':
            site3=0
        else:
            site3=form['site3'].value()
            e3 = Site.objects.get(id=site3)
            size_shop_total=size_shop_total+e3.site_size
        if form['site4'].value()=='':
            site4=0
        else:
            site4=form['site4'].value()
            e4 = Site.objects.get(id=site4)
            size_shop_total=size_shop_total+e4.site_size

        property_size =form['property_size'].value()

        print(type(size_shop_total))
        print(type(property_size))






        # =e1.site_size+e2.site_size+e3.site_size+e4.site_size


        not_permitted=1

        if size_shop_total!=int(property_size):
            not_permitted=0;
        print(form.is_valid())


        if form.is_valid() and not_permitted==1:
            form.save()
            return redirect(properties_view)

        else:
            # print("else")
            return render(request,'agreement/error.html', {'msg': 'Property Size and Site size does not match.'})

    return render(request, 'agreement/property.html', {'form': form})
def rent_input_view(request):
    form = RentlineForm(request.POST or None)
    if form.is_valid():
        post=form.save()
        e = Agreement.objects.get(agrm_id=post.agreement_ref)

        return redirect(agreement_detail_view,pk=e.id)
    return render(request, 'agreement/rent.html', {'form': form})

def rent_input_view_new(request,id):
    form = RentlineForm(request.POST or None)
    not_permitted=1
    e = Agreement.objects.get(id=id)
    total_months=e.total_months

    rent=e.rentline.aggregate(Sum('total_months'))


    for item in rent.values():
        a=item
    print(type(a))
    passed=1
    if a is None:
        passed=0


    if passed==1:
        if a>total_months:
            not_permitted=0
            print("Sum of months in agreement" +str(a))
            print("Total months in the agreement"+str(total_months))


        # print("Not permitted value"+str(not_permitted))
        print(form.is_valid())
        # print(form)

    print(form.is_valid())
    # request.POST._mutable=True
    form.agreement_ref=e
    # form.data['agreement_ref']=e.agrm_id
    # print(form.agreement_ref)
    # print(form.data['start_period'])
    # print(form.data['agreement_ref'])
    print(form.errors)
    print(form)
    if not_permitted==1:
        if form.is_valid():
            post=form.save(commit=False)
            if a is None:
                final=int(form['total_months'].value())
                if final>total_months:
                    return render(request,'agreement/error.html', {'msg': 'Added rent month is bigger'})
            else:
                final=int(form['total_months'].value())+a
                if final>total_months:
                    return render(request,'agreement/error.html', {'msg': 'Added rent month is bigger'})


            post=form.save()
            print(a)
            print(total_months)

            post.agreement_ref=e
            post.save()
            return redirect(agreement_detail_view,pk=e.id)

    elif not_permitted==0:
        return render(request,'agreement/error.html', {'msg': 'Rent Month Already exceeded'})
    return render(request, 'agreement/rent.html', {'form': form})




def adv_input_view_new(request,id):
    form = AdvancePaymentlineForm(request.POST or None)


    not_permitted=1
    e = Agreement.objects.get(id=id)
    total_amount=e.agrement_advance_amount
    rent=e.advanceline.aggregate(Sum('advance_adjustment_per_month'))
    print(rent)
    for item in rent.values():
        a=item
    print(type(a))
    passed=1
    if a is None:
        passed=0


    if passed==1:
        if a>total_amount:
            not_permitted=0
            print("Sum of months in agreement" +str(a))
            print("Total months in the agreement"+str(total_months))


        # print("Not permitted value"+str(not_permitted))
        print(form.is_valid())
        # print(form)

    print(form.is_valid())
    # request.POST._mutable=True
    form.agreement_ref=e
    # form.data['agreement_ref']=e.agrm_id
    # print(form.agreement_ref)
    # print(form.data['start_period'])
    # print(form.data['agreement_ref'])
    print(form.errors)
    print(form)
    if not_permitted==1:
        if form.is_valid():
            post=form.save(commit=False)
            if a is None:
                final=int(form['advance_adjustment_per_month'].value())
                if final>total_amount:
                    return render(request,'agreement/error.html', {'msg': 'Added Adjustment Amount is bigger'})
            else:
                final=int(form['total_months'].value())+a
                if final>total_amount:
                    return render(request,'agreement/error.html', {'msg': 'Added Adjustment Amount is bigger'})


            post=form.save()
            print(a)
            # print(total_months)

            post.agreement_ref=e
            post.save()
            return redirect(agreement_detail_view,pk=e.id)

    elif not_permitted==0:
        return render(request,'agreement/error.html', {'msg': 'Adjustment Amount Already exceeded'})
    return render(request, 'agreement/advance.html', {'form': form})







def security_input_view(request):
    form = SecuritylineForm(request.POST or None)
    if form.is_valid():
        form.save()
    return render(request, 'agreement/Security.html', {'form': form})
def advance_input_view(request):
    form = AdvancePaymentlineForm(request.POST or None)
    if form.is_valid():
        post=form.save()
        e = Agreement.objects.get(agrm_id=post.agreement_ref)

        return redirect(agreement_detail_view,pk=e.id)
        # return redirect('success')
        # return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    return render(request, 'agreement/advance.html', {'form': form})

def success(request):
    return HttpResponse("File successfully uploaded")

def agreement_input_view(request):
    form = AgreementForm(request.POST or None)



    if '_next' in request.POST and form.is_valid():
        post=form.save()
        return redirect(agreement_detail_view,pk=post.id)
    if '_save' in request.POST and form.is_valid():
        form.save()
        return redirect(agreement_view)

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

    rent_rou=total_rou_calculation(pk)
    # agreement = get_object_or_404(Agreement,id=pk)
    agreement=Agreement.objects.prefetch_related('rentline').get(id=pk)

    e = Agreement.objects.get(id=pk)
    rent=e.rentline.all()
    security=e.securityline.all()
    advance=e.advanceline.all()
    print(agreement)
    print(rent)
    print(advance)
    # users = User.objects.get(id=pk).prefetch_related('item_set')
    # agreement=agreement.rent
    return render(request, 'agreement/agreement_detail.html', context={'agreement': agreement, 'rent':rent,'security':security, 'advance':advance,'rent_rou':rent_rou})
def agreement_detail_view_agrm(request,pk):
    # agreement = get_object_or_404(Agreement,id=pk)
    agreement=Agreement.objects.prefetch_related('rentline').get(agrm_id=pk)

    e = Agreement.objects.get(agrm_id=pk)
    rent=e.rentline.all()
    security=e.securityline.all()
    advance=e.advanceline.all()
    print(agreement)
    print(rent)
    print(advance)
    # users = User.objects.get(id=pk).prefetch_related('item_set')
    # agreement=agreement.rent
    return render(request, 'agreement/agreement_detail.html', context={'agreement': agreement, 'rent':rent,'security':security, 'advance':advance})


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


def total_rou_calculation(pk):

    #get agreement related rent objects

    e = Agreement.objects.get(id=pk)
    count=e.rentline.all().count()
    b=e.rentline.all()




    # print(len(b))
    month=0;
    total_pv=0;

    for i in b.values_list():

        # print(i[4])
        present_value=np.pv(.10/12,int(i[5]),-(int(i[4])-int(i[6])),0)
        # print(present_value)

        rate=.10/12
        future_value=present_value/(1+rate)**month
        # print("hash")
        # print(future_value)
        total_pv=total_pv+future_value
        # print("hash")
        month=month+i[5]

    print(total_pv)
    print(e.agrement_advance_amount)

    total_rou=total_pv+int(e.agrement_advance_amount)
    print(total_rou)

    return total_rou
