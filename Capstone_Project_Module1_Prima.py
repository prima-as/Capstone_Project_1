# The case study of this Capstone is about Car Rental
# This program is intended for Car Rental Business Owner to help them easily monitor their vehicle inventory.
# The program consist of 7 main manu which are : [1. List of Vehicle, 2. New Vehicle Entry, 3. Change Vehicle List, 4. Remove Vehicle List, 5. Car Rental Form, 6. Rental Revenue Report, 7. Exit]
# The list consist of 8 information colum, which are = [1. Car ID (Key/Unique), 2. Plate Number, 2. Brand, 3. Model, 4. Transmission, 5. Type, 6. Year of Manufacture, 7. Rental Price/Day, 8. Status]

# Make a global variabel
main_menu_list = ('1. List of Vehicle', '2. New Vehicle Entry', '3. Change Vehicle List', '4. Remove Vehicle List', '5. Customer Information', '6. Rental Revenue Report', '7. Exit')
vehicle_list_menu = ('1. All Vehicle List', '2. Select Specific Vehicle', '3. Return To Main Menu')
new_vehicle_entry_menu = ('1. Add New Car', '2. Return to Main Menu')
change_vehicle_list_menu = ('1. Change the Vehicle Data', '2. Return to Main Menu')
Remove_vehicle_list_menu = ('1. Remove Vehicle Data', '2. Return to Main Menu')
car_rental_form_menu = ('1. Rental Car Form', '2. Return Car Form', '3. Customer List', '4. Return to Main Menu')
car_list_header = ['Plate Number (Primary Key)', 'Brand', 'Model', 'Transmission', 'Type', 'Year Of Manufacture', 'Rental Price/Day', 'Status']
fleet_list = [['B1234WFA','Toyota','Avanza','Manual','MPV','2021',300_000,'Rented'],['F2345DAS','Honda','Brio','Automatic','City Car','2023',350_000,'Maintenance'],['P7890GA','Toyota','Innova','Hybrid','MPV','2023',600_000,'Rented'],['F6578RA','Suzuki','Fronx','Automatic','SUV','2025',500_000,'Rented'],['B534LL','BYD','Seal','EV','Sedan','2022',700_000,'Available']]
customer_header = ('Plate Number', 'Name', 'Phone Number', 'Total Rental Days', 'Payment', 'Status')
list_of_customer = [['P7890GA', 'Ade', '085256749082', 3, 600_000, 'Renting'],['B1234WFA', 'Sukrono', '082354679877', 2, 300_000, 'Returned'],['B1234WFA', 'Arzan', '085278965426', 4, 300_000, 'Renting'],['F6578RA', 'Puspita', '087792337824', 1, 500_000, 'Renting']]
header_for_print = f'{car_list_header[0]:^30}|{car_list_header[1]:^10}|{car_list_header[2]:^8}|{car_list_header[3]:^13}|{car_list_header[4]:^10}|{car_list_header[5]:^20}|{car_list_header[6]:^17}|{car_list_header[7]:^12}'
line_for_header = f'{'-'*30}+{'-'*10}+{'-'*8}+{'-'*13}+{'-'*10}+{'-'*20}+{'-'*17}+{'-'*12}'

# ====== Make a function ======
# Main menu fuction
def main_menu():
    for menu in main_menu_list:
        print(menu)
    print()

def list_of_sub_menu(item_in_main_menu): 
    for item in item_in_main_menu:
        print(item)

# List of Vehicle menu function
def list_of_all_fleet():
    print('\nAll Vehicle List: ')
    print(header_for_print)
    print(line_for_header)
    for i in range(len(fleet_list)):
        print(f'{fleet_list[i][0]:^30}|{fleet_list[i][1]:^10}|{fleet_list[i][2]:^8}|{fleet_list[i][3]:^13}|{fleet_list[i][4]:^10}|{fleet_list[i][5]:^20}|{fleet_list[i][6]:^17}|{fleet_list[i][7]:^12}')

def category_list(input_filter_category): 
    filter_category_list = set()
    filtered_list = ''
    if int(input_filter_category)-1 in range(len(car_list_header)):
        for i in range(len(fleet_list)):
            filter_category_list.add(fleet_list[i][int(input_filter_category)-1])
        filtered_category = list(filter_category_list)
        for i in range(len(filtered_category)):
            filtered_list += (f'{i+1}. {filtered_category[i]}\n')
    else:
        print('\n')
    return filtered_list, list(filter_category_list)

def filter_fleet_list(input_filter_item, input_filter_category):
    filtered_fleet_in_list = []
    filtered_fleet_print = ''
    for j in range(len(fleet_list)):
        if input_filter_item == fleet_list[j][int(input_filter_category)-1]:
            filtered_fleet_print += (f'{fleet_list[j][0]:^30}|{fleet_list[j][1]:^10}|{fleet_list[j][2]:^8}|{fleet_list[j][3]:^13}|{fleet_list[j][4]:^10}|{fleet_list[j][5]:^20}|{fleet_list[j][6]:^17}|{fleet_list[j][7]:^12}\n')
            filtered_fleet_in_list.append(fleet_list[j][int(input_filter_category)-1])
    return filtered_fleet_print, filtered_fleet_in_list

def filter_by_category(): 
    while True:
        print('\nList of Category: ')
        for i in range(len(car_list_header)):
            print(i+1, car_list_header[i])
        print()
        while True:
            input_filter_category = input('Which category would you like to filter from items above? (1-8) ')
            number = []
            for i in range(len(car_list_header)):
                number.append(str(i+1))
            if input_filter_category in number and '1' <= input_filter_category <= str(len(car_list_header)) and not input_filter_category == '':
                break
            else:
                print('\n***** Your input is invalid *****\n')
                continue
        category_for_print, category_in_list = category_list(input_filter_category)
        print('\nList of filter Category:')
        print(category_for_print)
        while True:
            item_to_input = input('Choose the item to filter from the list above: (in number) ')
            number1 = []
            for i in range(len(category_in_list)):
                number1.append(str(i+1))
            if item_to_input in number and '1' <= item_to_input <= str(len(category_in_list)) and not item_to_input == '':
                break
            else:
                print('\n***** Your input is invalid *****\n')
                continue
        category_item_list = category_in_list[int(item_to_input)-1]
        filtered_vehicle = filter_fleet_list(category_item_list, input_filter_category)
        print('\nList of vehicle:')
        print(header_for_print)
        print(line_for_header)
        print(filtered_vehicle[0])
        break

def fleet_filtered_by_odd_even(filter_item):
    odd_even = []
    for i in range(len(fleet_list)):
        plate_number = ''
        for j in fleet_list[i][0]:
            if '0' <= j <= '9':
                plate_number += j        
        odd_even.append(int(plate_number[-1]))
    if filter_item == 'odd':
        print(header_for_print)
        print('-'*124)
        for i in range(len(odd_even)):
            if odd_even[i] % 2 != 0:
                print(f'{fleet_list[i][0]:^30}|{fleet_list[i][1]:^10}|{fleet_list[i][2]:^8}|{fleet_list[i][3]:^13}|{fleet_list[i][4]:^10}|{fleet_list[i][5]:^20}|{fleet_list[i][6]:^17}|{fleet_list[i][7]:^12}')
    elif filter_item == 'even':
        print(header_for_print)
        print('-'*124)
        for i in range(len(odd_even)):
            if odd_even[i] % 2 == 0:
                print(f'{fleet_list[i][0]:^30}|{fleet_list[i][1]:^10}|{fleet_list[i][2]:^8}|{fleet_list[i][3]:^13}|{fleet_list[i][4]:^10}|{fleet_list[i][5]:^20}|{fleet_list[i][6]:^17}|{fleet_list[i][7]:^12}')
    else:
        print('***** Your input is invalid *****')

def list_of_filtered_fleet():
    while True:
        print('\n~~~~~~ Select Specific vehicle ~~~~~~\n')
        print('1. Filter by Category\n2. Filter by Odd or Even Plate Number\n3. Return to List Vehicle Menu\n')
        filter_vehicle_item = input('Choose the filter item: (1-3) ')
        if filter_vehicle_item == '1':
            filter_by_category()
        elif filter_vehicle_item == '2':
            print()
            odd_even = input('Input with odd or even: (odd/even) ').lower()
            print()
            fleet_filtered_by_odd_even(odd_even)
            print()
        elif filter_vehicle_item == '3':
            break
        else:
            print('\n***** The selected menu option does not exist *****\n')
            continue
        while True:
            question = input('Would you like to continue filtering? (yes/no) ')
            if question == 'yes':
                list_of_filtered_fleet()
            elif question == 'no':
                break
            else:
                print('\n***** Your input is invalid *****\n')
                continue
        break

# New Vehicle Entry menu function
def digit_check(value):
    number = ('0123456789')
    num_check = set()
    for i in value:
        if not i in number:
            num_check.add('wrong')
        else:
            num_check.add('correct')
    if 'wrong' in num_check or num_check == set():
        print('\n***** Your input is invalid *****\n')
    else:
        return value

def plate_number_check(input_plate_number):
    for i in fleet_list:
        if i[0] == input_plate_number:
            return i[0]

def add_vehicle(plate_number):            
    while True:
        question = input('\nDo you want to continue add the car? (yes/no) ').lower()
        if question == 'yes':
            print()
            input_plate_number = plate_number
            input_car_brand = input('Enter the Car Brand: (Toyota/Honda/...) ').title()
            input_car_model = input('Enter the Car Model: (Avanza/Brio/...) ').title()
            input_car_transmission = input('Enter the Car Transmission type: (Manual/Automatic/EV/Hybrid) ').capitalize()                
            input_car_type = input('Enter the Car Type: (MPV/SUV/City Car/...) ').title()
            input_year_of_manufacture = input('Enter the Year of Manufacture: (2024/2025/...) ')
            while True:
                input_rental_price_perday = input('Enter the Car Rental Price/Day: (300000/...) ')
                if digit_check(input_rental_price_perday) == input_rental_price_perday:
                    break
            while True:
                input_status = input('Enter the Status of the car: (Available/Rented/Maintenance) ').capitalize()
                if not input_status in ['Available', 'Rented', 'Maintenance'] or input_status == '':
                    print('\n***** Your input is invalid *****\n')
                    continue
                break
            print()
            print(header_for_print)
            print(line_for_header)
            print(f'{input_plate_number:^30}|{input_car_brand:^10}|{input_car_model:^8}|{input_car_transmission:^13}|{input_car_type:^10}|{input_year_of_manufacture:^20}|{input_rental_price_perday:^17}|{input_status:^12}\n')
            while True:
                save = input('Do you want to save the data? (yes/no) ').lower()
                if save == 'yes':
                    fleet_list.append([input_plate_number, input_car_brand, input_car_model, input_car_transmission, input_car_type, input_year_of_manufacture, input_rental_price_perday, input_status])
                    print('\n***** Your new car data has been inserted *****')
                    list_of_all_fleet()
                    break
                elif save == 'no':
                    print('\n***** Your data is not saved *****\n')
                    break            
                else:
                    print('\n***** Your input is invalid *****\n')
                    continue
        elif question == 'no':
            print('\n***** Cancelled adding the Car *****')
            break
        else:
            print('\n***** Your input is invalid *****')
            continue
        break
    return fleet_list

def new_vehicle():
    while True:
        input_plate_number = input('Enter the plate number to check the fleet: ').upper()
        if plate_number_check(input_plate_number) == input_plate_number:
            print(f'\n***** The Car with plate number "{input_plate_number}" is in the Garage *****')
            break
        else:
            print(f'\n***** The Car with plate number "{input_plate_number}" is "NOT" in the Garage *****')
            add_vehicle(input_plate_number)
        break

# Change Vehicle List Function
def plate_number_index(input_plate_number):
    input_index_filter = 0
    for i in range(len(fleet_list)):
        if input_plate_number == fleet_list[i][0]:
            input_index_filter = fleet_list[i].index(input_plate_number)
    return input_index_filter

def update_item(category, plate_number, update_value):
    index_header = car_list_header.index(category)
    for j in range(len(fleet_list)):
        if car_list_header[index_header] == 'Rental Price/Day' and plate_number == fleet_list[j][0]:
            fleet_list[j][car_list_header.index(category)] = int(update_value)
            break
        elif car_list_header[index_header] == category and plate_number == fleet_list[j][0]:
            fleet_list[j][car_list_header.index(category)] = update_value
            break
    fleet_list_update = fleet_list
    return fleet_list_update

def updated_vehicle():
    while True:
        input_plate_number1 = input('Enter the plate number to check the fleet: ').upper()
        print()
        index_plate_number = plate_number_index(input_plate_number1)
        if plate_number_check(input_plate_number1) == input_plate_number1:
            print(header_for_print)
            print(line_for_header) 
            print(filter_fleet_list(input_plate_number1, index_plate_number + 1)[0])
            while True:
                input_update_vehicle = input('Do you want to continue update? (yes/no) ').lower()
                if input_update_vehicle == 'yes':
                    print()
                    while True:
                        input_category = input('Enter the name of Category you want to update: (plate number/brand/model/...) ').title()
                        if not input_category in car_list_header:
                            print(f'\n***** "{input_category.upper()}" is not in the category *****\n')
                            continue
                        print()
                        break
                    while True:
                        input_update_value = input('Enter the new value you want: ').title()
                        if input_category == 'Rental Price/Day':
                            check_digit = digit_check(input_update_value)
                            if check_digit == input_update_value:
                                print()
                                break
                        else:
                            continue
                    while True:
                        input_save_question = input('Do you want to save the changes? (yes/no) ').lower()
                        if input_save_question == 'yes':
                            update_item(input_category, input_plate_number1, input_update_value)
                            list_of_all_fleet()
                            print('\n***** The Data has been successfully updated *****\n')
                            break
                        elif input_save_question == 'no':
                            print('\n***** The update was cancelled *****\n')
                            break
                        else:
                            print('\n***** Your input is invalid *****\n')
                            continue
                elif input_update_vehicle == 'no':
                    print('\n***** Cancelled updating data *****')
                    break
                else:
                    print('\n***** Your input is invalid *****\n')
                    continue
            break
        else:
            print(f'***** The car with plate number "{input_plate_number1}" is "NOT" in the garage *****')
            break

# Remove Vehicle List Function
def remove_vehicle_from_list(input_plate_number):
    for i in range(len(fleet_list)):
        if input_plate_number == fleet_list[i][0]:
            del fleet_list[i]
            break
    return fleet_list

def remove_vehicle():
    while True:
        input_plate_number2 = input('Enter the plate number to check the fleet: ').upper()
        print()
        plate_number_index2 = plate_number_index(input_plate_number2)
        if plate_number_check(input_plate_number2) == input_plate_number2:
            print(header_for_print)
            print(line_for_header)
            print(filter_fleet_list(input_plate_number2, plate_number_index2 + 1)[0])
            while True:
                input_remove_vehicle = input('Do you want to remove the data? (yes/no) ').lower()
                if input_remove_vehicle == 'yes':
                    print()
                    remove_vehicle_from_list(input_plate_number2)
                    print('***** The Data has been successfully removed *****')
                    list_of_all_fleet()
                    break
                elif input_remove_vehicle == 'no':
                    print('\n***** The remove data was cancelled *****')
                    break
                else:
                    print('\n***** Your input is invalid *****\n')
                    continue
            break
        else:
            print(f'***** The Car with plate number {input_plate_number2} is "NOT" in the garage *****')
            break

# Customer Information Function
def rental_form_check(input_plate_number): 
    for i in range(len(fleet_list)):
        if fleet_list[i][0] == input_plate_number and fleet_list[i][7] == 'Available':
            return 'Available'
        elif fleet_list[i][0] == input_plate_number and fleet_list[i][7] == 'Rented':
            return 'Rented'
        elif fleet_list[i][0] == input_plate_number and fleet_list[i][7] == 'Maintenance':
            return 'Maintenance'

def add_new_customer(input_plate_number):
    input_name = input('Enter the Customer Name: ').title()
    input_phone = input('Enter the Phone Number: ')
    while True:
        input_rental_days = input('Enter the total days of renting: (in number) ')
        if digit_check(input_rental_days) == input_rental_days:
            break
    while True:
        input_payment = input('Enter the Payment amount: ')
        if digit_check(input_payment) == input_payment:
            break
    rental_status = 'Renting'
    update_status = ''
    print(f'\n{customer_header[0]:^15}|{customer_header[1]:^15}|{customer_header[2]:^14}|{customer_header[3]:^20}|{customer_header[4]:^10}|{customer_header[5]:^10}')
    print(f'{'-'*15}+{'-'*15}+{'-'*14}+{'-'*20}+{'-'*10}+{'-'*10}')
    print(f'{input_plate_number:^15}|{input_name:^15}|{input_phone:^14}|{int(input_rental_days):^20}|{int(input_payment):^10,}|{rental_status:^10}\n')
    while True:
        question_rental_form = input('Do you want to save the data? (yes/no) ').lower()
        if question_rental_form == 'yes':
            list_of_customer.append([input_plate_number, input_name, input_phone, int(input_rental_days), int(input_payment), rental_status])
            category_to_update = 'Status'
            update_value = 'Rented'
            update_status = update_item(category_to_update, input_plate_number, update_value)
            print('\n***** The Customer data has been successfully updated *****')        
        elif question_rental_form == 'no':
            print('\n***** Cancel updating the data *****')
            break
        else: 
            print('\n***** Your input is invalid *****\n')
            continue
        break
    return update_status

def car_rental_form():
    input_plate_number3 = input('Enter the plate number to check the fleet: ').upper()
    check_form = rental_form_check(input_plate_number3)
    if check_form == 'Available':
        print('\n***** The Car is Available *****\n')
        update_rental_status = add_new_customer(input_plate_number3)
        return update_rental_status
    elif check_form == 'Rented':
        print(f'\n***** The Car with plate number "{input_plate_number3}" is being rented *****\n')
    elif check_form == 'Maintenance':
        print(f'\n***** The Car with plate number "{input_plate_number3}" is under maintenance')
    else:
        print(f'\n***** The Car with plate number "{input_plate_number3}" is not in the garage *****')

def car_return_status(input_plate_number):
    while True:
        question_for_car_return = input('Is the customer returned the car? (yes/no) ').lower()
        if question_for_car_return == 'yes':
            for i in range(len(list_of_customer)):
                if list_of_customer[i][0] == input_plate_number:
                    list_of_customer[i][5] = 'Returned'
            for j in range(len(fleet_list)):                                       
                if input_plate_number == fleet_list[j][0] and fleet_list[j][7] == 'Rented':
                    fleet_list[j][7] = 'Available'
            print('\n***** The data has been successfully updated *****')
            break
        elif question_for_car_return == 'no':
            print('\n***** Updating data is cancelled *****')
            break
        else:
            print('\n***** Your input is invalid *****\n')
            continue

def customer_valid_check():
    while True:
        check_customer_input = input('Is costumer data above valid? (yes/no/cancel) ').lower()
        if check_customer_input == 'yes':
            return 'yes'
        elif check_customer_input == 'no':
            return 'no'
        elif check_customer_input == 'cancel':
            return 'cancel'
        else:
            print('\n***** Your input is invalid *****\n')
            continue

def car_return_form():
    while True:
        input_plate_number4 = input('Enter the plate number to check the customer: ').upper()
        for i in list_of_customer:
            if input_plate_number4 == i[0] and i[5] == 'Renting':
                print(f'\n{customer_header[0]:^15}|{customer_header[1]:^15}|{customer_header[2]:^14}|{customer_header[3]:^20}|{customer_header[4]:^10}|{customer_header[5]:^10}')
                print(f'{'-'*15}+{'-'*15}+{'-'*14}+{'-'*20}+{'-'*10}+{'-'*10}')
                print(f'{i[0]:^15}|{i[1]:^15}|{i[2]:^14}|{i[3]:^20,}|{i[4]:^10,}|{i[5]:^10}')
                break        
        else:
            print(f'\n***** No Car with plate number "{input_plate_number4}" in being Rented *****\n')
            continue
        print()
        customer_check = customer_valid_check()
        if customer_check == 'yes':
            car_return_status(input_plate_number4)
            break
        elif customer_check == 'no':
            print('\n***** Please re-input the plate number *****\n')
            continue
        elif customer_check == 'cancel':
            print('\n***** Updating data is cancelled *****')
            break
        else:
            print('\n***** Your input is invalid *****\n')
            continue

def customer_list(category, value):
    print(f'\n{customer_header[0]:^15}|{customer_header[1]:^15}|{customer_header[2]:^14}|{customer_header[3]:^20}|{customer_header[4]:^10}|{customer_header[5]:^10}')
    print(f'{'-'*15}+{'-'*15}+{'-'*14}+{'-'*20}+{'-'*10}+{'-'*10}')
    if value == 'all':
        for i in range(len(list_of_customer)):    
            print(f'{list_of_customer[i][0]:^15}|{list_of_customer[i][1]:^15}|{list_of_customer[i][2]:^14}|{list_of_customer[i][3]:^20}|{list_of_customer[i][4]:^10,}|{list_of_customer[i][5]:^10}')
    elif category in customer_header:
        index_of_category = customer_header.index(category)
        for i in list_of_customer:
            if str(value) == str(i[index_of_category]).lower():
                print(f'{i[0]:^15}|{i[1]:^15}|{i[2]:^14}|{i[3]:^20,}|{i[4]:^10,}|{i[5]:^10}')
    else:
        print(f'\n***** No Customer with {category} {value} in the list *****\n')
        
def customer_list_filter():
    while True:
        print('\n~~~~~~   Customer List   ~~~~~~\n')
        print('1. All Customer\n2. Filter Customer\n3. Return to Customer Information\n')
        customer_menu = input('Select customer list option menu: (1-3) ')
        if customer_menu == '1':
            print()
            customer_list('','all')
            break
        elif customer_menu == '2':
            print()
            for i in customer_header:
                print(i)
            print()
            while True:
                input_category_customer = input('Enter name of category you want to filter from the list above: ').title()
                if not input_category_customer in customer_header:
                    print('\n***** Your input is invalid *****\n')
                    continue
                break
            while True:
                input_the_value = input(f'Enter the value you want from {input_category_customer}: ').lower()
                index_header_customer = customer_header.index(input_category_customer)
                for i in list_of_customer:
                    if input_the_value == str(i[index_header_customer]).lower():
                        break
                else:
                    print(f'\n***** The is no {input_category_customer} like {input_the_value} in customer list *****\n')
                    continue
                break
            customer_list(input_category_customer, input_the_value)
            break
        elif customer_menu == '3':
            break
        else:
            print('\n***** The selected menu option does not exist *****')
            continue

# ====== Make a program ======
# 1. Main Menu Program (printing and looping)
while True: # Printing and looping main menu
    print('======\t Irsyadi Car Rental \t======\n') 
    print('Main Menu:')
    main_menu()
    input_main_menu = input('Select a Main Menu option [1-7]: ')

# 2. List Of Vehicle menu program
    if input_main_menu == '1':
        while True:
            print('\n~~~~~~   List of Vehicle   ~~~~~~\n')
            list_of_sub_menu(vehicle_list_menu)
            print()
            input_vehicle = input('Select a List of Vehicle option [1-3]: ')
            if input_vehicle == '1':
                list_of_all_fleet()
            elif input_vehicle == '2':
                list_of_filtered_fleet()
            elif input_vehicle == '3':
                print()
                break
            else:
                print('\n***** The selected menu option does not exist *****\n')
    
# 3. New Vehicle Entry
    elif input_main_menu == '2':
        while True:
            print('\n~~~~~~  New Vehicle Entry  ~~~~~~\n')
            list_of_sub_menu(new_vehicle_entry_menu)
            print()
            input_vehicle_entry_menu = input('Select the New Vehicle Entry Menu Option: (1-2) ')
            print()
            if input_vehicle_entry_menu == '1':
                new_vehicle()
            elif input_vehicle_entry_menu == '2':
                print()
                break
            else:
                print('\n***** The selected menu option does not exist *****\n')

# 4. Change Vehicle List
    elif input_main_menu == '3':
        while True:
            print('\n~~~~~~  Change Vehicle List  ~~~~~~\n')
            list_of_sub_menu(change_vehicle_list_menu)
            print()
            input_change_vehicle_menu = input('Select the Change Vehicle List Option: (1-2) ')         
            print()
            if input_change_vehicle_menu == '1':
                updated_vehicle()
            elif input_change_vehicle_menu == '2':
                break
            else:
                print('***** The selected menu option does not exist *****')

# 5. Remove Vehicle List
    elif input_main_menu == '4':
        while True:
            print('\n~~~~~~  Remove Vehicle List  ~~~~~~\n')
            list_of_sub_menu(Remove_vehicle_list_menu)
            print()
            input_remove_vehicle_menu = input('Select the Remove Vehicle List Option: (1-2) ')
            print()        
            if input_remove_vehicle_menu == '1':
                remove_vehicle()
            elif input_remove_vehicle_menu == '2':
                break
            else:
                print('***** The selected menu option does not exist *****')

# 6. Car Rental Form
    elif input_main_menu == '5':
        while True:
            print('\n~~~~~~   Customer Information   ~~~~~~\n')
            list_of_sub_menu(car_rental_form_menu)
            print()
            input_car_rental_option = input('Select a Car Rental Form option [1-4]: ')
            if input_car_rental_option == '1':
                print('\nRental Form:')
                car_rental_form()
            elif input_car_rental_option == '2':
                print('\nReturn Form:')
                car_return_form()
            elif input_car_rental_option == '3':   
                customer_list_filter()
            elif input_car_rental_option == '4':  
                print() 
                break
            else:
                print('\n***** The selected menu option does not exist *****')  
                continue

# 7. Rental Revenue Report
    elif input_main_menu == '6':
        while True:
            password = 'Prima'
            input_password = input('Input the password to open the menu: ')
            if input_password == password:
                break
            else:
                print('\n***** The password is incorrect *****\n')
                continue
        print('\n~~~~~~   Rental Revenue Report   ~~~~~~\n')
        print(f'{'Rental_ID':^10} | {'Plate_Number':^15} | {'Customer_Name':^15} | {'Rental Days':^12} | {'Total_Revenue':^15} |')
        print(f'{'-'*10} + {'-'*15} + {'-'*15} + {'-'*12} + {'-'*15} +')
        revenue = []
        for i in list_of_customer:
            print(f'{list_of_customer.index(i)+1:^10} | {i[0]:^15} | {i[1]:^15} | {i[3]:^12} | {i[3]*i[4]:^15,} |')
            revenue.append(i[3]*i[4])
        print(f'{'-'*10} + {'-'*15} + {'-'*15} + {'-'*12} + {'-'*15} +')
        print(f'{'Summary':^10} | {'-':^15} | {'-':^15} | {'-':^12} | {sum(revenue):^15,} |\n')

# 8. Exit
    elif input_main_menu == '7':
        print('\n***** You are exit from the program *****\n')
        break
    else:
        print('\n***** The selected menu option does not exist *****\n')