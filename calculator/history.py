from typing import Callable, List
#from calculator.operation import Operation
from calculator.calculation import Calculation

class History:
    hist: List[Calculation] = []
  
    @classmethod
    def append_calc(cls, calc: Calculation):
        cls.hist.append(calc)

    @classmethod
    def get_history(cls) -> List[Calculation]:
        return cls.hist

    @classmethod
    def set_history(cls, newhist: List[Calculation]):
        cls.hist = newhist

    @classmethod
    def clear_history(cls):
        cls.hist.clear()

    @classmethod
    def get_last_calc(cls) -> Calculation:
        if cls.hist == []:
            return None
        return cls.hist[-1]

    @classmethod
    def get_index_calc(cls, index: int) -> Calculation:
        if len(cls.hist) > index:
            return cls.hist[index]
        return None            
