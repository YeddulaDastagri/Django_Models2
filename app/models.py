from django.db import models

# Create your models here.   
class Dpt(models.Model):
    dname=models.CharField(max_length=100) 
    dpt_no=models.IntegerField(primary_key=True) 
    loc=models.CharField(max_length=100)  
class Emp(models.Model):
    dpt_no=models.ForeignKey(Dpt,on_delete=models.CASCADE) 
    ename=models.CharField(max_length=100) 
    sal=models.DecimalField(max_digits=10,decimal_places=3) 
    emp_no=models.IntegerField(primary_key=True)  
    job=models.CharField(max_length=100) 
    hiredate=models.DateField() 
    comm=models.DecimalField(max_digits=10,decimal_places=3,null=True,blank=True) 
    mgr=models.ForeignKey('self',on_delete=models.SET_NULL,null=True,blank=True)
    
    

