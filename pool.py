from ball import Ball

def numinput(prompt):
    while True:
        try:
            num = float(input(prompt))
            if num != 0:
                return num
            else:
                print("Please enter a non-zero number.")
        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    u = numinput("Enter the x velocity of the ball: ")
    v = numinput("Enter the y velocity of the ball: ")

    ball = Ball(u, v)

    while ball.status == "moving":
        ball.update()
        ball.locate()

    print("Final status:", ball.status)
