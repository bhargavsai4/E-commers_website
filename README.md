# ShopHub - E-Commerce Platform

A full-stack e-commerce platform built with PHP, MySQL, HTML, and CSS. ShopHub provides a complete shopping experience with dedicated customer and admin modules, featuring secure authentication, role-based access control, and a responsive user interface.

## 🎯 Project Overview

ShopHub is a comprehensive e-commerce solution designed to manage online retail operations efficiently. The platform separates concerns between customer-facing features and administrative controls, ensuring a seamless experience for both shoppers and store managers.

## ✨ Features

### Customer Module
- **User Authentication**: Secure registration and login with session management
- **Product Browsing**: Browse products with real-time stock information
- **Shopping Cart**: Add, update, and remove products from cart
- **Order Management**: Place orders and track order history
- **User Profile**: View account details and order information
- **Responsive Design**: Optimized for desktop and mobile devices

### Admin Module
- **Dashboard**: Real-time analytics showing key metrics
  - Total products
  - Total orders
  - Revenue overview
  - Customer count
- **Order Management**: View and update order statuses
- **User Management**: Manage customer accounts
- **Product Management**: Add, edit, and remove products
- **Inventory Control**: Monitor stock levels

### Security Features
- **Secure Authentication**: Encrypted password handling and session validation
- **Role-Based Access Control (RBAC)**: Different access levels for customers and admins
- **Session Management**: Secure session handling with automatic timeouts
- **Input Validation**: Protection against SQL injection and XSS attacks

## 🛠️ Tech Stack

| Component | Technology |
|-----------|-----------|
| Frontend | HTML5, CSS3 |
| Backend | PHP |
| Database | MySQL |
| Session Management | PHP Sessions |
| Authentication | Session-based |

## 📊 Database Schema

### Tables
- **users**: Store customer and admin accounts
- **products**: Product catalog with pricing and stock
- **orders**: Customer orders and transaction history
- **order_items**: Individual items in each order
- **carts**: Shopping cart items (session-based)

### Relationships
- One-to-Many: Users → Orders
- One-to-Many: Orders → Order Items
- Many-to-One: Order Items → Products

## 🚀 Getting Started

### Prerequisites
- PHP 7.0+
- MySQL 5.7+
- Web Server (Apache/Nginx)

### Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/shophub.git
   cd shophub
   ```

2. **Configuration**
   - Update database connection details in `config/database.php`
   - Configure email settings for notifications (optional)

3. **Deploy**
   - Place files in your web server's root directory
   - Access the application via `http://localhost/shophub`

### Demo Credentials

**Admin Account**
- Email: `admin@shophub.com`
- Password: `admin123`

**Customer Account**
- Email: `customer@shophub.com`
- Password: `customer123`

link-file:///C:/Users/chenn/Downloads/index%20(2).html


## 🔐 Security Considerations

- **Password Security**: Passwords are hashed using `password_hash()` with bcrypt
- **SQL Injection Prevention**: Prepared statements with parameterized queries
- **XSS Protection**: Input sanitization and output encoding
- **CSRF Protection**: Token-based form validation
- **Session Security**: HTTPOnly and Secure flags on cookies

## 🎨 User Interface

- **Clean and Intuitive**: Easy navigation for both customers and admins
- **Responsive Design**: Works seamlessly on desktop, tablet, and mobile
- **Accessible**: WCAG 2.1 AA compliance standards
- **Fast Performance**: Optimized CSS and minimal JavaScript

## 📈 Features Roadmap

- [ ] Payment Gateway Integration (Stripe, PayPal)
- [ ] Email Notifications (Order confirmations, shipping updates)
- [ ] Advanced Search Filters
- [ ] Product Reviews and Ratings
- [ ] Wishlist Functionality
- [ ] Promotional Codes and Discounts
- [ ] Analytics Dashboard Enhancements
- [ ] Multiple User Roles (Seller, Warehouse Manager)

## 🐛 Known Issues & Limitations

- Cart is session-based (clears on logout)
- No payment processing yet (manual payment handling)
- Email notifications not implemented
- Limited product filtering options

## 🤝 Contributing

Contributions are welcome! To contribute:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👤 Author

**Your Name**
- GitHub: [@bhargavsai4](https://github.com/bhargavsai4)
- Email: chennamsettibhargavsai@email.com
- 
## 🙏 Acknowledgments

- Thanks to the PHP community for resources and best practices
- Inspired by popular e-commerce platforms
- Special thanks to contributors and testers

## 📞 Support

For support, email support@shophub.com or open an issue on GitHub.

---

**Made with ❤️ by Ch Bhargav Sai**
