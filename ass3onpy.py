def main():
    #Prompt user to enter bookID,dueDate,returnDate
    bookID = input("Enter bookID:")
    dueDate = int(input("Enter dueDate(as a num):"))
    returnDate = int(input("Enter returnDate(as a num):"))

    # Calculate daysOverdue
    daysOverdue = returnDate - dueDate
 
    #determine fineRate and fineAmount
    if daysOverdue <= 7:
        fineRate = 20 
    elif daysOverdue >=8 and daysOverdue <=14:
        fineRate = 50 
    elif daysOverdue >=15:
        fineRate = 100
    else:
        fineRate = 0

    fineAmount = fineRate * daysOverdue

    # Display results
    print("\n--- Book Details ---")
    print(f"1. Book ID: {bookID}")
    print(f"2. Due Date: {dueDate}")
    print(f"3. Return Date: {returnDate}")
    print(f"4. Days Overdue: {daysOverdue}")
    print(f"5. Fine Rate: Ksh {fineRate} per day")
    print(f"6. Fine Amount: Ksh {fineAmount}") 
   
main()
        
              
        



