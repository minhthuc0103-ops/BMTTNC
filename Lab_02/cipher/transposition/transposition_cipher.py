import math

class TranspositionCipher:
    def __init__(self):
        pass

    def encrypt(self, text, key):
        encrypted_text = ''
        for col in range(key):
            pointer = col
            while pointer < len(text):
                encrypted_text += text[pointer]
                pointer += key
        return encrypted_text

    def decrypt(self, text, key):
        # 1. Số cột của ma trận chính là key
        num_cols = key
        # 2. Tính số hàng đầy đủ của ma trận
        num_rows = math.ceil(len(text) / num_cols)
        # 3. Tính số ký tự bị dư ra ở hàng cuối cùng
        remainder = len(text) % num_cols

        # Khởi tạo danh sách lưu các chuỗi của từng cột sau khi tách ra
        cols_data = []
        start_idx = 0

        # 4. Cắt chuỗi mã hóa (text) ngược trở lại thành các cột dựa trên độ dài của từng cột
        for col in range(num_cols):
            # Nếu cột này nằm trong nhóm có ký tự ở hàng cuối cùng (khi remainder > 0)
            if remainder == 0 or col < remainder:
                col_length = num_rows
            else:
                col_length = num_rows - 1
            
            # Cắt lấy đoạn ký tự thuộc về cột hiện tại
            cols_data.append(text[start_idx : start_idx + col_length])
            start_idx += col_length

        # 5. Đọc lại ma trận theo từng hàng từ trái qua phải để khôi phục bản rõ (plain text)
        plain_text = ''
        for r in range(num_rows):
            for c in range(num_cols):
                # Kiểm tra xem tại tọa độ hàng r, cột c này có ký tự hợp lệ không
                if r < len(cols_data[c]):
                    plain_text += cols_data[c][r]

        return plain_text