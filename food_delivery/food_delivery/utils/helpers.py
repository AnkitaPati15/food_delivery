from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
import json


def get_page_data(queryset, page_num, page_size=10):
    """
    Paginate queryset and return paginated data.
    """
    paginator = Paginator(queryset, page_size)
    try:
        page = paginator.page(page_num)
    except (PageNotAnInteger, EmptyPage):
        page = paginator.page(1)

    return page


def search_queryset(queryset, search_fields, query):
    """
    Search queryset using multiple fields.
    """
    q_objects = Q()
    for field in search_fields:
        q_objects |= Q(**{f"{field}__icontains": query})
    return queryset.filter(q_objects)


def safe_json_loads(data, default=None):
    """
    Safely load JSON data.
    """
    try:
        return json.loads(data)
    except (json.JSONDecodeError, TypeError):
        return default or {}
