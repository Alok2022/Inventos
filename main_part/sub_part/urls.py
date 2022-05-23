from unicodedata import name
from django.urls import path
from . import views
urlpatterns= {
    path('',views.Home,name='Home'),
    path('contact_form_submission',views.contact_form_submission,name='contact_form_submission'),
    path('Register_form_submission',views.Register_form_submission,name='Register_form_submission'),

    path('login',views.login,name='login'),
    path('login_form',views.login_form,name='login_form'),
    path('Register',views.Register,name='Register'),
    path('dashboard/<int:id>',views.dashboard,name='dashboard'),
    path('frontOffice/<int:id>',views.frontOffice,name='frontOffice'),
    path('OPDOutpatient/<int:id>',views.OPDOutpatient,name='OPDOutpatient'),
    path('IPDInpatient/<int:id>',views.IPDInpatient,name='IPDInpatient'),
    path('Pharmacy/<int:id>',views.Pharmacy,name='Pharmacy'),
    path('Pathology/<int:id>',views.Pathology,name='Pathology'),
    path('Radiology/<int:id>',views.Radiology,name='Radiology'),
    path('OperationTheatre/<int:id>',views.OperationTheatre,name='OperationTheatre'),
    path('Ambulance/<int:id>',views.Ambulance,name='Ambulance'),
    path('Birth/<int:id>',views.Birth,name='Birth'),
    path('Death/<int:id>',views.Death,name='Death'),
    path('Humanresource/<int:id>',views.Humanresource,name='Humanresource'),
    path('BedStatus/<int:id>',views.BedStatus,name='BedStatus'),
    path('itemstock/<int:id>',views.itemstock,name='itemstock'),

# Front Office----->
    path('Frontofficeadd/<int:id>',views.Frontofficeadd,name='Frontofficeadd'),
    path('ProductAdd/<int:id>',views.ProductAdd,name='ProductAdd'),
    path('Frontofficevisit/<int:id>',views.Frontofficevisit,name='Frontofficevisit'),
    path('Frontofficeeditappoint/<int:id>/<int:row_id>',views.Frontofficeeditappoint,name='Frontofficeeditappoint'),
    path('edit_form_submission/<int:id>/<int:row_id>',views.edit_form_submission,name='edit_form_submission'),
    path('delete_frontoffice/<int:id>/<int:row_id>',views.delete_frontoffice,name='delete_frontoffice'),

    path('Frontofficevisitedit/<int:id>',views.Frontofficevisitedit,name='Frontofficevisitedit'),
    path('Frontofficevisitlist/<int:id>',views.Frontofficevisitlist,name='Frontofficevisitlist'),


    path('Smartdevice/<int:id>',views.Smartdevice,name='Smartdevice'),
    path('DeviceAdd/<int:id>',views.DeviceAdd,name='DeviceAdd'),
    path('SmartdeviceEdit/<int:id>',views.SmartdeviceEdit,name='SmartdeviceEdit'),
    
    
    path('SmartHome/<int:id>',views.SmartHome,name='SmartHome'),
    path('SmartHomeEdit/<int:id>',views.SmartHomeEdit,name='SmartHomeEdit'),

    path('InvenAssitance/<int:id>',views.InvenAssitance,name='InvenAssitance'),
    path('InvenAssitanceAdd/<int:id>',views.InvenAssitanceAdd,name='InvenAssitanceAdd'),
    path('InvenAssitanceEdit/<int:id>',views.InvenAssitanceEdit,name='InvenAssitanceEdit'),

    path('PathologyAdd/<int:id>',views.PathologyAdd,name='PathologyAdd'),
    path('PathologyEdit/<int:id>',views.PathologyEdit,name='PathologyEdit'),
    path('Pathologyreport/<int:id>',views.Pathologyreport,name='Pathologyreport'),

    path('RadiologyAdd/<int:id>',views.RadiologyAdd,name='RadiologyAdd'),
    path('RadiologyEdit/<int:id>',views.RadiologyEdit,name='RadiologyEdit'),
    path('Radiologyreport/<int:id>',views.Radiologyreport,name='Radiologyreport'),

    path('OperationTheatreAdd/<int:id>',views.OperationTheatreAdd,name='OperationTheatreAdd'),
    path('OperationTheatreEdit/<int:id>',views.OperationTheatreEdit,name='OperationTheatreEdit'),
    
    #*******************Track Your order Path*****************

    path('TrackAdd/<int:id>',views.TrackAdd,name='TrackAdd'),
    path('AddTrackupdate/<int:id>',views.AddTrackupdate,name='AddTrackupdate'),
    path('TrackEdit/<int:id>/<int:row_id>',views.TrackEdit,name='TrackEdit'),
    path('TrackEditupdate/<int:id>/<int:row_id>',views.TrackEditupdate,name='TrackEditupdate'),
    path('deleteAmbulance/<int:id>/<int:row_id>',views.deleteAmbulance,name='deleteAmbulance'),
    #********************************************************************
    path('BirthAdd/<int:id>',views.BirthAdd,name='BirthAdd'),
    path('BirthEdit/<int:id>',views.BirthEdit,name='BirthEdit'),
    path('DeathAdd/<int:id>',views.DeathAdd,name='DeathAdd'),
    path('DeathEdit/<int:id>',views.DeathEdit,name='DeathEdit'),
    path('InvenPay/<int:id>',views.InvenPay,name='InvenPay'),

    path('flagAdd/<int:id>',views.flagAdd,name='flagAdd'),
    path('flagEdit/<int:id>',views.flagEdit,name='flagEdit'),

    path('ProfileAdd/<int:id>',views.ProfileAdd,name='ProfileAdd'),
    path('ProfileEdit/<int:id>',views.ProfileEdit,name='ProfileEdit'),
    path('logout/<int:id>',views.logout,name='logout'),
    



}