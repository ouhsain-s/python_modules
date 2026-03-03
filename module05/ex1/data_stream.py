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
        self.count = 0
        self.avg = 0
        self.total = 0
        self.count_only_temp = 0

    def process_batch(self, data_batch: list[Any]) -> str:

        try:
            for data in data_batch:
                if isinstance(data, str):
                    tp, value = data.split(":")
                    if tp == "temp":
                        self.total += float(value)
                        self.count_only_temp += 1
                self.count += 1
            if self.count_only_temp > 0:
                avg = self.total / self.count_only_temp
            return (f"Sensor analysis: {self.count} readings processed,"
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
        self.operations = 0
        self.net_flow = 0

    def process_batch(self, data_batch: list[Any]) -> str:

        try:
            for data in data_batch:
                if isinstance(data, str):
                    movment_type, amount = data.split(":")
                    if movment_type == "buy":
                        self.net_flow += int(amount)
                        self.operations += 1
                    elif movment_type == "sell":
                        self.net_flow -= int(amount)
                        self.operations += 1
            return (f"Transaction analysis: {self.operations} operations, net "
                    f"flow: {self.net_flow:+} units")
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
        self.num_events = 0
        self.num_errors = 0

    def process_batch(self, data_batch: List[Any]) -> str:

        try:
            for data in data_batch:
                if isinstance(data, str):
                    self.num_events += 1
                    if data.lower() == "error":
                        self.num_errors += 1
            return (f"Event analysis: {self.num_events} events, "
                    f"{self.num_errors} error detected")
        except Exception as e:
            return f"Error Event data: {e}"

    def get_stats(self) -> dict[str: Union[str, int, float]]:
        stat = super().get_stats()
        stat["type"] = "System Events"
        return stat

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> list[Any]:
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


class StreamProcessor:
    def __init__(self):
        self.streams = []

    def add_stream(self, steam: DataStream) -> None:
        self.streams.append(steam)

    def process_all_steams(self,
                           data_steams: dict[DataStream: list[Any]]) -> None:
        for stream in self.streams:
            data = data_steams[stream]
            stream.process_batch(data)

            if isinstance(stream, SensorStream):
                print(f"- Sensor data: {stream.count} readings processed")
            elif isinstance(stream, TransactionStream):
                print(f"- Transaction data: {stream.operations} "
                      f"operations processed")
            elif isinstance(stream, EventStream):
                print(f"- Event data: {stream.num_events} events processed")


def initializing_sensor() -> SensorStream:
    print("Initializing Sensor Stream...")
    data = ["temp:22.5", "humidity:65", "pressure:1013"]
    sensor = SensorStream("TRANS_001")
    stat = sensor.get_stats()
    print(f"Stream ID:{stat["stream_id"]}, Type: {stat["type"]}")
    print("Processing sensor batch:", data)
    print(sensor.process_batch(data))
    sensor.count = 0
    return sensor


def initializing_transactions() -> TransactionStream:
    transaction = TransactionStream("SENSOR_001")
    stat = transaction.get_stats()
    data = ["buy:100", "sell:150", "buy:75"]

    print("Initializing Transaction Stream...")
    print(f"Stream ID: {stat["stream_id"]}, Type: {stat["type"]}")
    print("Processing transaction batch:", data)
    print(transaction.process_batch(data))
    transaction.operations = 0
    return transaction


def initializing_events() -> EventStream:
    events = EventStream("SENSOR_001")
    stat = events.get_stats()
    data = ["login", "error", "ERROR", "logout"]

    print("Initializing Event Stream...")
    print(f"Stream ID: {stat["stream_id"]}, Type: {stat["type"]}")
    print("Processing event batch:", data)
    print(events.process_batch(data))
    events.num_events = 0
    events.num_errors = 0
    return events


def polymorphic_stream_processing(streams: list) -> None:
    """Demonstrate polymorphism by processing all streams
    through same interface.StreamProcessor handles different
    types without knowing their details."""
    stream_porcessor = StreamProcessor()

    for stream in streams:
        stream_porcessor.add_stream(stream)

    sensor_data = ["temp:25.0", "humidity:73"]
    trans_data = ["buy:22", "sell:10", "buy:50", "sell:30"]
    event_data = ["login", "error", "ERROR"]

    stream_data: Dict[DataStream, List[str]] = {}

    for stream in streams:
        if isinstance(stream, SensorStream):
            stream_data[stream] = sensor_data
        elif isinstance(stream, TransactionStream):
            stream_data[stream] = trans_data
        elif isinstance(stream, EventStream):
            stream_data[stream] = event_data

    print("\n=== Polymorphic Stream Processing ===")
    print("Processing mixed stream types through unified interface...")

    print("\nBatch 1 Results:")
    stream_porcessor.process_all_steams(stream_data)


def stream_filtering_active(sensor_stream: SensorStream,
                            trans_stream: TransactionStream) -> None:
    """Demonstrate filtering feature on streams.
    Shows how each stream filters data based on its own criteria."""
    print("\nStream filtering active: High-priority data only")

    sensor_critical = ["temp:444", "temp:70.0", "humidity:436", "temp:33"]
    trans_large = ["buy:100", "sell:300", "buy:70"]

    print("Filtered results:"
          f" {len(sensor_stream.filter_data(sensor_critical, "critical"))}"
          " critical sensor alerts, "
          f"{len(trans_stream.filter_data(trans_large, "large"))}"
          " large transaction")


if __name__ == "__main__":
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===\n")
    streams = []
    streams.append(initializing_sensor())
    print(end="\n")
    streams.append(initializing_transactions())
    print(end="\n")
    streams.append(initializing_events())

    polymorphic_stream_processing(streams)
    sentor = SensorStream("ITZ_02")
    trance = TransactionStream("T_09")
    stream_filtering_active(sentor, trance)
