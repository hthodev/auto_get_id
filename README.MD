[![Join our Telegram](https://img.shields.io/badge/Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white)](https://t.me/airdropertoptop)

## Tính năng
1. Tự động lấy query_id
2. Tự động ref các kèo

## Các tải
1. **Kéo repo về máy**

   ```bash
   git clone https://github.com/hthodev/auto_get_id.git
   cd Auto_get_id
   ```

2. **Tạo máy ảo (window)**

    ```bash
    py -m venv myenv
    myenv\Scripts\activate
    ```

   
3. **Tải gói**

  ```bash
    pip install -r requirements.txt
  ```

## Configuration Settings

1. Mở webview (F12 trong telegram):
  Setting -> Advanced -> Experimental settings -> Turn on "Enable webview inspecting"

2. Tạo folder lưu các acc.
- Code đang mặc định là: - `D:\tg`

- Trong thư mục tg sẽ tạo 1 thư mục, ví dụ như số folder 1, trong folder acc sẽ có tdata, telegram.exe
Tải về ở đây [Download](https://telegram.org/dl/desktop/win64_portable)

3. Copy tất cả file đã tải về ở trang chủ tele và dán vào folder "1"

4. Open file `bots.txt` để input các kèo muốn thêm vào

5. Chạy bot

```bash
  py start.py
```

6. Đối với chạy lệnh ref.
- Lấy acc chính tạo 1 group, thêm tất cả các acc clone vào
- Dán tất cả các link liên quan đến các kèo muốn share
- Chạy lệnh ref
```bash
  py ref.py
```

Tham gia group trên telegram nếu chạy source code có lỗi gì cần fix, 
[![Join our Telegram](https://img.shields.io/badge/Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white)](https://t.me/airdropertoptop)

Source code được copy và sửa lại từ trang
[Copy left](https://github.com/cucumber-pickle)