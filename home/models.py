from django.db import models

# Create your models here.
class Department(models.Model):
    dep_name = models.CharField(max_length=100)
    dep_discription = models.TextField()
    
    def __str__(self):
        return self.dep_name
        
class Docter(models.Model):
    doc_name = models.CharField(max_length=255)
    doc_spec = models.CharField(max_length=255)
    doc_dept = models.ForeignKey(Department, on_delete = models.CASCADE)
    doc_img = models.ImageField(upload_to = 'docters')    
    
    def __str__(self):
        return 'DR.' + self.doc_name + ' - (' + self.doc_spec + ')'

class Booking(models.Model):
    p_name = models.CharField(max_length=255)
    p_phone = models.CharField(max_length=25)
    p_email = models.EmailField()
    doc_name = models.ForeignKey(Docter, on_delete = models.CASCADE)
    booking_date = models.DateTimeField()
    booking_on = models.DateTimeField(auto_now=True) 
    
    def __str__(self):
        return self.p_name   