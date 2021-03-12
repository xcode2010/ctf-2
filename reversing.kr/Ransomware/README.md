# Ransomware

## Stage 1
1. Check the executable with **Detect It Easy** and find it being packed by **UPX**.
2. Use *upx.exe* to decompress the executable.
3. Use **IDA Pro** to [static analyze](#static-analysis) the binary.
4. Use [XOR Cracker](https://wiremask.eu/tools/xor-cracker/) to guess the possible keys and, as mentioned in `readme.txt`, the encrypted file is an **executable**. Therefore, the key can easily be narrowed down to only ***one*** possiblity and its length is `13`.
5. Reverse the encryption to decypt the `file`. That is, for each byte `i` at position `j`, its corresponding byte should be `(i ^ 0xff) ^ key[j % 13]`.
6. After finishing decrypting `file`, analyze the new [**executable**](#stage-2).

### Static Analysis
1. Try decompile `main` function directly and get 
   ```
   Decompilation failure:
   xxxxxx: too big function
   ```
2. Take a look into the assembly can find that a big part of the excutable filled with the following, which does nothing but obfuscating.
   ```assembly
   60    pusha
   61    popa
   90    nop
   50    push    eax
   58    pop     eax
   53    push    ebx
   5B    pop     ebx
   ```
   Therefore, implement [`ida python`](./ida_python.py) to convert the pattern into `nop`s in the functions, `main` and `sub_401000`, which does nothing.
3. Decompile function `main` and observe.
   1. Ask user to enter `key`.
   2. Read the original file.
   3. **XOR** the byte in the `file` with `key` and **XOR** `0xff`.
   4. Write the encrypted result back to the file.

## Stage 2
1. Try executing the file and get `System Error`, missing `MSVCR100.dll`.
2. Instead of fixing the error, check it with **Detect It Easy** and find it also being packed by **UPX**.
3. Use *upx.exe* to decompress the executable.
4. Check `strings` contain in the file and the flag can be obtained.