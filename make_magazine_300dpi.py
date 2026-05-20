"""
Renders luxsmile_magazine.png at exactly 300 DPI press quality.
Page: 2.125" x 4.875"  ->  638 x 1463 pixels @ 300 DPI
All fonts minimum 8pt per Leaside magazine print spec.
"""
from PIL import Image, ImageDraw, ImageFont
import os

DPI    = 300
W_IN, H_IN = 2.125, 4.875
W = round(W_IN * DPI)   # 638
H = round(H_IN * DPI)   # 1463
S = DPI / 72.0           # 1 pt -> pixels

NAVY  = (27,  42,  74)
GOLD  = (201, 169, 110)
CREAM = (250, 246, 239)
WHITE = (255, 255, 255)

def ry(pt_y):
    """reportlab y (0=bottom) -> PIL y (0=top)"""
    return round((351 - pt_y) * S)

def px(pt):
    return round(pt * S)

F = "C:/Windows/Fonts/"
_fc = {}
def font(name, pt):
    key = (name, pt)
    if key not in _fc:
        try:
            _fc[key] = ImageFont.truetype(F + name, round(pt * S))
        except:
            _fc[key] = ImageFont.load_default()
    return _fc[key]

img  = Image.new("RGB", (W, H), CREAM)
draw = ImageDraw.Draw(img)

def rect(x, yb, w, h, color):
    draw.rectangle([px(x), ry(yb+h), px(x+w), ry(yb)], fill=color)

def hline(y, color, x0=0, x1=153, lw=0.5):
    ypx = ry(y)
    draw.line([(px(x0), ypx), (px(x1), ypx)], fill=color, width=max(1, round(lw*S)))

def vline(x, y0, y1, color, lw=0.5):
    xpx = px(x)
    draw.line([(xpx, ry(y1)), (xpx, ry(y0))], fill=color, width=max(1, round(lw*S)))

def tl(txt, x, y, f, color):
    draw.text((px(x), ry(y) - f.size), txt, font=f, fill=color)

def tr(txt, x, y, f, color):
    bb = draw.textbbox((0, 0), txt, font=f)
    draw.text((px(x) - (bb[2]-bb[0]), ry(y) - f.size), txt, font=f, fill=color)

def tc(txt, y, f, color, cx=76.5):
    bb = draw.textbbox((0, 0), txt, font=f)
    draw.text((px(cx) - (bb[2]-bb[0])//2, ry(y) - f.size), txt, font=f, fill=color)

# ══ 1. HEADER  y: 321–351 ═══════════════════════════════════════
rect(0, 321, 153, 30, CREAM)
hline(321, GOLD)

try:
    logo = Image.open(r"C:\Users\leili\luxsmile.github.io\logo.png").convert("RGBA")
    logo_size = px(22)
    logo = logo.resize((logo_size, logo_size), Image.LANCZOS)
    img.paste(logo, (px(5), ry(349)), logo)
except Exception as e:
    print(f"Logo: {e}")

tl("LuxSmile",               32, 337, font("timesbd.ttf", 12), NAVY)
tl("MOBILE DENTAL HYGIENE",  32, 327, font("arialbd.ttf",  8), NAVY)
tr("Leaside & Surrounding",  149, 341, font("arialbd.ttf",  8), NAVY)

# ══ 2. PHOTO  y: 261–321 ════════════════════════════════════════
try:
    photo = Image.open(r"C:\Users\leili\luxsmile.github.io\dental.jpg").convert("RGB")
    ph_w, ph_h = px(153), px(60)
    scale = max(ph_w/photo.width, ph_h/photo.height)
    nw, nh = round(photo.width*scale), round(photo.height*scale)
    photo = photo.resize((nw, nh), Image.LANCZOS)
    ox, oy = (nw-ph_w)//2, (nh-ph_h)//2
    photo = photo.crop((ox, oy, ox+ph_w, oy+ph_h))
    img.paste(photo, (0, ry(321)))
except Exception as e:
    print(f"Photo: {e}")
    rect(0, 261, 153, 60, (80, 110, 140))

# ══ 3. HEADLINE BOX  y: 191–261 ═════════════════════════════════
rect(0, 191, 153, 70, NAVY)

tc("AT YOUR DOOR  ·  OR OUR OFFICE", 255, font("arialbd.ttf", 8), GOLD)
hline(251, GOLD, x0=12, x1=141)
tc("Premium dental hygiene", 241, font("timesbi.ttf", 11), WHITE)
tc("that comes to you.",      229, font("timesbi.ttf", 11), WHITE)
tc("416-994-9669",            216, font("arialbd.ttf",  9), WHITE)
tc("Leili H. Zarrabi, RDH",  204, font("timesi.ttf",   8), GOLD)

# ══ 4. GOLD GIFT BAND  y: 133–191 ═══════════════════════════════
rect(0, 133, 153, 58, GOLD)

tc("NEW CLIENT GIFT",       187, font("arialbd.ttf",  8), NAVY)
hline(184, NAVY, x0=20, x1=133, lw=0.4)
tc("Complimentary",         176, font("timesi.ttf",   8), NAVY)
tc("Waterpik",              162, font("timesbi.ttf", 16), NAVY)
tc("$250+ value",           149, font("arialbd.ttf",  8), NAVY)
tc("While quantities last", 139, font("arialbd.ttf",  8), NAVY)

# ══ 5. TEETH WHITENING  y: 115–133 ══════════════════════════════
rect(0, 115, 153, 18, NAVY)
tc("TEETH WHITENING", 124, font("arialbd.ttf", 8), GOLD)

# ══ 6. STATS  y: 83–115  (3 columns) ════════════════════════════
rect(0, 83, 153, 32, CREAM)
hline(115, GOLD)
hline(83,  GOLD)
vline(51,  83, 115, GOLD)
vline(102, 83, 115, GOLD)

stats = [
    (25,  "15+",    font("arialbd.ttf",  9), "YRS EXPERIENCE"),
    (76,  "CDCP",   font("arialbd.ttf",  9), "ALL INSURANCE"),
    (127, "Direct", font("timesbi.ttf",  9), "Billing Avail."),
]
for cx, big, fb, sub in stats:
    tc(big, 105, fb,                     NAVY, cx=cx)
    tc(sub,  94, font("arialbd.ttf", 8), NAVY, cx=cx)

# ══ 7. SERVICES  y: 30–83 ═══════════════════════════════════════
rect(0, 30, 153, 53, CREAM)

tl("Full-service hygiene", 7, 75, font("timesbi.ttf", 9), NAVY)

# Consolidated services — 4 items per column
left_svcs = [
    "Oral Examination",
    "Teeth Cleaning",
    "Teeth Whitening",
    "Fluoride Treatment",
]
right_svcs = [
    "All Ages Welcome",
    "Gum Therapy",
    "Sealants",
    "Referrals",
]

f8 = font("arialbd.ttf", 8)
for i, (l, r) in enumerate(zip(left_svcs, right_svcs)):
    y = 64 - i * 10
    tl("- " + l, 7,  y, f8, NAVY)
    tl("- " + r, 79, y, f8, NAVY)

# ══ 8. FOOTER  y: 0–30 ══════════════════════════════════════════
rect(0, 0, 153, 30, NAVY)

tl("TEXT TO BOOK:",           7,  24, font("arialbd.ttf",  8), GOLD)
tl("416-994-9669",            7,  13, font("arialbd.ttf", 11), WHITE)
tr("Leili H. Zarrabi, RDH", 148,  22, font("timesi.ttf",   8), WHITE)

# ── Save ─────────────────────────────────────────────────────────
out_png = r"C:\Users\leili\luxsmile.github.io\luxsmile_magazine_300dpi.png"
out_jpg = r"C:\Users\leili\luxsmile.github.io\luxsmile_magazine_300dpi.jpg"

img.save(out_png, dpi=(300, 300))
img.save(out_jpg, dpi=(300, 300), quality=95, optimize=True)

for path in (out_png, out_jpg):
    kb = os.path.getsize(path) // 1024
    print(f"[OK] {os.path.basename(path)}  {kb} KB  ({W}x{H}px @ {DPI} DPI)")
