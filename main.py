import cv2

def cartoonize_image(img):
    """Convert an image into cartoon style."""
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.medianBlur(gray, 5)

    # Edge detection
    edges = cv2.adaptiveThreshold(
        gray, 255,
        cv2.ADAPTIVE_THRESH_MEAN_C,
        cv2.THRESH_BINARY, 9, 9
    )

    # Smooth the image using bilateral filter
    color = cv2.bilateralFilter(img, 9, 250, 250)

    # Combine edges and smoothed color
    cartoon = cv2.bitwise_and(color, color, mask=edges)
    return cartoon


def cartoonize_from_file(image_path, save_path="cartoon_output.jpg"):
    """Read an image file and save cartoonized version."""
    img = cv2.imread(image_path)
    if img is None:
        print("❌ Error: Image not found. Check the file path.")
        return
    cartoon = cartoonize_image(img)
    cv2.imshow("Cartoon Image", cartoon)
    cv2.imwrite(save_path, cartoon)
    print(f"✅ Cartoonized image saved as {save_path}")
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def cartoonize_from_webcam():
    """Cartoonize live video from webcam."""
    cap = cv2.VideoCapture(0)  # 0 = default webcam
    if not cap.isOpened():
        print("❌ Error: Cannot access webcam.")
        return

    print("🎥 Press 'q' to quit the live cartoon mode.")
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        cartoon = cartoonize_image(frame)
        cv2.imshow("Live Cartoon", cartoon)

        # Exit when 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    print("✅ Webcam cartoon mode ended.")


if __name__ == "__main__":
    print("Choose an option:")
    print("1. Cartoonize an image file")
    print("2. Cartoonize live webcam feed")
    choice = input("Enter 1 or 2: ")

    if choice == "1":
        path = input("Enter the image file path: ")
        cartoonize_from_file(path)
    elif choice == "2":
        cartoonize_from_webcam()
    else:
        print("❌ Invalid choice. Exiting.")
