# creditcard_approval_system

# Credit Card Approval System

Developed by *Shanmukhi9994*

---

## Project Overview

The *Credit Card Approval System* is a Django REST API application that manages customer data and credit card/loan approvals based on customer profiles, credit scores, and loan eligibility criteria.

The system includes:

- Customer registration and management
- Loan/credit card approval eligibility checks
- Loan creation and management
- Bulk data ingestion from Excel files
- Dockerized deployment for easy setup and scaling

---

## Features

- Custom customer_id as primary key for customers
- Credit score based loan/credit card approval process
- EMI calculation and payment tracking
- APIs to view loans for customers and specific loan details
- Data ingestion via Excel upload endpoint
- Fully dockerized for development and production

---

## Prerequisites

- [Docker](https://www.docker.com/get-started)
- [Docker Compose](https://docs.docker.com/compose/install/)

---

## Getting Started

### Clone the Repository

git clone https://github.com/Shanmukhi9994/credit-card-approval-system.git
cd credit-card-approval-system

text

### Build and Run with Docker Compose

Build and start containers with:

docker-compose up --build

text

For running containers in background:

docker-compose up -d

text

To stop and remove containers:

docker-compose down

text

---

## API Endpoints

| Endpoint                        | Method | Description                            |
|--------------------------------|--------|------------------------------------|
| /api/register-customer/       | POST   | Register a new customer              |
| /api/check-eligibility/       | POST   | Check loan/credit approval eligibility |
| /api/create-loan/             | POST   | Create a new loan/credit card record |
| /view-loan/<loan_id>/         | GET    | View loan details by loan ID         |
| /view-loans/<customer_id>/    | GET    | View all active loans for a customer |
| /api/fill-data/               | POST   | Upload Excel data to populate DB     |

---

## Example Requests

### Register Customer

curl -X POST http://localhost:8000/api/register-customer/
-H "Content-Type: application/json"
-d '{"first_name": "John", "last_name": "Doe", "age": 30, "phone_number": "1234567890", "monthly_income": 50000}'

text

### Check Eligibility

curl -X POST http://localhost:8000/api/check-eligibility/
-H "Content-Type: application/json"
-d '{"customer_id": 1, "loan_amount": 100000, "interest_rate": 10, "tenure": 12}'

text

### Create Loan

curl -X POST http://localhost:8000/api/create-loan/
-H "Content-Type: application/json"
-d '{"customer_id": 1, "loan_amount": 100000, "interest_rate": 10, "tenure": 12}'

text

---

## Docker Commands

- Build images and start services:

docker-compose up --build

text

- Start in detached mode:

docker-compose up -d

text

- View logs:

docker-compose logs -f

text

- Stop and clean up:

docker-compose down

text

---

## Project Structure

- api/ - Django app containing models, views, and serializers
- Dockerfile - Docker image setup
- docker-compose.yml - Docker Compose configuration
- customer_data.xlsx & loan_data.xlsx - Sample data files for data ingestion
- manage.py - Django management script

---

## Notes

- Ensure that the Excel files are mounted inside the container at /code/ for the fill-data endpoint to work.
- The system uses a custom primary key customer_id for Customer model; queries should use this field.
- EMI calculations and credit score logic are essential for loan approval decisions.

---

## Contribution

Contributions, issues, and feature requests are welcome!

---

© 2025 Shanmukhi9994
