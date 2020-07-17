from django.db import models

# Create your models here.


#SQL TABLE OF CONTACT
class Contact(models.Model):
	name = models.CharField(max_length=40, blank=False, null=False)
	phone_number = models.IntegerField(null=False, blank=False)
	email = models.EmailField(max_length=40, null=False, blank=False)
	message = models.TextField()
	timestamp = models.DateTimeField(auto_now_add=True)


	def __str__(self):
		return self.name
