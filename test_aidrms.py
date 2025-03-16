
import unittest
import numpy as np
import pandas as pd
from aidrms import RiskManagementSystem

class TestAIDRMS(unittest.TestCase):
    def setUp(self):
        self.data = pd.DataFrame({
            'feature1': np.random.rand(100),
            'feature2': np.random.rand(100),
            'feature3': np.random.rand(100),
            'feature4': np.random.rand(100)
        })
        self.target = np.random.randint(2, size=100)
        self.aidrms = RiskManagementSystem()

    def test_train_model(self):
        self.aidrms.train_model(self.data, self.target)
        self.assertIsNotNone(self.aidrms.model)

    def test_predict_risks(self):
        self.aidrms.train_model(self.data, self.target)
        predictions = self.aidrms.predict_risks(self.data[:5])
        self.assertEqual(len(predictions), 5)

if __name__ == '__main__':
    unittest.main()
