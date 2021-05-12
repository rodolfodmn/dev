from screen import Screen

def play():
    print('deu play')
    screen = Screen(600, 600, (0, 0, 0), 40, (255, 255, 255))
    screen.start()

if __name__ == "__main__":
    play()
