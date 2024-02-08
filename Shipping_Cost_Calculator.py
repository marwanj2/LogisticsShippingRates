# shipping cost calculator

## Input package weight and shipping rate
weight = float(input("Enter the package weight in kilograms: "))
rate = float(input("Enter the package rate in kilograms: "))

## calculate shipping cost
shipping_cost = weight * rate

## display the result
print(f"Shipping Cost: {shipping_cost} USD")
