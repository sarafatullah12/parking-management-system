from parking_lot import ParkingLot
from passes import MonthlyPass, SingleEntryPass
from datetime import date


def show_menu():
    print("\n=== Parking Management System ===")
    print("1. Vehicle Entry")
    print("2. Vehicle Exit")
    print("3. Available Parking Spaces")
    print("4. Add Monthly Pass")
    print("5. Use Single Entry Pass")
    print("6. Exit System")


def main():
    lot = ParkingLot()

    while True:
        show_menu()
        choice = input("Choose an option (1-6): ").strip()

        if choice == "1":
            plate = input("Enter vehicle plate number: ").strip()
            ticket = lot.enter_vehicle(plate)
            if ticket:
                print("Vehicle entered successfully")
                print("Spot:", ticket.spot)
                print("Entry time:", ticket.entry_time)
            else:
                print("Entry failed")

        elif choice == "2":
            plate = input("Enter vehicle plate number: ").strip()
            ticket = lot.exit_vehicle(plate)
            if ticket:
                print("Vehicle exited successfully")
                print("Exit time:", ticket.exit_time)
                print("Parking fee: $", ticket.fee)
            else:
                print("Vehicle not found")

        elif choice == "3":
            print("Available spaces:", lot.available_spots())

        elif choice == "4":
            plate = input("Enter plate number: ").strip()
            pass_id = input("Enter monthly pass ID: ").strip()
            expiry = input("Enter expiry date (YYYY-MM-DD): ").strip()

            y, m, d = map(int, expiry.split("-"))
            mp = MonthlyPass(pass_id, plate, date(y, m, d))
            lot.add_monthly_pass(mp)
            print("Monthly pass added successfully")

        elif choice == "5":
            pass_id = input("Enter single entry pass ID: ").strip()
            sp = SingleEntryPass(pass_id)
            lot.add_single_pass(sp)

            if lot.use_single_pass(pass_id):
                print("Single entry pass used successfully")
            else:
                print("Single entry pass invalid")

        elif choice == "6":
            print("Exiting system. Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
