from typing import Any
from abc import ABC, abstractmethod


class DataProcessor(ABC):
    @abstractmethod
    def process(self, data: Any) -> str:
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    def format_output(self, result: str) -> str:
        return f"Output: {result}"


class NumericProcessor(DataProcessor):
    def process(self, data: Any) -> str:

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
            return ""

    def validate(self, data: Any) -> bool:
        list_check = (data.__class__.__name__ == "list" and len(data)) and\
         all(n.__class__.__name__ in ["int", "float"] for n in data)
        int_check = (data.__class__.__name__ in ["int", "float"])

        if list_check or int_check:
            print("Validation: Numeric data verified")
            return True
        else:
            print("Validation: Numeric data is not verified")
            return False

    def format_output(self, result: str) -> str:
        if result:
            try:
                num = len(result.split(","))
                sum_nums = sum(int(n) for n in result.split(", "))
                avg = sum_nums / num
                return (f"Output: Processed {num} numeric values, "
                        f"sum={sum_nums}, avg={avg}")
            except ValueError:
                return "invalid data found"
        else:
            return "invalid data found"


class TextProcessor(DataProcessor):
    def process(self, data: Any) -> str:
        result = ""
        print("Processing data:", data)
        if self.validate(data):
            print("Validation: Text data verified")
            result = data
        else:
            print("Validation: Text data is not verified")
        return result

    def validate(self, data: Any) -> bool:
        return data.__class__.__name__ == "str"

    def format_output(self, result: str) -> str:
        num_words = len(result.split(" "))
        num_chars = len(result)
        return (f"Output: Processed text: {num_chars} characters,"
                f" {num_words} words")


class LogProcessor(DataProcessor):

    def process(self, data: Any) -> str:
        print(f"Processing data: \"{data}\"")
        result = ""
        if self.validate(data):
            try:
                type_ivent, event = data.split(":", 1)
                if type_ivent == "ERROR":
                    result = (f"[ALERT] {type_ivent} level detected:"
                              f"{event}")
                elif type_ivent == "INFO":
                    result = (f"[INFO] {type_ivent} level detected:"
                              f"{event}")
                else:
                    result = (f"[{type_ivent}] {type_ivent} level "
                              f"detected: {event}")
                print("Validation: Log entry verified")
                return result
            except Exception as e:
                result = f"Error: {e}"
                return result

    def validate(self, data: Any) -> bool:
        return (data.__class__.__name__ == "str")

    def format_output(self, result: str) -> str:
        return super().format_output(result)


def processing_multiple_data(proc_type: Any, data: Any) -> str:
    obj_type = proc_type()
    if obj_type.validate(data):
        format = obj_type.process(data)
        return obj_type.format_output(format)


def main():
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===\n")
    print("Initializing Numeric Processor...")
    nums = NumericProcessor()
    data = [1, 2, 3, 4, 5]
    format = nums.process(data)
    print(nums.format_output(format))
    print(end="\n")
    print("Initializing Text Processor...")
    text = TextProcessor()
    data = "Hello Nexus World"
    format = text.process(data)
    print(text.format_output(format))
    print(end="\n")
    print("Initializing Log Processor...")
    log = LogProcessor()
    print("Output:", log.process("ERROR: Connection timeout"))
    print(end="\n")

    print("=== Polymorphic Processing Demo ===\n")

    print("Processing multiple data types through same interface...")
    print("Result 0:", processing_multiple_data
          (NumericProcessor, [1, 2, 3, 4, 5]))
    print(end="\n")
    print("Result 1:", processing_multiple_data
          (TextProcessor, "Hello Nexus World"))
    print(end="\n")
    print("Result 2:", processing_multiple_data
          (LogProcessor, "INFO: System ready"))
    print("\nFoundation systems online. Nexus ready for advanced streams.")


if __name__ == "__main__":
    main()
