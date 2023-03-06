from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    
    path('s98ea7r6c6651251363h516556465',views.search,name='search'),
    
    path('a97846l65ld65a9695t48694a6454',views.alldata,name='alldata'),
    
    path('pr56465es52351ent55146h512ere',views.presenthere,name='presenthere'),
        
    path('registration',views.regis,name='regis'),
   
    path('l84694o65434g65498i687n635879',views.login,name='login'),
    
    path('l5364og65o63587u63587636t6376',views.logout,name='logout'),
    
    path('v696o6584lu6563n563teers68568',views.volunteers,name='volunteers'),
    
    path('da536494tar3213e963584s6e654t',views.datareset,name='datareset'),
    
    path('de654l65384et65eall321da63ta6',views.deletealldata,name='deletealldata'),
    
    path('s63564el6546ec655t351data6325',views.selectdata,name='selectdata'),
    
    path('e64m531pl634oyer56sregi64ster',views.employersregister,name='employersregister'),
    
    path('emplo65465yerdata635846te6534',views.employerdatadelete,name='employerdatadelete'),

    path('em5153l53213ye251r65alldata63',views.employersalldata,name='employersalldata'),

    path('em8plo65ye56r_54pa652156nel51',views.employer_panel,name='employer_panel'),

    path('se6541lecti625365_p6531anel31',views.selection_panel,name='selection_panel'),

    path('em845pl5164_se524ct203ed_6546',views.employer_selected_list,name='employer_selected_list'),

    path('c84654sv215364cnv635164e536r8',views.csvconver,name='csvconver'),

    path('e6546mp213loi23132onda21ta631',views.employeeregistrationdata,name='employeeregistrationdata'),

    path('e6351m515p542l546o7542y651465',views.employerregistrationdata,name='employerregistrationdata'),

    path('se632le520c5t5ed65a351t55a521',views.selecteddata,name='selecteddata'),

    path('pr56e63s632en5265352d6553h531',views.presendheredata,name='presendheredata'),


     # path('validate_email',views.validate_email,name='validate_email'),
    # path('submit',views.submit,name='submit'),
]




