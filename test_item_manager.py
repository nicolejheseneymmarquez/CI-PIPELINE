import unittest
from item_manager import ItemManager


class TestItemManager(unittest.TestCase):
    def setUp(self):
        self.manager = ItemManager()

    def test_add_item(self):
        item_id = self.manager.add_item("Apple")
        self.assertIn(item_id, self.manager.items)
        self.assertEqual(self.manager.items[item_id], "Apple")

    def test_update_item(self):
        item_id = self.manager.add_item("Banana")
        self.manager.update_item(item_id, "Grape")
        self.assertEqual(self.manager.items[item_id], "Grape")

    def test_update_nonexistent_item(self):
        with self.assertRaises(ValueError):
            self.manager.update_item(999, "Test")

    def test_delete_item(self):
        item_id = self.manager.add_item("Orange")
        self.manager.delete_item(item_id)
        self.assertNotIn(item_id, self.manager.items)

    def test_delete_nonexistent_item(self):
        with self.assertRaises(ValueError):
            self.manager.delete_item(999)

    def test_list_items(self):
        self.manager.add_item("Item1")
        self.manager.add_item("Item2")
        items = self.manager.list_items()
        self.assertEqual(len(items), 2)
        self.assertIn(1, items)
        self.assertIn(2, items)



if __name__ == "__main__":
    unittest.main()
