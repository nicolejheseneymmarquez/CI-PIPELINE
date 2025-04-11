class ItemManager:
    def __init__(self):
        self.items = {}
        self.next_id = 1

    def add_item(self, name):
        item_id = self.next_id
        self.items[item_id] = name
        self.next_id += 1
        return item_id

    def update_item(self, item_id, new_name):
        if item_id not in self.items:
            raise ValueError("Item ID not found.")
        self.items[item_id] = new_name

    def delete_item(self, item_id):
        if item_id not in self.items:
            raise ValueError("Item ID not found.")
        del self.items[item_id]

    def list_items(self):
        return self.items.copy()
