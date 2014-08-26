
while True:
    try:
        raw_input('press any key to quit:')
        break
    except ValueError:
        print ('Oops! Try again')
