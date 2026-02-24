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
        try:
            for data in data_batch:
                if isinstance(data, str):
                    tp, value = data.split(":")
                    if tp == "temp":
                        total += float(value)
                        count += 1
                else:
                    total += data
                    count += 1
            if count > 0:
                avg = total / count
            return (f"Sensor analysis: {count} readings processed,"
                    f" avg temp: {avg}°C")
        except Exception as e:
            return f"Error processing sensor data: {e}"

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        status = super().get_stats()
        status["type"] = "Environmental Data"
        return status

    def filter_data(self, data_batch: list[Any], criteria: Optional[str] = None) -> list[Any]:
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
