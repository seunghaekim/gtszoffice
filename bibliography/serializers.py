from rest_framework import serializers
from .models import *

class BookSerializer(serializers.ModelSerializer):
    lookup_field = 'slug'
    extra_kwargs = {
        'url': {'lookup_field': 'slug'}
    }

    class Meta:
        model = Book
        fields = ('id', 'title', 'subtitle', 'writer_str', 'designer_str', 'publisher_str', 'language', 'publisher_place', 'medium', 'page_amt', 'binding_type', 'pub_date', 'colorspace', 'price', 'slug', 'summary', 'figs', 'toc', 'images_related', 'distributor_related', 'updatetime', 'createtime', )


class BookshopSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Bookshop
        fields = ('name', 'name_eng', 'region', 'country', 'address', 'website', 'updatetime', 'createtime')