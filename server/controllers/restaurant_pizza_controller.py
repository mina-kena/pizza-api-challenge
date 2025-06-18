from flask import Blueprint, request, jsonify
from server import db
from server.models.restaurant_pizza import RestaurantPizza

restaurant_pizza_bp = Blueprint('restaurant_pizza', __name__)


@restaurant_pizza_bp.route('/restaurant_pizzas', methods=['POST'])
def create_restaurant_pizza():
    data = request.json
    
    
    if not all(key in data for key in ['price', 'pizza_id', 'restaurant_id']):
        return jsonify({"errors": ["Missing required fields"]}), 400
    
    if not 1 <= data['price'] <= 30:
        return jsonify({"errors": ["Price must be between 1 and 30"]}), 400
    
    try:
        new_rp = RestaurantPizza(
            price=data['price'],
            pizza_id=data['pizza_id'],
            restaurant_id=data['restaurant_id']
        )
        db.session.add(new_rp)
        db.session.commit()
        
        return jsonify({
            'id': new_rp.id,
            'price': new_rp.price,
            'pizza_id': new_rp.pizza_id,
            'restaurant_id': new_rp.restaurant_id
        }), 201
        
    except Exception as e:
        db.session.rollback()
        return jsonify({"errors": [str(e)]}), 400