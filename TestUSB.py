import psutil

drives = [d.device for d in psutil.disk_partitions()]

print("Danh sách các ổ đĩa:")
for drive in drives:
    print(drive)

print("\nDung lượng của từng ổ đĩa:")
for drive in drives:
    usage = psutil.disk_usage(drive)
    print(f"{drive}:")
    print(f"  Tổng dung lượng: {usage.total / (1024 ** 3):.2f} GB")
    print(f"  Dung lượng sử dụng: {usage.used / (1024 ** 3):.2f} GB")
    print(f"  Dung lượng trống: {usage.free / (1024 ** 3):.2f} GB")
    print(f"  Tỷ lệ sử dụng: {usage.percent}%")

import psutil

drives = psutil.disk_partitions()

print("Danh sách các ổ đĩa:")
for drive in drives:
    drive_name = drive.device
    drive_type = drive.fstype
    print(f"{drive_name} - Loại ổ đĩa: {drive_type}")
