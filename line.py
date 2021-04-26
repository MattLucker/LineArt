from PIL import Image, ImageDraw

def main():
    # Get an image
    base = Image.open("white.jpg").convert("RGB")

    # Need to adjust manually based on the length of the line.
    # TODO: figure that out.
    out = Image.new("RGB", (1200,1000), (0, 0, 0))

    # Get a drawing context
    d = ImageDraw.Draw(out)

    # Draw text, half opacity
    point1 = [800,200]
    point2 = [800,200]

    prime = 0
    length = 50000 # Adjust for line length
    for i in range(length):
        if i%10000==0:
            print(int(i/length*100),"/ 100")
        prime += isPrime(i)
        pair = []
        if prime%4==0:
            point2[0] += 1
        elif prime%4==1:
            point2[1] += 1
        elif prime%4==2:
            point2[0] -= 1
        elif prime%4==3:
            point2[1] -= 1

        line = [point1[0],point1[1],point2[0],point2[1]]
        d.line(line, fill=(0,255,255,128), width = 1, ) #0,255,255,128
        point1[0] = point2[0]
        point1[1] = point2[1]


    out.show()
    out.save('teal_line.png', format = 'PNG', optimize = True)


def isPrime(num):
    if num > 1:
        for i in range(2, int(num/2)+1):
            if (num % i) == 0:
                return 0
        else:
            return 1
    else:
        return 0

main()
