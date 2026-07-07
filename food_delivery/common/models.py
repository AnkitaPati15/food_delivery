from django.db import models
from django.utils import timezone


class SoftDeleteQuerySet(models.QuerySet):

    def delete(self):
        return self.update(
            is_deleted=True,
            deleted_at=timezone.now(),
        )

    def alive(self):
        return self.filter(is_deleted=False)

    def deleted(self):
        return self.filter(is_deleted=True)


class SoftDeleteManager(models.Manager):

    def get_queryset(self):
        return SoftDeleteQuerySet(
            self.model,
            using=self._db
        ).filter(
            is_deleted=False
        )


class SoftDeleteModel(models.Model):

    is_deleted = models.BooleanField(
        default=False
    )

    deleted_at = models.DateTimeField(
        null=True,
        blank=True
    )

    objects = SoftDeleteManager()

    all_objects = models.Manager()

    class Meta:
        abstract = True

    def delete(self, using=None, keep_parents=False):

        self.is_deleted = True
        self.deleted_at = timezone.now()

        self.save(using=using)

    # 👇 Add it here
    def restore(self):

        self.is_deleted = False
        self.deleted_at = None

        self.save()
        