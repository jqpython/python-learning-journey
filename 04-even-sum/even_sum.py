def even_numbers(numbers):
    count = 0
    for num in numbers:
        if num % 2 == 0:
            count = count + num
    print("Sum of the even numbers are:", count)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2]

even_numbers(numbers)
