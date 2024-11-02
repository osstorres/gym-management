# 🏋️ Gym Management App

An application for managing memberships, clients, and subscriptions in a gym. This app allows customization of memberships (e.g., weekly, monthly, or custom) and tracks client subscriptions. Built using Django and Django Admin for easy management and scalability.

## 📋 Features

- **Customizable Memberships**: Define various types of memberships like weekly, monthly, annual, or custom.
- **Client Management**: Add and manage clients with personal details.
- **Subscription Tracking**: Keep track of client memberships with start and end dates.
  
## 📂 Project Structure

```plaintext
gym_management/
├── gym_management/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── src/
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
└── manage.py
```

##  📄 Models Overview

* Membership: Defines types and pricing of memberships, including custom durations.
* Client: Stores client data like name, email, and phone number.
* MembershipSubscription: Tracks each client’s membership details, including start and end dates.

##  🎛️ Admin Configuration
All models are accessible and manageable through Django Admin. This allows easy tracking and updating of memberships, clients, and their subscriptions.

##  💼 License
This project is licensed under the MIT License. See the LICENSE file for more details.

