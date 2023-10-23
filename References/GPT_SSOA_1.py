import random
import matplotlib.pyplot as plt

# Define the number of suppliers and products
num_suppliers = 5
num_products = 1

# Generate or load data (supplier capacities, product costs, demand, etc.)
supplier_capacities = [random.randint(100, 500) for _ in range(num_suppliers)]
product_costs = [random.uniform(10, 50) for _ in range(num_products)]
demand = [random.randint(20, 100) for _ in range(num_products)]

# Initialize supplier agents
class SupplierAgent:
    def __init__(self, capacity):
        self.capacity = capacity

    def allocate_orders(self, demand):
        # Implement a strategy for order allocation
        # Example: Allocate orders to products randomly within capacity limits
        orders = [min(random.randint(0, self.capacity), demand[i]) for i in range(num_products)]
        return orders

# Create supplier agents
suppliers = [SupplierAgent(capacity) for capacity in supplier_capacities]

# Set the number of rounds (order allocation decisions)
num_rounds = 50

order_allocations = []  # Store order allocations for visualization

# Run the simulation (order allocation)
for round in range(num_rounds):
    total_cost = 0
    orders = [supplier.allocate_orders(demand) for supplier in suppliers]
    order_allocations.append(orders)
    
    # Calculate the cost based on product costs and orders
    for i in range(num_suppliers):
        for j in range(num_products):
            total_cost += product_costs[j] * orders[i][j]
    
    # Update supplier information and strategies (not implemented in this example)
    
    # Display results for each round (total cost, order allocation)
    print(f"Round {round+1} - Total Cost: {total_cost}")
    print("Order Allocation:")
    for i in range(num_suppliers):
        print(f"Supplier {i+1}: {orders[i]}")

# Create a visualization of order allocations over rounds
plt.figure(figsize=(10, 6))
for i in range(num_suppliers):
    allocations = [orders[i] for orders in order_allocations]
    plt.scatter(range(1, num_rounds + 1), allocations, label=f'Supplier {i + 1}')

plt.xlabel('Rounds')
plt.ylabel('Order Allocation')
plt.title('Order Allocation Over Rounds')
plt.legend()
plt.grid(True)
plt.show()

# Analyze results, make decisions based on objectives and constraints
# Implement further visualization or reporting as needed
