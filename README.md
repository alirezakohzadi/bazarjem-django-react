# BazarJem – Full-Stack Django & React Project

Welcome to **BazarJem**, a full-stack web application for tracking shipments and managing online orders. This project is built with **Django**, **Django REST Framework**, **JWT Authentication**, and **React**. It’s designed to be production-ready, scalable, and secure.

---

## 🛠️ Features

### User Authentication

* Register, login, logout, and manage user profiles using JWT tokens.
* Secure authentication with CSRF protection and HttpOnly cookies.

### Products & Categories

* Manage products with multiple options, images, prices, and special offers.
* Filter products by game type and categories like special offers, discounts, and popular items.

### Orders & Cart

* Users can add multiple products to a cart, place orders, and track their status.
* Upload screenshots and provide details for each order.

### Transactions & Wallet

* Wallet system with deposits and withdrawals.
* Transaction history with atomic operations to ensure balance integrity.

### Comments & Ratings

* Users can leave comments on products.
* Nested replies supported and admin approval required before publishing.

### Admin Features

* Approve or reject comments.
* Manage users and change user roles.

### Async Email Notifications

* Confirmation emails sent asynchronously when orders are placed.

---

## ⚡ Tech Stack

* **Backend:** Django, Django REST Framework, JWT
* **Frontend:** React + Vite
* **Database:** PostgreSQL (production) / SQLite (development)
* **File Uploads:** CKEditor for rich text, Pillow for image handling
* **Authentication:** JWT, secure cookies, CSRF protection
* **Others:** Threading for async tasks, caching for safe transactions

---

## 🚀 Installation

### Backend

```bash
git clone https://github.com/alirezakohzadi/bazarjem-django-react.git
cd backproject
python -m venv venv
# Activate virtual environment:
# Linux / macOS
source venv/bin/activate
# Windows
venv\Scripts\activate
pip install -r requirements.txt
```

### Frontend

```bash
cd frontend
npm install
npm run dev
```

### Usage

```bash
# Start backend server
python manage.py runserver

# Start frontend development server
npm run dev

# Open the app in your browser
# Default: http://localhost:5173
```

## Project Structure

```
backproject/
│
├─ user/                 # Custom user model and auth API
├─ products/             # Products, options, comments
├─ orders/               # Order management, cart
├─ payments/             # Wallet & transaction system
├─ backproject/          # Django settings & URLs
└─ frontend/             # React + Vite app
```

## 🔐 Security & Best Practices

* Secrets and `.env` files are excluded from GitHub.
* JWT Authentication with HttpOnly cookies.
* CSRF protection is enabled.
* Atomic transactions for wallet and order operations.

## 📬 Contact & Feedback

For questions or suggestions, feel free to contact me:

* GitHub: [alirezakohzadi](https://github.com/alirezakohzadi)
* Telegram: [Alireza_ko1](https://t.me/Alireza_ko1)
* Instagram: [@_alirezakohzadi](https://instagram.com/_alirezakohzadi)
