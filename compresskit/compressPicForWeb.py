"""将图片文件压缩到300kb以下
如果有工具的话就好了"""

"""
最理想的方式是把这个东西打包成一个便携版的exe，或者写相关的ps1文件也行；
在main里面可以设置preset_quality的值，调整压缩效果；

理论上应该可以压缩常见格式的图片，比如jpg, png
https://www.codecademy.com/resources/docs/pillow/image/convert

convert mode 可以调整，RGB算是比较合适的
"""

from PIL import Image
import os

def compress_image_fast(pic_path, output_folder, target_format='JPEG', com_quality=50):
    # Open the image file
    img = Image.open(pic_path)

    # Convert to RGB (necessary for JPG conversion)
    img = img.convert("RGB")
    
    # Create output filename with new extension
    base_name = os.path.basename(pic_path)
    new_name = os.path.splitext(base_name)[0] + '.jpg'
    output_path = os.path.join(output_folder, new_name)
    
    # Save as JPEG with the specified quality
    img.save(output_path, target_format, quality=com_quality, optimize=True)

    print(f"Converted and compressed {pic_path} to {output_path}")


def main():
    preset_quality = 50 
    t_path = os.path.abspath("./")
    
    output_folder = t_path+"/compressed"
    os.makedirs(output_folder, exist_ok=True)
    
    dir_ls = os.listdir(t_path)
    for f in dir_ls:
        # if f.lower().endswith('.png'):  # Check if file is a PNG
        #     compress_image_fast(pic_path=os.path.join(t_path, f), output_folder=output_folder, com_quality=preset_quality)
        compress_image_fast(pic_path=os.path.join(t_path, f), output_folder=output_folder, com_quality=preset_quality)

if __name__ == "__main__":
    print("warning: Now compress all png files in the current directory!")
    main()


