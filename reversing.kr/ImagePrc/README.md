# ImagePrc

執行 exe 會有一個類似小畫家的視窗和 `Check` 的按鈕，按完 `Check` 後，便會跳出顯示 `Wrong` 的視窗。  
使用 `ida pro` decompile 後，在 `WinMain` 的 function 中有 `WndClass.lpfnWndProc = sub_401130;`，即在視窗中所有的行為都在 `sub_401130` 定義。當按下 `check` 的按鈕，`sub_401130` 中定義會從 resource 中 load 一個 bitmap 的檔案，且跟現有視窗中的內容比較，若有不同處，便會跳出 `Wrong` 的視窗。  
利用 `Resource Hacker` 將此 resource 存出，然而，bitmap 的長寬並不是 hard-coded 的，從 assembly code 可以直接
```assembly
.text:0040131C 89 44 24 38      mov     [esp+98h+bmi.bmiHeader.biHeight], eax
.text:00401320 50               push    eax
.text:00401321 A1 F4 84 40 00   mov     eax, hbm
.text:00401326 89 4C 24 38      mov     [esp+9Ch+bmi.bmiHeader.biWidth], ecx
```
在 `0x40131C, 0x401326` 下 **breakpoint**，其相應的 `eax, ecx` 即為 bitmap 的長寬。  
知道長寬後，利用 python PIL 的 Image，將照片還原出來，直接將照片還原出來可以發現其上下顛倒，利用 transpose 將其轉換回來，便可以取得 flag。

