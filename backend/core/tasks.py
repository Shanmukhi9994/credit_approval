from celery import shared_task
import pandas as pd
from .models import Customer, Loan
from datetime import datetime
from django.db import transaction

@shared_task
def ingest_customer_data():
    df = pd.read_excel('/code/customer_data.xlsx')
    with transaction.atomic():
        for _, row in df.iterrows():
            Customer.objects.update_or_create(
                id=int(row['customer_id']),
                defaults=dict(
                    first_name=row['first_name'],
                    last_name=row['last_name'],
                    age=int(row.get('age', 0)) if 'age' in row else 0,
                    phone_number=str(row['phone_number']),
                    monthly_income=int(row['monthly_salary']),
                    approved_limit=int(row['approved_limit']),
                    current_debt=int(row['current_debt'] or 0),
                )
            )

@shared_task
def ingest_loan_data():
    df = pd.read_excel('/code/loan_data.xlsx')
    with transaction.atomic():
        for _, row in df.iterrows():
            customer = Customer.objects.get(id=int(row['customer_id']))
            Loan.objects.update_or_create(
                id=int(row['loan_id']),
                defaults=dict(
                    customer=customer,
                    loan_amount=float(row['loan_amount']),
                    tenure=int(row['tenure']),
                    interest_rate=float(row['interest_rate']),
                    monthly_repayment=float(row['monthly_repayment']),
                    emis_paid_on_time=int(row['EMIs paid on time']),
                    start_date=datetime.strptime(str(row['start_date']), "%Y-%m-%d").date(),
                    end_date=datetime.strptime(str(row['end_date']), "%Y-%m-%d").date(),
                    active=True
                )
            )
