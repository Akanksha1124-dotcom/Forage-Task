import json
from datetime import datetime

# Convert ISO format to milliseconds
def convert_iso_to_millis(iso_str):
    dt = datetime.strptime(iso_str, "%Y-%m-%dT%H:%M:%SZ")
    return int(dt.timestamp() * 1000)

# IMPLEMENT: transform_data_1
def transform_data_1(data):
    result = []
    for item in data:
        result.append({
            "timestamp": convert_iso_to_millis(item["time"]),
            "value": item["value"]
        })
    return result

# IMPLEMENT: transform_data_2
def transform_data_2(data):
    return data  # Already in the correct format

# Entry point
if __name__ == "__main__":
    with open("data-1.json") as f1, open("data-2.json") as f2, open("data-result.json") as fres:
        data1 = json.load(f1)
        data2 = json.load(f2)
        expected = json.load(fres)

    transformed = transform_data_1(data1) + transform_data_2(data2)
    transformed.sort(key=lambda x: x["timestamp"])

    assert transformed == expected, "Test failed!"
    print("✅ All tests passed!")
