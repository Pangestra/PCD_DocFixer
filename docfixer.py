import cv2
import numpy as np
import os
from tkinter import filedialog, Tk, Button, Label, messagebox

def enhance_contrast(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8, 8))
    return clahe.apply(gray)

def apply_threshold(image):
    return cv2.adaptiveThreshold(
        image, 255,
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY,
        11, 2
    )

def save_result(image, base_name="captured"):
    output_dir = "output"
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, f"{base_name}_fixed.png")
    cv2.imwrite(output_path, image)
    print(f"Hasil disimpan di: {output_path}")
    return output_path

def process_image(image, base_name="processed"):
    enhanced = enhance_contrast(image)
    thresholded = apply_threshold(enhanced)

    combined = np.hstack((
        cv2.cvtColor(enhanced, cv2.COLOR_GRAY2BGR),
        cv2.cvtColor(thresholded, cv2.COLOR_GRAY2BGR)
    ))
    cv2.imshow("Enhanced (kiri) vs Thresholded (kanan)", combined)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    return save_result(thresholded, base_name)

def open_file():
    file_path = filedialog.askopenfilename(
        title="Pilih Gambar Dokumen",
        filetypes=[("Gambar", "*.png *.jpg *.jpeg *.bmp")]
    )
    if not file_path:
        return

    image = cv2.imread(file_path)
    if image is None:
        messagebox.showerror("Error", "Gagal membuka gambar.")
        return

    filename = os.path.splitext(os.path.basename(file_path))[0]
    saved_path = process_image(image, filename)
    messagebox.showinfo("Sukses", f"Hasil disimpan di:\n{saved_path}")

def capture_from_camera():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        messagebox.showerror("Error", "Webcam tidak terdeteksi.")
        return

    print("Tekan [SPACE] untuk mengambil gambar, [ESC] untuk keluar.")
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        cv2.imshow("Tekan [SPACE] untuk scan", frame)

        key = cv2.waitKey(1)
        if key == 27:  # ESC
            break
        elif key == 32:  # SPACE
            cap.release()
            cv2.destroyAllWindows()
            saved_path = process_image(frame, "scan_cam")
            messagebox.showinfo("Sukses", f"Hasil disimpan di:\n{saved_path}")
            return

    cap.release()
    cv2.destroyAllWindows()

def main_ui():
    root = Tk()
    root.title("DocFixer - Peningkatan Kontras Dokumen")
    root.geometry("400x200")
    root.resizable(False, False)

    Label(root, text="DocFixer", font=("Arial", 18, "bold")).pack(pady=10)
    Label(root, text="Pilih metode input dokumen:", font=("Arial", 12)).pack(pady=5)

    Button(root, text="📷 Pilih Foto dari File", command=open_file, width=30, height=2).pack(pady=10)
    Button(root, text="📸 Ambil Gambar dari Kamera", command=capture_from_camera, width=30, height=2).pack()

    root.mainloop()

if __name__ == "__main__":
    main_ui()
