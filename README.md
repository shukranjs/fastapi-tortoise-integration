<div align="center">
  <h1>FastAPI Application with Scalable Architecture and Custom Tortoise ORM Field</h1>
  <p>This repository contains a scalable FastAPI application that leverages Tortoise ORM for efficient database interactions. The application is structured to ensure maintainability and scalability, following best practices for modern Python web development.</p>
</div>

## Overview

Tortoise ORM is a robust tool for working with databases in Python, especially in asynchronous codebases. However, a known limitation is the CharEnum field, which does not generate the corresponding schema for PostgreSQL databases. Instead, it defaults to a VARCHAR column type. To address this limitation, we've implemented a custom field class that ensures the correct SQL DDL (Data Definition Language) for PostgreSQL databases.

## Features

- **Scalable Architecture**: The application follows a scalable architecture, allowing for easy extension and maintenance as the project grows.
- **Tortoise ORM Integration**: Utilizes Tortoise ORM for efficient database operations, ensuring optimal performance and reliability.
- **Custom Field Class**: Implements a custom field class to generate the correct SQL DDL for PostgreSQL databases, overcoming limitations of the default CharEnum field.
- **FastAPI Integration**: Seamlessly integrates with FastAPI, a modern web framework for building APIs with Python, enabling rapid development and deployment.

## Installation and Setup

To run the application locally, follow these steps:

1. Clone the repository to your local machine:

   ```bash
   https://github.com/shukranjs/fastapi-tortoise-integration.git
   cd fastapi-tortoise-integration
   chmod +x run.sh
   ./run.sh
   ```

