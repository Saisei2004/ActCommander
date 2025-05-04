import tkinter as tk
from PIL import Image, ImageTk, ImageDraw, ImageFont
import qrcode
import time

# === 表示内容 ===
texts = ["Hello!", "KIT QR Test", "Final Stage!"]
texts = [
    "tell me what is the largest bowl on the shelf",
    "find a bowl in the study room then take it and give it to Angel in the study room",
    "tell me how many dice there are on the counter",
    "say What color is the Japanese flag? to the person raising their right arm in the bedroom",
    "tell me the name of the person at the bedroom",
    "meet Angel at the bedroom then find the person crossing one's arms in the kitchen",
    "navigate to the kitchen then find the person raising their right arm and follow them",
    "follow the person raising their right arm in the study room",
    "escort the person wearing a black shirt from the living room to the kitchen",
    "introduce yourself to Sophia in the bedroom and follow them to the kitchen",
    "tell me what is the biggest object on the table",
    "answer the quiz of the person giving the v sign in the kitchen",
    "tell me how many people in the living room are wearing white shirts",
    "tell me what is the lightest bowl on the desk",
    "greet the person wearing a white t shirt in the study room and follow them to the kitchen",
    "escort the person pointing to the left from the bedroom to the kitchen",
    "tell me how many people crossing one's arms are in the kitchen",
    "bring me a dice from the counter",
    "get a lunch box from the counter and put it on the table",
    "meet Angel in the study room and follow them to the kitchen",
    "tell the age of the person at the bedroom to the person at the study room",
    "follow Tom from the kitchen to the study room",
    "lead Mike from the study room to the bedroom",
    "look for a person pointing to the left in the living room and tell Why do robots move in a jerky way?"
]


# === フォント設定 ===
font_path = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
title_font = ImageFont.truetype(font_path, 40)
help_font = ImageFont.truetype(font_path, 20)
time_font = ImageFont.truetype(font_path, 30)

# === ウィンドウサイズ取得 ===
temp_root = tk.Tk()
screen_width = temp_root.winfo_screenwidth()
screen_height = temp_root.winfo_screenheight()
temp_root.destroy()

# === 操作説明表示 ===
help_text = [
    "J / → : Correct",
    "K : Wrong",
    "← : Back",
    "Space : Pause / Resume",
    "ESC : Exit"
]

# === 結果記録用 ===
lap_times = []
results = []
start_time = None
paused = False
pause_start = None
elapsed_pause = 0
max_lap_time = 0.0

# === QR画像作成 ===
qr_images = []
for i, text in enumerate(texts):
    qr = qrcode.make(text).convert("RGB")
    qr_w, qr_h = qr.size
    scale = (int(screen_height * 1)) // qr_h
    qr = qr.resize((qr_w * scale, qr_h * scale), Image.ANTIALIAS)
    qr_w, qr_h = qr.size

    img = Image.new("RGB", (screen_width, screen_height), "white")
    draw = ImageDraw.Draw(img)
    img.paste(qr, ((screen_width - qr_w) // 2, (screen_height - qr_h) // 2))

    header_text = f"[{i+1}/{len(texts)}] {text}"
    draw.rectangle([(0, 0), (screen_width, 70)], fill="white")
    draw.text((40, 15), header_text, font=title_font, fill="black")

    box_w, box_h = 360, 140
    box_x, box_y = screen_width - box_w - 20, screen_height - box_h - 20
    draw.rectangle([(box_x, box_y), (box_x + box_w, box_y + box_h)], fill="#DDDDDD")
    for j, line in enumerate(help_text):
        draw.text((box_x + 10, box_y + 10 + j * 25), line, font=help_font, fill="black")

    qr_images.append(img)

# === tkinter UI ===
root = tk.Tk()
root.attributes('-fullscreen', True)
canvas = tk.Canvas(root, bg="white", highlightthickness=0)
canvas.pack(fill=tk.BOTH, expand=True)

index = 0
time_text_id = None

def show_image(img):
    global img_tk, time_text_id
    img_tk = ImageTk.PhotoImage(img)
    canvas.delete("all")
    canvas.create_image(screen_width // 2, screen_height // 2, image=img_tk, anchor=tk.CENTER)
    update_time()

def update_time():
    global time_text_id, max_lap_time
    if start_time:
        if not paused:
            now = time.time()
            elapsed = now - start_time - elapsed_pause
            if elapsed > max_lap_time:
                max_lap_time = elapsed
            time_str = f"Time: {max_lap_time:.2f} sec"
        else:
            time_str = f"Paused (Max: {max_lap_time:.2f} sec)"
        if time_text_id:
            canvas.delete(time_text_id)
        time_text_id = canvas.create_text(100, screen_height - 50, text=time_str, font=("Arial", 24), fill="black", anchor="w")
    root.after(100, update_time)

def log_lap(result):
    global max_lap_time
    lap_times.append(round(max_lap_time, 2))
    results.append(result)
    reset_timer()

def reset_timer():
    global start_time, elapsed_pause, max_lap_time
    start_time = time.time()
    elapsed_pause = 0
    max_lap_time = 0.0

def next_image(result):
    global index
    if index < len(qr_images) - 1:
        log_lap(result)
        index += 1
        show_image(qr_images[index])
    elif index == len(qr_images) - 1:
        log_lap(result)
        show_results()
        root.quit()

def prev_image(event=None):
    global index
    if index > 0:
        index -= 1
        show_image(qr_images[index])
        reset_timer()

def pause_resume(event=None):
    global paused, pause_start, elapsed_pause
    if not paused:
        paused = True
        pause_start = time.time()
    else:
        paused = False
        elapsed_pause += time.time() - pause_start
        pause_start = None

def close_app(event=None):
    show_results()
    root.quit()

def show_results():
    print("\n==== Results ====")
    for i in range(len(lap_times)):
        print(f"{i+1}. {texts[i]} - {results[i]} - {lap_times[i]} sec")
    print("=================")

# === キー操作バインド ===
root.bind("<KeyPress-j>", lambda e: next_image("Correct"))
root.bind("<KeyPress-k>", lambda e: next_image("Wrong"))
root.bind("<Right>", lambda e: next_image("Correct"))
root.bind("<Left>", prev_image)
root.bind("<space>", pause_resume)
root.bind("<Escape>", close_app)

# === 初期表示・タイマー開始 ===
show_image(qr_images[index])
reset_timer()
root.mainloop()
