from abc import ABC, abstractmethod
from datetime import datetime


class PricingStrategy(ABC):
    """
    Abstract pricing strategy (ABC).
    Different pricing rules can be implemented by subclasses.
    """
    @abstractmethod
    def calculate_fee(self, entry_time: datetime, exit_time: datetime, vehicle_multiplier: float) -> float:
        pass


class StandardPricing(PricingStrategy):
    """
    Simple pricing: hourly_rate * hours * vehicle_multiplier
    """
    def __init__(self, hourly_rate: float = 5.0):
        self.hourly_rate = hourly_rate

    def calculate_fee(self, entry_time: datetime, exit_time: datetime, vehicle_multiplier: float) -> float:
        duration_seconds = (exit_time - entry_time).total_seconds()

        # Round up to the next hour, minimum 1 hour
        hours = max(1, int((duration_seconds + 3599) // 3600))

        fee = hours * self.hourly_rate * vehicle_multiplier
        return round(fee, 2)
