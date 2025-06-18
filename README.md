# Car Rental Program by Python
This is a Python-based application developed to support car rental business operations. 
The system allows the business owner to manage the entire vehicle inventory and customer transactions efficiently through an interactive menu.

## Features

The program is divided into **7 main menu sections**:

1. **List of Vehicle**  
   View all vehicles or filter them by category or plate number (odd/even).
   
2. **New Vehicle Entry**  
   Add a new vehicle to the fleet, with input validation and duplication check.

3. **Change Vehicle List**  
   Modify details of an existing vehicle based on its plate number.

4. **Remove Vehicle List**  
   Delete a vehicle entry from the fleet using the plate number.

5. **Customer Information**  
   - **Rental Form**: Register a new rental transaction.  
   - **Return Form**: Mark vehicle and customer status upon return.  
   - **Customer List**: Display or filter customer records by category.

6. **Rental Revenue Report**  
   View summarized income report by customer rental history.

7. **Exit**  
   Close the program.

---

## 🧾 Data Structure

### Fleet List (Vehicle Inventory)

Each vehicle is recorded with the following attributes:

- Plate Number *(Primary Key)*
- Brand
- Model
- Transmission Type
- Car Type
- Year of Manufacture
- Rental Price per Day
- Status *(Available, Rented, Maintenance)*

### Customer List

Each customer transaction contains:

- Plate Number
- Customer Name
- Phone Number
- Total Rental Days
- Payment
- Rental Status *(Renting, Returned)*

---

## 🔐 Admin Access

To access the **Rental Revenue Report**, the program requires password authentication.  
> Default Password: `Prima`

---

## ⚙️ Requirements

- Python 3.13 or higher
- No external dependencies (pure Python standard libraries)

---

## ✅ Status

- All known bugs fixed
- Stable for use in local environments
- Includes input validation and data safety checks

---

## 👨‍💻 Author

Developed by **Prima Ade Sukrono** as part of a Capstone Project for a Python learning track.
