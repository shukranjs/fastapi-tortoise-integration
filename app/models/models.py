from tortoise.models import Model
from tortoise import fields
from app.models.fields import CharEnumField
from app.schemas.schema import Status


class MyModel(Model):
    """
    A Tortoise ORM model that represents a database table 'my_model' with an Enum field 'status'.

    Attributes:
        id (int): The primary key of the model.
        status (Status): The status field which uses the custom CharEnumField.
    """

    id = fields.IntField(pk=True)
    status = CharEnumField(enum_type=Status, max_length=10)

    class Meta:
        table = "my_model"
