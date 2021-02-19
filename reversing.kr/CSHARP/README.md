# CSHARP

1. 目標：輸入特定 input 後可以得到 `Correct!!`

2. 用 dnSpy disassemble **CSharp.exe**

   1. 從 `private void InitializeComponent()` 可以找到當按下 Check Button 後，會呼叫 `private void btnCheck_Click(object sender, EventArgs e)`
   2. 在 `btnCheck_Click` 中嘗試呼叫 `private static void MetMetMet(string sss)`，將輸入值做 base64 encode之後，而其會呼叫`private static void MetMett(byte[] chk, byte[] bt)` 並根據encode 過後的值判斷為 `Correct!!` 還是 `Wrong`。
   3. 然而，MetMett 卻沒有辦法被正確 decompile，因為，MetMett 實際的值只會在程式開始執行後才被寫入相應的位置

3.  找出產生此部分值的function、用 ida pro 開啟檔案並找出MetMett 的位置

   1. 在 `public Form1()` 中，可以找到MetMett 內容產生的方式

   2. 從 ida pro 中可以找到未經過處理的 MetMett 內容從 0x2E0 開始

   3. dump 出其值，再將 dump 出的值，利用 python 對這些值做相同的處理

      （處理過程中可能會因為值不在 0~255 之間而產生 error，利用 % 255 將其限制）

   4. 利用 Hex View 找出處理完的 bytes 改寫入的位置，從 0x538 開始寫入處理過後的值

   5. 將 python 處理過後的值，重新寫回 CSharp.exe

4. 將處理過後的 CSharp.exe 丟入 dnSpy decompile

   其實只是簡單的 xor，逆推便可得原本的應要的輸入