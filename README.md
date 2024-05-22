# fastapi-tortoise-integration
This repository contains a scalable FastAPI application that uses Tortoise ORM for database interactions. The application is structured to ensure maintainability and scalability, adhering to best practices for modern Python web development. In the provided repository, we have addressed the limitation in Tortoise ORM where the CharEnum field does not generate the corresponding schema for PostgreSQL databases. Instead, it defaults to a VARCHAR column type. To overcome this limitation, we've implemented a custom field class that ensures the correct SQL DDL (Data Definition Language) for the underlying PostgreSQL database.

To run this app, run:
 - `sudo docker-compose up -d --build`
