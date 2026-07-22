from datetime import datetime
print("================================")
print("      EXPENSE TRACKER")
print("================================")

print("1. Add Expense")
print("2. View Expenses")
print("3. Calculate total Expense")
print("4. Delete Expense")
print("5. Update Expense")
print("6. Expense Summary")
print("7. Search Expense")
choice = input("Enter your choice: ")

if choice == "1":
    name = input("Enter expense name: ")
    amount = float(input("Enter amount: ₹"))
    category = input("Enter category: ")
    date = datetime.now().strftime("%d-%m-%Y")
    file = open("expenses.txt", "a")
    file.write(f"{name},{amount},{category},{date}\n")
    file.close()

    print("\n✅ Expense Saved Successfully!")

elif choice == "2":
    file = open("expenses.txt", "r")

    print("\n----- Expenses -----")

    for expense in file:
        data = expense.strip().split(",")

        if len(data) == 4:
            print("Expense :", data[0])
            print("Amount  : ₹", data[1])
            print("Category:", data[2])
            print("Date :",data[3])
       

        print("-----------------------")

    file.close()

elif choice == "3":
    file = open("expenses.txt", "r")

    total = 0

    for expense in file:
        data = expense.strip().split(",")
        total = total + float(data[1])

    file.close()

    print("Total Expense: ₹", total)

elif choice == "4":
    delete_name = input("Enter expense name to delete: ")

    file = open("expenses.txt", "r")
    expenses = file.readlines()
    file.close()

    file = open("expenses.txt", "w")

    for expense in expenses:
        if not expense.startswith(delete_name + ","):
            file.write(expense)

    file.close()

    print("✅ Expense deleted successfully!")

elif choice == "5":
    update_name = input("Enter expense name to update: ")

    file = open("expenses.txt", "r")
    expenses = file.readlines()
    file.close()

    file = open("expenses.txt", "w")

    for expense in expenses:
      data = expense.strip().split(",")

      if data[0] == update_name:
        new_amount = float(input("Enter new amount: ₹"))
        new_category = input("Enter new category: ")

        file.write(f"{update_name},{new_amount},{new_category}\n")

      else:
        file.write(expense)

    file.close()

    print("✅ Expense updated successfully!")

elif choice =="6":
    file = open("expenses.txt","r")
    expenses = file.readlines()
    file.close()

    summary = {}
    for expense in expenses:
      data = expense.strip().split(",")

      category = data[2]
      amount = float(data[1])

      if category in summary:
        summary[category] += amount
      else:
        summary[category] = amount

    print("\n----- Expense Summary -----")

    for category, total in summary.items():
       print(f"{category}: ₹{total}")

elif choice == "7":
    search_name=input("Enter expense name to search:")
    file=open("expenses.txt","r")
    expenses=file.readlines()
    file.close()

    found = False

    for expense in expenses:
       data = expense.strip().split(",")

       if data[0].lower() == search_name.lower():
        print("\nExpense Found!")
        print("Expense :", data[0])
        print("Amount  : ₹", data[1])
        print("Category:", data[2])
        print("Date    :", data[3])

        found = True

    if found==False:
        print("Expense not found!")


else:
    print("Invalid Choice!")