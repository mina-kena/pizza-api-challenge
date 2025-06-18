from server import create_app, db
from server.models.restaurant import Restaurant
from server.models.pizza import Pizza
from server.models.restaurant_pizza import RestaurantPizza

app = create_app()

@app.route('/')
def home():
    return "Welcome to the Pizza Restaurant API!"

if __name__ == '__main__':
    app.run(debug=True)