from __future__ import annotations
from dataclasses import dataclass
from statistics import mean, median, stdev
from typing import Iterable

@dataclass(frozen=True)
class Stats:
    count: int
    mean: float
    median: float
    stdev: float | None
    min: float
    max: float

def summarize(values: Iterable[float | int]) -> Stats:
    xs = [float(v) for v in values]
    if not xs:
        raise ValueError("summarize() requires at least one value")
    n = len(xs)
    return Stats(
        count=n,
        mean=mean(xs),
        median=median(xs),
        stdev=stdev(xs) if n > 1 else None,
        min=min(xs),
        max=max(xs),
    )

if __name__ == "__main__":
    print(summarize([1, 2, 3, 4]))
