from abc import ABC, abstractmethod

class BaseLLM(ABC):
    @abstractmethod
    def load_model(self, model_name: str):
        """Load the model by name."""
        pass

    @abstractmethod
    def predict(self, input_data):
        """Make a prediction using the model."""
        pass

    @abstractmethod
    def save_model(self, save_path: str):
        """Save the model to the specified path."""
        pass


