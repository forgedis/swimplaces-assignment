from rest_framework import viewsets, filters
from src.models import Location, Category
from .serializers import LocationSerializer
from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.db.models import Count

class LocationViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['id', 'name', 'dog_swimming']

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        dog_swimming_param = self.request.query_params.get('dog_swimming')

        if dog_swimming_param == Location.dog_swimming_choices[0][0]:
            queryset = queryset.filter(dog_swimming=Location.dog_swimming_choices[0][1])

        if dog_swimming_param == Location.dog_swimming_choices[1][0]:
            queryset = queryset.filter(dog_swimming=Location.dog_swimming_choices[1][1])

        serializer = self.get_serializer(queryset, many=True)
        context = {'location_data': serializer.data}

        return render(request, 'locations.html', context)
    
    def statistics(self, request, *args, **kwargs):
        context = {
            'number_of_locations': Location.objects.count(),
            'categories': Category.objects.exclude(name='').annotate(location_count=Count('location')).order_by('-location_count'),
            'top_10_locations': Location.objects.order_by('-rating')[:10],
        }

        return render(request, 'statistics.html', context)

    
class LocationDetailView(DetailView):
    model = Location
    template_name = 'location_detail.html'
    context_object_name = 'location'