import numpy as np

class LiveTelemetryNeuralNet:
    def __init__(self):
        np.random.seed(42)
        # Architettura: 4 Input -> 8 Hidden1 -> 6 Hidden2 -> 2 Output (Predicted Load, Anomaly Risk)
        self.W1 = np.random.randn(4, 8) * 0.3
        self.b1 = np.zeros((1, 8))
        self.W2 = np.random.randn(8, 6) * 0.3
        self.b2 = np.zeros((1, 6))
        self.W3 = np.random.randn(6, 2) * 0.3
        self.b3 = np.zeros((1, 2))
        self.learning_rate = 0.015
        self.epoch_counter = 0
        self.last_loss = 0.0012

    @staticmethod
    def sigmoid(x):
        return 1.0 / (1.0 + np.exp(-np.clip(x, -15, 15)))

    @staticmethod
    def sigmoid_deriv(x):
        return x * (1.0 - x)

    def forward_and_learn(self, cpu: float, ram: float, disk: float, procs: int) -> dict:
        # Normalizzazione input [0, 1]
        x = np.array([[cpu / 100.0, ram / 100.0, disk / 100.0, min(procs / 400.0, 1.0)]])
        
        # Forward pass
        h1 = self.sigmoid(np.dot(x, self.W1) + self.b1)
        h2 = self.sigmoid(np.dot(h1, self.W2) + self.b2)
        out = self.sigmoid(np.dot(h2, self.W3) + self.b3)

        # Target auto-supervisionato (stima carico futuro e anomalia)
        target_load = min(1.0, (cpu * 0.6 + ram * 0.4) / 100.0)
        target_anomaly = 1.0 if (cpu > 85 or ram > 90) else (cpu * ram) / 10000.0
        y = np.array([[target_load, target_anomaly]])

        # Backpropagation live
        error = y - out
        self.last_loss = float(np.mean(np.square(error)))
        
        d_out = error * self.sigmoid_deriv(out)
        d_h2 = d_out.dot(self.W3.T) * self.sigmoid_deriv(h2)
        d_h1 = d_h2.dot(self.W2.T) * self.sigmoid_deriv(h1)

        self.W3 += h2.T.dot(d_out) * self.learning_rate
        self.W2 += h1.T.dot(d_h2) * self.learning_rate
        self.W1 += x.T.dot(d_h1) * self.learning_rate
        self.epoch_counter += 1

        return {
            "epoch": self.epoch_counter,
            "loss": round(self.last_loss, 6),
            "predicted_load": round(float(out[0, 0]) * 100, 1),
            "anomaly_score": round(float(out[0, 1]) * 100, 1),
            "layers": {
                "input": [round(float(v), 2) for v in x[0]],
                "hidden1": [round(float(v), 2) for v in h1[0]],
                "hidden2": [round(float(v), 2) for v in h2[0]],
                "output": [round(float(v), 2) for v in out[0]]
            }
        }

neural_engine = LiveTelemetryNeuralNet()
