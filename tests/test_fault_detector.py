
import unittest
from backend.fault_detector import diagnose_fault


class TestFaultDetector(unittest.TestCase):

    def test_normal_readings(self):
        status, faults = diagnose_fault(60, 40, 5)
        self.assertEqual(status, "NORMAL")
        self.assertEqual(faults, [])

    def test_single_fault(self):
        status, faults = diagnose_fault(90, 40, 5)
        self.assertEqual(status, "WARNING")
        self.assertEqual(faults, ["High Temperature"])

    def test_multiple_faults(self):
        status, faults = diagnose_fault(90, 75, 5)
        self.assertEqual(status, "CRITICAL")
        self.assertEqual(
            faults,
            ["High Temperature", "Excessive Vibration"]
        )

    def test_all_faults(self):
        status, faults = diagnose_fault(90, 75, 9)
        self.assertEqual(status, "CRITICAL")
        self.assertEqual(len(faults), 3)

    def test_values_at_thresholds(self):
        status, faults = diagnose_fault(85, 70, 8)
        self.assertEqual(status, "NORMAL")
        self.assertEqual(faults, [])


if __name__ == "__main__":
    unittest.main()
