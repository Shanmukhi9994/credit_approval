from rest_framework import serializers
from .models import Customer, Loan

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = [ 'customer_id','first_name', 'last_name', 'age', 'phone_number', 'monthly_income', 'approved_limit', 'current_debt']

    def create(self, validated_data):
        monthly_income = validated_data.get('monthly_income')
        approved_limit = round(36 * monthly_income / 100000) * 100000
        validated_data['approved_limit'] = approved_limit
        return super().create(validated_data)

class LoanSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer(read_only=True)  # Nested representation of the customer

    class Meta:
        model = Loan
        fields = ['id', 'customer', 'loan_amount', 'tenure', 'interest_rate', 'monthly_repayment', 'emis_paid_on_time', 'start_date', 'end_date', 'active']

class CreateCustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['first_name', 'last_name', 'age', 'phone_number', 'monthly_income']

class CreateLoanSerializer(serializers.ModelSerializer):
    customer_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Loan
        fields = ['customer_id', 'loan_amount', 'interest_rate', 'tenure']

    def create(self, validated_data):
        customer_id = validated_data.pop('customer_id')
        customer = Customer.objects.get(id=customer_id)
        return Loan.objects.create(customer=customer, **validated_data)
