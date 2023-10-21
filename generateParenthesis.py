def generateParenthesis(n):
    if n == 0:
        return []

    results = []
    stack = [("", 0, 0)]  # (current_string, open_count, close_count)

    while stack:
        current_str, open_count, close_count = stack.pop()

        if open_count == n and close_count == n:
            results.append(current_str)
        else:
            if open_count < n:
                stack.append((current_str + "(", open_count + 1, close_count))

            if close_count < open_count:
                stack.append((current_str + ")", open_count, close_count + 1))

    return results

# Test cases
print(generateParenthesis(3))
print(generateParenthesis(1))
