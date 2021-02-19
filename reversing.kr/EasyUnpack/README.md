# EasyUnpack

題目要找 OEP，直接 x32dbg 跑，發現他解壓縮完就有一個 jmp，且其直接跳到即 OEP，且此 jmp 之後全部皆為 `00`。
