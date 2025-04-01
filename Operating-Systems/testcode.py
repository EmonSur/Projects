# Define a ListNode class to represent each node in a linked list, which helps manage memory blocks.
class ListNode:
    def __init__(self, start_address, size):
        self.start_address = start_address  # Start address of the memory block
        self.size = size  # Size of the memory block
        self.next_node = None  # Pointer to the next node in the linked list

# Base class for memory management that provides an interface and common attributes for memory management strategies.
class MemoryManagement:
    def __init__(self, memory_size):
        self.memory_size = memory_size  # Total size of memory being managed
        self.free_memory_list = ListNode(0, memory_size)  # Initialize the list of free memory blocks
        self.total_free_memory = memory_size  # Track the total free memory available

    # Placeholder methods that will be implemented by subclasses.
    def allocate_memory(self, process_id, requested_size):
        pass

    def deallocate_memory(self, process_id, start_address, size):
        pass

    def update_free_memory_list_after_allocation(self, start_address, size):
        pass

    def update_free_memory_list_after_deallocation(self, start_address, size):
        pass

# Implements the Buddy System algorithm for memory management, inheriting from MemoryManagement.
class BuddySystem(MemoryManagement):
    def __init__(self, memory_size, page_size):
        super().__init__(memory_size)
        self.page_size = page_size  # Size of a single page in KB
        # Predefined memory block structure
        self.block_sizes = [2 * page_size, 4 * page_size, 8 * page_size, 16 * page_size, 32 * page_size, 64 * page_size, 128 * page_size]  # Block sizes in KB
        self.block_count = [16, 16, 8, 4, 2, 1, 1]  # Corresponding counts for each block size
        self.blocks = self.initialize_blocks()
        self.allocations = {}  # Track allocations by process ID

    def initialize_blocks(self):
        blocks = {}
        address = 0
        for size, count in zip(self.block_sizes, self.block_count):
            blocks[size] = [{'start_address': address + i * size, 'used': False} for i in range(count)]
            address += size * count
        return blocks

    def find_suitable_block(self, requested_size):
        for size, block_list in self.blocks.items():
            if size >= requested_size:
                for block in block_list:
                    if not block['used']:
                        return block, size
        return None, None

    def allocate_memory(self, process_id, requested_size):
        block, block_size = self.find_suitable_block(requested_size)
        if block:
            block['used'] = True
            self.allocations[process_id] = block
            self.total_free_memory -= block_size
            print(f"Allocated {requested_size} KB for Process ID {process_id} in a block of {block_size // self.page_size} pages.")
        else:
            print("Allocation failed: No suitable block available.")

    def deallocate_memory(self, process_id):
        if process_id in self.allocations:
            block = self.allocations.pop(process_id)
            block_size = [size for size in self.block_sizes if block in self.blocks[size]][0]
            block['used'] = False
            self.total_free_memory += block_size
            print(f"Deallocated memory for Process ID {process_id}.")
        else:
            print(f"No memory to deallocate for Process ID {process_id}.")

class Page:
    def __init__(self, process_id=None):
        self.process_id = process_id
        self.reference_bit = 0

class MemoryBlock:
    def __init__(self, start_address, size, used=False):
        self.start_address = start_address
        self.size = size
        self.used = used

class ExtendedBuddySystem:
    def __init__(self, memory_size, page_size):
        self.memory_size = memory_size
        self.page_size = page_size
        self.total_free_memory = memory_size
        self.blocks = []
        self.initialize_blocks()
        self.allocations = {}  # Maps process_id to MemoryBlock

    def initialize_blocks(self):
        # Initialize based on the predefined structure
        block_sizes = [2, 4, 8, 16, 32, 64, 128]  # Sizes in number of pages
        block_count = [16, 16, 8, 4, 2, 1, 1]  # Count of each block size
        address = 0
        for size, count in zip(block_sizes, block_count):
            for _ in range(count):
                self.blocks.append(MemoryBlock(address, size * self.page_size))
                address += size * self.page_size

    def find_suitable_block(self, requested_size):
        for block in self.blocks:
            if not block.used and block.size >= requested_size:
                return block
        return None

    def allocate_memory(self, process_id, requested_size):
        block = self.find_suitable_block(requested_size)
        if block:
            block.used = True
            self.allocations[process_id] = block
            self.total_free_memory -= block.size
            print(f"Allocated {requested_size} KB for Process ID {process_id} at address {block.start_address}")
        else:
            print("Allocation failed: No suitable block available.")

    def deallocate_memory(self, process_id):
        if process_id in self.allocations:
            block = self.allocations.pop(process_id)
            block.used = False
            self.total_free_memory += block.size
            print(f"Deallocated memory for Process ID {process_id}.")
        else:
            print(f"No memory to deallocate for Process ID {process_id}.")

    # Simplified for demonstration; real page replacement logic would be more complex
    def page_replacement(self, process_id, requested_size):
        # Example replacement strategy: deallocate the first allocated block
        if self.allocations:
            old_process_id, block = next(iter(self.allocations.items()))
            self.deallocate_memory(old_process_id)
            self.allocate_memory(process_id, requested_size)
        else:
            print("Page replacement failed: No pages to replace.")




# Represents an extension of MemoryManagement for implementing the Clock Algorithm for page replacement.
class ClockAlgorithm(MemoryManagement):
    def __init__(self, memory_size):
        super().__init__(memory_size)
        self.clock_hand_1 = 0  # Initialize the first clock hand
        self.clock_hand_2 = 0  # Initialize the second clock hand

    # Placeholder for the Clock algorithm implementation.
    def page_replacement(self):
        pass

    # Method to update the positions of the clock hands.
    def update_clock_hands(self):
        pass

# Function to simulate memory management using the specified MemoryManagement instance and a sequence of requests.
def simulate_memory_management(memory_manager, requests, total_memory_blocks):
    print("Initial memory status:")
    print(f"Total memory size: {memory_manager.memory_size} KB")
    print(f"Free memory blocks: {memory_manager.total_free_memory} KB")
    print()

    for request in requests:
        operation = request[0]
        process_id = request[1]

        # For allocate requests, which include a size
        if operation == "allocate":
            requested_size = request[2]  # Get the requested size for allocation
            print(f"Processing {operation} request for Process ID {process_id}, Size: {requested_size} KB")
            memory_manager.allocate_memory(process_id, requested_size)
        elif operation == "deallocate":
            # For deallocate requests, which do not include a size
            print(f"Processing {operation} request for Process ID {process_id}")
            memory_manager.deallocate_memory(process_id)
        elif operation == "replacement":
            # Handle other types of operations as needed
            memory_manager.page_replacement()

        print("Updated memory status:")
        print(f"Free memory blocks: {memory_manager.total_free_memory} KB")
        print()

    print("Final memory status:")
    free_memory_blocks = memory_manager.total_free_memory // memory_manager.min_block_size
    print(f"Free memory blocks: {free_memory_blocks}")

    print("Final memory fragmentation:")
    fragmentation_percentage = ((total_memory_blocks - free_memory_blocks) / total_memory_blocks) * 100
    print(f"Fragmentation: {fragmentation_percentage}%")


if __name__ == "__main__":
    system = ExtendedBuddySystem(4096, 4)  # 4MB memory, 4KB per page

    # Attempt to fill up the memory with several allocations
    system.allocate_memory(1, 512)  # 512KB
    system.allocate_memory(2, 1024) # 1024KB
    system.allocate_memory(3, 512)  # 512KB
    # This allocation should push the system to near or full capacity
    system.allocate_memory(4, 2048) # 2048KB

    # Triggering page replacement by trying to allocate more memory
    system.page_replacement(5, 256) # 256KB, should trigger replacement
    system.deallocate_memory(5)

    print(f"\nFinal memory status:")
    print(f"Total free memory: {system.total_free_memory} KB")



