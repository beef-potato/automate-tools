import os

bat_name = "hide.bat"
input_pic = "greeting2.png"


def get_file():
    compressed_file_ls = [f for f in os.listdir() if f.endswith("zip") or f.endswith("rar")]
    # print(compressed_file_ls)
    return compressed_file_ls

def create_command(compress_ls):
    with open(bat_name, "w", encoding="utf-8") as f:
        for comf in compress_ls:
            out_name = os.path.basename(comf)+"pic"+".png"
            temp_line = fr"copy /b  {input_pic} + {comf} {out_name}"
            f.write(temp_line)
            f.write("\n")



create_command(compress_ls=get_file())

# 目前代码的问题是，大文件处理后名称只有kb级别的数据；日文copy会有中文乱码；所以需要事先改名；




