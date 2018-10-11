from models import cheetoz
from serializers import getcheetozdata
from rest_framework import generics
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.http import HttpResponse

# Create your views here.

security_key = 'cheetozsecuritykeycode'

class JSONResponse(HttpResponse):
	def __init__(self, data, **kwargs):
		content = JSONRenserer.render(data)
		kwargs['content_type'] = 'application/json'
		super(JSONResponse, self).__init__(content, **kwargs)

def cheetoz_set_score(request):
	if request.method == 'GET':
		prescore = 0
		try:
			phonenumber = request.GET['phonenumber']
			score = request.GET['score']
			key = request.GET['key']
			if key  != security_key:
				return HttpResponse('false')
			prescore = cheetoz.objects.get(phonenumber=phonenumber)
			if int(score) > int(prescore.score):
				prescore.score = score
				prescore.save()
				return HttpResponse('ok')
			else:
				return HttpResponse('false')
		except Exception, e:
			if str(e) == 'cheetoz matching query does not exist.':
				try:
					query = cheetoz(phonenumber=phonenumber, score=score)
					query.save()
					return HttpResponse('true')
				except:
					return HttpResponse('false')
			return HttpResponse(e)
		return HttpResponse(prescore)

class cheetozview(generics.ListCreateAPIView):
	queryset = cheetoz.objects.all()
	serializer_class = getcheetozdata
