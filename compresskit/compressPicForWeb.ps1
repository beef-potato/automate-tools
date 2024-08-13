$virtueFolder = "D:\code\python\virtues"

$selectedFile = "D:\code\python\virtues\galPicRestore\Scripts\activate.ps1"
# 自定义的虚拟环境，里面至少需要pillow


Write-Output "激活虚拟环境: $selectedFile"
Invoke-Expression ". `"$selectedFile`""


py ./compressPicForWeb.py


