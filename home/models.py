from django.db import models

class RoomDetails(models.Model):
    name = models.CharField(max_length=100)
    guest_count = models.IntegerField(default=3)
    price = models.DecimalField(decimal_places=1, max_digits=10)
    types = models.CharField(max_length=100)
    image = models.ImageField()
    availability = models.BooleanField(default=True)
    About = models.CharField(max_length=500)
    
    def __str__(self):
        return self.name
    

class Booking(models.Model):
    GENDER_CHOICES = (
    ('Male', 'Male'),
    ('FeMale', 'Female'),
    )
    Name = models.CharField(max_length=100, blank = False, null = False)
    Gender = models.CharField(max_length=6, choices = GENDER_CHOICES, default = 'Male')

    check_in_date = models.DateField()
    check_out_date = models.DateField()
    Email = models.EmailField(max_length=100)
    Phone = models.IntegerField()
    Number_Of_Adult = models.IntegerField()
    Number_of_Children = models.IntegerField()


    def __str__(self):
        return self.Name
    
    


