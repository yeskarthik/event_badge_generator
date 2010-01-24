import os
from PIL import Image
PAGE_SIZES = {
                "A3":(11.7,16.5),
                "A4":(8.3,11.7)
            }

number_of_rows_in_page = 4
number_of_columns_in_page = 2
selected_paper = "A3"
page_size_in_pix =  [int(data*72) for data in PAGE_SIZES[selected_paper]]
box_coords = []
new_image = Image.new("RGB",page_size_in_pix,color=(255,255,255))
tile_width = page_size_in_pix[0]/number_of_columns_in_page
tile_height = page_size_in_pix[1]/number_of_rows_in_page

for r in range(number_of_rows_in_page):
    for c in range(number_of_columns_in_page):
        y = r * tile_height
        x = c * tile_width
        box_coords.append((x,y))

count = 0
for f in os.listdir(os.curdir + "\\sample"):
    i = Image.open("sample\\"+ f)
    r_i = i.resize((tile_width,tile_height))
    new_image.paste(r_i,box_coords[count])
    count+=1
new_image.save("tile.jpg")

