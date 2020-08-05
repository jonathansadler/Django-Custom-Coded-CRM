from django.db import models

# Create your models here.



class Close(models.Model):	
	first_name = models.CharField(max_length=25)
	last_name = models.CharField(max_length=25)
	product_no = models.CharField(max_length=25)
	credit_card_no = models.CharField(max_length=25)
	billing_address = models.CharField(max_length=25)
	shipping_address = models.CharField(max_length=25)
	invoice_no = models.CharField(max_length=25)
	def __str__(self):
		return str(self.invoice_no)




class Call(models.Model):
	call_no = models.AutoField(primary_key=True)
	time_of_call = models.DateField()
	recording = models.CharField(max_length=25)
	willingness_to_buy =  models.CharField(max_length=25)
	notes =  models.CharField(max_length=25)
	close =  models.OneToOneField(Close, blank=True, null=True, on_delete = models.CASCADE)
	schedule_call_back = models.DateField()

	def __str__(self):
		return str(self.call_no)

class Qualify(models.Model):
	age = models.CharField(max_length=25)
	sex = models.CharField(max_length=25)
	martial_status = models.BooleanField(default=False)
	occupation = models.CharField(max_length=25)
	role = models.CharField(max_length=25)
	budget = models.CharField(max_length=25)
	time_of_call = models.DateField()
	qualified = models.BooleanField(default=False)
	notes = models.CharField(max_length=25)
	recording = models.CharField(max_length=25)
	schedule_call_back = models.DateField()
	
	def __str__(self):
		return str(self.qualified)



class Lead(models.Model):
	lead_id = models.AutoField(primary_key=True)
	first_name = models.CharField(max_length=25)
	last_name = models.CharField(max_length=25)
	email = models.CharField(max_length=25)
	phone_number = models.CharField(max_length=25)
	role = models.CharField(max_length=25)
	time = models.DateField()
	qualifed = models.OneToOneField(Qualify, blank=True, null=True, on_delete = models.CASCADE)
	sales_call = models.ForeignKey(Call, blank=True, null=True, on_delete=models.CASCADE)

	def __str__(self):
		return str(self.lead_id) + " " + str(self.first_name) + " "  + str(self.last_name) 


"""
        max_length=2,    
        blank=True,
        null=True


blank=True, null=True


max_length=2

        models.CharField: {'widget': TextInput(attrs={'size':'20'})},
        models.CharField: {'widget': Textarea(attrs={'rows':1, 'cols':1})},

str(self.add_report

"""        