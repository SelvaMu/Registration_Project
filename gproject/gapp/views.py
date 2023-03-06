from django.shortcuts import render, redirect
from . import models
from django.contrib.auth.models import auth
from django.contrib import messages
from pytz import timezone
from datetime import datetime
import smtplib
from email.message import EmailMessage
from django.db import transaction



def home(request):
    """Render the home page template"""
    return render(request, 'index.html')

@transaction.atomic
def volunteers(request):
    try:
        # if not request.user.is_authenticated:
        #     return render(request,'index.html')
        # else:
        if request.session['logged_in']==True:

            if request.method == "POST":
                searched = request.POST.get('searchi', '')
                det = models.Employee_Registration_DataBase.objects.filter(Employee_ID=searched)
                d=models.Employee_Registration_DataBase.objects.get(Employee_ID=searched)
                    
                if models.Employer_Access_DataBase.objects.filter(Employer_ID=searched).exists():    
                        # If search result exists, save it to a new data object
                    messages.info(request,"Enter Registration Number Already Sent")
                    return render(request,'volunteers.html')
                else:
                    data = models.Employer_Access_DataBase(
                                Employer_ID=d.Employee_ID, Student_Name=d.Student_Name, Father_Mother_Name=d.Father_Mother_Name, Email_ID=d.Email_ID, Mobile_Number=d.Mobile_Number, 
                                Aadhar_ID_Number=d.Aadhar_ID_Number, Date_Of_Birth=d.Date_Of_Birth, Gender=d.Gender, District=d.District,Community=d.Community, Private_Job_Portal=d.Private_Job_Portal, 
                                Section=d.Section,Physically_Disabled=d.Physically_Disabled, Highest_Qualification=d.Highest_Qualification, Qualified_Year=d.Qualified_Year, Registered_Date=d.Registered_Date, Percentage=d.Percentage)
                    data.save()
                    messages.info(request,"Submitted Successfully")
                        # except:
                        #     return render(request, 'volunteers.html')
                    return render(request, 'volunteers.html', {'searched': searched, 'det': det})
                
            else:
                return render(request, 'volunteers.html')
        else:
             return render(request,'index.html')
    
    except:
        # print(f"Exception: {str()}")

        transaction.set_rollback(True)
        messages.info(request,"User Not Found")
        return render(request,'volunteers.html')


@transaction.atomic
def employersregister(request):
    try:
        if request.method=="POST":
            
            name=request.POST['name']
            email=request.POST['email']
            number=request.POST['number']
            companyname=request.POST['companyname']
            ind_time = datetime.now(timezone("Asia/Kolkata")).strftime('%Y-%m-%d')
            date=ind_time
            i_d="EMP"+number

            if(models.Eployers_Table.objects.filter(Employer_Number=number).exists()):
                        # Create a new employee object with the form data
                messages.info(request,"Entered Mobile Number Already Exists")
                return render(request, 'employer_register.html') 
            else:
                try:
                    msg = EmailMessage()
                    msg['Subject'] = 'Welcome To Mega Job Fair 11/03/2023'
                    msg['From'] = 'DEO TENKASI JOB FAIR 2023'
                    msg['To'] = email
                    msg.set_content(f'''Respected sir/madam,
    You have invited to the mega job fair 2023, your token number is {i_d}
    (http://127.0.0.1:8000/em8plo65ye56r_54pa652156nel51)
    ''')

                            # Connect to SMTP server and send the message
                    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as connection:
                        email_address = 'lsm160898@gmail.com'
                        email_password = 'qtovsexbajhvhath'
                        connection.login(email_address, email_password)
                        connection.send_message(msg)
                    with transaction.atomic():
                        employee = models.Eployers_Table(
            Employers_ID= i_d,Employer_Name=name,  Email_ID=email, Employer_Number=number, Employer_Company_Name=companyname,Registered_Date=date)
                        employee.save()
                                
                        messages.info(request,f"You have registered successfully. Your Token Number is {i_d}.")
                        return render(request,"employer_register.html")

                
                except:
                    transaction.set_rollback(True)
                    messages.info(request,"Verify Your Email ID or Change Email ID")
                    return render(request, 'employer_register.html')
        else:    
            return render(request,'employer_register.html')
    except:
        transaction.set_rollback(True)
        messages.info(request,"Server Down Register Again...")
        return render(request,'employer_register.html')

@transaction.atomic
def login(request):
    try:
        if request.method=="POST":
            username=request.POST["username"]
            password=request.POST["password"]
            usern="admin"
            password1="Admin@2023"
            logon='volunteers'
            password2="Government@2023"
            if username==usern and password1==password:
                user=auth.authenticate(username=username,password=password)

                if user is not None:
                    request.session['logged_in']=True 
                    return render(request, 'search.html')
                else:
                    messages.info(request,"User Name or Password is wrong")
                    return render(request,"index.html")
            
            elif username==logon and password2==password:
                user=auth.authenticate(username=username,password=password)
                if user is not None:
                    request.session['logged_in']=True                
                    return render(request, 'volunteers.html')
                else:
                    messages.info(request,"User Name or Password is wrong")
                    return render(request,"index.html")
            else:
                messages.info(request,"User name or Password is wrong")
                return render(request,"index.html")
        
        else:
            return render(request,"index.html")
    except:
        transaction.set_rollback(True)
        messages.info(request,"Server Down Reload Again...")
        return render(request,'index.html')

@transaction.atomic
def logout(request):
    try:

        if request.session.get("logged_in"):
            auth.logout(request)
            request.session["logged_in"] = False
        
        return render(request,'index.html')
    except:
        transaction.set_rollback(True)
        messages.info(request,"Server Down Load Again...")
        return render(request,'index.html')


@transaction.atomic
def employersalldata(request):
    try:
        # if not request.user.is_authenticated:
        #     return render(request,'index.html')
        # else:
        t = models.Eployers_Table.objects.count()
        if request.session['logged_in']==True:
            if request.method=='POST':
                
                searched = request.POST.get('searchi', '')
                det = models.Eployers_Table.objects.filter(Employers_ID=searched)
                # If search result exists, save it to a new data object
                return render(request, 'employerdata.html', {'searched': searched, 'det': det,'t':t})
            else:
                all_members = models.Eployers_Table.objects.all
                # all_members = vvm.objects.all
                return render(request,'employerdata.html',{'all':all_members,'t':t})
        else:
            return render(request,"index.html")
    except:
        transaction.set_rollback(True)
        messages.info(request,"No Data Found")
        return render(request,'employerdata.html')
    
@transaction.atomic
def employer_panel(request):
    try:
        if request.method == "POST":
                    searched = request.POST.get('searchi', '')
                    
                    det = models.Employer_Access_DataBase.objects.filter(Employer_ID=searched)
                    
                    return render(request, 'employerpanel.html', {'searched': searched, 'det': det})
                    
        else:
            messages.info(request,"No data Found")
            return render(request, 'employerpanel.html')
    except:
        transaction.set_rollback(True)
        messages.info(request,"No Data Found")
        return render(request,'employerpanel.html')
    


@transaction.atomic  
def selection_panel(request):
    try:

        if request.method=="POST":
            searched = request.POST.get('searchi', '')
            submit_id=request.POST.get('employer_id','')
            selection=request.POST.get('employee','')

            data=models.Employer_Access_DataBase.objects.get(Employer_ID=searched)

            employer=models.Eployers_Table.objects.get(Employers_ID=submit_id)

            if selection == "Select":

            # if models.Employers_Selection.objects.filter(Employer_ID=searched).exists():
                data1 = models.Employers_Selection(
                Employer_ID=data.Employer_ID, Student_Name=data.Student_Name, Father_Mother_Name=data.Father_Mother_Name, Email_ID=data.Email_ID, Mobile_Number=data.Mobile_Number, 
                            
                Aadhar_ID_Number=data.Aadhar_ID_Number, Date_Of_Birth=data.Date_Of_Birth, Gender=data.Gender, District=data.District,Community=data.Community, Private_Job_Portal=data.Private_Job_Portal, 
                            
                Section=data.Section,Physically_Disabled=data.Physically_Disabled, Highest_Qualification=data.Highest_Qualification, Qualified_Year=data.Qualified_Year, Percentage=data.Percentage,
                            
                Employers_ID=employer.Employers_ID,Employer_Name=employer.Employer_Name,Email_ID1=employer.Email_ID,Employer_Number=employer.Employer_Number,Employer_Company_Name=employer.Employer_Company_Name,
                            
                Registered_Date1=employer.Registered_Date,Select_Cantidate=selection)
                data1.save()
                messages.info(request,"Submitted Successfully")
                return render(request,'employerselectiontable.html')
            else:
                messages.info(request,"Successfully Submited")
                return render(request,'employerselectiontable.html')
                    
            #     messages.info(request,"Already Submit")
            #     return render(request,'employerselectiontable.html')
        else:
            return render(request,'employerselectiontable.html')
    except:
        transaction.set_rollback(True)
        messages.info(request,"No Data Found")
        return render(request,'employerselectiontable.html')


@transaction.atomic
def employer_selected_list(request):
    try:
        # if not request.user.is_authenticated:
        #     return render(request,'index.html')
        # else:
        t = models.Employers_Selection.objects.count()
        if request.session['logged_in']==True:
            if request.method=='POST':
        
                searched = request.POST.get('searchi', '')
                det = models.Employers_Selection.objects.filter(Employer_ID=searched)
                # If search result exists, save it to a new data object
                return render(request, 'employerselectedlist.html', {'searched': searched, 'det': det,'t':t})
            else:
                all_members = models.Employers_Selection.objects.all
                # all_members = vvm.objects.all
                return render(request,'employerselectedlist.html',{'all':all_members,'t':t})
        else:
            return render(request,"index.html")
    except:
        transaction.set_rollback(True)
        messages.info(request,"No Data Found")
        return render(request,'employerselectedlist.html')
    

@transaction.atomic
def alldata(request):
    try:
        # if not request.user.is_authenticated:
        #     return render(request,'index.html')
        # else:
        t = models.Employee_Registration_DataBase.objects.count()
        if request.session['logged_in']==True:
            if request.method=='POST':
        
                searched = request.POST.get('searchi', '')
                det = models.Employee_Registration_DataBase.objects.filter(Employee_ID=searched)
                # If search result exists, save it to a new data object
                return render(request, 'alldata.html', {'searched': searched, 'det': det,'t':t})
            else:
                all_members = models.Employee_Registration_DataBase.objects.all
                # all_members = vvm.objects.all
                return render(request,'alldata.html',{'all':all_members,'t':t})
        else:
            return render(request,"index.html")
    except:
        transaction.set_rollback(True)
        messages.info(request,"No Data Found")
        return render(request,'alldata.html')

@transaction.atomic
def presenthere(request):
    try:
        # if not request.user.is_authenticated:
        #     return render(request,'index.html')
        # else:
        t = models.Employer_Access_DataBase.objects.count()
        if request.session['logged_in']==True:
            if request.method=="POST":
                searched = request.POST.get('searchi', '')
                det = models.Employer_Access_DataBase.objects.filter(Employer_ID=searched)
                # If search result exists, save it to a new data object
                return render(request, 'presenthere.html', {'searched': searched, 'det': det,'t':t})
            else:
                all_members = models.Employer_Access_DataBase.objects.all
                # all_members = vvm.objects.all
                return render(request,'presenthere.html',{'all':all_members,'t':t})
        else:
            return render(request,"index.html")
    except:
        transaction.set_rollback(True)
        messages.info(request,"No Data Found")
        return render(request,'presenthere.html')

@transaction.atomic
def datareset(request):
    # if not request.user.is_authenticated:
    #         return render(request,'index.html')
    # else:
    try:

        if request.session['logged_in']==True:
            return render(request,"datareset.html")
    except:
        transaction.set_rollback(True)
        messages.info(request,"Server Down Reload Again...")
        return render(request,'datareset.html')
    

@transaction.atomic
def deletealldata(request):
    # if not request.user.is_authenticated:
    #         return render(request,'index.html')
    # else:
    try:

        if request.method=="POST":
            if request.session['logged_in']==True:
                models.Employee_Registration_DataBase.objects.all().delete()
                models.Employer_Access_DataBase.objects.all().delete()
                messages.info(request,"Successfully Deleted All data from employee Table")
                return render(request,'alldatadeleted.html')
        else:
            return render(request,'alldatadeleted.html')
    except:
        transaction.set_rollback(True)
        messages.info(request,"Server Down... Try Again....")
        return render(request,'alldatadeleted.html')

@transaction.atomic
def selectdata(request):
    # if not request.user.is_authenticated:
    #         return render(request,'index.html')
    # else:
    try:
            
        if request.method=='POST':
            if request.session['logged_in']==True:
                id=request.POST['id']
                if id is not None:
                    select = models.Employer_Access_DataBase.objects.filter(Employer_ID=id).first()
                    if select is not None:
                        select.delete()
                        messages.success(request, "Successfully deleted selected data from employee table.")
                        return render(request,'selectdata.html')
                    else:
                        messages.warning(request, "No data found with the provided ID.")
                        return render(request,'selectdata.html')
        else:
            return render(request,'selectdata.html')
        
    except:
        transaction.set_rollback(True)
        messages.info(request,"Server Down Try Again")
        return render(request,'selectdata.html')

@transaction.atomic
def employerdatadelete(request):
    try:

        if request.method=="POST":
            if request.session['logged_in']==True:
                models.Eployers_Table.objects.all().delete()
                models.Employers_Selection.objects.all().delete()
                
                messages.info(request,"Successfully Deleted All data from Employer Table And Selevted List")
                return render(request,'employerdatadelete.html')
        else:
            return render(request,'employerdatadelete.html')
    except:
        transaction.set_rollback(True)
        messages.info(request,"Server Down Try Again")
        return render(request,'employerdatadelete.html')


@transaction.atomic
def search(request):
    try:
        # if not request.user.is_authenticated:
        #     return render(request,'index.html')
            
        # else:
        if request.session['logged_in']==True:
                
            if request.method == "POST":
                searched = request.POST.get('searchi', '')
                det = models.Employee_Registration_DataBase.objects.filter(Employee_ID=searched)
                    # If search result exists, save it to a new data object   
                    
                return render(request, 'search.html', {'searched': searched, 'det': det})
            else:
                return render(request, 'search.html')
                
        else:
            return render(request,'index.html')
        
    except:
        messages.info(request,"User Not Found")
        return render(request, 'search.html')



from django.shortcuts import render
from .utils import export_to_csv

def csvconver(request):
    if request.session['logged_in']==True:
        return render(request,'csvconvertion.html')

def employeeregistrationdata(request):
    # Call the export_to_csv function with your model and filename
    response = export_to_csv(models.Employee_Registration_DataBase, 'Employee All Registration Data')

    # Return the response object
    return response

def employerregistrationdata(request):
    # Call the export_to_csv function with your model and filename
    response = export_to_csv(models.Eployers_Table, 'Employers All Registration Data')

    # Return the response object
    return response


def selecteddata(request):
    # Call the export_to_csv function with your model and filename
    response = export_to_csv(models.Employers_Selection, 'Selected Student Data')

    # Return the response object
    return response


def presendheredata(request):
    # Call the export_to_csv function with your model and filename
    response = export_to_csv(models.Employer_Access_DataBase, 'Present Student Data')

    # Return the response object
    return response


@transaction.atomic
def regis(request):
    try:
        if request.method == "POST":
                
                # Retrieve form data from the request
            
            name = request.POST.get('name', '')
            father = request.POST['mfname']
            email = request.POST.get('email', '')
            number = request.POST.get('number', '')
            aadhar = request.POST.get('aadhar', '')
            dob = request.POST.get('dob', '')
            gender = request.POST.get('gender', '')
            dist = request.POST['district']
            community = request.POST['community']
            job = request.POST.get('employee', '')
            pwd = request.POST.get('yy', '')
            section=request.POST.get('section', '')
            ind_time = datetime.now(timezone("Asia/Kolkata")).strftime('%Y-%m-%d')
            date = ind_time
            ed1_q = request.POST.get('qualification', '')
            ed1_y = request.POST.get('year','')
            ed1_p = request.POST.get('percentage', '')
            i_d="TET"+number
            
            if( models.Employee_Registration_DataBase.objects.filter(Mobile_Number=number).exists() ):
                        # Create a new employee object with the form data
                messages.info(request,"Entered Mobile Number is Alread Exists")
                return render(request, 'register.html') 
            else:
                try:
                        # if validateemail:
                    msg = EmailMessage()
                    msg['Subject'] = 'Successfully Applied For Mega Job Fair Date : 11/03/2023, Time : 8:30 A.M '
                    msg['From'] = 'DEO TENKASI JOB FAIR 2023'
                    msg['To'] = email
                    msg.set_content(f'''Hi! {name}, Your Token Number is {i_d}.
Job Fair Location (இடம்) : S.Veerasamy Chettiar College of Engineering and Technology
                            (https://goo.gl/maps/4SS7inUFPaz74tdw6)
Date(தேதி) : 11/03/2023
Time(நேரம்) : 8:30 A.M
For ensuring  hassle free entry, Show  this token number at the Counter/Volunteer and attend the interview 
பதிவு கவுண்டர் இல் நெரிசலை தவிர்க்க இந்த டோக்கன் நம்பர்-  யினை 
தன்னார்வலர்களிடம் அல்லது  பணியாளர்களிடம் காண்பித்து முகாமில் நேரடியாக பங்கு கொள்ளலாம்
''')

                            # Connect to SMTP server and send the message
                    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as connection:
                        email_address = 'lsm160898@gmail.com'
                        email_password = 'qtovsexbajhvhath'
                        connection.login(email_address, email_password)
                        connection.send_message(msg)
                    with transaction.atomic():
                        employee = models.Employee_Registration_DataBase(
                        Employee_ID= i_d,Student_Name=name, Father_Mother_Name=father, Email_ID=email, Mobile_Number=number, Aadhar_ID_Number=aadhar, Date_Of_Birth=dob,
                        Gender=gender, District=dist,Community=community, Private_Job_Portal=job, Physically_Disabled=pwd,Section=section, Highest_Qualification=ed1_q, Qualified_Year=ed1_y, Registered_Date=date,
                        Percentage=ed1_p
                                    )
                        employee.save()

                               
                    messages.info(request,f"You have registered successfully. Your Token Number is {i_d}. Take Screenshot.")
                    return render(request,"register.html")

                # else:
                #         messages.info(request,"Verify your Email ID or Change Email ID")
                #         return render(request, 'register.html')
                except:
                    transaction.set_rollback(True)
                    messages.info(request,"Verify your Email id or Change Email ID")
                    return render(request, 'register.html')
        else:
                # Render the registration form if the request method is not POST
            return render(request, 'register.html')
    except:
        transaction.set_rollback(True)
        messages.info(request,"Server Down Register Again")
        return render(request,'register.html')
