from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.cache import cache_page
from .models import Property
from .utils import get_all_properties


@cache_page(60 * 15)  # Cache for 15 minutes
def property_list(request):
    """
    View to return all properties with 15-minute caching
    Uses low-level cache API for queryset caching
    """
    properties = get_all_properties()
    data = []
    
    for prop in properties:
        data.append({
            'id': prop.id,
            'title': prop.title,
            'description': prop.description,
            'price': str(prop.price),
            'location': prop.location,
            'created_at': prop.created_at.isoformat(),
        })
    
    return JsonResponse({'properties': data})
