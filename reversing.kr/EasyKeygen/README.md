# EasyKeygen

題目問 Input Name, Serial，兩者相符即回傳 Correct!，且題目要求 Input Serial 要找到 `5B134977135E7D13` 對應的 Input Name。  
從 ida 可以看出 serial 就是 name 依序跟 [16, 32, 48] 循環 xor 結果的 Hex，因此只要將 serial 依序跟 [16, 32, 48] 循環 xor 後（`a xor b = c -> a = b xor c`），用 ascii 印出即是答案。