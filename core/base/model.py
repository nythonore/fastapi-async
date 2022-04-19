import uuid
from tortoise import fields, models


class UUIDMixin():
  id = fields.UUIDField(pk=True, unique=True, default=uuid.uuid4)


class TimeStampMixin():
  created_at = fields.DatetimeField(auto_now_add=True)
  updated_at = fields.DatetimeField(auto_now=True)
  deleted_at = fields.DatetimeField(null=True)


class Model(models.Model, UUIDMixin, TimeStampMixin):
  class Meta:
    abstract = True
