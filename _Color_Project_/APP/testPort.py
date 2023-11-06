import serial

# Khởi tạo một đối tượng Serial với cổng và tốc độ baudrate
ser = serial.Serial('/dev/ttyUSB0', 9600)  # Thay '/dev/ttyUSB0' và 9600 bằng thông số của bạn


command = "0003"
ser.write(command.encode())  # Encode chuỗi thành dạng bytes và gửi đi

# Đóng cổng serial sau khi ho
