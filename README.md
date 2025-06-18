#  Pizza Restaurant API

A RESTful API for managing pizza restaurants, their menus, and pizza relationships.

# Quick Start

1. **Install dependencies**:
   ```bash
   pipenv install && pipenv shell

   flask db upgrade
python server/seed.py

python -m server.app


API Endpoints

Restaurants
Method	Endpoint	Description
GET	/restaurants	Get all restaurants
GET	/restaurants/<int:id>	Get a specific restaurant
DELETE	/restaurants/<int:id>	Delete a restaurant
PATCH	/restaurants/<int:id>	Update restaurant details
Pizzas
Method	Endpoint	Description
GET	/pizzas	Get all pizza types
Restaurant Pizzas
Method	Endpoint	Description
POST	/restaurant_pizzas	Create a pizza-restaurant link

Project Structure
text
pizza-api-challenge/
├── server/
│   ├── __init__.py       # App factory
│   ├── app.py            # Main app
│   ├── models/           # Database models
│   ├── controllers/      # API routes
│   └── seed.py           # Sample data
├── migrations/           # Database migrations
└── README.md             # File


Database Models
Restaurant: id, name, address

Pizza: id, name, ingredients

RestaurantPizza: id, price, restaurant_id, pizza_id

Troubleshooting
Common Issues
404 Errors: Ensure IDs exist (check with flask shell)

400 Errors: Validate request JSON format

Database Issues: Try:

bash
rm -f instance/pizza.db
flask db upgrade
python server/seed.py


License
MIT

Copyright (c) [2025] [Timina Makena]



