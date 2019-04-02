from PIL import Image
import glob

base_list = [];
edit_list = [];
tran_list = [];
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
            break;
    for filename3 in glob.glob('demo/output3/*.jpg'):
        if filename[5:] == filename3[13:]:
            im3 = Image.open(filename3);
            tran_list.append(im3);
            break;
for i in range(len(edit_list)):
    width, height = edit_list[i].size;
    base_rgb = base_list[i].convert('RGB');
    edit_rgb = edit_list[i].convert('RGB');
    tran_rgb = tran_list[i].convert('RGB');
    img = Image.new('RGB', (width, height), "white")
    pixels = img.load();
    for x in range(width):
        for y in range(height):
            r1,g1,b1 = base_rgb.getpixel((x,y));
            r2,g2,b2 = edit_rgb.getpixel((x,y));
            r3,g3,b3 = tran_rgb.getpixel((x,y));

            if (abs(r1-r2) <= 20) and (abs(g1-g2) <= 20) and (abs(b1-b2) <= 20):
                pixels[x,y] = (r3,g3,b3);
            else:
                pixels[x,y] = (r1,g1,b1);

    img.save('demo/output4/' + filename_list[i], 'JPEG');
print('...........');



