import qrcode


def generate_qr_code(text, file_name):
    """
    生成二维码并保存为图片
    :param text: 要编码的文本或URL
    :param file_name: 保存的文件名
    """
    # 创建QRCode对象
    qr = qrcode.QRCode(
        version=1,  # 控制二维码大小（1-40），数字越大二维码越大
        error_correction=qrcode.constants.ERROR_CORRECT_M,  # 错误纠正级别
        box_size=10,  # 每个小格子包含的像素数
        border=4,  # 边框包含的格子数
    )

    # 添加数据
    qr.add_data(text)

    # 生成二维码
    qr.make(fit=True)

    # 创建图像
    img = qr.make_image(fill_color="black", back_color="white")

    # 保存图像
    img.save(file_name)


# 主程序从这里开始（没有缩进）
if __name__ == "__main__":
    # 要编码的内容
    text = "https://en.wikipedia.org/wiki/"

    # 保存的文件名
    file_name = "qrcode.png"

    # 调用函数生成二维码
    generate_qr_code(text, file_name)

    print(f"QR code saved as {file_name}")