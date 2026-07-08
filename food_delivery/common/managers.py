from django.db import models


class QuerySet(models.QuerySet):
    """
    Custom QuerySet with common utility methods.
    """

    def active(self):
        """Filter for active items (not deleted)."""
        return self.filter(is_deleted=False)

    def deleted(self):
        """Filter for deleted items."""
        return self.filter(is_deleted=True)

    def search(self, query, search_fields):
        """
        Search across multiple fields.
        """
        from django.db.models import Q

        q_objects = Q()
        for field in search_fields:
            q_objects |= Q(**{f"{field}__icontains": query})
        return self.filter(q_objects)


class Manager(models.Manager):
    """
    Custom Manager that uses QuerySet.
    """

    def get_queryset(self):
        return QuerySet(self.model, using=self._db)

    def active(self):
        return self.get_queryset().active()

    def deleted(self):
        return self.get_queryset().deleted()

    def search(self, query, search_fields):
        return self.get_queryset().search(query, search_fields)
