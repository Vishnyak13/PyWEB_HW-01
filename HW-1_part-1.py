from abc import ABC, abstractmethod
import pickle
import json

FILENAME = 'data'


class SerializationInterface(ABC):
    @abstractmethod
    def serialize(self, data):
        pass

    @abstractmethod
    def deserialize(self, data):
        pass


class PickleSerialization(SerializationInterface):
    def serialize(self, data):
        with open(FILENAME + '.pickle', 'wb') as f:
            pickle.dump(data, f)

    def deserialize(self, data):
        with open(FILENAME + '.pickle', 'rb') as f:
            return pickle.load(f)


class JsonSerialization(SerializationInterface):
    def serialize(self, data):
        with open(FILENAME + '.json', 'w') as f:
            json.dump(data, f)

    def deserialize(self, data):
        with open(FILENAME + '.json', 'r') as f:
            return json.load(f)


if __name__ == '__main__':
    data = {'Name': 'Evgeniy', 'Surname': 'Vishnitskiy', 'Age': 34, 'City': 'Zaporiyia'}
    pickle_serializer = PickleSerialization()
    pickle_serializer.serialize(data)
    print(pickle_serializer.deserialize(data))
    json_serializer = JsonSerialization()
    json_serializer.serialize(data)
    print(json_serializer.deserialize(data))