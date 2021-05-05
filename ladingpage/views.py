# from django.http import HttpResponse
# from django.template import Template, Context
from django.shortcuts import render

# def plantilla(request):
#      plantillaExterna = open("C:\Trabajo2\entorno1\ladingpage\ladingpage\plantillas\plantilla.html")
#      template = Template(plantillaExterna.read())
#      plantillaExterna.close()
#      contexto = Context()
#      documento = template.render(contexto)
#      return HttpResponse(documento)

def index(request):
    return render(request,'index.html')