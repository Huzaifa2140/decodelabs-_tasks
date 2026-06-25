import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r"C:/Users/HP/AppData/Local/Programs/Tesseract-OCR/tesseract.exe"
image_path = "Sample image.png"
img = cv2.imread(image_path)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (3, 3), 0)
thresh = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

# psm 6 works well for a single uniform block of text
custom_config = "--psm 6"
data = pytesseract.image_to_data(thresh, config=custom_config, output_type=pytesseract.Output.DICT)

recognized_text = ""
confidences = []

for i in range(len(data["text"])):
    word = data["text"][i].strip()
    conf = int(data["conf"][i])
    if word and conf > 0:
        recognized_text += word + " "
        confidences.append(conf)

avg_confidence = sum(confidences) / len(confidences) if confidences else 0

print("Recognized Text:", recognized_text.strip())
print("Average Confidence:", round(avg_confidence, 2), "%")

if avg_confidence >= 80:
    print("Status: PASSED (confidence above 80% threshold)")
else:
    print("Status: LOW CONFIDENCE, result may be unreliable")

cv2.imwrite("processed_output.png", thresh)
