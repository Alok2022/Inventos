
from django.shortcuts import render
from numpy import take
from .models import contact_table
from .models import Regist_table, prod_table, device_table,Track_table
from django.contrib import messages,auth
# Create your views here.
def Home(request):
    return render(request,'Home.html')

#contact
def contact_form_submission(request):
    if request.method=='POST':
        el1=contact_table(your_name=request.POST.get('your_name'),
                          surname=request.POST.get('surname'),
                          email_id=request.POST.get('email_id'),
                          subject=request.POST.get('subject'),
                          message=request.POST.get('message'))

        el1.save()
        print("success")
        messages.error(request,'Thanks for Your message,our team will contact you soon',extra_tags='contact_msg')                    
        return render(request,'Home.html')
    else:
        print("failed")
        return render(request,'Home.html')   

def login(request):
   return render(request,'Login.html')
def login_form(request):
    if Regist_table.objects.filter(username=request.POST['username'],password=request.POST['password']).exists():
        el1=Regist_table.objects.get(username=request.POST['username'],password=request.POST['password'])
        take_username=el1.username
        take_emailid=el1.email_id
        take_id=el1.id
        print("logger id is :",take_id)
        print("logger emailid is :",take_emailid)
        print("logger user name is:",take_username)
        #*********************************************#
        user_data=Regist_table.objects.get(email_id=take_emailid)  
        #**********************************************#  
        return render(request,'dashboard.html',{'user_data':user_data})
    else:
        messages.error(request,'invalid username or password',extra_tags='failed')
        return render(request,'Login.html')  
  
def Register(request):
   return render(request,'Register.html')   

def Register_form_submission(request):
    if request.method=='POST':
        if  Regist_table.objects.filter(username=request.POST['username'],email_id=request.POST['email_id']):
            messages.error(request,'Already used username and email_id!...',extra_tags='taken')
            return render(request,'Register.html')
        elif Regist_table.objects.filter(username=request.POST['username']):
            messages.error(request,'username already taken!..',extra_tags='taken')
            return render(request,'Register.html')
        elif Regist_table.objects.filter(email_id=request.POST['email_id']):
            messages.error(request,'email_id already taken!..',extra_tags='taken')
            return render(request,'Register.html')
        else:
            el1= Regist_table(username=request.POST.get('username'),
                            email_id=request.POST.get('email_id'),
                            password=request.POST.get('password'),
                            confrim_password=request.POST.get('confrim_password'))
        el1.save()
        print("*******Successs******")
        messages.error(request,'succesfully registered!....',extra_tags='regit')
        return render(request,'Login.html')   

    else:
        print("######Failed#######")
        return render(request,'Register.html')








def dashboard(request,id):
     user_data=Regist_table.objects.get(id=id)
     collect_count=prod_table.objects.all().count()
     colllect_count=device_table.objects.all().count()
     Track_count=Track_table.objects.all().count()
     return render(request,'dashboard.html',{'user_data':user_data,'collect_count':collect_count,'colllect_count':colllect_count,'Track_count':Track_count})
      
def frontOffice(request,id):
     user_data=Regist_table.objects.get(id=id)
     view_data= prod_table.objects.all()
     return render(request,'front Office.html',{'user_data':user_data,'view_data':view_data})
def OPDOutpatient(request,id):
    user_data=Regist_table.objects.get(id=id)
    view_data= device_table.objects.all()
    return render(request,'OPD - Out patient.html',{'user_data':user_data,'view_data':view_data})
def IPDInpatient(request,id):
    user_data=Regist_table.objects.get(id=id)
    return render(request,'IPD - In patient.html',{'user_data':user_data})
def Pharmacy(request,id):
    user_data=Regist_table.objects.get(id=id)
    return render(request,'Pharmacy.html',{'user_data':user_data})
def Pathology(request,id):
    user_data=Regist_table.objects.get(id=id)
    return render(request,'Pathology.html',{'user_data':user_data})
def Radiology(request,id):
    user_data=Regist_table.objects.get(id=id)
    return render(request,'Radiology.html',{'user_data':user_data})  
def OperationTheatre(request,id):
    user_data=Regist_table.objects.get(id=id)
    return render(request,'Operation Theatre.html',{'user_data':user_data})
def Ambulance(request,id):
    user_data=Regist_table.objects.get(id=id)
    view_data=Track_table.objects.all()
    return render(request,'ambulance.html',{'user_data':user_data,'view_data':view_data})
def Birth(request,id):
    user_data=Regist_table.objects.get(id=id)
    return render(request,'birth.html',{'user_data':user_data}) 
def Death(request,id):
    user_data=Regist_table.objects.get(id=id)
    return render(request,'death.html',{'user_data':user_data})
def Humanresource(request,id):
    user_data=Regist_table.objects.get(id=id)
    return render(request,'human resource.html',{'user_data':user_data})
def BedStatus(request,id):
    user_data=Regist_table.objects.get(id=id)
    return render(request,'bed status.html',{'user_data':user_data})
def itemstock(request,id):
    user_data=Regist_table.objects.get(id=id)
    return render(request,'itemstock.html',{'user_data':user_data}) 

    # Page Content Front Office--
def Frontofficeadd(request,id):
    user_data=Regist_table.objects.get(id=id)
    return render(request,'Front Office Add Appointment.html',{'user_data':user_data})

def ProductAdd(request,id):
    user_data=Regist_table.objects.get(id=id)
    if request.method=='POST':
        el1=prod_table(Product_id=request.POST.get('Product_id'),
                            Product_name=request.POST.get('Product_name'),
                            Date_Time=request.POST.get('Date_Time'),
                            Phone=request.POST.get('Phone'),
                            Gender=request.POST.get('Gender'),
                            Customer=request.POST.get('Customer'),
                            Source=request.POST.get('Source'),
                            Inventos_Cust=request.POST.get('Inventos_Cust'),
                            status=request.POST.get('status'))
        el1.save()
        messages.error(request,'successfully added',extra_tags='Addprod')
        view_data= prod_table.objects.all()
        
        return render(request,'front Office.html',{'user_data':user_data,'view_data':view_data})
    else:
        return render(request,'Front Office Add Appointment.html',{'user_data':user_data})

def Frontofficevisit(request,id):
    user_data=Regist_table.objects.get(id=id)
    return render(request,'Front Office Add visitor.html',{'user_data':user_data})
def Frontofficeeditappoint(request,id,row_id):
    user_data=Regist_table.objects.get(id=id)
    edit_data= prod_table.objects.get(id=row_id)
    return render(request,'Front Office Edit Appointment.html',{'user_data':user_data,'edit_data':edit_data})

def edit_form_submission(request,id,row_id):
    el1=prod_table.objects.filter(id=row_id).update(Product_id=request.POST.get('Product_id'),
                                                    Product_name=request.POST.get('Product_name'),
                                                    Date_Time=request.POST.get('Date_Time'),
                                                    Phone=request.POST.get('Phone'),
                                                    Gender=request.POST.get('Gender'),
                                                    Customer=request.POST.get('Customer'),
                                                    Source=request.POST.get('Source'),
                                                    Inventos_Cust=request.POST.get('Inventos_Cust'),
                                                    status=request.POST.get('status'))
    messages.error(request,'Successfully Updated',extra_tags='Addprod')
    user_data=Regist_table.objects.get(id=id)
    edit_data=prod_table.objects.get(id=row_id)
    view_data=prod_table.objects.all()
    return render(request,'front Office.html',{'user_data':user_data,'edit_data':edit_data,'view_data':view_data})

def delete_frontoffice(request,id,row_id):
    el1=prod_table.objects.get(id=row_id)
    el1.delete()
    messages.error(request,'sucessfully delete',extra_tags='Addprod')
    user_data=Regist_table.objects.get(id=id)
    view_data=prod_table.objects.all()
    return render(request,'front Office.html',{'user_data':user_data,'view_data':view_data})
                                                    

def Frontofficevisitedit(request,id):
    user_data=Regist_table.objects.get(id=id)
    return render(request,'Front Office Edit visitor.html',{'user_data':user_data}) 
def Frontofficevisitlist(request,id):
    user_data=Regist_table.objects.get(id=id)
    return render(request,'Front Office visitor list.html',{'user_data':user_data})     

# ********Smart Device******

def Smartdevice(request,id):
    user_data=Regist_table.objects.get(id=id)
    return render(request,'Smart.html',{'user_data':user_data})

def DeviceAdd(request,id):
    user_data=Regist_table.objects.get(id=id)
    if request.method=='POST':
        el1=device_table(DeviceName=request.POST.get('DeviceName'),
                         Product=request.POST.get('Product'),
                         ProductId=request.POST.get('ProductId'),
                         ManufacturingId=request.POST.get('ManufacturingId'),
                         ManufactureDate=request.POST.get('ManufactureDate'),
                         Comment=request.POST.get('Comment'),
                         CustomerHelpLine=request.POST.get('CustomerHelpLine'),
                         TotalProduct=request.POST.get('TotalProduct'))
        el1.save()
        messages.error(request,'successfully added Device',extra_tags='SmatDev')
        view_data= device_table.objects.all()
        return render(request,'OPD - Out patient.html',{'user_data':user_data,'view_data':view_data})
    else:
        return render(request,'Smart.html',{'user_data':user_data})

# Smart Device Edit

def SmartdeviceEdit(request,id):
    user_data=Regist_table.objects.get(id=id)
    return render(request,'SmartEdit.html',{'user_data':user_data})  

def SmartHome(request,id):
    user_data=Regist_table.objects.get(id=id)
    return render(request,'SmartHome.html',{'user_data':user_data})
def SmartHomeEdit(request,id):
    user_data=Regist_table.objects.get(id=id)
    return render(request,'SmartHomeEdit.html',{'user_data':user_data}) 

def InvenAssitance(request,id):
    user_data=Regist_table.objects.get(id=id)
    return render(request,'InvenAssitance.html',{'user_data':user_data})
def InvenAssitanceAdd(request,id):
    user_data=Regist_table.objects.get(id=id)
    return render(request,'InvenAssitanceAdd.html',{'user_data':user_data})
def InvenAssitanceEdit(request,id):
    user_data=Regist_table.objects.get(id=id)
    return render(request,'InvenAssitanceEdit.html',{'user_data':user_data})

def PathologyAdd(request,id):
    user_data=Regist_table.objects.get(id=id)
    return render(request,'Pathology Add test.html',{'user_data':user_data})
def PathologyEdit(request,id):
    user_data=Regist_table.objects.get(id=id)
    return render(request,'Pathology edit test.html',{'user_data':user_data})
def Pathologyreport(request,id):
    user_data=Regist_table.objects.get(id=id)
    return render(request,'Pathology Test Report.html',{'user_data':user_data})  
def RadiologyAdd(request,id):
    user_data=Regist_table.objects.get(id=id)
    return render(request,'Radiology Add test.html',{'user_data':user_data}) 
def RadiologyEdit(request,id):
    user_data=Regist_table.objects.get(id=id)
    return render(request,'Radiology edit test.html',{'user_data':user_data})
def Radiologyreport(request,id):
    user_data=Regist_table.objects.get(id=id)
    return render(request,'Radiology Test Report.html',{'user_data':user_data})  
def OperationTheatreAdd(request,id):
    user_data=Regist_table.objects.get(id=id)
    return render(request,'operationtheatre Add.html',{'user_data':user_data})
def OperationTheatreEdit(request,id):
    user_data=Regist_table.objects.get(id=id)
    return render(request,'operationtheatre edit.html',{'user_data':user_data}) 
def TrackAdd(request,id):
    user_data=Regist_table.objects.get(id=id)
    return render(request,'ambulance add list.html',{'user_data':user_data})

#************************Tracking My Order ***************
def AddTrackupdate(request,id):
    user_data=Regist_table.objects.get(id=id)
    if request.method=='POST':
        el1=Track_table(ProductNo=request.POST.get('ProductNo'),
                         ProductModel=request.POST.get('ProductModel'),
                         ProductName=request.POST.get('ProductName'),
                         Customername=request.POST.get('Customername'),
                         customerNo=request.POST.get('customerNo'),
                         Delivery_update=request.POST.get('Delivery_update'),
                         userText=request.POST.get('userText'))
        el1.save()
        messages.error(request,'Tracking Device',extra_tags='trak')
        view_data=Track_table.objects.all()
        return render(request,'ambulance.html',{'user_data':user_data,'view_data':view_data})
    else:
        return render(request,'ambulance add list.html',{'user_data':user_data})

def TrackEdit(request,id,row_id):
    user_data=Regist_table.objects.get(id=id)
    edit_data=Track_table.objects.get(id=row_id)
    return render(request,'ambulance edit list.html',{'user_data':user_data,'edit_data':edit_data})

    #****************Edit Track********************
def TrackEditupdate(request,id,row_id):
    el1=Track_table.objects.filter(id=row_id).update(ProductNo=request.POST.get('ProductNo'),
                                                     ProductModel=request.POST.get('ProductModel'),
                                                     ProductName=request.POST.get('ProductName'),
                                                     Customername=request.POST.get('Customername'),
                                                     customerNo=request.POST.get('customerNo'),
                                                     Delivery_update=request.POST.get('Delivery_update'),
                                                     userText=request.POST.get('userText'))
    messages.error(request,'Successfully Updated',extra_tags='trak')
    user_data=Regist_table.objects.get(id=id)
    edit_data=Track_table.objects.get(id=row_id)
    view_data=Track_table.objects.all()
    return render(request,'ambulance.html',{'user_data':user_data,'edit_data':edit_data,'view_data':view_data})

def deleteAmbulance(request,id,row_id):
    el1=Track_table.objects.get(id=row_id)
    el1.delete()
    messages.error(request,'sucessfully delete',extra_tags='trak')
    user_data=Regist_table.objects.get(id=id)
    view_data=Track_table.objects.all()
    return render(request,'ambulance.html',{'user_data':user_data,'view_data':view_data})    


def BirthAdd(request,id):
    user_data=Regist_table.objects.get(id=id)
    return render(request,'birth add list.html',{'user_data':user_data})
def BirthEdit(request,id):
    user_data=Regist_table.objects.get(id=id)
    return render(request,'birth edit list.html',{'user_data':user_data})
def DeathAdd(request,id):
    user_data=Regist_table.objects.get(id=id)
    return render(request,'death add list.html',{'user_data':user_data})
def DeathEdit(request,id):
    user_data=Regist_table.objects.get(id=id)
    return render(request,'death edit list.html',{'user_data':user_data})

def InvenPay(request,id):
    user_data=Regist_table.objects.get(id=id)
    return render(request,'Human Resource add list.html',{'user_data':user_data})

def flagAdd(request,id):
    user_data=Regist_table.objects.get(id=id)
    return render(request,'bed add list.html',{'user_data':user_data})
def flagEdit(request,id):
    user_data=Regist_table.objects.get(id=id)
    return render(request,'bed edit list.html',{'user_data':user_data})
def ProfileAdd(request,id):
    user_data=Regist_table.objects.get(id=id)
    return render(request,'item stock add.html',{'user_data':user_data})
def ProfileEdit(request,id):
    user_data=Regist_table.objects.get(id=id)
    return render(request,'item stock edit.html',{'user_data':user_data})  
def logout(request,id):
    user_data=Regist_table.objects.get(id=id)
    auth.logout(request)
    return render(request,'Login.html',{'user_data':user_data})         


                                                