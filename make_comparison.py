"""
Places the burgundy and bronze magazine ads side by side on one wide page,
so they can be compared in a single view.
"""
import os
from pypdf import PdfReader, PdfWriter, Transformation, PageObject

BASE = r"C:\Users\leili\luxsmile.github.io"
LEFT  = os.path.join(BASE, "luxsmile_magazine.pdf")          # burgundy
RIGHT = os.path.join(BASE, "luxsmile_magazine_bronze.pdf")   # bronze
OUT   = os.path.join(BASE, "luxsmile_magazine_compare.pdf")

GAP = 24  # points of white space between the two ads

p_left  = PdfReader(LEFT).pages[0]
p_right = PdfReader(RIGHT).pages[0]

w = float(p_left.mediabox.width)
h = float(p_left.mediabox.height)

canvas = PageObject.create_blank_page(width=w * 2 + GAP, height=h)
canvas.merge_transformed_page(p_left,  Transformation().translate(0, 0))
canvas.merge_transformed_page(p_right, Transformation().translate(w + GAP, 0))

writer = PdfWriter()
writer.add_page(canvas)
with open(OUT, "wb") as f:
    writer.write(f)

print(f"[OK] Side-by-side comparison created: {os.path.basename(OUT)}")
print("  Left: burgundy   |   Right: bronze")
