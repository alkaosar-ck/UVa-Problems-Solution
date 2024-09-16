def calculate_area_of_triangle(Ax, Ay, Bx, By, Cx, Cy):
    return abs(Ax*(By - Cy) + Bx*(Cy - Ay) + Cx*(Ay - By)) / 2

def main():
    N = int(input()) 
    for _ in range(N):

        Ax, Ay, Bx, By, Cx, Cy = map(float, input().split())

        area_ABC = calculate_area_of_triangle(Ax, Ay, Bx, By, Cx, Cy)
        
        area_PQR = area_ABC / 7
        
        print(round(area_PQR))

if __name__ == "__main__":
    main()
