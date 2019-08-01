classroom_seating = [
  [None, "Pumpkin", None, None],
  ["Socks", None, "Mimi", None],
  ["Gismo", "Shadow", None, None],
  ["Smokey","Toast","Pacha","Mau"]
]

#Question 1:
def find_free_seats(classroom):
    for row_index, row in enumerate(classroom):
        for col_index, column in enumerate(row):
            # print(f'Row {row_index} - seat {col_index}.')
            # print(column)
            if not column:
                # print(column)
                print(f'Row {row_index+1} seat {col_index+1} is free.')

        # Row 1 seat 1 is free.



find_free_seats(classroom_seating)
