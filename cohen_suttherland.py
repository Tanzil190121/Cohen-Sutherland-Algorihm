import matplotlib.pyplot as plt

INSIDE = 0  
LEFT = 1    
RIGHT = 2  
BOTTOM = 4 
TOP = 8     

def compute_code(x, y, x_min, y_min, x_max, y_max):
    code = INSIDE
    if x < x_min:   
        code |= LEFT
    elif x > x_max:  
        code |= RIGHT
    if y < y_min:    
        code |= BOTTOM
    elif y > y_max:  
        code |= TOP
    return code

def cohen_sutherland_clip(x1, y1, x2, y2, x_min, y_min, x_max, y_max):
    code1 = compute_code(x1, y1, x_min, y_min, x_max, y_max)
    code2 = compute_code(x2, y2, x_min, y_min, x_max, y_max)
    accept = False

    while True:
        if code1 == 0 and code2 == 0:
            accept = True
            break
        elif code1 & code2 != 0:
            break
        else:
            x = y = 0
            if code1 != 0:
                code_out = code1
            else:
                code_out = code2

            if code_out & TOP:
                x = x1 + (x2 - x1) * (y_max - y1) / (y2 - y1)
                y = y_max
            elif code_out & BOTTOM:
                x = x1 + (x2 - x1) * (y_min - y1) / (y2 - y1)
                y = y_min
            elif code_out & RIGHT:
                y = y1 + (y2 - y1) * (x_max - x1) / (x2 - x1)
                x = x_max
            elif code_out & LEFT:
                y = y1 + (y2 - y1) * (x_min - x1) / (x2 - x1)
                x = x_min

            if code_out == code1:
                x1, y1 = x, y
                code1 = compute_code(x1, y1, x_min, y_min, x_max, y_max)
            else:
                x2, y2 = x, y
                code2 = compute_code(x2, y2, x_min, y_min, x_max, y_max)

    if accept:
        return (x1, y1, x2, y2)
    else:
        return None

def plot_line(x1, y1, x2, y2, clipped_line, x_min, y_min, x_max, y_max):
    fig, ax = plt.subplots()
    ax.set_xlim(x_min - 10, x_max + 10)
    ax.set_ylim(y_min - 10, y_max + 10)

   
    plt.plot([x1, x2], [y1, y2], color='blue', label='Original Line')

    
    plt.plot([x_min, x_max, x_max, x_min, x_min], [y_min, y_min, y_max, y_max, y_min], color='black', label='Clipping Window')

    
    if clipped_line:
        plt.plot([clipped_line[0], clipped_line[2]], [clipped_line[1], clipped_line[3]], color='red', label='Clipped Line')

    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title('Cohen-Sutherland Line Clipping Algorithm')
    plt.legend()
    plt.grid()
    plt.show()

x1, y1 = map(int, input("Enter the starting point (x1, y1): ").split())
x2, y2 = map(int, input("Enter the ending point (x2, y2): ").split())
x_min, y_min = map(int, input("Enter the bottom-left corner of the window (x_min, y_min): ").split())
x_max, y_max = map(int, input("Enter the top-right corner of the window (x_max, y_max): ").split())

clipped_line = cohen_sutherland_clip(x1, y1, x2, y2, x_min, y_min, x_max, y_max)
plot_line(x1, y1, x2, y2, clipped_line, x_min, y_min, x_max, y_max)
