https://github.com/gpsgibb/Steganography

但是和常用的方法不同，直接改名无法正常解压，加密效果更加好，但是使用门槛略高；

于是乎，虽然不会batch, 但是至少还是会python, 那就自动生成python脚本好了，虽然结构丑陋了一点。

## 注意

copy \b [input.png] + [file] [output.png] 

顺序很重要。如果`+`前面的文件名是rar的话，图片不可预览，且有几率报错无法解压；需要保证 input pic 和 output pic 的后缀名一致，然后第一个处理的文件是同格式的文件。

[参考文章](https://owomoe.net/dev/168.html)

winrar解压读取文件ascii码的时候，会识别其独有的 Rar! 序列，因此可以把rar文件放到后面。就算是*分卷压缩*也可以正常使用winrar打开并且解压所有的文件。

需要注意的是，隐写之前最好重命名压缩文件为中文或者英文名称，防止名称编码不同导致隐写失败，具体原理未知。

## use

```
py hide.py
```

会生成一个bat文件

```
hide.bat
```

会生成以当前目录所有压缩文件为名称，以greeting2.png为输入图片的两个文件。

