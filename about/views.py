from django.shortcuts import render
from django.http import HttpResponse
from django_user_agents.utils import get_user_agent

from about.models import Courses, Experience, Projects, Testimonials

def home(request):
    print('00000000')
    print(request.user_agent.is_pc)
    if request.user_agent.is_pc:
        return render(request, 'about/base.html')
    else:
        # return HttpResponse("This device isn't comaptible yet! Please use a laptop :)")
        return render(request, 'about/base.html')


def sections(request):
    context = {}
    context['courses'] = Courses.objects.all().order_by('-id')
    context['experience'] = Experience.objects.all().order_by('-id')
    context['projects'] = Projects.objects.all().order_by('-id')
    context['testimonials'] = Testimonials.objects.all().order_by('-id')

    return render(request, 'about/sections.html', context)

def ssl(request):
    return HttpResponse("Ic_uyTPJhB9Q8Vqv2OIm_QV94tlJo-D59n9pWof4lzc.-TbmTJ2BHVCcNYioVcEspxPNivdTF3Qc34ltWNCmxGo")
