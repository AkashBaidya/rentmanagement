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


from agreement.forms import SiteEditForm
from agreement.forms import PersonEditForm
from agreement.forms import AgreementEditForm
from agreement.forms import PropertyEditForm

from agreement.models import Agreement
from agreement.models import Rentline
from agreement.models import AdvancePaymentline
from agreement.models import Site
from agreement.models import Person
from agreement.models import Properties
from agreement.models import LocalArea
from django.shortcuts import get_object_or_404

from django.core import validators

from django.db.models import Sum

import numpy as np

from django.http import JsonResponse

from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.csrf import csrf_exempt


from django.db.models import Max




# Create your views here.
@csrf_protect
@login_required
def dashboard_view(request):
    return render(request, 'agreement/dashboard.html')
def error_view(request):
    return render(request, 'agreement/error.html')


@login_required
def sites_input_view(request):
    form = SiteForm(request.POST or None)
    if form.is_valid():
        print(form)
        # print(request.POST['site_extension'].value())
        instance=form.save(commit=False)
        instance.site_code=instance.site_code.upper()
        if instance.site_type=='STORE':
            instance.site_extension=check_maximum_extension(request.POST['site_code'])
        else:
            print("Hello")
        instance.save()

        return redirect(sites_view)
    else:
        print(form.errors)
    return render(request, 'agreement/sites.html', {'form': form})

@login_required
def sites_edit_view(request,id):
    obj=get_object_or_404(Site,id=id)
    form = SiteEditForm(request.POST or None,instance=obj)
    if form.is_valid():
        form.save()
        return redirect(sites_view)
    else:
        messages.success(request,"Please try again")
    return render(request, 'agreement/sites_update.html', {'form': form})




@login_required
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

@login_required
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

@login_required
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


@login_required
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
@login_required
def person_edit_view(request,id):
    obj=get_object_or_404(Person,id=id)
    form = PersonEditForm(request.POST or None,instance=obj)
    if form.is_valid():
        form.save()
        return redirect(person_view)
    else:
        messages.success(request,"Please try again")
    return render(request, 'agreement/person_update.html', {'form': form})


@login_required
def property_edit_view(request,id):
    obj=get_object_or_404(Properties,id=id)
    form = PropertyEditForm(request.POST or None,instance=obj)
    if form.is_valid():
        form.save()
        return redirect(person_view)
    else:
        messages.success(request,"Please try again")
    return render(request, 'agreement/property_update.html', {'form': form})


@login_required
def agreement_edit_view(request,id):
    obj=get_object_or_404(Agreement,id=id)
    form = AgreementEditForm(request.POST or None,instance=obj)
    if form.is_valid():
        e=form.save()
        return redirect(agreement_detail_view,pk=e.id)
    else:
        messages.success(request,"Please try again")
    return render(request, 'agreement/agreement_update.html', {'form': form})


@login_required
def person_input_view(request):
    # print(PersonForm)
    #
    # print(request.POST)

    form = PersonForm(request.POST or None)


    print(form)
    if form.is_valid():

        # f=form.save()
        name=request.POST['name']
        phone=request.POST['phone']
        person_type=request.POST['person_type']
        nid=request.POST['nid']
        tin=request.POST['tin']
        email=request.POST['email']
        dealing_person_status=request.POST['dealing_person_status']
        division=request.POST['division']
        district=request.POST['district']
        thana=request.POST['thana']
        postcode=request.POST['postcode']
        village=request.POST['village']
        sis_supplier_code=request.POST['sis_supplier_code']
        name_of_dealing_person=request.POST['name_of_dealing_person']
        email_of_dealing_person=request.POST['email_of_dealing_person']
        relationship=request.POST['relationship']
        address=request.POST['address']

        instance=Person(name=name, phone=phone,person_type=person_type,nid=nid, tin=tin, email=email, dealing_person_status=dealing_person_status, division=division, district=district, thana=thana, village=village, postcode=postcode,address=address, sis_supplier_code=sis_supplier_code,name_of_dealing_person=name_of_dealing_person,email_of_dealing_person=email_of_dealing_person,relationship=relationship)
        instance.save()
        return redirect(person_view)
    return render(request, 'agreement/person.html', {'form': form})


@login_required
def property_input_view(request):
    form = PropertyForm(request.POST or None)
    #print(form)
    print(request.POST)
    #print("first test")

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

        print("size shop total"+str(size_shop_total))
        print("property size"+property_size)

        if size_shop_total!=int(property_size):
            not_permitted=0;
        #print(form.is_valid())


        if form.is_valid() and not_permitted==1:
            post=form.save(commit=False)
            # instance=form.save(commit=False)
            post.type=request.POST.get('type')
            post.desc=request.POST['desc']
            post.status=request.POST['status']
            post.property_size=request.POST['property_size']

            post.division=request.POST['division']
            post.district=request.POST['district']
            post.thana=request.POST['thana']

            post.postcode=request.POST['postcode']
            post.village=request.POST['village']

            # instance.number_of_owner=request.POST['number_of_owner']
            # instance.owner1=request.POST['owner1']
            # instance.owner2=request.POST['owner2']
            # instance.owner3=request.POST['owner3']
            # instance.owner4=request.POST['owner4']
            # instance.owner5=request.POST['owner5']
            #
            post.number_of_sites=request.POST['number_of_sites']
            # instance.site1=request.POST['site1']
            # instance.percentage_of_first_site=request.POST['percentage_of_first_site']
            #
            # instance.site2=request.POST['site2']
            # instance.percentage_of_second_site=request.POST['percentage_of_second_site']
            #
            # instance.site3=request.POST['site3']
            # instance.percentage_of_third_site=request.POST['percentage_of_third_site']
            #
            # instance.site4=request.POST['site4']
            # instance.percentage_of_fourth_site=request.POST['percentage_of_fourth_site']

            post.save()
            print("not error")
            print(request.POST['postcode'])
            # print(instance.save())
            return redirect(properties_view)

        else:
            # print("else")
            print(form.errors)
            print("error")
            return render(request,'agreement/error.html', {'msg': 'Property Size and Site size does not match.'})

    return render(request, 'agreement/property.html', {'form': form})


@login_required
def rent_input_view(request):
    form = RentlineForm(request.POST or None)
    if form.is_valid():
        post=form.save()
        e = Agreement.objects.get(agrm_id=post.agreement_ref)

        return redirect(agreement_detail_view,pk=e.id)
    return render(request, 'agreement/rent.html', {'form': form})



@login_required
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



@login_required
def adv_input_view_new(request,id):
    form = AdvancePaymentlineForm(request.POST or None)


    not_permitted=1
    e = Agreement.objects.get(id=id)
    total_amount=e.agreement_advance_amount
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






@login_required
def security_input_view(request):
    form = SecuritylineForm(request.POST or None)
    if form.is_valid():
        form.save()
    return render(request, 'agreement/Security.html', {'form': form})


@login_required
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


@login_required
def agreement_input_view(request):
    form = AgreementForm(request.POST or None)
    print(request.POST)



    if '_next' in request.POST and form.is_valid():
        post=form.save(commit=False)
        post.agreement_date=request.POST['agreement_date']
        post.effected_date_as_actual=request.POST['effected_date_as_actual']
        post.effected_date_as_per_agreement=request.POST['effected_date_as_per_agreement']
        post.agreement_cat_type=request.POST['agreement_cat_type']
        post.notice_period=request.POST['notice_period']
        post.file_no=request.POST['file_no']
        post.serial_no=request.POST['serial_no']
        post.agreement_advance_amount=request.POST['agreement_advance_amount']
        post.agreement_security_amount=request.POST['agreement_security_amount']
        site1=form['main_site'].value()
        print(site1)
        print(" test begin")
        print(post.properties.type)
        print("test end")
        post.properties.type='not available'
        print(post.properties.type)
        post.properties.save()
        post.agrm_id=create_id_for_agreement(post.main_site,post.file_no,post.serial_no)
        post.save()
        return redirect(agreement_detail_view,pk=post.id)
    else:
        print(form.errors)

    if '_save' in request.POST and form.is_valid():
        post=form.save(commit=False)
        post=form.save(commit=False)
        post.agreement_date=request.POST['agreement_date']
        post.effected_date_as_actual=request.POST['effected_date_as_actual']
        post.effected_date_as_per_agreement=request.POST['effected_date_as_per_agreement']
        post.agreement_cat_type=request.POST['agreement_cat_type']
        post.notice_period=request.POST['notice_period']
        post.file_no=request.POST['file_no']
        post.serial_no=request.POST['serial_no']
        post.agreement_advance_amount=request.POST['agreement_advance_amount']
        post.agreement_security_amount=request.POST['agreement_security_amount']
        site1=form['main_site'].value()

        post.agrm_id=create_id_for_agreement(post.main_site,post.file_no,post.serial_no)
        post.save()
        return redirect(agreement_view)
    else:
        print(form.errors)

    return render(request, 'agreement/agreement.html', {'form': form})

@login_required
def sites_view(request):
    all_sites = Site.objects.all()
    return render(request, 'agreement/sites_result.html', {'all_sites': all_sites})


@login_required
def rent_detail_view(request):

    rent= Agreement.objects.all().select_related('rentline').values()
    # rent= Rentline.objects.all().select_related('agreement_ref').values()
    return render(request, 'agreement/rent_detail.html', context={'rent': rent})

@login_required
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


@login_required
def security_detail_view(request,ag):
    # agreement = get_object_or_404(Agreement,id=pk)
    e = Agreement.objects.get(id=ag)
    rent=e.securityline.all()
    # users = User.objects.get(id=pk).prefetch_related('item_set')
    # agreement=agreement.rent
    return render(request, 'agreement/security_detail.html', context={'rent': rent})

@login_required
def advance_detail_view(request,ag):
    # agreement = get_object_or_404(Agreement,id=pk)
    e = Agreement.objects.get(id=ag)
    rent=e.advanceline.all()
    # users = User.objects.get(id=pk).prefetch_related('item_set')
    # agreement=agreement.rent
    return render(request, 'agreement/advance_detail.html', context={'rent': rent})
@login_required
def agreement_view(request):
    all_agreement = Agreement.objects.all()
    return render(request, 'agreement/agreement_result.html', {'all_agreement': all_agreement})

@login_required
def agreement_activated_view(request):
    all_agreement = Agreement.objects.filter(status__iexact='submitted')
    return render(request, 'agreement/agreement_activate_list.html', {'all_agreement': all_agreement})

@login_required
def agreement_detail_view(request,pk):

    rent_rou=total_rou_calculation(pk)
    # agreement = get_object_or_404(Agreement,id=pk)
    agreement=Agreement.objects.prefetch_related('rentline').get(id=pk)

    e = Agreement.objects.get(id=pk)
    rent=e.rentline.all()
    security=e.securityline.all()
    advance=e.advanceline.all()
    print(e.agreement_advance_amount)
    # print(agreement)
    # print(rent)
    # print(advance)
    # users = User.objects.get(id=pk).prefetch_related('item_set')
    # agreement=agreement.rent
    return render(request, 'agreement/agreement_detail.html', context={'agreement': agreement, 'rent':rent,'security':security, 'advance':advance,'rent_rou':rent_rou})

@login_required
def agreement_detail_view_activate(request,pk):

    rent_rou=total_rou_calculation(pk)
    # agreement = get_object_or_404(Agreement,id=pk)
    agreement=Agreement.objects.prefetch_related('rentline').get(id=pk)

    e = Agreement.objects.get(id=pk)
    rent=e.rentline.all()
    security=e.securityline.all()
    advance=e.advanceline.all()
    print(e.agreement_advance_amount)
    # print(agreement)
    # print(rent)
    # print(advance)
    # users = User.objects.get(id=pk).prefetch_related('item_set')
    # agreement=agreement.rent
    return render(request, 'agreement/agreement_activate.html', context={'agreement': agreement, 'rent':rent,'security':security, 'advance':advance,'rent_rou':rent_rou})


@login_required
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

@login_required
def properties_view(request):
    all_properties = Properties.objects.all()
    return render(request, 'agreement/property_results.html', {'all_properties': all_properties})
@login_required
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
    print(e.id)
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
    print(e.agreement_advance_amount)
    # print(e.agreement_advance_amount)
    #
    total_rou=total_pv+int(e.agreement_advance_amount)
    print(total_rou)


    # return total_pv
    return total_rou


def autocomplete_div_view(request):
    print("hello")
    if 'term' in request.GET:
        search_qs = LocalArea.objects.filter(division__startswith=request.GET.get('term'))
        print(search_qs)
        division_list=list()
        # print q
        for d in search_qs:
            division_list.append(d.division)


        print(division_list)


        return JsonResponse(division_list,safe=False)
    else:
        return JsonResponse([1, 2, 3, 4], safe=False)
    # return render(request, 'agreement/property_results.html', {'all_properties': all_properties})
    # return JsonResponse(division,safe=False)
def autocomplete_postcode_view(request):
    print("hello")
    if 'term' in request:

        search_qs = LocalArea.objects.filter(postcode__startswith=request.GET.get('term'))
        division=list()
        # print q
        for d in search_qs:
            division.append(d.division)


        print(division)


        return JsonResponse(division,safe=False)

    return render(request, 'agreement/property_results.html', {'all_properties': all_properties})

@csrf_exempt
def update_agreement_status_view(request, id):
    # csrfContext = RequestContext(request)
    # dictionary for initial data with
    # field names as keys
    context ={}

    print(type(id))
    print(id)

    # id=int(id)
    #
    # fetch the object related to passed id
    obj = get_object_or_404(Agreement, id = id)

    obj.status='submitted'
    obj.save()
    print(obj.status)

    return JsonResponse([1, 2, 3, 4], safe=False)
@csrf_exempt
def update_agreement_status_new_view(request, id):
    # csrfContext = RequestContext(request)
    # dictionary for initial data with
    # field names as keys
    context ={}

    print(type(id))
    print(id)

    # id=int(id)
    #
    # fetch the object related to passed id
    obj = get_object_or_404(Agreement, id = id)

    obj.status='activated'
    obj.save()
    print(obj.status)

    return JsonResponse([1, 2, 3, 4], safe=False)

def check_maximum_extension(shop_code):


    return_value=1
    try:
        obj=Site.objects.filter(site_code__contains=shop_code)
        a=obj.aggregate(Max('site_extension'))
        return_value=a['site_extension__max']+1
        print(return_value)
        return return_value

    except:
        print(None)
        return return_value
        # print("None")

def create_id_for_agreement(shop_code,file_no,serial_no):


    return_value=''
    # print("Check value")
    # print(type(shop_code).__name__)
    # site=type(shop_code).__name__

    # site_code=site.value().split('-')[0]


    # obj=Site.objects.filter(site_code__exact=site_code)
    site_name=shop_code.site_code
    site_extension=shop_code.site_extension
    site_type=shop_code.site_type

    # print(shop_code.site_type)
    # site_type=obj.site_type
    return_value=site_name+str(site_extension)+'-'+site_type+'-'+file_no+'-'+serial_no

    print(return_value)
    return return_value
    # try:
    #     obj=Site.objects.filter(site_code__exact=shop_code)
    #     site_type=obj.site_type
    #     return_value=shop_code+'-'+site_type+'-'+file_no+'-'+serial_no
    #
    #     print(return_value)
    #     return return_value
    #
    # except:
    #     print(None)
    #     return return_value





    # pass the object as instance in form
    # form = GeeksForm(request.POST or None, instance = obj)
    #
    # # save the data from the form and
    # # redirect to detail_view
    # if form.is_valid():
    #     form.save()
    #     return HttpResponseRedirect("/"+id)
    #
    # # add form dictionary to context
    # context["form"] = form
    #
    # return render(request, "update_view.html", context)
