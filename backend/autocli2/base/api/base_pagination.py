# Python - library import:
import inspect
import math

# Rest framework - import:
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

    # Pagination response schema:
    def get_paginated_response(self, data):
        return Response({
            'page_results': data,
            'page_objects': self.page.paginator.count,
            'page_count': math.ceil(self.page.paginator.count/self.page_size),
            'page_links': {
                'page_next': self.get_next_link(),
                'page_previous': self.get_previous_link()
            }
        })


class BaseSmallPaginator(BasePaginator):
    # Pagination page size:
    page_size = 10


class BaseMediumPaginator(BasePaginator):
    # Pagination page size:
    page_size = 50


class BaseLargePaginator(BasePaginator):
    # Pagination page size:
    page_size = 100
