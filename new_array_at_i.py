""" Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

Follow-up: what if you can't use division? """

# Brute Force
def list_product(lst):
    tmp_list = []
    for i in lst:
        tmp_var = 1
        for j in lst:
            if i != j:
                tmp_var *= j
        tmp_list.append(tmp_var) 
    return tmp_list     

# Multiply and divide
def multiply_divide(lst):
    product = 1
    tmp_list2 = []

    for i in lst:
        product *= i

    for i in lst:
        tmp_list2.append(int(product / i))

    return tmp_list2        

# No division version
def products(nums):
    # Generate prefix products
    prefix_products = []
    for num in nums:
        if prefix_products:
            prefix_products.append(prefix_products[-1] * num)
        else:
            prefix_products.append(num)

    # Generate suffix products
    suffix_products = []
    for num in reversed(nums):
        if suffix_products:
            suffix_products.append(suffix_products[-1] * num)
        else:
            suffix_products.append(num)
    suffix_products = list(reversed(suffix_products))

    # Generate result
    result = []
    for i in range(len(nums)):
        if i == 0:
            result.append(suffix_products[i + 1])
        elif i == len(nums) - 1:
            result.append(prefix_products[i - 1])
        else:
            result.append(prefix_products[i - 1] * suffix_products[i + 1])
    return result


cur_list = [1, 2, 3, 4, 5]
new_list = list_product(cur_list)
print(new_list)    

new_list2 = multiply_divide(cur_list)
print(new_list2)

new_list3 = products(cur_list)
print(new_list3)


