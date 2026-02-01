from datetime import date


class MonthlyPass:
    """
    Monthly pass linked to a vehicle plate and expiry date.
    """
    def __init__(self, pass_id: str, plate: str, expiry_date: date):
        self.pass_id = pass_id
        self.plate = plate
        self.expiry_date = expiry_date

    def is_valid(self, today: date) -> bool:
        return today <= self.expiry_date


class SingleEntryPass:
    """
    Single entry pass that can be used only once.
    """
    def __init__(self, pass_id: str):
        self.pass_id = pass_id
        self.used = False

    def can_use(self) -> bool:
        return not self.used

    def mark_used(self):
        self.used = True
