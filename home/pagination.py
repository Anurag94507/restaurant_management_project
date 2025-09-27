from rest_framework.pagination import PageNumberPagination

class MenuItemPagination(PageNumberPagination):
    page_size = 12
    page_size_query_param = 'page_sizes'
    max_page_size = 100