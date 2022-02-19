from django import template
from formulario.models import CatForm

register = template.Library()

@register.filter
def get_form_etapa(formularios,c,e):
    return formularios.objects.filter(componente=c,etapa=e)