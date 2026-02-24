from typing import Any, Dict, Union, Optional, List
from abc import ABC, abstractmethod


class DataStream(ABC):
    def __init__(self, stream_id: str) -> None:
        self.stream_id = stream_id
        super().__init__()

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        pass

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        return data_batch

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {"stream_id": self.stream_id}


class SensorStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)

    def process_batch(self, data_batch: list[Any]) -> str:
        count = 0
        avg = 0
        total = 0
        count_only_temp = 0
        try:
            for data in data_batch:
                if isinstance(data, str):
                    tp, value = data.split(":")
                    if tp == "temp":
                        total += float(value)
                        count_only_temp += 1
                count += 1
            if count_only_temp > 0:
                avg = total / count_only_temp
            return (f"Sensor analysis: {count} readings processed,"
                    f" avg temp: {avg}°C")
        except Exception as e:
            return f"Error processing sensor data: {e}"

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        status = super().get_stats()
        status["type"] = "Environmental Data"
        return status

    def filter_data(self, data_batch: list[Any],
                    criteria: Optional[str] = None) -> list[Any]:
        try:
            if criteria is None:
                return data_batch
            if criteria == "critical":
                return ([data for data in data_batch if isinstance(data, str)
                        and data.startswith("temp:")
                        and float(data.split(":")[1]) > 35])
            return []
        except Exception as e:
            print(f"Error filtering sensor data: {e}")
            return []


class TransactionStream(DataStream):
    def __init__(self, stream_id):
        super().__init__(stream_id)

    def process_batch(self, data_batch: list[Any]) -> str:
        operations = 0
        net_flow = 0
        try:
            for data in data_batch:
                if isinstance(data, str):
                    movment_type, amount = data.split(":")
                    if movment_type == "buy":
                        net_flow += int(amount)
                        operations += 1
                    elif movment_type == "sell":
                        net_flow -= int(amount)
                        operations += 1
            return (f"Transaction analysis: {operations} operations, net flow:"
                    f"{net_flow:+} units")
        except Exception as e:
            return f"Error processing transaction data: {e}"

    def get_stats(self) -> dict[str, Union[str, int, float]]:
        stat = super().get_stats()
        stat["type"] = "Financial Data"
        return stat

    def filter_data(self, data_batch: list[Any],
                    criteria: Optional[str] = None) -> list[Any]:
        if criteria is None:
            return data_batch
        try:
            if criteria == "large":
                return ([data for data in data_batch if isinstance(data, str)
                        and int(data.split(":")[1]) > 180])
            return []
        except Exception as e:
            print(f"Error filtering transaction data: {e}")
            return []


class EventStream(DataStream):
    def __init__(self, stream_id):
        super().__init__(stream_id)

    def process_batch(self, data_batch: List[Any]) -> str:
        num_events = 0
        num_errors = 0

        try:
            for data in data_batch:
                if isinstance(data, str):
                    num_events += 1
                    if data.lower() == "error":
                        num_errors += 1
            return (f"Event analysis: {num_events} events, {num_errors} "
                    "error detected")
        except Exception as e:
            return f"Error Event data: {e}"

    def get_stats(self) -> dict[str: Union[str, int, float]]:
        stat = super().get_stats()
        stat["type"] = "System Events"
        return stat

    def filter_data(self, data_batch: List[Any], criteria: Optional[str] = None) -> list[Any]:
        if criteria is None:
            return data_batch
        try:
            if criteria == "error":
                return ([data for data in data_batch if isinstance(data, str)
                         and data.lower() == "error"])
            return []
        except Exception as e:
            print(f"Error filtering event data: {e}")
            return []


def initializing_sensor():
    print("Initializing Sensor Stream...")
    data = ["temp:22.5", "humidity:65", "pressure:1013"]
    sensor = SensorStream("TRANS_001")
    stat = sensor.get_stats()
    print(f"Stream ID:{stat["stream_id"]}, Type: {stat["type"]}")
    print("Processing sensor batch:", data)
    print(sensor.process_batch(data))


def initializing_transactions():
    transaction = TransactionStream("SENSOR_001")
    stat = transaction.get_stats()
    data = ["buy:100", "sell:150", "buy:75"]

    print("Initializing Transaction Stream...")
    print(f"Stream ID: {stat["stream_id"]}, Type: {stat["type"]}")
    print("Processing transaction batch:", data)
    print(transaction.process_batch(data))


def initializing_events():
    events = EventStream("SENSOR_001")
    stat = events.get_stats()
    data = ["login", "error", "ERROR", "logout"]

    print("Initializing Event Stream...")
    print(f"Stream ID: {stat["stream_id"]}, Type: {stat["type"]}")
    print("Processing event batch:", data)
    print(events.process_batch(data))


if __name__ == "__main__":
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===\n")
    initializing_sensor()
    print(end="\n")
    initializing_transactions()
    print(end="\n")
    initializing_events()
