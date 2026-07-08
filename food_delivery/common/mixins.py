from django.db import models
from django.utils import timezone


class TimestampMixin(models.Model):
    """
    Mixin that adds created_at and updated_at fields to a model.
    """

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class SoftDeleteMixin(models.Model):
    """
    Mixin that adds soft delete functionality to a model.
    """

    deleted_at = models.DateTimeField(null=True, blank=True)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        abstract = True

    def soft_delete(self):
        """Mark the object as deleted."""
        self.deleted_at = timezone.now()
        self.is_deleted = True
        self.save()

    def restore(self):
        """Restore a soft-deleted object."""
        self.deleted_at = None
        self.is_deleted = False
        self.save()


class ActiveManager(models.Manager):
    """
    Manager for handling soft-deleted objects.
    Returns only non-deleted objects by default.
    """

    def get_queryset(self):
        return super().get_queryset().filter(is_deleted=False)

    def all_including_deleted(self):
        return super().get_queryset()

    def only_deleted(self):
        return super().get_queryset().filter(is_deleted=True)
