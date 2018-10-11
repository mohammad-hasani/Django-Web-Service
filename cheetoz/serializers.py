from rest_framework import serializers
from models import cheetoz

class getcheetozdata(serializers.ModelSerializer):
	class Meta:
		model = cheetoz
		field = ('phonenumber', 'score')
