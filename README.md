# Flight Status Updater

This project is a real-time flight status updater system built with Django for the backend and Bootstrap for the frontend. It includes functionalities for updating flight statuses, fetching current statuses, and sending notifications via SMS using RabbitMQ.

## Tech Stack

### Frontend
- **HTML**: Used for structuring the web pages.
- **CSS**: For styling the web pages.
- **JavaScript**: For dynamic interactions on the client side.
- **Bootstrap**: For responsive design and styling.

### Backend
- **Django**: Python-based web framework for developing the backend logic.
- **RabbitMQ**: Message broker for handling real-time notifications.

### Additional Tools and Libraries
- **Pika**: Python client for RabbitMQ to send and receive messages.
- **Twilio**: For sending SMS notifications.
- **Mock Data**: Simulated data for testing the system.

## Features
- **Real-Time Updates**: Display current flight statuses including delays, cancellations, and gate changes.
- **Notifications**: Sends notifications via SMS using RabbitMQ.
- **Mock Data Integration**: Uses mock data to simulate integration with external airport systems.

## Endpoints

### Fetch All Flight Statuses
- **URL**: `/flights/`
- **Method**: `GET`
- **Description**: Returns a list of all flights and their statuses.

### Fetch Specific Flight Status
- **URL**: `/flights/<flight_number>/`
- **Method**: `GET`
- **Description**: Returns the status of a specific flight.

### Update Flight Status
- **URL**: `/flights/update/`
- **Method**: `POST`
- **Description**: Simulates updating flight status using mock data and sends notifications.

## Running the Project
