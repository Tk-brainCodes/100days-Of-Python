test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))

coverage = 5

def paint_calc(height, width, cover):
    number_of_paint = (height * width) % cover
    rounded_up = round(number_of_paint)
    print(f"You need to buy {rounded_up} paints")



paint_calc(height=test_h, width=test_w, cover=coverage)