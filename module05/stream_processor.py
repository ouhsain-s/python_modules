from typing import Any, List, Dict, Union, Optional, Protocol
from abc import ABC, abstractmethod

class DataProcessor(ABC):
    @abstractmethod
    def process(self, data: Any) -> str:
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    def format_output(self, result: str) -> str:
        pass


class NumericProcessor(DataProcessor):
    def process(self, data: any) -> str:

        print(f"Processing data: {data}")
        try:
            tmp = []
            num_format = ""
            if self.validate(data):
                if data.__class__.__name__ == "list":
                    for n in data:
                        tmp.append(int(n))
            else:
                tmp.append(int(data))

            num_format = ", ".join(str(n) for n in tmp)
            return num_format
        except (ValueError, TypeError):
            return "3, 3, 3"

    def validate(self, data: Any) -> bool:
        list_check = (data.__class__.__name__ == "list" and len(data)) and\
         all(n.__class__.__name__ in ["int", "float"] for n in data)
        int_check = (data.__class__.__name__ in ["int", "float"])

        if list_check or int_check:
            print("Validation: Numeric data verified")
            return True
        else:
            print("Validation: Numeric data not verified")
            return False

    def format_output(self, result: str) -> str:
        if result:
            try:
                num = len(result.split(","))
                sum_nums = sum(int(n) for n in result.split(", "))
                avg = sum_nums / num
                print(f"Output: Processed {num} numeric values, sum={sum_nums}, avg={avg}")
            except ValueError:
                print("Output: ")
        else:
            print("Output: ")


class TextProcessor(DataProcessor):
    pass


class LogProcessor(DataProcessor):
    pass


def main():
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===\n")
    print("Initializing Numeric Processor...")
    nums = NumericProcessor()
    data = [1, 2, 3, 4, 5]
    format = nums.process(data)
    nums.format_output(format)



if __name__ == "__main__":
    main()