def swap_variables(var1, var2):
    print(f"Before swapping: var1 = {var1}, var2 = {var2}")

    # Swapping the values
    var1, var2 = var2, var1

    print(f"After swapping: var1 = {var1}, var2 = {var2}")

# Example usage
if __name__ == "__main__":
    # You can replace these values with your own
    variable1 = 5
    variable2 = 10

    swap_variables(variable1, variable2)
