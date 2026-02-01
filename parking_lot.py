from datetime import datetime, date
from pricing import StandardPricing
from passes import MonthlyPass, SingleEntryPass


class Ticket:
    """
    Represents one parking session
    """
    def __init__(self, plate, spot):
        self.plate = plate
        self.spot = spot
        self.entry_time = datetime.now()
        self.exit_time = None
        self.fee = 0.0


class ParkingLot:
    """
    Main parking lot system
    """
    def __init__(self, total_spots=300):
        self.total_spots = total_spots
        self.pricing = StandardPricing()
        self.parked = {}           # plate -> Ticket
        self.monthly_passes = {}   # plate -> MonthlyPass
        self.single_passes = {}    # pass_id -> SingleEntryPass
        self.next_spot = 1

    # ---------- Space ----------
    def available_spots(self):
        return self.total_spots - len(self.parked)

    # ---------- Pass management ----------
    def add_monthly_pass(self, mp: MonthlyPass):
        self.monthly_passes[mp.plate] = mp

    def has_valid_monthly_pass(self, plate):
        mp = self.monthly_passes.get(plate)
        return mp is not None and mp.is_valid(date.today())

    def add_single_pass(self, sp: SingleEntryPass):
        self.single_passes[sp.pass_id] = sp

    def use_single_pass(self, pass_id):
        sp = self.single_passes.get(pass_id)
        if sp and sp.can_use():
            sp.mark_used()
            return True
        return False

    # ---------- Entry ----------
    def enter_vehicle(self, plate):
        if self.available_spots() <= 0:
            return None
        if plate in self.parked:
            return None

        ticket = Ticket(plate, self.next_spot)
        self.parked[plate] = ticket

        self.next_spot += 1
        if self.next_spot > self.total_spots:
            self.next_spot = 1

        return ticket

    # ---------- Exit ----------
    def exit_vehicle(self, plate, vehicle_multiplier=1.0):
        ticket = self.parked.get(plate)
        if ticket is None:
            return None

        ticket.exit_time = datetime.now()
        ticket.fee = self.pricing.calculate_fee(
            ticket.entry_time,
            ticket.exit_time,
            vehicle_multiplier
        )

        del self.parked[plate]
        return ticket
