from reportlab.pdfgen import canvas
from reportlab.lib.colors import CMYKColor
from reportlab.lib.utils import ImageReader
from PIL import Image
import os

W, H = 153, 351  # 2.125" x 4.875" in points

# ── Pre-process dental photo ────────────────────────────────────────
PHOTO_H = 60  # points tall for photo section
try:
    img = Image.open(r"C:\Users\leili\luxsmile.github.io\dental.jpg").convert("RGB")
    scale = max(W / img.width, PHOTO_H / img.height)
    nw = int(img.width * scale)
    nh = int(img.height * scale)
    img = img.resize((nw, nh), Image.Resampling.LANCZOS)
    left = (nw - W) // 2
    top  = (nh - PHOTO_H) // 2
    img  = img.crop((left, top, left + W, top + PHOTO_H))
    img.save(r"C:\Users\leili\luxsmile.github.io\dental_compressed.jpg", "JPEG", quality=80)
except Exception as e:
    print(f"Photo prep error: {e}")

# ── CMYK colors ─────────────────────────────────────────────────────
NAVY  = CMYKColor(0.89, 0.78, 0.34, 0.51)   # deep navy
GOLD  = CMYKColor(0.00, 0.16, 0.45, 0.21)   # champagne gold
CREAM = CMYKColor(0.00, 0.02, 0.04, 0.02)   # warm ivory
WHITE = CMYKColor(0, 0, 0, 0)
BLACK = CMYKColor(0, 0, 0, 1.0)             # 100K only

# ── Canvas ───────────────────────────────────────────────────────────
c = canvas.Canvas(
    r"C:\Users\leili\luxsmile.github.io\luxsmile_magazine.pdf",
    pagesize=(W, H)
)
c.setPageCompression(1)

# ════════════════════════════════════════════════════════════════
# 1. HEADER  y: 321–351  (30 pt)
# ════════════════════════════════════════════════════════════════
c.setFillColor(CREAM)
c.rect(0, 321, W, 30, fill=1, stroke=0)

# gold bottom rule
c.setStrokeColor(GOLD)
c.setLineWidth(0.5)
c.line(0, 321, W, 321)

# Logo image (PNG with transparency)
try:
    logo = ImageReader(r"C:\Users\leili\luxsmile.github.io\logo.png")
    c.drawImage(logo, 4, 323, width=26, height=26, mask="auto",
                preserveAspectRatio=True)
    logo_right = 34
except Exception as e:
    print(f"Logo error: {e}")
    c.setStrokeColor(NAVY)
    c.setLineWidth(1)
    c.circle(16, 336, 11, fill=0, stroke=1)
    c.setFont("Times-Bold", 9)
    c.setFillColor(NAVY)
    c.drawCentredString(16, 333, "L")
    logo_right = 31

# Brand name & tagline
c.setFont("Times-Bold", 12)
c.setFillColor(NAVY)
c.drawString(logo_right + 2, 337, "LuxSmile")

c.setFont("Helvetica-Bold", 4.5)
c.setFillColor(NAVY)
c.drawString(logo_right + 2, 329, "MOBILE DENTAL HYGIENE")

# Location (right-aligned)
c.setFont("Helvetica-Bold", 4)
c.setFillColor(NAVY)
c.drawRightString(149, 337, "LEASIDE & SURROUNDING AREA")

# ════════════════════════════════════════════════════════════════
# 2. PHOTO  y: 261–321  (60 pt)
# ════════════════════════════════════════════════════════════════
try:
    photo = ImageReader(r"C:\Users\leili\luxsmile.github.io\dental_compressed.jpg")
    c.drawImage(photo, 0, 261, width=W, height=60)
except:
    c.setFillColor(CMYKColor(0.5, 0.25, 0.15, 0.35))
    c.rect(0, 261, W, 60, fill=1, stroke=0)
    c.setFillColor(WHITE)
    c.setFont("Helvetica-Bold", 7)
    c.drawCentredString(W/2, 289, "[dental photo]")

# ════════════════════════════════════════════════════════════════
# 3. HEADLINE BOX  y: 191–261  (70 pt)
# ════════════════════════════════════════════════════════════════
c.setFillColor(NAVY)
c.rect(0, 191, W, 70, fill=1, stroke=0)

# Eyebrow
c.setFont("Helvetica-Bold", 5)
c.setFillColor(GOLD)
c.drawCentredString(W/2, 255, "AT YOUR DOOR  OR  OUR OFFICE")

c.setStrokeColor(GOLD)
c.setLineWidth(0.5)
c.line(12, 252, W - 12, 252)

# Main headline
c.setFont("Times-Bold", 11)
c.setFillColor(WHITE)
c.drawCentredString(W/2, 241, "Premium dental hygiene")
c.drawCentredString(W/2, 229, "that comes to you.")

# Service area
c.setFont("Helvetica-Bold", 6)
c.setFillColor(WHITE)
c.drawCentredString(W/2, 215, "Leaside & Surrounding Area")

c.line(12, 206, W - 12, 206)

# Byline
c.setFont("Times-Bold", 6.5)
c.setFillColor(GOLD)
c.drawCentredString(W/2, 197, "Leili H Zarrabi, RDH")

# ════════════════════════════════════════════════════════════════
# 4. WATERPIK GIFT BAND  y: 133–191  (58 pt)
# ════════════════════════════════════════════════════════════════
c.setFillColor(GOLD)
c.rect(0, 133, W, 58, fill=1, stroke=0)

c.setFont("Helvetica-Bold", 5)
c.setFillColor(NAVY)
c.drawCentredString(W/2, 185, "*  FIRST-VISIT GIFT  *")

c.setStrokeColor(NAVY)
c.setLineWidth(0.4)
c.line(18, 182, W - 18, 182)

c.setFont("Times-Bold", 7.5)
c.setFillColor(NAVY)
c.drawCentredString(W/2, 173, "Complimentary")

c.setFont("Times-Bold", 16)
c.setFillColor(NAVY)
c.drawCentredString(W/2, 159, "Waterpik")

c.setFont("Helvetica-Bold", 5)
c.setFillColor(NAVY)
c.drawCentredString(W/2, 151, "A $250+ value  (While quantities last)")

c.line(18, 147, W - 18, 147)

# Phone CTA – centered, fits full width
c.setFont("Helvetica-Bold", 5.5)
c.setFillColor(NAVY)
c.drawCentredString(W/2, 141, "CALL OR TEXT TO BOOK:")

c.setFont("Helvetica-Bold", 10)
c.setFillColor(NAVY)
c.drawCentredString(W/2, 133, "416-994-9669")

# ════════════════════════════════════════════════════════════════
# 5. TEETH WHITENING STRIP  y: 115–133  (18 pt)
# ════════════════════════════════════════════════════════════════
c.setFillColor(NAVY)
c.rect(0, 115, W, 18, fill=1, stroke=0)

c.setFont("Helvetica-Bold", 7)
c.setFillColor(GOLD)
c.drawCentredString(W/2, 125, "TEETH WHITENING")

c.setFont("Helvetica-Bold", 5)
c.setFillColor(WHITE)
c.drawCentredString(W/2, 117, "Advanced technology  -  Little to no sensitivity")

# ════════════════════════════════════════════════════════════════
# 6. STATS ROW  y: 83–115  (32 pt)
# ════════════════════════════════════════════════════════════════
c.setFillColor(CREAM)
c.rect(0, 83, W, 32, fill=1, stroke=0)

c.setStrokeColor(GOLD)
c.setLineWidth(0.5)
c.line(0, 115, W, 115)
c.line(0, 83, W, 83)
# vertical dividers
for x in (38, 76, 114):
    c.line(x, 83, x, 115)

stats = [
    (19,  "15",     ["YRS", "EXP"]),
    (57,  "CDCP",   ["ALL PLANS", "ACCEPTED"]),
    (95,  "Direct", ["BILLING", "AVAILABLE"]),
    (133, "Leaside",["& AREA", "SERVICE"]),
]
for cx, big, sub in stats:
    c.setFont("Helvetica-Bold", 9)
    c.setFillColor(NAVY)
    c.drawCentredString(cx, 102, big)
    c.setFont("Helvetica-Bold", 4.5)
    for j, line in enumerate(sub):
        c.drawCentredString(cx, 95 - j * 7, line)

# ════════════════════════════════════════════════════════════════
# 7. SERVICES  y: 30–83  (53 pt)
# ════════════════════════════════════════════════════════════════
c.setFillColor(CREAM)
c.rect(0, 30, W, 53, fill=1, stroke=0)

c.setFont("Helvetica-Bold", 5)
c.setFillColor(GOLD)
c.drawString(7, 77, "OUR SERVICES")

c.setFont("Times-Bold", 8.5)
c.setFillColor(NAVY)
c.drawString(7, 69, "Full-service hygiene")

left_svcs  = ["Complete Oral Exam", "Teeth Cleaning", "Stain Removal",
               "Fluoride Treatment", "Sealants (Cavity Protection)"]
right_svcs = ["Advanced Gum Therapy", "Children's Hygiene", "Seniors & Special Care",
               "Oral Health Education", "Referrals"]

c.setFont("Helvetica-Bold", 4.5)
c.setFillColor(NAVY)
for i, (l, r) in enumerate(zip(left_svcs, right_svcs)):
    y = 61 - i * 7
    c.drawString(7,  y, "- " + l)
    c.drawString(79, y, "- " + r)

# ════════════════════════════════════════════════════════════════
# 8. FOOTER  y: 0–30  (30 pt)
# ════════════════════════════════════════════════════════════════
c.setFillColor(NAVY)
c.rect(0, 0, W, 30, fill=1, stroke=0)

c.setFont("Helvetica-Bold", 5)
c.setFillColor(GOLD)
c.drawString(7, 22, "TEXT OR CALL:")

# Large phone number – full legibility
c.setFont("Helvetica-Bold", 12)
c.setFillColor(WHITE)
c.drawString(7, 9, "416-994-9669")

# Name & credential (right side)
c.setFont("Times-Bold", 6.5)
c.setFillColor(WHITE)
c.drawRightString(148, 21, "Leili H Zarrabi, RDH")

c.setFont("Helvetica-Bold", 4)
c.setFillColor(WHITE)
c.drawRightString(148, 13, "REGISTERED DENTAL HYGIENIST")


# ════════════════════════════════════════════════════════════════
c.save()

size_kb = os.path.getsize(r"C:\Users\leili\luxsmile.github.io\luxsmile_magazine.pdf") // 1024
print("[OK] luxsmile_magazine.pdf created")
print(f"     Size : {size_kb} KB")
print(f"     Page : 2.125 x 4.875 inches (PDF points: 153 x 351)")
print(f"     Color: CMYK, 100K black only")
