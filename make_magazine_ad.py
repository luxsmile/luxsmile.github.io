from reportlab.pdfgen import canvas
from reportlab.lib.colors import CMYKColor
from reportlab.lib.utils import ImageReader
from PIL import Image
import qrcode
import os

# Page size: 2.125" x 4.875" = 153 x 351 points
W, H = 153, 351

BASE = r"C:\Users\leili\luxsmile.github.io"

# ── Prepare dental photo (cropped to fit, compressed) ────────────
dental_compressed = os.path.join(BASE, "dental_compressed.jpg")
try:
    dental_img = Image.open(os.path.join(BASE, "dental.jpg")).convert("RGB")
    # Photo area is 153 x 54 pt -> ~300 DPI: 638 x 225 px
    target_w, target_h = 640, 226
    sc = max(target_w / dental_img.width, target_h / dental_img.height)
    nw, nh = round(dental_img.width * sc), round(dental_img.height * sc)
    dental_img = dental_img.resize((nw, nh), Image.Resampling.LANCZOS)
    ox, oy = (nw - target_w) // 2, (nh - target_h) // 2
    dental_img = dental_img.crop((ox, oy, ox + target_w, oy + target_h))
    dental_img.save(dental_compressed, "JPEG", quality=80, optimize=True)
except Exception as e:
    print(f"Photo prep: {e}")

# ── Generate QR code -> luxsmile.ca ──────────────────────────────
qr_path = os.path.join(BASE, "qr_luxsmile.png")
qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_M, border=2)
qr.add_data("https://luxsmile.ca")
qr.make(fit=True)
qr_img = qr.make_image(fill_color="black", back_color="white")
qr_img.save(qr_path)

c = canvas.Canvas(os.path.join(BASE, "luxsmile_magazine.pdf"), pagesize=(W, H))
c.setPageCompression(1)

# ── CMYK colors matching luxsmile.ca (newsprint-safe) ────────────
# Website: charcoal black #1f1d1a, champagne gold #ccb180, white
CHARCOAL = CMYKColor(0, 0, 0, 1.0)            # 100K black, crisp on newsprint
GOLD     = CMYKColor(0.00, 0.13, 0.37, 0.20)  # champagne gold #ccb180
WHITE    = CMYKColor(0, 0, 0, 0)
BLACK    = CMYKColor(0, 0, 0, 1.0)

# ═════════════════════════════════════════════════════════════════
# 1. HEADER  y: 309-351  (42 pt) — white, logo, black + gold brand
# ═════════════════════════════════════════════════════════════════
c.setFillColor(WHITE)
c.rect(0, 309, W, 42, fill=1, stroke=0)

try:
    logo = ImageReader(os.path.join(BASE, "logo.png"))
    c.drawImage(logo, 5, 313, width=34, height=34,
                mask='auto', preserveAspectRatio=True)
except Exception as e:
    print(f"Logo: {e}")

c.setFont("Times-Bold", 18)
c.setFillColor(BLACK)
c.drawString(42, 332, "LuxSmile")

c.setFont("Helvetica-Bold", 8)
c.setFillColor(GOLD)
c.drawString(42, 320, "MOBILE DENTAL")
c.drawString(42, 311.5, "HYGIENE")

c.setStrokeColor(GOLD)
c.setLineWidth(1)
c.line(0, 309, W, 309)

# ═════════════════════════════════════════════════════════════════
# 2. PHOTO  y: 255-309  (54 pt)
# ═════════════════════════════════════════════════════════════════
try:
    photo = ImageReader(dental_compressed)
    c.drawImage(photo, 0, 255, width=W, height=54)
except Exception:
    c.setFillColor(CHARCOAL)
    c.rect(0, 255, W, 54, fill=1, stroke=0)

# ═════════════════════════════════════════════════════════════════
# 3. CHARCOAL HEADLINE BLOCK  y: 205-255  (50 pt) — like site hero
# ═════════════════════════════════════════════════════════════════
c.setFillColor(CHARCOAL)
c.rect(0, 205, W, 50, fill=1, stroke=0)

c.setFont("Helvetica-Bold", 6)
c.setFillColor(GOLD)
c.drawCentredString(W/2, 245, "LEASIDE  &  SURROUNDING  AREAS")

c.setFont("Times-Bold", 12)
c.setFillColor(WHITE)
c.drawCentredString(W/2, 231, "Premium dental hygiene")
c.drawCentredString(W/2, 218, "that comes to you.")

c.setFont("Times-BoldItalic", 7.5)
c.setFillColor(GOLD)
c.drawCentredString(W/2, 208.5, "Leili H Zarrabi, RDH  ·  15+ years")

# ═════════════════════════════════════════════════════════════════
# 4. GIFT CARD  y: 145-205  (60 pt) — white card, gold double frame
# ═════════════════════════════════════════════════════════════════
c.setFillColor(WHITE)
c.rect(0, 145, W, 60, fill=1, stroke=0)

c.setStrokeColor(GOLD)
c.setLineWidth(1.2)
c.rect(6, 148, W - 12, 54, fill=0, stroke=1)
c.setLineWidth(0.4)
c.rect(9, 151, W - 18, 48, fill=0, stroke=1)

c.setFont("Helvetica-Bold", 6.5)
c.setFillColor(GOLD)
c.drawCentredString(W/2, 191, "F I R S T - V I S I T   G I F T")

c.setFont("Times-BoldItalic", 11)
c.setFillColor(BLACK)
c.drawCentredString(W/2, 179, "Complimentary")

c.setFont("Times-Bold", 20)
c.setFillColor(BLACK)
c.drawCentredString(W/2, 161, "Waterpik")

c.setFont("Helvetica-Bold", 5.8)
c.setFillColor(BLACK)
c.drawCentredString(W/2, 153.5, "A $250+ value  ·  While quantities last")

# ═════════════════════════════════════════════════════════════════
# 5. WHITENING STRIP  y: 123-145  (22 pt) — charcoal with gold
# ═════════════════════════════════════════════════════════════════
c.setFillColor(CHARCOAL)
c.rect(0, 123, W, 22, fill=1, stroke=0)

c.setFont("Helvetica-Bold", 9.5)
c.setFillColor(GOLD)
c.drawCentredString(W/2, 135, "TEETH  WHITENING")

c.setFont("Helvetica-Bold", 5.5)
c.setFillColor(WHITE)
c.drawCentredString(W/2, 126.5, "Advanced technology  ·  Little to no sensitivity")

# ═════════════════════════════════════════════════════════════════
# 6. SERVICES  y: 58-123  (65 pt) — white, black text, essentials
# ═════════════════════════════════════════════════════════════════
c.setFillColor(WHITE)
c.rect(0, 58, W, 65, fill=1, stroke=0)

c.setFont("Helvetica-Bold", 6)
c.setFillColor(GOLD)
c.drawCentredString(W/2, 114, "O U R   C A R E")

services = [
    "Full Mouth Examination",
    "Thorough Teeth Cleaning",
    "Children's & Seniors' Cleaning",
    "Referrals to Specialists",
]
c.setFillColor(BLACK)
y = 103
for s in services:
    c.setFont("Helvetica-Bold", 7.5)
    c.drawCentredString(W/2, y, s)
    y -= 10

c.setStrokeColor(GOLD)
c.setLineWidth(0.5)
c.line(14, 68, W - 14, 68)
c.setFont("Helvetica-Bold", 6.5)
c.setFillColor(BLACK)
c.drawCentredString(W/2, 60.5, "CDCP & all insurance plans  ·  Direct billing")

# ═════════════════════════════════════════════════════════════════
# 7. FOOTER  y: 0-58  (58 pt) — charcoal, phone + website + QR code
# ═════════════════════════════════════════════════════════════════
c.setFillColor(CHARCOAL)
c.rect(0, 0, W, 58, fill=1, stroke=0)

# QR code on right (white tile so it scans on newsprint)
QR_S = 42
c.setFillColor(WHITE)
c.rect(W - QR_S - 8, 8, QR_S, QR_S, fill=1, stroke=0)
c.drawImage(ImageReader(qr_path), W - QR_S - 8, 8, width=QR_S, height=QR_S)

# Left side: call to action
c.setFont("Helvetica-Bold", 6)
c.setFillColor(GOLD)
c.drawString(8, 45, "CALL OR TEXT TO BOOK")

c.setFont("Helvetica-Bold", 12.5)
c.setFillColor(WHITE)
c.drawString(8, 31, "416·994·9669")

c.setFont("Times-Bold", 10)
c.setFillColor(GOLD)
c.drawString(8, 17, "luxsmile.ca")

c.setFont("Helvetica-Bold", 5)
c.setFillColor(WHITE)
c.drawString(8, 8, "SCAN TO VISIT OUR WEBSITE")

# ═════════════════════════════════════════════════════════════════
c.save()

size_kb = os.path.getsize(os.path.join(BASE, "luxsmile_magazine.pdf")) // 1024
print("[OK] Magazine flyer created: luxsmile_magazine.pdf")
print(f"  Size: {size_kb} KB")
print(f"  Dimensions: 2.125 x 4.875 inches")
print(f"  Colors: website palette - charcoal black + champagne gold + white")
print(f"  QR code links to https://luxsmile.ca")
