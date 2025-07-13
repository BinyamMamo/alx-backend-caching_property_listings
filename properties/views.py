from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.cache import cache_page
from .models import Property


@cache_page(60 * 15)  # Cache for 15 minutes
def property_list(request):
    """
    View to return all properties with 15-minute caching
    """
    properties = Property.objects.all()
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
