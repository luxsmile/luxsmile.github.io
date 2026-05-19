"""
Renders luxsmile_magazine.png at exactly 300 DPI press quality.
Page: 2.125" x 4.875"  ->  638 x 1463 pixels @ 300 DPI
"""
from PIL import Image, ImageDraw, ImageFont
import os

# ── Canvas size ───────────────────────────────────────────────────
DPI    = 300
W_IN, H_IN = 2.125, 4.875
W = round(W_IN * DPI)   # 638
H = round(H_IN * DPI)   # 1463

S = DPI / 72.0           # scale: 1 reportlab point -> pixels

# ── Colors (RGB) ─────────────────────────────────────────────────
NAVY  = (27,  42,  74)
GOLD  = (201, 169, 110)
CREAM = (250, 246, 239)
WHITE = (255, 255, 255)
DARK  = (26,  26,  26)

# ── Coordinate helpers ────────────────────────────────────────────
# reportlab: y=0 bottom, y=351 top
# PIL:        y=0 top,    y=H   bottom
def ry(pt_y):
    """reportlab y-point -> PIL pixel y (top of that point line)"""
    return round((351 - pt_y) * S)

def px(pt):
    return round(pt * S)

# ── Font loader ───────────────────────────────────────────────────
F = "C:/Windows/Fonts/"
_font_cache = {}
def font(name, pt):
    key = (name, pt)
    if key not in _font_cache:
        size_px = max(8, round(pt * S))
        try:
            _font_cache[key] = ImageFont.truetype(F + name, size_px)
        except:
            _font_cache[key] = ImageFont.load_default()
    return _font_cache[key]

# ── Drawing helpers ───────────────────────────────────────────────
img  = Image.new("RGB", (W, H), CREAM)
draw = ImageDraw.Draw(img)

def rect(x_pt, y_pt_bottom, w_pt, h_pt, color):
    x0 = px(x_pt)
    y0 = ry(y_pt_bottom + h_pt)
    x1 = px(x_pt + w_pt)
    y1 = ry(y_pt_bottom)
    draw.rectangle([x0, y0, x1, y1], fill=color)

def hline(y_pt, color, x0_pt=0, x1_pt=153, width_pt=0.5):
    y = ry(y_pt)
    draw.line([(px(x0_pt), y), (px(x1_pt), y)],
              fill=color, width=max(1, round(width_pt * S)))

def text_left(txt, x_pt, y_pt_baseline, fnt, color):
    """Draw text left-aligned; y_pt_baseline is reportlab baseline."""
    draw.text((px(x_pt), ry(y_pt_baseline) - fnt.size), txt,
              font=fnt, fill=color)

def text_right(txt, x_pt, y_pt_baseline, fnt, color):
    bbox = draw.textbbox((0, 0), txt, font=fnt)
    tw = bbox[2] - bbox[0]
    draw.text((px(x_pt) - tw, ry(y_pt_baseline) - fnt.size), txt,
              font=fnt, fill=color)

def text_center(txt, y_pt_baseline, fnt, color, cx_pt=76.5):
    bbox = draw.textbbox((0, 0), txt, font=fnt)
    tw = bbox[2] - bbox[0]
    x = px(cx_pt) - tw // 2
    draw.text((x, ry(y_pt_baseline) - fnt.size), txt,
              font=fnt, fill=color)

# ════════════════════════════════════════════════════════════════
# 1. HEADER  y: 321-351
# ════════════════════════════════════════════════════════════════
rect(0, 321, 153, 30, CREAM)
hline(321, GOLD)

# Logo
try:
    logo = Image.open(r"C:\Users\leili\luxsmile.github.io\logo.png").convert("RGBA")
    logo_size = px(26)
    logo = logo.resize((logo_size, logo_size), Image.LANCZOS)
    img.paste(logo, (px(4), ry(349)), logo)
except Exception as e:
    print(f"Logo: {e}")

# LuxSmile
text_left("LuxSmile",         32, 337, font("timesbd.ttf", 12), NAVY)
text_left("MOBILE DENTAL HYGIENE", 32, 330, font("arialbd.ttf", 4.5), NAVY)
text_right("Leaside & Surrounding Area", 150, 326, font("arial.ttf", 3.5), NAVY)

# ════════════════════════════════════════════════════════════════
# 2. PHOTO  y: 261-321
# ════════════════════════════════════════════════════════════════
try:
    photo = Image.open(r"C:\Users\leili\luxsmile.github.io\dental.jpg").convert("RGB")
    ph_w, ph_h = px(153), px(60)
    scale = max(ph_w / photo.width, ph_h / photo.height)
    nw, nh = round(photo.width * scale), round(photo.height * scale)
    photo = photo.resize((nw, nh), Image.LANCZOS)
    ox = (nw - ph_w) // 2
    oy = (nh - ph_h) // 2
    photo = photo.crop((ox, oy, ox + ph_w, oy + ph_h))
    img.paste(photo, (0, ry(321)))
except Exception as e:
    print(f"Photo: {e}")
    rect(0, 261, 153, 60, (80, 110, 140))

# ════════════════════════════════════════════════════════════════
# 3. HEADLINE BOX  y: 191-261
# ════════════════════════════════════════════════════════════════
rect(0, 191, 153, 70, NAVY)

text_center("AT YOUR DOOR  OR  OUR OFFICE", 255, font("arialbd.ttf", 5), GOLD)
hline(252, GOLD, x0_pt=12, x1_pt=141)
text_center("Premium dental hygiene", 241, font("timesbi.ttf", 11), WHITE)
text_center("that comes to you.",     229, font("timesbi.ttf", 11), WHITE)
text_center("416-994-9669",           217, font("arialbd.ttf",  9), WHITE)
text_center("Leili H Zarrabi, RDH",  205, font("timesi.ttf",  6.5), GOLD)

# ════════════════════════════════════════════════════════════════
# 4. GOLD GIFT BAND  y: 133-191
# ════════════════════════════════════════════════════════════════
rect(0, 133, 153, 58, GOLD)

text_center("*  FIRST-VISIT GIFT  *", 185, font("arialbd.ttf", 5),   NAVY)
hline(182, NAVY, x0_pt=18, x1_pt=135, width_pt=0.4)
text_center("Complimentary",          173, font("timesi.ttf",  7.5), NAVY)
text_center("Waterpik",               159, font("timesbi.ttf", 16),  NAVY)
text_center("A $250+ value  (While quantities last.)", 145,
            font("arialbd.ttf", 5), NAVY)

# ════════════════════════════════════════════════════════════════
# 5. TEETH WHITENING  y: 115-133
# ════════════════════════════════════════════════════════════════
rect(0, 115, 153, 18, NAVY)
text_center("TEETH WHITENING",                        125, font("arialbd.ttf", 7), GOLD)
text_center("Advanced technology  -  Little to no sensitivity",
            117, font("arialbd.ttf", 5), WHITE)

# ════════════════════════════════════════════════════════════════
# 6. STATS  y: 83-115  (3 columns)
# ════════════════════════════════════════════════════════════════
rect(0, 83, 153, 32, CREAM)
hline(115, GOLD)
hline(83,  GOLD)
hline(83, GOLD, x0_pt=51, x1_pt=51, width_pt=0.5)  # vertical
hline(83, GOLD, x0_pt=102, x1_pt=102, width_pt=0.5) # vertical

# draw verticals as actual vertical lines
for x_pt in (51, 102):
    draw.line([(px(x_pt), ry(115)), (px(x_pt), ry(83))],
              fill=GOLD, width=max(1, round(0.5 * S)))

stats = [
    (25,  "15",     ["YRS", "EXP"]),
    (76,  "CDCP",   ["& All Insurance", "Plans Accepted"]),
    (127, "Direct", ["BILLING", "AVAILABLE"]),
]
for cx, big, sub in stats:
    text_center(big, 102, font("arialbd.ttf", 9), NAVY, cx_pt=cx)
    for j, line in enumerate(sub):
        text_center(line, 95 - j*7, font("arial.ttf", 4.5), NAVY, cx_pt=cx)

# ════════════════════════════════════════════════════════════════
# 7. SERVICES  y: 30-83
# ════════════════════════════════════════════════════════════════
rect(0, 30, 153, 53, CREAM)

text_left("OUR SERVICES",      7, 77, font("arialbd.ttf", 5),   GOLD)
text_left("Full-service hygiene", 7, 69, font("timesbi.ttf", 8.5), NAVY)

left_svcs  = ["Complete Oral Exam", "Teeth Cleaning", "Stain Removal",
               "Fluoride Treatment", "Sealants (Cavity Protection)"]
right_svcs = ["Advanced Gum Therapy", "Children's Hygiene", "Seniors & Special Care",
               "Oral Health Education", "Referrals"]

for i, (l, r) in enumerate(zip(left_svcs, right_svcs)):
    y = 61 - i * 7
    text_left("- " + l, 7,  y, font("arialbd.ttf", 4.5), NAVY)
    text_left("- " + r, 79, y, font("arialbd.ttf", 4.5), NAVY)

# ════════════════════════════════════════════════════════════════
# 8. FOOTER  y: 0-30
# ════════════════════════════════════════════════════════════════
rect(0, 0, 153, 30, NAVY)

text_left("TEXT OR CALL:",         7, 24, font("arialbd.ttf", 5),   GOLD)
text_left("416-994-9669",          7, 12, font("arialbd.ttf", 12),  WHITE)
text_right("Leili H Zarrabi, RDH",148, 17, font("timesi.ttf", 6.5), WHITE)
text_right("REGISTERED DENTAL HYGIENIST",
           148, 9, font("arial.ttf", 4), WHITE)

# ── Save ─────────────────────────────────────────────────────────
out_png = r"C:\Users\leili\luxsmile.github.io\luxsmile_magazine_300dpi.png"
out_jpg = r"C:\Users\leili\luxsmile.github.io\luxsmile_magazine_300dpi.jpg"

img.save(out_png, dpi=(300, 300))
img.save(out_jpg, dpi=(300, 300), quality=95, optimize=True)

for path in (out_png, out_jpg):
    kb = os.path.getsize(path) // 1024
    print(f"[OK] {os.path.basename(path)}  {kb} KB  ({W}x{H}px @ {DPI} DPI)")
