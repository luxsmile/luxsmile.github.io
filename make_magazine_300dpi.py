"""
Renders luxsmile_magazine.png at exactly 300 DPI press quality.
Page: 2.125" x 4.875"  ->  638 x 1463 pixels @ 300 DPI
All fonts minimum 8pt per Leaside magazine print spec.

Layout (bottom to top in reportlab pts):
  Footer:       y   0 –  38   (38pt)
  Services:     y  38 – 126   (88pt)
  Stats:        y 126 – 164   (38pt)
  Whitening:    y 164 – 182   (18pt)
  Side-by-side: y 182 – 262   (80pt)   navy left | gold right
  Photo:        y 262 – 317   (55pt)
  Header:       y 317 – 351   (34pt)
  Total = 351pt
"""
from PIL import Image, ImageDraw, ImageFont
import os

DPI         = 300
W_IN, H_IN  = 2.125, 4.875
W = round(W_IN * DPI)   # 638
H = round(H_IN * DPI)   # 1463
S = DPI / 72.0           # 1 pt -> pixels

NAVY  = (27,  42,  74)
GOLD  = (201, 169, 110)
CREAM = (250, 246, 239)
WHITE = (255, 255, 255)
DARK  = (40,  40,  40)

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
    draw.rectangle([px(x), ry(yb + h), px(x + w), ry(yb)], fill=color)

def hline(y, color, x0=0, x1=153, lw=0.5):
    draw.line([(px(x0), ry(y)), (px(x1), ry(y))],
              fill=color, width=max(1, round(lw * S)))

def vline(x, y0, y1, color, lw=0.5):
    draw.line([(px(x), ry(y1)), (px(x), ry(y0))],
              fill=color, width=max(1, round(lw * S)))

def tl(txt, x, y, f, color):
    draw.text((px(x), ry(y) - f.size), txt, font=f, fill=color)

def tr(txt, x, y, f, color):
    bb = draw.textbbox((0, 0), txt, font=f)
    draw.text((px(x) - (bb[2] - bb[0]), ry(y) - f.size), txt, font=f, fill=color)

def tc(txt, y, f, color, cx=76.5):
    bb = draw.textbbox((0, 0), txt, font=f)
    draw.text((px(cx) - (bb[2] - bb[0]) // 2, ry(y) - f.size),
              txt, font=f, fill=color)


# ══ 1. HEADER  y: 317–351  (34pt) ═══════════════════════════════
rect(0, 317, 153, 34, CREAM)
hline(317, GOLD)

try:
    logo_path = r"C:\Users\leili\luxsmile.github.io\images\luxsmile-logo-navy.png"
    logo = Image.open(logo_path).convert("RGBA")
    logo_sz = px(33)                          # 33pt — fills the header nicely
    logo = logo.resize((logo_sz, logo_sz), Image.LANCZOS)
    header_px = round(34 * S)                 # header height in pixels
    top_y = (header_px - logo_sz) // 2        # vertically centred
    img.paste(logo, (px(2), top_y), logo)
except Exception as e:
    print(f"Logo: {e}")

tl("LuxSmile",              38, 338, font("timesbd.ttf", 12), NAVY)
tl("MOBILE DENTAL HYGIENE", 38, 326, font("arialbd.ttf",  8), NAVY)


# ══ 2. PHOTO  y: 262–317  (55pt) ════════════════════════════════
try:
    photo = Image.open(
        r"C:\Users\leili\luxsmile.github.io\dental.jpg"
    ).convert("RGB")
    ph_w, ph_h = px(153), px(55)
    scale = max(ph_w / photo.width, ph_h / photo.height)
    nw = round(photo.width  * scale)
    nh = round(photo.height * scale)
    photo = photo.resize((nw, nh), Image.LANCZOS)
    ox = (nw - ph_w) // 2
    oy = (nh - ph_h) // 2
    photo = photo.crop((ox, oy, ox + ph_w, oy + ph_h))
    img.paste(photo, (0, ry(317)))
except Exception as e:
    print(f"Photo: {e}")
    rect(0, 262, 153, 55, (70, 100, 130))

hline(262, GOLD)   # thin gold line between photo and side section


# ══ 3. SIDE-BY-SIDE  y: 182–262  (80pt) ═════════════════════════
#   Left navy column  x: 0–77
#   Right gold column x: 77–153

rect(0,  182, 77,  80, NAVY)   # navy left
rect(77, 182, 76,  80, GOLD)   # gold right
vline(77, 182, 262, CREAM, lw=1)   # cream divider line

# ── Navy left: "Premium dental hygiene" ──────────────────────────
tl("AT YOUR DOOR",     4, 254, font("arialbd.ttf", 8), GOLD)
tl("OR OUR OFFICE",   4, 244, font("arialbd.ttf", 8), GOLD)
hline(240, GOLD, x0=4, x1=73)

tc("Premium dental",    229, font("timesbi.ttf", 9), WHITE, cx=38)
tc("hygiene that",      219, font("timesbi.ttf", 9), WHITE, cx=38)
tc("comes to you.",     209, font("timesbi.ttf", 9), WHITE, cx=38)

tc("Leaside &",         197, font("arialbd.ttf", 8), GOLD,  cx=38)
tc("Surrounding",       187, font("arialbd.ttf", 8), GOLD,  cx=38)

# ── Gold right: "New Client Gift" ────────────────────────────────
tc("NEW CLIENT GIFT",   254, font("arialbd.ttf",  8), NAVY, cx=115)
hline(250, NAVY, x0=80, x1=150, lw=0.4)
tc("Complimentary",     241, font("timesi.ttf",   8), NAVY, cx=115)
tc("Waterpik",          227, font("timesbi.ttf", 14), NAVY, cx=115)
tc("$250+ value",       214, font("arialbd.ttf",  8), NAVY, cx=115)
tc("Call or Text:",     202, font("arialbd.ttf",  8), NAVY, cx=115)
tc("416·994·9669",      191, font("arialbd.ttf",  9), NAVY, cx=115)

hline(182, GOLD)   # bottom border of side section


# ══ 4. TEETH WHITENING  y: 164–182  (18pt) ══════════════════════
rect(0, 164, 153, 18, NAVY)
tc("TEETH WHITENING", 173, font("arialbd.ttf", 8), GOLD)


# ══ 5. STATS  y: 126–164  (38pt, 3 columns) ═════════════════════
rect(0, 126, 153, 38, CREAM)
hline(164, GOLD)
hline(126, GOLD)
vline(51,  126, 164, GOLD)
vline(102, 126, 164, GOLD)

stats = [
    (25,  "15+",    font("arialbd.ttf", 9), "Yrs. Exp."),
    (76,  "CDCP",   font("arialbd.ttf", 9), "+ All Plans"),
    (127, "Direct", font("timesbi.ttf", 9), "Billing"),
]
for cx, big, fb, sub in stats:
    tc(big, 150, fb,                     NAVY, cx=cx)
    tc(sub, 138, font("arialbd.ttf", 8), NAVY, cx=cx)


# ══ 6. SERVICES  y: 38–126  (88pt) ══════════════════════════════
rect(0, 38, 153, 88, CREAM)

tc("Full service hygiene",        118, font("timesbi.ttf", 9), NAVY)
tc("including, but not limited to:", 107, font("arialbd.ttf", 8), NAVY)

services = [
    "Complete oral examination",
    "Teeth cleaning",
    "Teeth whitening",
    "Sealant and fluoride treatment",
    "Referrals to specialists",
]
f8 = font("arialbd.ttf", 8)
for i, svc in enumerate(services):
    tl("•  " + svc, 12, 95 - i * 11, f8, NAVY)


# ══ 7. FOOTER  y: 0–38  (38pt) ══════════════════════════════════
rect(0, 0, 153, 38, NAVY)

tl("TEXT TO BOOK:",           7,  30, font("arialbd.ttf",  8), GOLD)
tl("416-994-9669",            7,  17, font("arialbd.ttf", 11), WHITE)
tr("Leili H. Zarrabi, RDH", 148,  28, font("timesi.ttf",   8), WHITE)


# ── Save ─────────────────────────────────────────────────────────
out_png = r"C:\Users\leili\luxsmile.github.io\luxsmile_magazine_300dpi.png"
out_jpg = r"C:\Users\leili\luxsmile.github.io\luxsmile_magazine_300dpi.jpg"

img.save(out_png, dpi=(300, 300))
img.save(out_jpg, dpi=(300, 300), quality=95, optimize=True)

for path in (out_png, out_jpg):
    kb = os.path.getsize(path) // 1024
    print(f"[OK] {os.path.basename(path)}  {kb} KB  ({W}x{H}px @ {DPI} DPI)")
