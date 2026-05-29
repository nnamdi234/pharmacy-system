pharmacy = {
    "Paracetamol": {
        "category":    "Painkiller",
        "price":       150,
        "stock":       100,
        "description": "Relieves mild to moderate pain and fever"
    },
    "Amoxicillin": {
        "category":    "Antibiotic",
        "price":       800,
        "stock":       40,
        "description": "Treats bacterial infections"
    },
    "Vitamin C": {
        "category":    "Supplement",
        "price":       300,
        "stock":       75,
        "description": "Boosts immune system"
    },
    "Ibuprofen": {
        "category":    "Painkiller",
        "price":       200,
        "stock":       60,
        "description": "Reduces inflammation, pain and fever"
    },
    "Metformin": {
        "category":    "Diabetes",
        "price":       500,
        "stock":       30,
        "description": "Controls blood sugar levels"
    },
    "Loratadine": {
        "category":    "Antihistamine",
        "price":       250,
        "stock":       5,
        "description": "Treats allergies and hay fever"
    },
    "Atorvastatin": {
        "category":    "Cholesterol",
        "price":       450,
        "stock":       50,
        "description": "Lowers cholesterol and reduces risk of heart disease"
    },
    "Omeprazole": {
        "category":    "Antacid",
        "price":       350,
        "stock":       80,
        "description": "Treats heartburn, acid reflux, and stomach ulcers"
    },
    "Amlodipine": {
        "category":    "Blood Pressure",
        "price":       300,
        "stock":       90,
        "description": "Treats high blood pressure and chest pain (angina)"
    },
    "Cetirizine": {
        "category":    "Antihistamine",
        "price":       180,
        "stock":       120,
        "description": "Relieves allergy symptoms like runny nose, sneezing, and itchy eyes"
    },
    "Azithromycin": {
        "category":    "Antibiotic",
        "price":       950,
        "stock":       25,
        "description": "Treats a wide variety of bacterial infections"
    }
}



def find_drug(name):
    for drug_name in pharmacy:
        if drug_name.lower() == name.lower():
            return drug_name
    return None

def add_drug():
    print("_______ADD A DRUG_________")

    name = input('Enter the name of the drug: > ')
    category = input('Enter the category of the drug: > ')
    price = input('Enter the price of the drug: > ')
    stock = input('Enter the quantity of drugs to add: > ')
    description = input('Enter the description of the drug: >')

    pharmacy[name] = {"category": category, "price": price, "stock": stock, "description": description}

    print(f"You have successfully added '{name}' to the pharmacy")


def remove_drug():
    print("________REMOVE A DRUG_________")

    name = input('Enter the name of the drug: > ')

    drug_name = find_drug(name)

    if drug_name is None:
        print("This drug is not found")
        return
    
    del pharmacy[drug_name]

    print(f"You have successfully removed '{name}' from the pharmacy")


def search_for_drug():
    print("______SEARCH FOR A DRUG______")

    name = input("Enter the name of the drug: > ")

    drug_name = find_drug(name)

    if drug_name is None:
        print("This drug is not found")
        return
    
    drug = pharmacy[drug_name]

    category = drug["category"]
    price = drug["price"]
    stock = drug["stock"]

    print(f"The drug name: {drug_name}")
    print(f"The drug category: {category}")
    print(f"The drug price: #{price}")
    print(f"Qty in stock: {stock}")



def show_menu():
    print("")
    print(" Pharmacy system ")
    print(" 1. Add / Restock a drug ")
    print(" 2. Search for a drug")
    print(" 3. Dipense drug to customer")
    print(" 4. Restock a drug ")
    print(" 5. Remove a drug ")
    print(" 6. List all drugs ")
    print(" 7. Browse by category ")
    print(" 8. View sales log ")
    print(" 0. Exit ")



def main():
    print("")
    print(" Welcome to the Pharmacy System")
    print("" + str(len(pharmacy)) + " drugs loaded. ")

    show_menu()
    
    choice = input("Select an option from the menu: > ")

    if choice == "1": 
        add_drug()
        print("" + str(len(pharmacy)) + " drugs now in the pharmacy. ")

    if choice == '2':
        search_for_drug()

    if choice == '5':
        remove_drug()
        print("" + str(len(pharmacy)) + " drugs now in the pharmacy. ")


main()