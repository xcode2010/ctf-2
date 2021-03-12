# Music Player

根據提示需要使 bypass 所有 `1-minute-check-routine` 才能得到 flag。  
用 **detect it easy** 可以發現是用 `Visual Basic` 寫的，可以利用 **VB Decompiler** decompile，可以發現 `TMR_POS_Timer_4044C0` 的函式，可以看到有關於 ***60000*** 的判斷，直接將 `jl (2 bytes)` patch 成  `jmp (1 byte)`（將缺少的 1 byte 補為 `nop`），重新執行卻會發現在播到一分鐘時，跳出 
```
Run-time error: '380':
Invalid property value
```
用 x32dbg attach 上去 debug 可以發現在 `0x4046AB` 有一個 `jge` 此時 jump 不會成立，而使其跳 error，因此，同樣將其 patch 為 `jmp` 後執行。  
此時，當播放超過一分鐘時，caption 變會改變，由 `MP3 Player` 改為 flag。
