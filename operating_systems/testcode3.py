class ListNode:
    # this is a node for a linked list to keep track of memory blocks
    def __init__(self, block=None, next_node=None):
        self.block = block  # this stores the memory block
        self.next = next_node  # this points to the next node in the list

class Block:
    # represents a block of memory
    def __init__(self, size_kb, num_pages, is_free=True):
        self.size_kb = size_kb  # size of the block in kilobytes
        self.num_pages = num_pages  # number of pages in the block
        self.is_free = is_free  # indicates if the block is free or not
        self.process_id = None  # id of the process using this block, None if free
        self.accessed = False  # flag to track if the block has been accessed

class MemoryManagement:
    # manages the allocation and deallocation of memory blocks
    def __init__(self):
        self.head = None  # head of the linked list of memory blocks
        self.initialize_blocks()  # initializes the memory blocks

    def initialize_blocks(self):
        # initializes the blocks based on predefined sizes and counts
        block_specs = [
            (1024, 256, 1), (512, 128, 2), (256, 64, 2),
            (128, 32, 4), (64, 16, 4), (32, 8, 8),
            (16, 4, 16), (8, 2, 32)
        ]
        for size_kb, num_pages, count in block_specs:
            for _ in range(count):
                self.add_block(Block(size_kb, num_pages))

    def add_block(self, block):
        # adds a block to the linked list
        new_node = ListNode(block=block, next_node=self.head)
        self.head = new_node

    def allocate_memory_first_fit(self, process_id, size_kb):
        # allocates memory using first fit strategy
        current = self.head
        while current:
            block = current.block
            if block.is_free and block.size_kb >= size_kb:
                block.is_free = False
                block.process_id = process_id
                block.accessed = True
                print("Allocated %dKB to Process %d in a block of %dKB." % (size_kb, process_id, block.size_kb))
                return
            current = current.next
        print("No suitable block found for Process %d, attempting page replacement..." % process_id)
        self.second_chance_page_replacement(process_id, size_kb)

    def deallocate_memory(self, process_id):
        # deallocates memory for a given process id
        current = self.head
        while current:
            block = current.block
            if block.process_id == process_id:
                block.is_free = True
                block.process_id = None
                block.accessed = False
                print("Deallocated memory for Process %d." % process_id)
                return
            current = current.next
        print("Process %d not found for deallocation." % process_id)

    def access_page(self, process_id):
        # marks a block as accessed for a given process id
        current = self.head
        while current:
            block = current.block
            if block.process_id == process_id and not block.is_free:
                block.accessed = True
                print("Accessed block for Process %d." % process_id)
                return
            current = current.next
        print("Access failed: Process %d not found." % process_id)

    def second_chance_page_replacement(self, process_id, size_kb):
        # attempts to replace a block using the second chance algorithm
        replaced = self.attempt_replace_non_accessed(process_id, size_kb)
        if not replaced:
            self.reset_accessed_flags()
            self.attempt_replace_non_accessed(process_id, size_kb, ignore_accessed=True)

    def attempt_replace_non_accessed(self, process_id, size_kb, ignore_accessed=False):
        # tries to find a block for replacement, respecting the accessed flag unless ignored
        current = self.head
        while current:
            block = current.block
            if not block.is_free and ((not block.accessed) or ignore_accessed) and block.size_kb >= size_kb:
                print("Replacing block for Process %d with Process %d." % (block.process_id, process_id))
                self.deallocate_memory(block.process_id)
                self.allocate_memory_first_fit(process_id, size_kb)
                return True
            current = current.next
        if not ignore_accessed:
            print("No suitable block found for replacement. All blocks were accessed recently.")
        return False

    def reset_accessed_flags(self):
        # resets the accessed flag for all blocks
        current = self.head
        while current:
            if not current.block.is_free:
                current.block.accessed = False
            current = current.next

if __name__ == "__main__":
    mm = MemoryManagement()
    mm.allocate_memory_first_fit(1, 100)
    mm.allocate_memory_first_fit(2, 500)
    mm.access_page(2)
    mm.allocate_memory_first_fit(3, 500)
    mm.allocate_memory_first_fit(4, 500)
    mm.allocate_memory_first_fit(5, 500)
    mm.allocate_memory_first_fit(6, 500)

