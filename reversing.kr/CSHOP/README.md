# CSHOP

1. 用 dnSpy disassemble **CSharp.exe**
2. 可以發現需要點擊一個大小為 0 的 button 才能將 flag 顯示出來
3. 其在 assign 值得時候順序是被打亂的，和顯示時並不相同
4. 可以根據每個 label 的位置，從左至右取得其 click 後應有的值，便可得到 flag

> 解到一半發現，button 的 `tabIndex` 是 0，根本就只要按一下 enter 或 space 其實就可以觸發 buttonClick，然後看到 flag 了⋯⋯