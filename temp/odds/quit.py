
while True:
    try:
        input= raw_input('press any key to quit:')
        if input in 'abcd': 
            raise KeyboardInterrupt
        break
    except ValueError:
        print ('Oops! Try again')
