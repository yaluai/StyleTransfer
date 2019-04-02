from PIL import Image
import glob

base_list = [];
edit_list = [];
filename_list = [];
print('...........');
for filename in glob.glob('demo/*.jpg'):
    im = Image.open(filename);
    base_list.append(im);
    for filename2 in glob.glob('output1/*.jpg'):
        if filename[5:] == filename2[8:-4]:
            im2 = Image.open(filename2);
            edit_list.append(im2);
            filename_list.append(filename2[8:-4]);



for i in range(len(edit_list)):
    width, height = edit_list[i].size;
    base_rgb = base_list[i].convert('RGB');
    edit_rgb = edit_list[i].convert('RGB');
    img = Image.new('RGB', (width, height), "white")
    pixels = img.load();
    for x in range(width):
        for y in range(height):
            r1,g1,b1 = base_rgb.getpixel((x,y));
            r2,g2,b2 = edit_rgb.getpixel((x,y));

            if (abs(r1-r2) <= 15) and (abs(g1-g2) <= 15) and (abs(b1-b2) <= 15):
                pixels[x,y] = (r1,g1,b1);
    img.save('demo/output2/' + filename_list[i], 'JPEG');
print('...........');







