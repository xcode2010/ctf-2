# EasyCrack
用 ida pro decompile 找一下就可以看到 `if ( v3[0] != 'a' || strncmp(&v3[1], Str2, 2u) || strcmp(&v3[3], aR3versing) || String != 'E' )` ，`v3` 就是 Dialog 的 input string，因此只要使輸入符合此判斷的條件即可。