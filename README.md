# Django SaaS Application

Welcome to the Django SaaS project! This application is a scalable software-as-a-service (SaaS) platform built with Django. It features user authentication, e-commerce functionality, course management, and more. Below you will find details about the project structure, core features, and setup instructions to get started.

## Table of Contents
1. [Project Overview](#project-overview)
2. [Features](#features)
3. [Project Structure](#project-structure)
4. [Installation](#installation)
5. [Usage](#usage)
6. [Technologies Used](#technologies-used)

## Project Overview
This Django SaaS platform includes several core features that are essential for a SaaS application. It contains custom authentication, shopping cart, checkout functionality, course and subscription management, and more. This project can serve as a template for a wide variety of SaaS applications, ranging from online learning platforms to e-commerce solutions.

## Features
- **Custom User Authentication**: Registration, login, email verification, password reset, and profile management using Django Allauth.
- **Shopping Cart & Checkout**: Add products to a shopping cart, proceed to checkout, and manage orders.
- **Course Management**: View and manage educational content including videos, documents, and resources.
- **Subscriptions**: Users can subscribe to services or newsletters.
- **Pages Module**: Static pages such as FAQs, About Us, and Contact are handled through the `pages` app.
- **Admin Interface**: Customizable Django admin panel to manage all models and users.
- **Responsive Frontend**: Frontend designed using Tailwind CSS and Flowbite components.
- **Error Handling**: Graceful error handling with custom error pages.

## Project Structure
The project is organized into several Django apps, each handling a distinct feature:

```
.
├── README.md
└── src
    ├── cart
    ├── checkouts
    ├── core
    ├── course
    ├── custom_auth
    ├── customers
    ├── home
    ├── pages
    ├── shop
    ├── subscriptions
    ├── templates
    └── utils
```

- **cart**: Handles cart-related logic like adding/removing items.
- **checkouts**: Manages the checkout and payment process.
- **core**: Contains main project settings, URLs, WSGI, and ASGI configurations.
- **course**: Manages educational content and courses.
- **custom_auth**: Handles user registration, login, profile updates, and authentication utilities.
- **customers**: Stores customer-specific information.
- **home**: Manages homepage views, static pages, and general content.
- **pages**: Handles additional static pages, including error handling.
- **shop**: Manages product listings and e-commerce-related features.
- **subscriptions**: Allows users to manage their subscriptions.
- **templates**: Contains reusable HTML templates for the frontend.
- **utils**: Contains utility functions and reusable scripts (e.g., authentication helpers).

## Installation
To set up the project locally, follow these steps:

1. **Clone the repository**:
   ```sh
   git clone https://github.com/your-username/django-saas.git
   cd django-saas
   ```

2. **Set up a virtual environment**:
   ```sh
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**:
   ```sh
   pip install -r requirements.txt
   ```

4. **Configure environment variables**:
   Create a `.env` file in the root directory and add the necessary environment variables (e.g., `SECRET_KEY`, `DEBUG`, `DATABASE_URL`).

5. **Apply migrations**:
   ```sh
   python manage.py migrate
   ```

6. **Create a superuser** to access the admin panel:
   ```sh
   python manage.py createsuperuser
   ```

7. **Run the server**:
   ```sh
   python manage.py runserver
   ```

8. **Access the application**:
   Open your browser and go to `http://127.0.0.1:8000/`.

## Usage
- **Homepage**: Navigate to the homepage to view available products, courses, and services.
- **User Authentication**: Register and log in to access personalized features.
- **Cart and Checkout**: Add products to your cart and proceed to checkout.
- **Profile Management**: Update your profile information from the profile page.
- **Admin Access**: Access the admin panel at `/admin/` to manage the content and users.

## Technologies Used
- **Backend**: Django 5.1.4
- **Frontend**: HTML, Tailwind CSS, Flowbite components
- **Database**: SQLite (default, can be replaced with PostgreSQL or MySQL)
- **Authentication**: Django Allauth for user management
- **Other**: JavaScript for interactivity, Flowbite for enhanced styling and components

Feel free to contribute by submitting pull requests or reporting issues.

