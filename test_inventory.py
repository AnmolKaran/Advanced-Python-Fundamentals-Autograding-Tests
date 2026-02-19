import pytest
# Assumes the student's file is named 'hero_inventory.py'
from hero_inventory import search_messy_backpack, search_shop, equip_item

class TestHerosInventory:

    # 1. Testing Linear Search
    def test_search_messy_backpack_found(self):
        backpack = ["Rope", "Torch", "Sword", "Map", "Apple"]
        result = search_messy_backpack(backpack, "Sword")
        assert result == 2, f"Expected index 2 for 'Sword', but got {result}"

    def test_search_messy_backpack_missing(self):
        backpack = ["Rope", "Torch", "Sword"]
        result = search_messy_backpack(backpack, "Laser Gun")
        assert result == -1, f"Expected -1 for missing item, but got {result}"

    # 2. Testing Binary Search
    def test_search_shop_found(self):
        shop = ["Armor", "Boots", "Helmet", "Potion", "Shield", "Wand"]
        result = search_shop(shop, "Potion")
        assert result == 3, f"Expected index 3 for 'Potion', but got {result}"

    def test_search_shop_found_boundaries(self):
        shop = ["Armor", "Boots", "Helmet", "Potion", "Shield", "Wand"]
        assert search_shop(shop, "Armor") == 0, "Failed to find the first item in the list."
        assert search_shop(shop, "Wand") == 5, "Failed to find the last item in the list."

    def test_search_shop_missing(self):
        shop = ["Armor", "Boots", "Helmet"]
        result = search_shop(shop, "Pizza")
        assert result == -1, f"Expected -1 for missing item, but got {result}"

    # 3. Testing Equip Item (The Swap Logic)
    def test_equip_item_swaps_correctly(self):
        backpack = ["Rope", "Torch", "Sword", "Map"]
        equip_item(backpack, "Map")
        
        assert backpack[0] == "Map", "The item to equip was not found at index 0."
        assert backpack[3] == "Rope", "The old item at index 0 was not swapped correctly to the target's old position."
        assert len(backpack) == 4, "The size of the backpack should not change."

    def test_equip_item_missing_does_nothing(self):

        backpack = ["Rope", "Torch", "Sword"]
        original_copy = backpack.copy()
        
        equip_item(backpack, "Invisibility Cloak")
        
        # If the item isn't there, the list should look exactly the same
        assert backpack == original_copy, (
            "Logic Error: The backpack changed even though the item wasn't found. "
            "Check your if-statement condition! Are you checking if the ITEM is -1 or the INDEX is -1?"
        )
