from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor
from reportlab.lib.utils import ImageReader
from PIL import Image as PILImage
import os

W, H = 153, 351
c = canvas.Canvas(r"C:\Users\leili\luxsmile.github.io\luxsmile_flyer.pdf", pagesize=(W, H))

GREEN = HexColor('#1B2A4A')   # Deep midnight navy
GOLD  = HexColor('#C9A96E')   # Champagne gold
CREAM = HexColor('#FAF6EF')   # Warm ivory
WHITE = HexColor('#ffffff')
DARK  = HexColor('#1a1a1a')

# ── Pre-process dental photo ─────────────────────────────────────
PHOTO_H = 53
img = PILImage.open(r"C:\Users\leili\luxsmile.github.io\dental.jpg").convert("RGB")
iw, ih = img.size
scale = max(W / iw, PHOTO_H / ih)
nw, nh = int(iw * scale), int(ih * scale)
img = img.resize((nw, nh), PILImage.Resampling.LANCZOS)
left = (nw - W) // 2
top  = (nh - PHOTO_H) // 2
img  = img.crop((left, top, left + W, top + PHOTO_H))
img.save(r"C:\Users\leili\luxsmile.github.io\dental_flyer.jpg", "JPEG", quality=80)

# ════════════════════════════════════════════════════════════
# 1. HEADER  y: 321–351  (30 pt)
# ════════════════════════════════════════════════════════════
c.setFillColor(CREAM)
c.rect(0, 321, W, 30, fill=1, stroke=0)
c.setStrokeColor(GOLD)
c.setLineWidth(0.5)
c.line(0, 321, W, 321)

# Logo
c.drawImage(r"C:\Users\leili\luxsmile.github.io\logo.png",
            4, 323, width=26, height=26, mask='auto', preserveAspectRatio=True)

# Brand name & tagline
c.setFillColor(GREEN)
c.setFont("Times-Bold", 12)
c.drawString(32, 337, "LuxSmile")
c.setFont("Helvetica-Bold", 4.5)
c.drawString(32, 330, "MOBILE DENTAL HYGIENE")

# Location — right corner
c.setFont("Helvetica", 3.5)
c.drawRightString(150, 326, "Leaside & Surrounding Area")

# ════════════════════════════════════════════════════════════
# 2. PHOTO  y: 268–321  (53 pt)
# ════════════════════════════════════════════════════════════
c.saveState()
p = c.beginPath()
p.rect(0, 268, W, 53)
c.clipPath(p, stroke=0)
c.drawImage(r"C:\Users\leili\luxsmile.github.io\dental_flyer.jpg",
            0, 268, width=W, height=53)
c.restoreState()

# ════════════════════════════════════════════════════════════
# 3. GREEN HEADLINE BOX  y: 200–268  (68 pt)
# ════════════════════════════════════════════════════════════
c.setFillColor(GREEN)
c.rect(0, 200, W, 68, fill=1, stroke=0)

# Eyebrow
c.setFillColor(GOLD)
c.setFont("Helvetica-Bold", 5)
c.drawCentredString(W/2, 260, "AT YOUR DOOR  OR  OUR OFFICE")

c.setStrokeColor(GOLD)
c.setLineWidth(0.5)
c.line(12, 257, W - 12, 257)

# Main headline
c.setFillColor(WHITE)
c.setFont("Times-Italic", 9)
c.drawCentredString(W/2, 247, "Premium dental hygiene")
c.drawCentredString(W/2, 236, "that comes to you.")

# Phone number
c.setFont("Helvetica-Bold", 9)
c.drawCentredString(W/2, 224, "416-994-9669")

# Name
c.setFillColor(GOLD)
c.setFont("Times-Italic", 6.5)
c.drawCentredString(W/2, 212, "Leili H Zarrabi, RDH")

# ════════════════════════════════════════════════════════════
# 4. GOLD GIFT BAND  y: 158–200  (42 pt)
# ════════════════════════════════════════════════════════════
c.setFillColor(GOLD)
c.rect(0, 158, W, 42, fill=1, stroke=0)

c.setFillColor(GREEN)
c.setFont("Helvetica-Bold", 5)
c.drawCentredString(W/2, 196, "*  FIRST-VISIT GIFT  *")

c.setStrokeColor(GREEN)
c.setLineWidth(0.4)
c.line(18, 193, W - 18, 193)

c.setFont("Times-Italic", 6)
c.drawCentredString(W/2, 184, "Complimentary")

c.setFont("Times-Italic", 13)
c.drawCentredString(W/2, 172, "Waterpik")

c.setFont("Helvetica", 4)
c.drawCentredString(W/2, 162, "A $250+ value  (While quantities last.)")

# ════════════════════════════════════════════════════════════
# 5. TEETH WHITENING  y: 138–158  (20 pt)
# ════════════════════════════════════════════════════════════
c.setFillColor(GREEN)
c.rect(0, 138, W, 20, fill=1, stroke=0)

c.setStrokeColor(GOLD)
c.setLineWidth(0.4)
c.line(7, 153, 40, 153)
c.line(113, 153, 146, 153)

c.setFillColor(GOLD)
c.setFont("Helvetica-Bold", 5)
c.drawCentredString(W/2, 151, "TEETH WHITENING")

c.setFillColor(WHITE)
c.setFont("Times-Italic", 5.5)
c.drawCentredString(W/2, 142, "Advanced technology  -  Little to no sensitivity")

# ════════════════════════════════════════════════════════════
# 6. STATS  y: 108–138  (30 pt)  — 3 columns
# ════════════════════════════════════════════════════════════
c.setFillColor(CREAM)
c.rect(0, 108, W, 30, fill=1, stroke=0)

c.setStrokeColor(GOLD)
c.setLineWidth(0.5)
c.line(0, 138, W, 138)
c.line(0, 108, W, 108)
c.line(51, 108, 51, 138)
c.line(102, 108, 102, 138)

stats = [
    (25,  "15",     ["YRS", "EXP"]),
    (76,  "CDCP",   ["& All Insurance", "Plans Accepted"]),
    (127, "Direct", ["BILLING", "AVAILABLE"]),
]
for cx, big, sub in stats:
    c.setFillColor(GREEN)
    c.setFont("Helvetica-Bold", 8)
    c.drawCentredString(cx, 127, big)
    c.setFont("Helvetica", 3.5)
    for j, line in enumerate(sub):
        c.drawCentredString(cx, 120 - j * 7, line)

# ════════════════════════════════════════════════════════════
# 7. SERVICES  y: 32–108  (76 pt)
# ════════════════════════════════════════════════════════════
c.setFillColor(CREAM)
c.rect(0, 32, W, 76, fill=1, stroke=0)

c.setFillColor(GOLD)
c.setFont("Helvetica", 4)
c.drawString(7, 101, "OUR CARE")

c.setFillColor(GREEN)
c.setFont("Times-Italic", 8)
c.drawString(7, 93, "Full-service hygiene")

c.setFillColor(DARK)
c.setFont("Helvetica", 3.8)
c.drawString(7, 85, "Modern technology, gentle hands, no rushed visits.")

left  = ["Complete Oral Exam", "Teeth Cleaning", "Stain Removal",
         "Fluoride Treatments", "Sealants (Cavity Protection)"]
right = ["Advanced Gum Therapy", "Children's Hygiene",
         "Seniors & Special Care", "Oral Health Education", "Referrals to Specialists"]

for i, (l, r) in enumerate(zip(left, right)):
    y = 78 - i * 8
    c.setFillColor(GREEN)
    c.setFont("Helvetica", 3.8)
    c.drawString(7,  y, "- " + l)
    c.drawString(79, y, "- " + r)

# ════════════════════════════════════════════════════════════
# 8. FOOTER  y: 0–32  (32 pt)
# ════════════════════════════════════════════════════════════
c.setFillColor(GREEN)
c.rect(0, 0, W, 32, fill=1, stroke=0)

c.setFillColor(GOLD)
c.setFont("Helvetica-Bold", 5)
c.drawString(7, 24, "TEXT OR CALL:")

c.setFillColor(WHITE)
c.setFont("Helvetica-Bold", 10)
c.drawString(7, 12, "416-994-9669")

c.setFont("Times-Italic", 6.5)
c.drawRightString(148, 17, "Leili H Zarrabi, RDH")

c.setFont("Helvetica", 3.5)
c.drawRightString(148, 9, "REGISTERED DENTAL HYGIENIST")

c.save()

size_kb = os.path.getsize(r"C:\Users\leili\luxsmile.github.io\luxsmile_flyer.pdf") // 1024
print("[OK] luxsmile_flyer.pdf created")
print(f"     Size : {size_kb} KB")
