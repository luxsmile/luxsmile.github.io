"""
Renders the ORIGINAL magazine flyer (first version) at 300 DPI.
Navy blue + gold colour scheme, original layout before any edits.
Output: luxsmile_magazine_original_300dpi.png / .jpg
"""
from PIL import Image, ImageDraw, ImageFont
import os

DPI   = 300
W_IN, H_IN = 2.125, 4.875
W = round(W_IN * DPI)   # 638
H = round(H_IN * DPI)   # 1463

S     = DPI / 72.0       # 1 reportlab point -> pixels
H_PT  = 351              # total height in points

NAVY  = (27,  42,  74)
GOLD  = (201, 169, 110)
CREAM = (250, 246, 239)
WHITE = (255, 255, 255)
DARK  = (26,  26,  26)

img  = Image.new("RGB", (W, H), CREAM)
draw = ImageDraw.Draw(img)

F = "C:/Windows/Fonts/"
_fc = {}
def fnt(name, pt):
    k = (name, pt)
    if k not in _fc:
        try:   _fc[k] = ImageFont.truetype(F + name, max(8, round(pt * S)))
        except: _fc[k] = ImageFont.load_default()
    return _fc[k]

def ry(pt_y):
    return round((H_PT - pt_y) * S)

def px(pt):
    return round(pt * S)

def fill(x_pt, y_bot, w_pt, h_pt, color):
    draw.rectangle([px(x_pt), ry(y_bot+h_pt), px(x_pt+w_pt), ry(y_bot)], fill=color)

def hline(y_pt, color, x0=0, x1=153, lw=0.5):
    y = ry(y_pt)
    draw.line([(px(x0), y), (px(x1), y)], fill=color, width=max(1, round(lw*S)))

def vline(x_pt, y_bot, y_top, color, lw=0.5):
    draw.line([(px(x_pt), ry(y_top)), (px(x_pt), ry(y_bot))],
              fill=color, width=max(1, round(lw*S)))

def tl(txt, x_pt, y_base, f, color):
    draw.text((px(x_pt), ry(y_base) - f.size), txt, font=f, fill=color)

def tr(txt, x_pt, y_base, f, color):
    bb = draw.textbbox((0,0), txt, font=f)
    draw.text((px(x_pt)-(bb[2]-bb[0]), ry(y_base)-f.size), txt, font=f, fill=color)

def tc(txt, cx_pt, y_base, f, color):
    bb = draw.textbbox((0,0), txt, font=f)
    draw.text((px(cx_pt)-(bb[2]-bb[0])//2, ry(y_base)-f.size), txt, font=f, fill=color)

# ─── 1. HEADER  y: 321-351 ──────────────────────────────────────
fill(0, 321, 153, 30, CREAM)
hline(321, GOLD)

# Logo circle with "L"
cx, cy, r = px(19), ry(336), px(8)
draw.ellipse([cx-r, cy-r, cx+r, cy+r], outline=NAVY, width=max(1, round(1*S)))
tc("L", 19, 333, fnt("timesbd.ttf", 8), NAVY)

# Logo text
tl("LuxSmile",              36, 337, fnt("timesbd.ttf", 12), NAVY)
tl("MOBILE DENTAL HYGIENE", 36, 330, fnt("arialbd.ttf", 5),  NAVY)

# Right header
tr("LEASIDE & SURROUNDING", 148, 339, fnt("arialbd.ttf", 5), NAVY)
tr("TORONTO · ON",          148, 333, fnt("arialbd.ttf", 5), NAVY)

# ─── 2. PHOTO  y: 268-321 ───────────────────────────────────────
try:
    photo = Image.open(r"C:\Users\leili\luxsmile.github.io\dental.jpg").convert("RGB")
    ph_w, ph_h = px(153), px(53)
    sc = max(ph_w/photo.width, ph_h/photo.height)
    nw, nh = round(photo.width*sc), round(photo.height*sc)
    photo = photo.resize((nw, nh), Image.LANCZOS)
    ox, oy = (nw-ph_w)//2, (nh-ph_h)//2
    photo = photo.crop((ox, oy, ox+ph_w, oy+ph_h))
    img.paste(photo, (0, ry(321)))
except Exception as e:
    fill(0, 268, 153, 53, (80,110,140))
    print(f"Photo: {e}")

# ─── 3. NAVY BOX  y: 200-268 ────────────────────────────────────
fill(0, 200, 153, 68, NAVY)

tl("AT YOUR DOOR. OR OUR OFFICE.", 7, 260, fnt("arialbd.ttf", 5),  GOLD)
tl("Premium dental hygiene",       7, 251, fnt("timesbd.ttf", 9),  WHITE)
tl("that comes to you.",           7, 242, fnt("timesbd.ttf", 9),  WHITE)
tl("Quality, modern care within",  7, 231, fnt("arialbd.ttf", 8),  WHITE)
tl("your home, office, or care",   7, 223, fnt("arialbd.ttf", 8),  WHITE)
tl("residence. Registered Dental", 7, 215, fnt("arialbd.ttf", 8),  WHITE)
tl("Hygienist • 15+ years",        7, 207, fnt("arialbd.ttf", 8),  WHITE)
tl("Leili H Zarrabi, RDH",         7, 198, fnt("timesbd.ttf", 5),  GOLD)

# ─── 4. GOLD BAND  y: 158-200 ───────────────────────────────────
fill(0, 158, 153, 42, GOLD)

tl("FIRST-VISIT GIFT",        7, 195, fnt("arialbd.ttf", 5),  NAVY)
tl("Complimentary",           7, 186, fnt("timesbd.ttf", 7),  NAVY)
tl("Waterpik",                7, 174, fnt("timesbd.ttf", 12), NAVY)
tl("A $250+ value • While quantities last", 7, 167, fnt("arialbd.ttf", 5), NAVY)

# Vertical divider
vline(100, 160, 198, (180,150,90), lw=0.75)

# Right side phone
tl("CALL OR TEXT:", 103, 191, fnt("arialbd.ttf", 5),  NAVY)
tl("416·994·9669", 103, 175, fnt("arialbd.ttf", 10), NAVY)

# ─── 5. WHITENING STRIP  y: 140-158 ────────────────────────────
fill(0, 140, 153, 18, NAVY)
tc("TEETH WHITENING", 76, 151, fnt("arialbd.ttf", 6), GOLD)
tc("Advanced technology • Little to no sensitivity", 76, 143, fnt("arialbd.ttf", 5), WHITE)

# ─── 6. STATS  y: 106-140 (4 columns) ──────────────────────────
fill(0, 106, 153, 34, CREAM)
hline(140, GOLD); hline(106, GOLD)
for x in (38, 76, 114):
    vline(x, 106, 140, GOLD)

stats = [
    (19,  "15",     ["YEARS OF", "EXPERIENCE"],     "arialbd.ttf", 10),
    (57,  "CDCP",   ["& ALL", "INSURANCE"],          "arialbd.ttf", 7),
    (95,  "Direct", ["BILLING", "AVAILABLE"],        "timesbi.ttf", 7),
    (133, "Leaside",["& SURR.", "AREAS"],            "arialbd.ttf", 6),
]
for cx, big, sub, fname, fsize in stats:
    tc(big, cx, 128, fnt(fname, fsize), NAVY)
    for j, line in enumerate(sub):
        tc(line, cx, 119 - j*6, fnt("arial.ttf", 5), NAVY)

# ─── 7. SERVICES  y: 32-106 ─────────────────────────────────────
fill(0, 32, 153, 74, CREAM)
tl("OUR CARE",           7, 101, fnt("arialbd.ttf", 5),  GOLD)
tl("Full-service hygiene",7, 93,  fnt("timesbi.ttf", 9),  NAVY)
tl("Modern tech, gentle hands,", 7, 86, fnt("arialbd.ttf", 5), DARK)
tl("no rushed visits.",          7, 80, fnt("arialbd.ttf", 5), DARK)

left_svcs  = ["Complete Oral Exam", "Emergency Exam", "Teeth Cleaning",
               "Stain Removal", "Teeth Whitening", "Fluoride Treatment"]
right_svcs = ["Sealants", "Advanced Gum Therapy", "Children's Hygiene",
               "Seniors & Special Care", "Oral Health Education", "Referrals to Specialists"]

for i, (l, r) in enumerate(zip(left_svcs, right_svcs)):
    y = 73 - i*7
    tl("• " + l, 7,  y, fnt("arialbd.ttf", 5), NAVY)
    tl("• " + r, 79, y, fnt("arialbd.ttf", 5), NAVY)

# ─── 8. FOOTER  y: 0-32 ─────────────────────────────────────────
fill(0, 0, 153, 32, NAVY)
tl("TEXT TO BOOK",          7,  24, fnt("arialbd.ttf", 5),  GOLD)
tl("416·994·9669",          7,  11, fnt("arialbd.ttf", 11), WHITE)
tr("Leili H Zarrabi",       148, 22, fnt("timesbd.ttf", 7),  WHITE)
tr("REGISTERED DENTAL HYGIENIST", 148, 14, fnt("arialbd.ttf", 5), WHITE)

# ─── Save ────────────────────────────────────────────────────────
out_png = r"C:\Users\leili\luxsmile.github.io\luxsmile_magazine_original_300dpi.png"
out_jpg = r"C:\Users\leili\luxsmile.github.io\luxsmile_magazine_original_300dpi.jpg"

img.save(out_png, dpi=(300, 300))
img.save(out_jpg, dpi=(300, 300), quality=95, optimize=True)

for path in (out_png, out_jpg):
    kb = os.path.getsize(path) // 1024
    print(f"[OK] {os.path.basename(path)}  {kb} KB  ({W}x{H}px @ {DPI} DPI)")
