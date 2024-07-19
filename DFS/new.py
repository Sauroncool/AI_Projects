def function(input_string):
    # Split the input string by commas to get the individual elements
    elements = input_string.split(',')
    # Generate the desired output format
    output = [(name, 10) for name in elements]
    # Print the output
    print(*output, sep=', ')
    return

# Example usage
input_data = "H,J,H5"
function(input_data)

