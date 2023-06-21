from django.db import models

# Create your models here.

class Department(models.Model):
    depart_name = models.CharField(max_length=30, null=True, blank=True)
    depart_decs = models.TextField()
    
    class Meta:
        verbose_name = 'Department'
        verbose_name_plural = 'Department'
        
    def __str__(self) :
        return self.depart_name


class Doctor(models.Model):
    doc_name = models.CharField(max_length=30, null=True, blank=True)
    doc_spec = models.CharField(max_length=100, null=True, blank=True)
    depart_name = models.ForeignKey(Department, on_delete=models.CASCADE)
    doc_image = models.ImageField(upload_to='doctors')
    
    class Meta:
        verbose_name = 'Doctors'
        verbose_name_plural = 'Doctors'
        
    def __str__(self):
        return self.doc_name
        

class Booking(models.Model):
    p_name = models.CharField(max_length = 100)
    p_phonenumber = models.CharField(max_length = 100)
    p_email = models.EmailField()
    doc_name = models.ForeignKey(Doctor, on_delete=models.CASCADE)   
    booking_date = models.DateField()
    booking_on = models.DateField(auto_now=True) 
    