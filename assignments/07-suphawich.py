open_parenthesis = ['(', '{', '[']
close_parenthesis = [')', '}', ']']

# <-- use stack
def check_parenthesis_stack(arr, stack = []):
    if (len(arr) == 0):
        if (len(stack) != 0):
            return 'NOT OK'
        return 'OK'
    
    value = arr[0]
    if (value in open_parenthesis):
        stack.append(value)
    elif (value in close_parenthesis and close_parenthesis.index(value) == open_parenthesis.index(stack[-1])):
        stack.pop()
    return check_parenthesis_stack(arr[1:], stack)

data = "{[[]]{()}}"
# data = "[{}"
print(f"Data: {data}")
data = list(data)

result = check_parenthesis_stack(data)
print(f"Result: {result}")