from rest_framework.pagination import PageNumberPagination


class StandardResultsSetPagination(PageNumberPagination):
    """
    Standard pagination for list views.
    Default page size: 10
    """

    page_size = 10
    page_size_query_param = "page_size"
    max_page_size = 100


class LargeResultsSetPagination(PageNumberPagination):
    """
    Pagination for large result sets.
    Default page size: 50
    """

    page_size = 50
    page_size_query_param = "page_size"
    max_page_size = 100
