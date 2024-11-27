def bodlai_daw(a, i, j):
    if(i < 0 or j >= len(a)): # check kortesi jodi ultapalta indices dey
        return("indices thik nai")
    else:
        a[i], a[j] = a[j], a[i]  # way to swap in python

a = [1,2,3,4,5]
first_pos,second_pos = 0,3 # indices, kothai swap hobe

bodlai_daw(a, first_pos, second_pos)

print(a)