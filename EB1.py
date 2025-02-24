def calculate_electricity_bill():
    # Prompt the user to enter CustomerID, CustomerName, and UnitConsumed
    customer_id = input("Enter Customer ID: ")
    customer_name = input("Enter Customer Name: ")
    units_consumed = float(input("Enter Units Consumed: "))

    # Calculate charges based on units consumed
    if units_consumed <= 199:
        charge_per_unit = 1.20
    elif 200 <= units_consumed < 400:
        charge_per_unit = 1.50
    elif 400 <= units_consumed < 600:
        charge_per_unit = 1.80
    else:
        charge_per_unit = 2.00

    # Calculate total bill before surcharge
    total_bill = units_consumed * charge_per_unit

    # Apply surcharge if the bill exceeds Ksh 400
    if total_bill > 400:
        surcharge = total_bill * 0.15
        total_bill += surcharge

    # Ensure minimum bill is Ksh 100
    if total_bill < 100:
        total_bill = 100

    # Display output
    print("\nElectricity Bill Details:")
    print(f"Customer ID: {customer_id}")
    print(f"Customer Name: {customer_name}")
    print(f"Units Consumed: {units_consumed}")
    print(f"Charges per Unit: Ksh {charge_per_unit:.2f}")
    print(f"Total Amount to Pay: Ksh {total_bill:.2f}")

# Run function
calculate_electricity_bill()
