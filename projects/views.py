from django.shortcuts import render
from projects.models import Project

# Create your views here.
def project_index(request):
	projects = Project.objects.all()
	context = {
		'projects': projects,
	}
	return render(request, 'project_index.html', context)


def project_detail(request, key):
	project = Project.objects.get(pk=key)
	context = {
		'project': project,
	}
	return render(request, 'project_detail.html', context)
