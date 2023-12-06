class Singleton:
    _unique_instance = None

    def __new__(cls):
        if cls._unique_instance is None:
            cls._unique_instance = super(Singleton, cls).__new__(cls)

        return cls._unique_instance

    def getValue(self) -> str:
        return self.value

    def setValue(self, value: str):
        self.value = value
