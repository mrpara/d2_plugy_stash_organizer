class Page:
    # Page class for ordering items in physical space
    def __init__(self):
        self.spaces = [[0] * 10 for _ in range(10)]  # Stash pages are 10x10
        self.items = []

    def is_collision(self, x_position, x_size, y_position, y_size):
        # Check if an item with size (x_size, y_size) inserted at position (x_position, y_position) collides with
        # ant existing item on the page
        for x in range(x_size):
            for y in range(y_size):
                if x_position + x > 9 or y_position + y > 9 or\
                        self.spaces[x_position + x][y_position + y] > 0:
                    return True
        return False

    def allocate(self, x_position, x_size, y_position, y_size):
        # Allocate the space for an item size (x_size, y_size) inserted at position (x_position, y_position)
        for x in range(x_size):
            for y in range(y_size):
                self.spaces[x_position + x][y_position + y] += 1

    def insert_item(self, item):
        # Attempt to insert an item into the page. Go over each position in the page until either we find a position
        # in which inserting the item will not collide with any existing items, in which case we allocate the space for
        # the item as well as modify the item data to reflect the new location, or we run out of spaces.
        # Return whether the item was inserted or not.
        allocated = False
        for x in range(10):
            for y in range(10):
                if not allocated and not self.is_collision(x, item.x_size, y, item.y_size):
                    item.set_position(x, y)
                    self.items.append(item)
                    self.allocate(x, item.x_size, y, item.y_size)
                    allocated = True
        return allocated

    def num_items(self):
        return len(self.items)