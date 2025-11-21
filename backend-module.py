# modules/admin/routes.py - Admin Module Backend (Minimal)

from flask import Blueprint, render_template, request, jsonify, session
from werkzeug.security import check_password_hash
from database.db import db
from bson import ObjectId
from config import Config

admin_bp = Blueprint('admin', __name__, url_prefix='/admin')

# ============================================
# AUTHENTICATION
# ============================================

@admin_bp.route('/')
def index():
    return render_template('admin/login.html')


@admin_bp.route('/login', methods=['POST'])
def login():
    data = request.json

    # Verify access code
    if data.get('access_code') != Config.ADMIN_ACCESS_CODE:
        return jsonify({'error': 'Invalid access code'}), 403

    # Verify credentials
    user = db.users.find_one({'email': data['email'], 'role': 'admin'})
    if not user or not check_password_hash(user['password'], data['password']):
        return jsonify({'error': 'Invalid credentials'}), 401

    # Save session
    session['user_id'] = str(user['_id'])
    session['role'] = 'admin'

    return jsonify({
        'id': str(user['_id']),
        'name': user['name'],
        'role': 'admin'
    })


@admin_bp.route('/logout', methods=['POST'])
def logout():
    session.clear()
    return jsonify({'message': 'Logged out'})


# ============================================
# DASHBOARD
# ============================================

@admin_bp.route('/dashboard')
def dashboard():
    if 'user_id' not in session or session.get('role') != 'admin':
        return render_template('admin/login.html')

    return render_template('admin/dashboard.html')


@admin_bp.route('/stats', methods=['GET'])
def get_stats():
    if session.get('role') != 'admin':
        return jsonify({'error': 'Unauthorized'}), 403

    product_count = db.products.count_documents({})
    order_count = db.orders.count_documents({})

    # Total revenue pipeline
    pipeline = [
        {'$group': {'_id': None, 'total': {'$sum': '$total'}}}
    ]
    revenue = list(db.orders.aggregate(pipeline))
    total_revenue = revenue[0]['total'] if revenue else 0

    return jsonify({
        'products': product_count,
        'orders': order_count,
        'revenue': total_revenue
    })


# ============================================
# PRODUCTS
# ============================================

@admin_bp.route('/products', methods=['GET', 'POST', 'DELETE'])
def manage_products():
    if session.get('role') != 'admin':
        return jsonify({'error': 'Unauthorized'}), 403

    # Add product
    if request.method == 'POST':
        data = request.json
        product = {
            'name': data['name'],
            'price': float(data['price']),
            'category': data['category'],
            'stock': int(data['stock']),
            'description': data.get('description', ''),
            'icon': data.get('icon', '📦')
        }
        result = db.products.insert_one(product)
        return jsonify({
            'message': 'Product added',
            'id': str(result.inserted_id)
        })

    # Delete product
    if request.method == 'DELETE':
        product_id = request.args.get('id')
        db.products.delete_one({'_id': ObjectId(product_id)})
        return jsonify({'message': 'Product deleted'})

    # Get all products
    products = list(db.products.find())
    for p in products:
        p['_id'] = str(p['_id'])
    return jsonify(products)


# ============================================
# ORDERS
# ============================================

@admin_bp.route('/orders', methods=['GET'])
def get_orders():
    if session.get('role') != 'admin':
        return jsonify({'error': 'Unauthorized'}), 403

    orders = list(db.orders.find().sort('created_at', -1))

    for order in orders:
        order['_id'] = str(order['_id'])

        # Fetch customer name
        user = db.users.find_one({'_id': ObjectId(order['user_id'])})
        order['customer_name'] = user['name'] if user else 'Unknown'

    return jsonify(orders)


__all__ = ['admin_bp']
