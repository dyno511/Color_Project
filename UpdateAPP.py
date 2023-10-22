import requests
import zipfile
import os

# URL của tệp ZIP cần tải về
zip_file_url = "http://api.duyvo26.xyz/Color_Project/2110793809/9416382725"

# Thư mục cần giải nén và ghi đè
target_directory = ""

# Tải tệp ZIP từ URL
response = requests.get(zip_file_url)

# Kiểm tra xem tải về có thành công không
if response.status_code == 200:
    # Lưu tệp ZIP vào một tệp cục bộ
    with open("downloaded_file.zip", "wb") as f:
        f.write(response.content)

    # Giải nén tệp ZIP và ghi đè lên thư mục cũ
    with zipfile.ZipFile("downloaded_file.zip", "r") as zip_ref:
        zip_ref.extractall(target_directory)
        
    # Xóa tệp ZIP tải về (tuỳ chọn)
    os.remove("downloaded_file.zip")
else:
    print("Lỗi khi tải tệp ZIP.")

