from typing import Sequence, Optional, Union
from dataclasses import dataclass


@dataclass
class Statistics:
    count: int
    average: float
    maximum: float
    minimum: float
    total: float
    
    def __str__(self):
        return (
            f"Statistics(count={self.count}, "
            f"average={self.average:.2f}, "
            f"max={self.maximum}, "
            f"min={self.minimum})"
        )


def calculate_statistics(values: Sequence[Union[int, float]]) -> Optional[Statistics]:
    if not values:
        return None
    
    total = sum(values)
    count = len(values)
    average = total / count
    maximum = max(values)
    minimum = min(values)
    
    return Statistics(
        count=count,
        average=average,
        maximum=maximum,
        minimum=minimum,
        total=total
    )
