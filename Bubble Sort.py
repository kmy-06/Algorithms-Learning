# Bubble sort is suitable for 10 floating point values or less than 1000 items; other good sorting include: insertionsort, selectionsort. (counting sort does not work.)
# Bubble sort has a decreasing range of interest: the algorithm keeps track of the range of interest and restricts that range over time to reduce the number of items considered.


def bubble_sort(scores, numbers):
  swapped = True

  while swapped:
    swapped = False # assume we cannot find a pair to swap
    for i in range(0, len(scores)-1):
      if scores[i] < scores[i+1]: # change the sign to >, if you want decresing sorting
        temp = scores[i]
        scores[i] = scores[i+1]
        scores[i+1] = temp
        temp = numbers[i]
        numbers[i] = numbers[i+1]
        numbers[i+1] = temp
        swapped = True
        
scores = [60, 50, 69, 40, 53, 66]

number_of_scores = len(scores)
solution_numbers = list(range(number_of_scores))

bubble_sort(scores,solution_numbers)

print(scores)
print(solution_numbers)

# [69, 66, 60, 53, 50, 40]
# [2, 5, 0, 4, 1, 3]


# 1000 integers use: heapsort, quicksort, mergesort, quicksort(best)
# 100000 integers with values between 0 and 1000 use: pigeonhole sort, countingsort(best)
# 100000 integers with values between 0 and 1 billion use: ( pigeonhole sort, bucketsort. ) <- they are generally for large integers. E.g 1 million integers with uniform distriution
