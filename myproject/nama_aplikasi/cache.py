from django.core.cache import cache

def get_data():
   data = cache.get('cached_data')
   if not data:
       # Expensive database query or data generation
       data = perform_expensive_operation()
       cache.set('cached_data', data, timeout=3600)  # Cache for 1 hour
   return data