from flask import Blueprint, request, jsonify
from server import db
from server.models.restaurant_pizza import RestaurantPizza
from server.models.restaurant import Restaurant
from server.models.pizza import Pizza

restaurant_pizza_bp = Blueprint('restaurant_pizzas', __name__)

@restaurant_pizza_bp.route('/restaurant_pizzas', methods=['POST'])
def create_restaurant_pizza():
    data = request.json
    
    
    if not all(key in data for key in ['price', 'pizza_id', 'restaurant_id']):
        return jsonify({"errors": ["Missing required fields"]}), 400
    
    if not 1 <= data['price'] <= 30:
        return jsonify({"errors": ["Price must be between 1 and 30"]}), 400
    
    
    if not Restaurant.query.get(data['restaurant_id']):
        return jsonify({"errors": ["Restaurant not found"]}), 400
    if not Pizza.query.get(data['pizza_id']):
        return jsonify({"errors": ["Pizza not found"]}), 400
    
    try:
        rp = RestaurantPizza(
            price=data['price'],
            pizza_id=data['pizza_id'],
            restaurant_id=data['restaurant_id']
        )
        db.session.add(rp)
        db.session.commit()
        
        
        pizza = Pizza.query.get(data['pizza_id'])
        restaurant = Restaurant.query.get(data['restaurant_id'])
        
        return jsonify({
            'id': rp.id,
            'price': rp.price,
            'pizza': pizza.to_dict(),
            'restaurant': restaurant.to_dict()
        }), 201
        
    except Exception as e:
        db.session.rollback()
        return jsonify({"errors": [str(e)]}), 400