import time

def typing_test():
    text = input()
    print("Type this text as fast as you can:")
    print(text)
    
    input("Press Enter to start...")
    
    start_time = time.time()
    user_text = input()
    end_time = time.time()
    
    if user_text == text:
        time_taken = end_time - start_time
        wpm = len(text.split()) / time_taken * 60
        print("Congratulations! You typed the text correctly!")
        print("Time taken: {:.2f} seconds".format(time_taken))
        print("Your typing speed: {:.2f} WPM".format(wpm))
    else:
        print("Sorry, you typed the text incorrectly. Please try again.")

typing_test()
