from abc import ABC, abstractmethod
from typing import Any, List, Optional, Union, Dict


class DataStream(ABC):
    """Abstract base class for all data streams.
    Child classes must implement process_batch method."""

    def __init__(self, stream_id: str) -> None:
        """Initialize the stream with a unique ID.
        Sets up the base stream configuration."""
        super().__init__()
        self.stream_id = stream_id

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        """Abstract method - child classes MUST implement this.
        Purpose: Process a list of data and return result string."""
        pass

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        """Default filter method - returns data unchanged.
        Child classes can override to add specific filtering."""
        return data_batch

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        """Return basic stream statistics.
        Child classes can override to add more stats."""
        return {"stream_id": self.stream_id}


class SensorStream(DataStream):
    """Stream handler for sensor data like temperature and humidity.
    Processes environmental readings and calculates averages."""

    def __init__(self, stream_id: str) -> None:
        """Initialize sensor stream with ID and tracking variables.
        Sets up count, total, average for calculations."""
        super().__init__(stream_id)
        self.count: int
        self.total: float
        self.average: float

    def process_batch(self, data_batch: List[Any]) -> str:
        """Process sensor readings and calculate temperature average.
        Returns string with readings count and average temperature."""
        self.count = 0
        self.total = 0
        self.average = 0
        temp_count = 0
        try:
            for data in data_batch:
                if isinstance(data, str):
                    label, value = data.split(':')
                    if label == "temp":
                        self.total += float(value)
                        temp_count += 1
                    self.count += 1
                else:
                    self.total += data
                    self.count += 1
                    temp_count += 1

            if temp_count > 0:
                self.average = self.total / temp_count
            return (f"{self.count} readings processed, avg temp: "
                    f"{self.average}°C")
        except Exception as e:
            return f"Error processing sensor data: {e}"

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        """Return sensor stream statistics.
        Includes stream ID and data type."""
        stats = super().get_stats()
        stats["type"] = "Environmental Data"
        return stats

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        """Filter sensor data based on criteria.
        If criteria is 'critical', returns only high temperature readings."""
        if criteria is None:
            return data_batch

        filtered = []
        if criteria == "critical":
            for data in data_batch:
                if isinstance(data, str):
                    label, value = data.split(':')
                    if label == "temp" and float(value) > 35:
                        filtered.append(data)
        return filtered


class TransactionStream(DataStream):
    """Stream handler for financial transaction data.
    Processes buy/sell operations and calculates net flow."""

    def __init__(self, stream_id: str) -> None:
        """Initialize transaction stream with ID and tracking variables.
        Sets up operations count and net flow for calculations."""
        super().__init__(stream_id)
        self.operations: int
        self.net_flow: int

    def process_batch(self, data_batch: List[Any]) -> str:
        """Process buy/sell transactions and calculate net flow.
        Returns string with operations count and net flow result."""
        self.operations = 0
        self.net_flow = 0
        try:
            for data in data_batch:
                if isinstance(data, str):
                    operation_type, v_amount = data.split(':')
                    amount = int(v_amount)
                    if operation_type == "buy":
                        self.net_flow += amount
                    elif operation_type == "sell":
                        self.net_flow -= amount
                    self.operations += 1
                else:
                    self.net_flow += data
                    self.operations += 1
            if self.net_flow >= 0:
                return (f"{self.operations} operations, net flow: "
                        f"+{self.net_flow} units")
            else:
                return (f"{self.operations} operations, net flow: "
                        f"{self.net_flow} units")
        except Exception as e:
            return f"Error Transaction data: {e}"

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        """Return transaction stream statistics.
        Includes stream ID and data type."""
        stats = super().get_stats()
        stats["type"] = "Financial Data"
        return stats

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        """Filter transaction data based on criteria.
        If criteria is 'large', returns only high amount transactions."""
        if criteria is None:
            return data_batch

        filtered = []
        if criteria == "large":
            for data in data_batch:
                if isinstance(data, str):
                    _, amount = data.split(':')
                    if int(amount) > 180:
                        filtered.append(data)
        return filtered


class EventStream(DataStream):
    """Stream handler for system event data.
    Processes events like login, logout, error and counts them."""

    def __init__(self, stream_id: str) -> None:
        """Initialize event stream with ID and tracking variables.
        Sets up events count and errors count."""
        super().__init__(stream_id)
        self.events: int
        self.errors: int

    def process_batch(self, data_batch: List[Any]) -> str:
        """Process system events and count errors.
        Returns string with events count and errors count."""
        self.events = 0
        self.errors = 0
        try:
            for data in data_batch:
                if isinstance(data, str):
                    self.events += 1
                    if data == "error":
                        self.errors += 1
                else:
                    self.events += 1
            return (f"{self.events} events, {self.errors} error detected")
        except Exception as e:
            return f"Error Event data: {e}"

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        """Return event stream statistics.
        Includes stream ID and data type."""
        stats = super().get_stats()
        stats["type"] = "System Events"
        return stats

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        """Filter event data based on criteria.
        If criteria is 'error', returns only error events."""
        if criteria is None:
            return data_batch

        filtered = []
        if criteria == "error":
            filtered = [data for data in data_batch if data == "error"]
        return filtered


class StreamProcessor:
    """Manager class that handles multiple streams polymorphically.
    Can process any DataStream type through same interface."""

    def __init__(self) -> None:
        """Initialize processor with empty streams list.
        Streams will be added using add_stream method."""
        self.__streams: List[Any] = []

    def add_stream(self, stream: DataStream) -> None:
        """Add a stream to the processor's list.
        Any DataStream child type can be added."""
        self.__streams.append(stream)

    def process_all(self, stream_data: Dict) -> None:
        """Process all streams using polymorphism.
        Calls same method on different stream types -
        each behaves differently."""
        for stream in self.__streams:
            data = stream_data[stream]
            stream.process_batch(data)

            if isinstance(stream, SensorStream):
                print(f"- Sensor data: {stream.count} readings processed")
            elif isinstance(stream, TransactionStream):
                print(f"- Transaction data: {stream.operations} "
                      f"operations processed")
            elif isinstance(stream, EventStream):
                print(f"- Event data: {stream.events} events processed")


def initializing_sensor_stream(sensor_stream: SensorStream) -> None:
    """Demo function for sensor stream.
    Shows how sensor stream processes environmental data."""

    print("\nInitializing Sensor Stream...")
    data_batch = ["temp:22.5", "humidity:65", "pressure:1013"]
    stats = sensor_stream.get_stats()
    print(f"Stream ID: {stats['stream_id']}, Type: {stats['type']}")
    print(f"Processing sensor batch: {data_batch}")
    print("Sensor analysis:", sensor_stream.process_batch(data_batch))


def initializing_transaction_stream(trans_stream: TransactionStream) -> None:
    """Demo function for transaction stream.
    Shows how transaction stream processes buy/sell data."""
    print("\nInitializing Transaction Stream...")
    data_batch = ["buy:100", "sell:150", "buy:75"]
    stats = trans_stream.get_stats()
    print(f"Stream ID: {stats['stream_id']}, Type: {stats['type']}")
    print(f"Processing transaction batch: {data_batch}")
    print("Transaction analysis:", trans_stream.process_batch(data_batch))


def initializing_event_stream(event_stream: EventStream) -> None:
    """Demo function for event stream.
    Shows how event stream processes system events."""
    print("\nInitializing Event Stream...")
    data_batch = ["login", "error", "logout"]
    stats = event_stream.get_stats()
    print(f"Stream ID: {stats['stream_id']}, Type: {stats['type']}")
    print(f"Processing transaction batch: {data_batch}")
    print(f"Event analysis: {event_stream.process_batch(data_batch)}")


def polymorphic_stream_processing(sensor_stream: SensorStream,
                                  trans_stream: TransactionStream,
                                  event_stream: EventStream) -> None:
    """Demonstrate polymorphism by processing all streams
    through same interface.StreamProcessor handles different
    types without knowing their details."""
    stream_porcess = StreamProcessor()

    stream_porcess.add_stream(sensor_stream)
    stream_porcess.add_stream(trans_stream)
    stream_porcess.add_stream(event_stream)

    sensor_data = ["temp:20.0", "humidity:70"]
    trans_data = ["buy:200", "sell:100", "buy:50", "sell:50"]
    event_data = ["login", "logout", "login"]

    stream_data: Dict[DataStream, List[str]] = {}
    stream_data[sensor_stream] = sensor_data
    stream_data[trans_stream] = trans_data
    stream_data[event_stream] = event_data

    print("\n=== Polymorphic Stream Processing ===")
    print("Processing mixed stream types through unified interface...")

    print("\nBatch 1 Results:")
    stream_porcess.process_all(stream_data)


def stream_filtering_active(sensor_stream: SensorStream,
                            trans_stream: TransactionStream) -> None:
    """Demonstrate filtering feature on streams.
    Shows how each stream filters data based on its own criteria."""
    print("\nStream filtering active: High-priority data only")

    sensor_critical = ["temp:35.5", "temp:40.0", "humidity:50", "temp:32.0"]
    trans_large = ["buy:200", "sell:100", "buy:180"]

    sensor_filtered = sensor_stream.filter_data(sensor_critical, "critical")
    trans_filtered = trans_stream.filter_data(trans_large, "large")

    critical_count = len(sensor_filtered)

    large_count = len(trans_filtered)

    print(f"Filtered results: {critical_count} critical sensor alerts, "
          f"{large_count} large transaction")


def main():
    """Main function that runs the complete stream processing demo.
    Creates streams, processes them, and shows polymorphism in action."""
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===")

    sensor_stream = SensorStream("SENSOR_001")
    initializing_sensor_stream(sensor_stream)

    trans_stream = TransactionStream("TRANS_001")
    initializing_transaction_stream(trans_stream)

    event_stream = EventStream("EVENT_001")
    initializing_event_stream(event_stream)

    polymorphic_stream_processing(sensor_stream, trans_stream, event_stream)

    stream_filtering_active(sensor_stream, trans_stream)

    print("\nAll streams processed successfully. Nexus throughput optimal.")


if __name__ == "__main__":
    main()
