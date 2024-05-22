from tortoise.backends.base.schema_generator import BaseSchemaGenerator
from tortoise.fields import CharField
from enum import Enum
from typing import Any, Optional, Type


class CharEnumField(CharField):
    """
    A custom CharField that enforces enum types for values.

    Attributes:
        enum_type (Type[Enum]): The Enum type that this field accepts.
    """

    def __init__(self, enum_type: Type[Enum], *args: Any, **kwargs: Any) -> None:
        self.enum_type = enum_type
        super().__init__(*args, **kwargs)

    def to_db_value(self, value: Optional[Enum], instance: Any) -> Optional[str]:
        """
        Convert the Python value to a database-compatible value.

        Args:
            value (Optional[Enum]): The value to be converted.
            instance (Any): The instance being converted.

        Returns:
            Optional[str]: The value converted for database storage.
        """
        if value is None:
            return None
        if not isinstance(value, self.enum_type):
            raise ValueError(f"Value '{value}' is not a valid {self.enum_type}")
        return value.value

    def to_python_value(self, value: Optional[str]) -> Optional[Enum]:
        """
        Convert the database value to a Python-compatible value.

        Args:
            value (Optional[str]): The value to be converted.

        Returns:
            Optional[Enum]: The Python-compatible value.
        """
        if value is None:
            return None
        try:
            return self.enum_type(value)
        except ValueError:
            raise ValueError(f"Value '{value}' is not a valid {self.enum_type}")


class PostgresEnumSchemaGenerator(BaseSchemaGenerator):
    """
    Schema generator for PostgreSQL that supports custom Enum fields.
    """

    def _generate_column_sql(self, model: Any, field: CharField) -> str:
        """
        Generate the SQL for a column in the table.

        Args:
            model (Any): The model that contains the field.
            field (CharField): The field to generate SQL for.

        Returns:
            str: The SQL for the column.
        """
        if isinstance(field, CharEnumField):
            enum_name = f"{model._meta.db_table}_{field.model_field_name}_enum"
            return f'"{field.model_field_name}" {enum_name} NOT NULL'
        return super()._generate_column_sql(model, field)

    def _generate_create_enum_type(self, model: Any, field: CharField) -> Optional[str]:
        """
        Generate the SQL to create an Enum type in the database.

        Args:
            model (Any): The model that contains the field.
            field (CharField): The field to generate the Enum type for.

        Returns:
            Optional[str]: The SQL to create the Enum type, or None if not applicable.
        """
        if isinstance(field, CharEnumField):
            enum_name = f"{model._meta.db_table}_{field.model_field_name}_enum"
            enum_values = ", ".join(f"'{v.value}'" for v in field.enum_type)
            return f"CREATE TYPE {enum_name} AS ENUM ({enum_values});"
        return None

    def _generate_create_table(self, model: Any) -> str:
        """
        Generate the SQL to create a table, including Enum types.

        Args:
            model (Any): The model to generate the table for.

        Returns:
            str: The SQL to create the table.
        """
        create_enum_statements = []
        for field in model._meta.fields_map.values():
            create_enum_sql = self._generate_create_enum_type(model, field)
            if create_enum_sql:
                create_enum_statements.append(create_enum_sql)

        create_enum_sql = "\n".join(create_enum_statements)
        create_table_sql = super()._generate_create_table(model)
        return f"{create_enum_sql}\n{create_table_sql}"
