from datetime import datetime


class Drug:
    def __init__(self, name, price, amount, expire_date):
        self.name = name
        self.price = price
        self.amount = amount
        self.expire_date = expire_date

    def is_expired(self):
        expire_date_obj = datetime.strptime(self.expire_date, '%Y-%m-%d')
        return datetime.now() > expire_date_obj

class Pharmacy:
    def __init__(self):
        self.drugs = {}

    def add_drug(self, name, price, amount, expired_date):
        self.drugs[name] = Drug(name, price, amount, expired_date)
        print(f"{name} drug added to the pharmacy")

    def delete_drug(self, name):
        if name in self.drugs:
            del self.drugs[name]
            print(f"{name} deleted")

    def control_drugs(self, name, new_amount):
        if name in self.drugs:
            self.drugs[name].amount = new_amount
            print(f'{name} has been restored')
        else:
            print(f"{name} not found")

    def delete_expired_drugs(self):
        expired_drugs = list(filter(lambda name: self.drugs[name].is_expired(), self.drugs))
        if expired_drugs:
            for drug in expired_drugs:
                self.delete_drug(drug)
                print(f"{drug} deleted because of expired\n")

        else:
            print('No expired drugs found')

    def display_all_drugs(self):
        for drug in self.drugs.values():
            print(f"Drug: {drug.name}, Price: {drug.price}, Amount: {drug.amount}, Expiry Date: {drug.expire_date}")


pharmacy1 = Pharmacy()

while True:
    print('1. Add drugs')
    print('2. Delete drugs')
    print('3. Add new amount to the drugs')
    print('4. Delete expired drugs')
    print('5. Show all drugs')
    print('6. Exit')

    choice = input('Enter your choice: ')

    if choice == '1':
        name = input('Enter the name: ')
        price = input('Enter the price: ')
        amount = input('Enter the amount: ')
        expire_date = input('Enter expired date: ')

        pharmacy1.add_drug(name, price, amount, expire_date)

    elif choice == '2':
        deleted_name = input('Enter the name: ')
        pharmacy1.delete_drug(deleted_name)

    elif choice == '3':
        new_name = input('Enter the drug name: ')
        new_amount = input('Enter the amount of it: ')

        pharmacy1.control_drugs(new_name, new_amount)

    elif choice == '4':
        pharmacy1.delete_expired_drugs()

    elif choice == '5':
        pharmacy1.display_all_drugs()

    elif choice == '6':
        break