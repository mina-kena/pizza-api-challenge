from server import create_app, db  # Keep this import
from server.models.restaurant import Restaurant
from server.models.pizza import Pizza
from server.models.restaurant_pizza import RestaurantPizza
from server.controllers.restaurant_controller import restaurant_bp
from server.controllers.pizza_controller import pizza_bp
from server.controllers.restaurant_pizza_controller import restaurant_pizza_bp

app = create_app()  # This line is KEY - must come before db operations

# Register blueprints
app.register_blueprint(restaurant_bp)
app.register_blueprint(pizza_bp)
app.register_blueprint(restaurant_pizza_bp)

@app.route('/')
def home():
    return "Welcome to the Pizza Restaurant API!"

if __name__ == '__main__':
    app.run(debug=True)