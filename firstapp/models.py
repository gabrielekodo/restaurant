from django.db import models

# Create your models here.
class MenuItems(models.Model):
     name=models.CharField(max_length=255)
     description = models.CharField(max_length=1000,default='')
     image = models.CharField(max_length=1000,default='https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExZDViaXlpMWc1N2ttODhqaXV2b3Z2eHgwdzdkMTVzcXduMTAyYjdzbSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/84ZzhsJZWlE3e/giphy.gif')
     price=models.IntegerField()

     def __str__(self):
         return self.name


class Reservation(models.Model):
    first_name=models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
    guest_count=models.IntegerField()
    reservation_time=models.DateTimeField(auto_now=True)
    comments=models.CharField(max_length=1000)

    def __str__(self):
        return self.first_name+' '+self.last_name
