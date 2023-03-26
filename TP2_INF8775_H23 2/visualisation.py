import sys
from PIL import Image, ImageDraw
from algo_glouton import TSP as TSP_GLOUTON
from graphe import TSP as TSP_MST
from algo_dynamique import TSP as TSP_DYN

def get_coords(file_name):  
    f = open(file_name, "r")
    coords = []
    N = int(f.readline())
    print(f"N : {N} ")

    for i in range(N):
        line = f.readline()
        coords.append(tuple(int(coord) for coord in line.split("  ")))
    return coords

# Create visual support 
def draw_points(path, filename):
    img = Image.new('RGB', (2000+2 , 2000+2), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    
    for i, coord in enumerate(path):
        # print point
        x1, y1 = coord
        # create Point
        draw.point((x1 + 1, y1 + 1), fill=(0, 0, 0))
        # print path to next
        if i < len(path)-1:
            x2, y2 = path[i+1]
            # create line
            draw.line((x1+1, y1+1, x2+1, y2+1), fill=(0, 0, 0), width=1)

    # Save Image
    img.save(f"{filename}.png")
    
if __name__ == "__main__":
    file_name = "N15_"
    for i in range(5):
        file= file_name + str(i)
        draw_points(TSP_GLOUTON(get_coords(file)), file+"_GLOUTON")
    file_name = "N50_"
    for j in range(5):
        file= file_name + str(j)
        draw_points(TSP_MST(get_coords(file)), file+"_TSP")
    """
    file_name = "N15_"
    for k in range(1):
        file= file_name + str(j)
        draw_points(TSP_DYN(get_coords(file)), file+"_DYNAMIQUE")
    """    
    