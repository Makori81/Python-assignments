def main():
    #Prompt user to enter bookID,dueDate,returnDate
    book_ID = input("Enter book_ID:")
    due_Date = int(input("Enter due_Date(as a num):"))
    return_Date = int(input("Enter return_Date(as a num):"))

    # Calculate daysOverdue
    days_Overdue = return_Date - due_Date
 
    #determine fineRate and fineAmount
    if days_Overdue <= 7:
        fine_Rate = 20 
    elif days_Overdue >=8 and days_Overdue <=14:
        fine_Rate = 50 
    elif days_Overdue >=15:
        fine_Rate = 100
    else:
        fine_Rate = 0

    fine_Amount = fine_Rate * days_Overdue

    # Display results
    print("\n--- Book Details ---")
    print(f"1. Book ID: {book_ID}")
    print(f"2. Due Date: {due_Date}")
    print(f"3. Return Date: {return_Date}")
    print(f"4. Days Overdue: {days_Overdue}")
    print(f"5. Fine Rate: Ksh {fine_Rate} per day")
    print(f"6. Fine Amount: Ksh {fine_Amount}") 
   
main()
        
              
        



