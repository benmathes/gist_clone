from django.db import models
import uuid


class Change(models.Model):
    """
    If I decide to implement storing just diffs for space saving, this model
    will be used.
    """
    created_at = models.DateTimeField(auto_now_add=True)
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
