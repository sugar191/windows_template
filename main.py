import os
import sys
import customtkinter as ctk


def resource_path(relative_path: str) -> str:
    """--onefile ビルド時も正しいパスを返す（PyInstaller対応）"""
    base = getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base, relative_path)


def main():
    ctk.set_appearance_mode("System")   # "System" | "Dark" | "Light"
    ctk.set_default_color_theme("blue")  # "blue" | "green" | "dark-blue"

    app = ctk.CTk()
    app.title("App")
    app.geometry("400x300")

    # ウィンドウアイコンの設定（assets/icon.ico を用意したら有効にする）
    # icon_path = resource_path("assets/icon.ico")
    # if os.path.exists(icon_path):
    #     app.iconbitmap(icon_path)

    label = ctk.CTkLabel(app, text="Hello, World!", font=ctk.CTkFont(size=20))
    label.pack(expand=True)

    app.mainloop()


if __name__ == "__main__":
    main()
