from django.db import models


# Create your models here.


class Employee_Registration_DataBase(models.Model):
    
    Employee_ID = models.CharField(max_length=100,null=True)

    Student_Name = models.CharField(max_length=100)

    Father_Mother_Name = models.CharField(max_length=100)

    Email_ID = models.CharField(max_length=100)

    Mobile_Number = models.CharField(max_length=100)

    Aadhar_ID_Number = models.CharField(max_length=100)

    Date_Of_Birth = models.DateField(max_length=100)

    Gender = models.CharField(max_length=100)

    District = models.CharField(max_length=100)

    Community = models.CharField(max_length=100,null=True)
    
    Private_Job_Portal = models.CharField(max_length=100)

    Physically_Disabled = models.CharField(max_length=100)

    Section=models.CharField(max_length=100,null=True)

    Registered_Date = models.DateField(max_length=100)

    Highest_Qualification = models.CharField(max_length=100)
    
    Qualified_Year = models.CharField(max_length=100)
    
    Percentage = models.CharField(max_length=100)
    
    

    def __str__(self):

        return str(self.Employee_ID)+'  '+ str(self.Student_Name)
    
# class employeer(models.Model):
#     data=models.TextField(max_length=100)


class Employer_Access_DataBase(models.Model):

    Employer_ID = models.CharField(max_length=100,null=True)
    
    Student_Name = models.CharField(max_length=100)

    Father_Mother_Name = models.CharField(max_length=100)
    
    Email_ID = models.CharField(max_length=100)
    
    Mobile_Number = models.CharField(max_length=100)
    
    Aadhar_ID_Number = models.CharField(max_length=100)
    
    Date_Of_Birth = models.DateField(max_length=100)
    
    Gender = models.CharField(max_length=100)
    
    District = models.CharField(max_length=100)

    Community = models.CharField(max_length=100,null=True)
    
    Private_Job_Portal = models.CharField(max_length=100)
    
    Physically_Disabled = models.CharField(max_length=100)

    Section=models.CharField(max_length=100,null=True)
    
    Registered_Date = models.DateField(max_length=100)

    Highest_Qualification = models.CharField(max_length=100)
    
    Qualified_Year = models.CharField(max_length=100)
    
    Percentage = models.CharField(max_length=100)

    def __str__(self):

        return str(self.Employer_ID)+'  '+ str(self.Student_Name)
    

class Eployers_Table(models.Model):
    

    Employers_ID = models.CharField(max_length=100,null=True)
    
    Employer_Name=models.CharField(max_length=100)

    Email_ID=models.CharField(max_length=100)

    Employer_Number=models.CharField(max_length=100)

    Employer_Company_Name=models.CharField(max_length=100)

    Registered_Date = models.DateField(max_length=100)

    def __str__(self):

        return str(self.Employers_ID)+'  '+ str(self.Employer_Company_Name)
    


class Employers_Selection(models.Model):

    Employer_ID = models.CharField(max_length=100,null=True)
    
    Student_Name = models.CharField(max_length=100)

    Father_Mother_Name = models.CharField(max_length=100)
    
    Email_ID = models.CharField(max_length=100)
    
    Mobile_Number = models.CharField(max_length=100)
    
    Aadhar_ID_Number = models.CharField(max_length=100)
    
    Date_Of_Birth = models.DateField(max_length=100)
    
    Gender = models.CharField(max_length=100)
    
    District = models.CharField(max_length=100)

    Community = models.CharField(max_length=100,null=True)
    
    Private_Job_Portal = models.CharField(max_length=100)
    
    Physically_Disabled = models.CharField(max_length=100)

    Section=models.CharField(max_length=100,null=True)
    

    Highest_Qualification = models.CharField(max_length=100)
    
    Qualified_Year = models.CharField(max_length=100)
    
    Percentage = models.CharField(max_length=100)




    Employers_ID = models.CharField(max_length=100,null=True)
    
    Employer_Name=models.CharField(max_length=100)

    Email_ID1=models.CharField(max_length=100,null=True)

    Employer_Number=models.CharField(max_length=100)

    Employer_Company_Name=models.CharField(max_length=100)

    Registered_Date1 = models.DateField(max_length=100,null=True)

    Select_Cantidate=models.CharField(max_length=100)

    def __str__(self):
        return str(self.Employers_ID)+' '+str(self.Employer_ID)
    


