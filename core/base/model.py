from tortoise import fields, models


class Model(models.Model):
  id = fields.IntField(pk=True)

  async def serialize(self):
    data = {}

    for field in self._meta.db_fields:
      data[field] = getattr(self, field)

    for field in self._meta.backward_fk_fields:
      data[field] = await getattr(self, field).all().values()

    return data

  class Meta:
    abstract = True
