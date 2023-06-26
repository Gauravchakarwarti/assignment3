#Write a Python function to sum all the numbers in a list.


#Sample List : (8, 2, 3, 0, 7)

#Expected Output : 20


#Explanation:


#Summation should like 8+2+3+0+7 = 20



#solution

def sum_numbers(numbers):
    return sum(numbers)
sample_list = [8,2,3,0,7]
result = sum_numbers(sample_list)
print(result)
