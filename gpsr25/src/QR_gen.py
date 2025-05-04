import tkinter as tk
from PIL import Image, ImageTk, ImageDraw, ImageFont
import qrcode
import time

# === 表示内容 ===
texts = ["Hello!", "KIT QR Test", "Final Stage!"]

texts = [
    "go to the bedroom then meet Alice and answer a quiz",
    "navigate to the living room then find a box and get it and place it on the tall table",
    "go to the bedroom then find a box and take it and deliver it to me",
    
    "find a person pointing to the left in the office and escort them to the bedroom",
    "look for a standing person in the bedroom and follow them to the living room",
    "find a person raising their right arm in the bedroom and tell where you come from",

    "meet Bob in the bedroom and follow them",
    "meet Bob in the living room and answer a question",
    "meet Alice in the living room and say where you come from",

    "tell me how many people raising their right arm are in the office",
    "tell me how many people looking back are in the kitchen",
    "tell me how many people pointing to the left are in the bedroom",

    "tell me the name of the person at the bedroom",
    "tell me the shirt color of the person in the kitchen",
    "tell me the height of the person at the living room",

    "tell what day today is to the person raising their right arm in the living room",
    "tell where RoboCup is held this year to the person giving the V sign in the living room",
    "tell what the time is to the person giving the V sign in the bedroom",

    "answer the question of the person pointing to the left in the living room",
    "answer the question of the person giving the V sign in the office",
    "answer the question of the person raising their right arm in the kitchen",

    "follow Bob from the bedroom to the kitchen",
    "follow Charlie from the office to the bedroom",
    "follow Bob from the living room to the office",

    "escort Charlie from the office to the kitchen",
    "lead Charlie from the living room to the office",
    "take Charlie from the office to the living room",

    "guide the sitting person from the office to the bedroom",
    "lead the person crossing one's arms from the bedroom to the kitchen",
    "take the person looking back from the kitchen to the bedroom",

    "lead the person wearing a black blouse from the living room to the kitchen",
    "lead the person wearing a black coat from the office to the living room",
    "escort the person wearing a red shirt from the office to the office",

    "salute the person wearing a gray blouse in the bedroom and follow them",
    "introduce yourself to the person wearing an orange sweater in the bedroom and tell what the weather is like today",
    "salute the person wearing a black blouse in the living room and guide them to the office",

    "say hello to Bob in the living room and say what day today is",
    "greet Charlie in the office and answer a quiz",
    "say hello to Bob in the bedroom and answer a question",

    "meet Charlie at the living room then look for them in the living room",
    "meet Alice at the living room then look for them in the bedroom",
    "meet Bob at the office then look for them in the living room",

    "tell me how many people in the living room are wearing gray shirts",
    "tell me how many people in the office are wearing red shirts",
    "tell me how many people in the bedroom are wearing yellow t shirts",

    "tell the name of the person at the living room to the person at the kitchen",
    "tell the name of the person at the bedroom to the person at the kitchen",
    "tell the height of the person at the living room to the person at the office",

    "tell the name of the person at the bedroom to the person at the kitchen",
    "tell the shirt color of the person at the kitchen to the person at the bedroom",
    "tell the height of the person at the office to the person at the kitchen",

    "follow the sitting person in the office",
    "follow the person looking back at the office",
    "follow the person crossing one's arms at the office",

    "get a cup from the shelf and place it on the tall table",
    "fetch a box from the tall table and bring it to the squatting person in the living room",
    "get a box from the tall table and put it on the shelf",

    "locate a cup in the bedroom then fetch it and place it on the tall table",
    "look for a bottle in the kitchen then take it and bring it to the person pointing to the left in the kitchen",
    "find a bottle in the office then fetch it and put it on the tall table",

    "tell me how many cups there are on the tall table",
    "tell me how many cups there are on the table",
    "tell me how many bottles there are on the tall table",

    "tell me what is the largest object on the table",
    "tell me what is the smallest object on the table",
    "tell me what is the lightest object on the table",

    "give me a bottle from the table",
    "bring me a bottle from the table",
    "give me a bottle from the tall table",

    "tell me what is the largest bottle on the table",
    "tell me what is the lightest box on the shelf",
    "tell me what is the largest box on the table"
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
    scale = (int(screen_height * 0.7)) // qr_h
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
