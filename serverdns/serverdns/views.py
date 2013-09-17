# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.utils import timezone

from models import dsmapping


def index(request):
	latest_mapping_list = dsmapping.objects.all().order_by('-cdate')[:10]
	context = {'latest_mapping_list': latest_mapping_list}
	return render(request, 'index.html', context)

def create(request,pn,ip):
	try:
		mapping = dsmapping.objects.get(pname=pn)
		mapping.sip=ip;
		mapping.cdate=timezone.now();
		mapping.save()
		return HttpResponse("Update")
	except dsmapping.DoesNotExist:
		mapping = dsmapping(pname=pn,sip=ip,cdate=timezone.now())
		mapping.save()
		return HttpResponse("Create")

def retrieve(request,pn):
	mapping = get_object_or_404(dsmapping, pname=pn)
	return HttpResponse("%s" %mapping.sip)