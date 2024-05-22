import os
from dotenv import load_dotenv
from tortoise import Tortoise

# Load environment variables from .env file
load_dotenv()

# Print environment variables for debugging purposes (optional)
print(os.getenv("POSTGRES_USER"))
print(os.getenv("POSTGRES_PASSWORD"))
print(os.getenv("POSTGRES_DB"))

# Tortoise ORM configuration dictionary
TORTOISE_ORM = {
    "connections": {
        "default": f"postgres://{os.getenv('POSTGRES_USER')}:{os.getenv('POSTGRES_PASSWORD')}@db:5432/{os.getenv('POSTGRES_DB')}"
    },
    "apps": {
        "models": {
            "models": ["app.models.models", "aerich.models"],
            "default_connection": "default",
        }
    },
}


async def init_db():
    """
    Initialize the Tortoise ORM database connection and generate schemas.
    """
    await Tortoise.init(config=TORTOISE_ORM)
    await Tortoise.generate_schemas()
