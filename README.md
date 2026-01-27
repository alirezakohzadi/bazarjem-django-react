# BazarJem – Full-Stack Django & React Project

Welcome to **BazarJem**, a full-stack web application for tracking shipments and managing online orders. This project is built with **Django**, **Django REST Framework**, **JWT Authentication**, and **React**. It’s designed to be **production-ready**, scalable, and secure.

---

## 🛠️ Features

- **User Authentication**  
  Register, login, logout, and manage user profiles using JWT tokens.

- **Products & Categories**  
  Manage products with multiple options, images, prices, and special offers.

- **Orders & Cart**  
  Users can add multiple products to a cart, place orders, and track their status.

- **Transactions & Wallet**  
  Secure wallet system with deposits, withdrawals, and balance tracking.

- **Comments & Ratings**  
  Users can leave comments on product options with nested replies.

- **Admin Features**  
  Admins can approve comments, manage users, and change user roles.

- **Async Email Notifications**  
  Users get confirmation emails asynchronously when orders are created.

---

## ⚡ Tech Stack

- **Backend:** Django, Django REST Framework, JWT  
- **Frontend:** React + Vite  
- **Database:** PostgreSQL / SQLite (dev)  
- **File Uploads:** CKEditor, Pillow for image handling  
- **Authentication:** JWT, secure cookies, CSRF protection  
- **Others:** Threading for async tasks, caching for safe transactions

---

## 🚀 Installation

### Backend

```bash
git clone https://github.com/alirezakohzadi/bazarjem-django-react.git
cd backproject
python -m venv venv
source venv/bin/activate  # Linux / macOS
venv\Scripts\activate     # Windows
pip install -r requirements.txt
