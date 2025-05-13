#Expense Tracker
ex=[]
v=[]
t=[]
def main():
    print("\n========== Expense Tracker ==========")
    print("1. Add Money Received")
    print("2. Record Money Spent")
    print("3. View Total Monthly Expense")
    print("4. View Budget")
    print("5. Set Monthly Expense Limit")
    print("6. Exit")
    print("=====================================")
    n=input("Enter your choice(1-6):")
    if n=="1":
        add()
    elif n=="2":
        spent()
    elif n=="3":
        total()
    elif n=="4":
        view()
    elif n=="5":
        set_m()
    else:
        exit_a()

def add():
    while True:
        r=input("Enter the money you recieved:₹")
        s=input("Enter the source of income:")
        income={"amount":float(r), "source":s}
        ex.append(income)
        p=input("Did you recieve money from any other source?(yes/no):").lower()
        if(p=="yes"):
            continue
        else:
            break

def spent():
    while True:
        g=input("Enter the money you spent:₹")
        y=input("Enter the category in which you have spent the money:")
        spend={"amount":float(g),"category":y}
        v.append(spend)
        c=input("Did you spent money in any other?(yes/no):").lower()
        if(c=="yes"):
            continue
        else:
            break

def total():
    while True:
        print("Enter the category(shopping/food/travel/medical/entertainment..etc / exit and amount")
        a=input("Enter the category or exit:").lower()
        if(a=="exit"):
            break
        am=input("Enter amount: ₹")
        try:
            amoun=float(am)
            r={"category":a, "amount":amoun}
        except ValueError:
            print("Invalid")
            continue
        t.append(r)
        total=sum(item["amount"] for item in t)
        print("Total Expense is:",total)

def view():
    print("View Budget")
    if v:
        print("\n Your expense")
        for i in v:
            print(f"-{i['category']}: ₹{i['amount']}")
    else:
        print("No expense data is found")
    if ex:
        total=sum(i['amount'] for i in ex)
        print("Your income")
        for i in ex:
            print(f"-{i['source']} : ₹{i['amount']}")
        print(f"Total Income: ₹{total}")
    else:
        print("No income data found")

def set_m():
    print("Set your monthly budget")
    budget=float(input("Enter your monthly budget:"))
    total=0
    while True:
        amount=input("Enter your expense amount from 0, and stop:")
        if(amount=="0" or amount=="stop"):
            break
        try:
            total=total+float(amount)
            s=budget-total
            print("Remaining budget:",s)
        except ValueError:
            print("Invalid")
            continue
    if (total>budget):
        print("Your limit has exceeded")
    else:
        print("You stayed within your limit this month")

def exit_a():
    print("Your exepense has stored successfully")
    exit()

while True:
    main()
    
        
        
            

            
            
            
        
        
