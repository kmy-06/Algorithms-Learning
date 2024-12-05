def bubble_sort(scores, numbers):
  swapped = True

  while swapped:
    swapped = False
    for i in range(0, len(scores)-1):
      if scores[1] < scores[i+1]:
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
