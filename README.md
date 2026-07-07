# BazarJem – Full-Stack Django & React Gaming Store

Welcome to **BazarJem**, a modern full-stack gaming marketplace built with **Django**, **Django REST Framework**, **React**, and **JWT Authentication**. The platform allows users to browse gaming products, manage orders, maintain a wallet, and enjoy a secure and responsive shopping experience.

---

## 🛠️ Features

### 👤 User Authentication

* User registration and login with JWT Authentication.
* Secure authentication using HttpOnly Cookies and CSRF Protection.
* Profile management.

### 🎮 Gaming Products

* Browse gaming products with images, descriptions, prices, and special offers.
* Product categorization and filtering.
* Search functionality.
* Popular products, discounts, and featured items.

### 🛒 Shopping Cart & Orders

* Add products to the shopping cart.
* Place and manage orders.
* Track order status.
* Upload screenshots or additional information for custom orders.

### 💳 Wallet & Transactions

* Built-in wallet system.
* Deposit and withdrawal operations.
* Complete transaction history.
* Atomic database operations for financial integrity.

### ⭐ Comments & Reviews

* Users can submit comments on products.
* Nested replies.
* Admin approval before publishing comments.

### ⚙️ Admin Dashboard

* Manage products, users, categories, and orders.
* Approve or reject comments.
* Manage user roles and permissions.

### 📧 Email Notifications

* Asynchronous email notifications after successful orders.

---

## ⚡ Tech Stack

**Backend**

* Django
* Django REST Framework
* JWT Authentication
* PostgreSQL / SQLite

**Frontend**

* React
* Vite
* JavaScript

**Other Technologies**

* CKEditor
* Pillow
* Threading
* Caching
* Secure Cookies
* CSRF Protection

---

## 🚀 Installation

### Backend

```bash
git clone https://github.com/alirezakohzadi/bazarjem-django-react.git
cd backproject

python -m venv venv

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

---

## ▶️ Usage

```bash
python manage.py runserver
```

```bash
npm run dev
```

Open your browser:

```
http://localhost:5173
```

---

## 📁 Project Structure

```
backproject/
│
├── user/              # Authentication & User Management
├── products/          # Products, Categories & Reviews
├── orders/            # Shopping Cart & Orders
├── payments/          # Wallet & Transactions
├── backproject/       # Django Configuration
└── frontend/          # React + Vite Application
```

---

## 🔐 Security

* JWT Authentication
* HttpOnly Cookies
* CSRF Protection
* Secure Password Handling
* Atomic Database Transactions
* Environment Variables (.env)

---

## 📬 Contact

**GitHub:** https://github.com/alirezakohzadi

**Telegram:** @Alireza_ko1

**Instagram:** @_alirezakohzadi

---

## 📌 About

**BazarJem** is a modern gaming e-commerce platform developed with Django and React. It provides a complete online shopping experience for gaming products, featuring secure authentication, shopping cart, wallet system, order management, and an administrative dashboard.
