from scenario import Canvas

def main():
    c = Canvas()
    for i in range(4):
        for j in range(6):
            c.draw_point("A", [i,j])
            print()

if __name__ == "__main__":
    main()