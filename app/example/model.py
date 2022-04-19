import uuid
from tortoise import fields
from core.base.model import Model


class Example(Model):
  name = fields.CharField(max_length=40)

  class Meta:
    table = 'examples'
