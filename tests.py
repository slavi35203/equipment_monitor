import logic
import unittest


class EquipmentTests(unittest.TestCase):

    def test_get_all_equipment(self):
        equipment = logic.get_all_equipment()
        self.assertIsNotNone(equipment)

    def test_get_equipment_by_type(self):
        equipment = logic.get_equipment_by_type(1)
        self.assertIsNotNone(equipment)


class ProtocolTests(unittest.TestCase):
    def test_protocol_lifecycle(self):
        user_id = 1
        result = logic.create_protocol(user_id, "Equipment", equipment_id=1)
        self.assertTrue(result > 0)


if __name__ == "__main__":
    unittest.main()