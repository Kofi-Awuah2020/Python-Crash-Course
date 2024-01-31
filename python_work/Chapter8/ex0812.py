def sandwich_order(*sandwiches):
    """Function prints the order summary of sandwiches"""
    print("\nHere is your order: ")
    for sandwich_type in sandwiches:
        print(f"- {sandwich_type.title()} sandwich.")

sandwich_order('P & J')
sandwich_order('egg', 'tuna')
sandwich_order('cheese', 'chicken', 'bacon')