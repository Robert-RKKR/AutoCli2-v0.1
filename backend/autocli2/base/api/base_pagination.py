# Python import:
import inspect
import math

# Rest framework import:
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


# All paginator classes:
class BasePaginator(PageNumberPagination):
    # Pagination page query name:
    page_query_param = 'page_number'
    page_query_description = 'A page number within the paginated result set.'
    # Pagination size query name:
    page_size_query_param = 'page_size'
    page_size_query_description = 'Number of results to return per page.'
    # Pagination max size:
    max_page_size = 1000
    # Pagination last page query name:
    last_page_strings = ('last_page',)
    # Page details:
    page_details = None

    # Pagination response schema:
    def get_paginated_response(self, data):
        return Response({
            'page_links': {
                'page_next': self.get_next_link(),
                'page_previous': self.get_previous_link()
            },
            'page_count': self.page.paginator.count,
            'page_details': self.page_details,
            # 'page_count': math.ceil(self.page.paginator.count/self.size),
            'page_results': data
        })

    # Pagination paginate_queryset function extension:
    def paginate_queryset(self, queryset, request, view=None):

        # Run only if request contain page_details=True value:
        # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

        # Collect class details:
        class_representation = queryset.model
        class_all_attributes = inspect.getmembers(class_representation)
        class_filtered_attributes = []
        # Filter class attributes:
        for attribut in class_all_attributes:
            if not attribut[0].startswith('_'):
                class_filtered_attributes.append(attribut)
        # Add resoult to page details variable:
        self.page_details = class_filtered_attributes

        # Extend paginate_queryset function:
        super().paginate_queryset(queryset, request, view)


class BaseSmallPaginator(BasePaginator):
    # Pagination page size:
    page_size = 10


class BaseMediumPaginator(BasePaginator):
    # Pagination page size:
    page_size = 50


class BaseLargePaginator(BasePaginator):
    # Pagination page size:
    page_size = 100
