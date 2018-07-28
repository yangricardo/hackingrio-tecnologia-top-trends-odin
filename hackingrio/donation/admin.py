from django.contrib import admin
from donation.models import DonatedBeneficiary, Donation, Beneficiary

# Register your models here.
admin.site.register([DonatedBeneficiary, Donation, Beneficiary])