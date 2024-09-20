class MemoryBlock:
    def __init__(self, start_address, size, next_block=None):
        self.start_address = start_address
        self.size = size
        self.process_id = None  # No process allocated initially
        self.accessed = False
        self.next = next_block  # Pointer to the next memory block

class BuddySystem:
    def __init__(self, total_memory):
        self.head = MemoryBlock(0, total_memory)  # Start with a single large block
        self.total_memory = total_memory
        self.free_memory = total_memory

    def allocate_memory(self, process_id, size):
        # Simplified allocation: first-fit approach
        prev, current = None, self.head
        while current:
            if current.process_id is None and current.size >= size:
                if current.size > size:  # Split the block if it's larger than requested
                    new_block = MemoryBlock(current.start_address + size, current.size - size, current.next)
                    current.size = size
                    current.next = new_block
                current.process_id = process_id
                self.free_memory -= size
                print(f"Memory allocated: Process {process_id}, Size {size}KB")
                return
            prev, current = current, current.next
        print("Allocation failed: Insufficient memory.")

    def deallocate_memory(self, process_id):
        # Find the block by process ID and mark it as free
        current = self.head
        while current:
            if current.process_id == process_id:
                self.free_memory += current.size
                current.process_id = None
                print(f"Memory deallocated: Process {process_id}")
                return
            current = current.next
        print(f"Deallocation failed: Process {process_id} not found.")

    def print_memory_status(self):
        print(f"Total memory: {self.total_memory}KB, Free memory: {self.free_memory}KB")

class ClockAlgorithm:
    def __init__(self, buddy_system):
        self.buddy_system = buddy_system
        self.clock_hand = self.buddy_system.head  # Start the clock at the head of the memory blocks

    def run_clock(self):
        # Simulate the clock running, checking each block
        while True:  # Loop to simulate continuous operation
            if self.clock_hand.process_id and not self.clock_hand.accessed:
                # This block has not been accessed since the last check and is allocated, so deallocate it
                print(f"Clock replacing process {self.clock_hand.process_id}")
                self.buddy_system.deallocate_memory(self.clock_hand.process_id)
            elif self.clock_hand.process_id:
                # Mark as not accessed for the next round
                self.clock_hand.accessed = False

            # Move the clock hand forward
            if self.clock_hand.next:
                self.clock_hand = self.clock_hand.next
            else:
                self.clock_hand = self.buddy_system.head  # Loop back to the start

# Example usage
if __name__ == "__main__":
    bs = BuddySystem(1024)  # Initialize the Buddy System with 1MB of memory
    clock = ClockAlgorithm(bs)  # Initialize the Clock Algorithm with the Buddy System

    bs.allocate_memory(1, 256)  # Allocate 256KB for Process 1
    bs.allocate_memory(2, 256)  # Allocate 256KB for Process 2
    # Simulate accessing Process 1's memory block
    for block in [bs.head, bs.head.next, bs.head.next.next, bs.head.next.next.next]:
        if block and block.process_id == 1:
            block.accessed = True
            break

    clock.run_clock()  # Run the clock algorithm once for demonstration

    bs.print_memory_status()  # Print the current memory status
