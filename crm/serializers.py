from rest_framework import serializers

from .models import ( 
	Lead
)

class LeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lead
        fields = (
            'lead_id', 
            'first_name',
            'last_name',
            'email',
            'phone_number',
            'role',
            'time',
            'qualifed',
            'sales_call'
        )



"""

	lead_id = models.AutoField(primary_key=True)
	first_name = models.CharField(max_length=25)
	last_name = models.CharField(max_length=25)
	email = models.CharField(max_length=25)
	phone_number = models.CharField(max_length=25)
	role = models.CharField(max_length=25)
	time = models.DateField()
	qualifed = models.OneToOneField(Qualify, blank=True, null=True, on_delete = models.CASCADE)
	sales_call = models.ForeignKey(Call, blank=True, null=True, on_delete=models.CASCADE)

"""	        