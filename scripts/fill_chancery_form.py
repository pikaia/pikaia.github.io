"""Fill page 1 of the Chancery of the Roman Catholic Archdiocese of
Singapore "Archival Holdings Search Request Form" (v.3, 1 Jun 2018) and
append an itemised attachment page.

The blank form is a flat PDF (no AcroForm fields), so text is stamped at
fixed coordinates via a reportlab overlay merged with pypdf. Field values
come from a JSON file (see docs/copyright/chancery-request-*.json). One
request per post/video, per the Chancery's terms.

    python scripts/fill_chancery_form.py \
        --template docs/copyright/ArchivalHoldingsSearchRequestForm_v3-1Jun2018.pdf \
        --data     docs/copyright/chancery-request-2026-08-jalan-payoh-lai.json \
        --out      docs/copyright/chancery-request-2026-08-jalan-payoh-lai-FILLED.pdf \
        --sign

With --sign, the requestor's name is rendered in a script font in the
"Signature of requestor" box on page 2 (the same thing DocuSign / Google
do when you type your name) - it is Chris's own name on his own request,
at his direction. The script never submits anything.
"""
import argparse
import json
import os
import textwrap
from io import BytesIO

from pypdf import PdfReader, PdfWriter
from reportlab.lib.colors import Color
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas

PAGE_W, PAGE_H = 595.2, 841.8
FONT = "Helvetica"

# Script font for the typed signature. Segoe Script ships with Windows;
# fall back to Ink Free, then to Helvetica-Oblique if neither is present.
_SCRIPT_CANDIDATES = [
    ("SegoeScript", r"C:\Windows\Fonts\segoesc.ttf"),
    ("InkFree", r"C:\Windows\Fonts\Inkfree.ttf"),
]

# Page-2 "Signature of requestor" box, PDF points (origin bottom-left).
SIGNATURE_POS = (398, 690)
SIGNATURE_SIZE = 22

# (x, y) baselines in PDF points, origin bottom-left. Tuned against the
# blank v.3 form; see the --debug crosshair overlay when adjusting.
POS = {
    "full_name":        (138, 536),
    "organization":     (138, 515),
    "email":            (138, 488),
    "contact_no":       (470, 488),
    "date_of_enquiry":  (138, 468),
    "purpose_academic": (150, 416),   # "X" on the blank before "Academic/ educational"
    "usage_title":      (315, 373),   # after the "Title of publication:" label
    "usage_publisher":  (222, 344),
    "usage_language":   (300, 305),
    "description":      (138, 278),
}
USAGE_TITLE_WRAP = 40
USAGE_TITLE_LEADING = 11
DESC_WRAP = 66            # chars per line in the description box
DESC_LEADING = 12.5


def _overlay_page1(data):
    buf = BytesIO()
    c = canvas.Canvas(buf, pagesize=(PAGE_W, PAGE_H))
    c.setFillColor(Color(0, 0, 0.55))   # dark blue, reads as "filled in"

    def put(key, text, size=10):
        x, y = POS[key]
        c.setFont(FONT, size)
        c.drawString(x, y, text)

    put("full_name", data["full_name"], 10)
    # underline the surname
    s = data.get("surname_start_char")
    if s is not None:
        x, y = POS["full_name"]
        c.setFont(FONT, 10)
        pre = c.stringWidth(data["full_name"][:s], FONT, 10)
        sur = c.stringWidth(data["full_name"][s:], FONT, 10)
        c.setLineWidth(0.6)
        c.line(x + pre, y - 1.0, x + pre + sur, y - 1.0)

    put("organization", data["organization"], 9.5)
    put("email", data["email"], 10)
    put("contact_no", data["contact_no"], 10)
    put("date_of_enquiry", data["date_of_enquiry"], 10)

    if data.get("purpose") == "academic":
        x, y = POS["purpose_academic"]
        c.setFont("Helvetica-Bold", 11)
        c.drawString(x, y, "X")

    # "Information about intended usage" is the Chancery's commercial-only
    # sub-block; skip it for a non-commercial request (the Description box
    # and attachment carry the detail).
    if data.get("fill_intended_usage"):
        x, y = POS["usage_title"]
        c.setFont(FONT, 8.5)
        for i, ln in enumerate(textwrap.wrap(data["usage_title"], USAGE_TITLE_WRAP)[:2]):
            c.drawString(x, y - i * USAGE_TITLE_LEADING, ln)
        put("usage_publisher", data["usage_publisher"], 8.5)
        put("usage_language", data["usage_language"], 9)

    x, y = POS["description"]
    c.setFont(FONT, 8.5)
    line = 0
    for para in data["description_box"].split("\n"):
        for ln in textwrap.wrap(para, DESC_WRAP) or [""]:
            c.drawString(x, y - line * DESC_LEADING, ln)
            line += 1

    if data.get("_debug"):
        c.setFillColor(Color(1, 0, 0))
        for k, (px, py) in POS.items():
            c.setFont(FONT, 4)
            c.line(px - 4, py, px + 4, py)
            c.line(px, py - 4, px, py + 4)
            c.drawString(px + 5, py + 1, k)

    c.showPage()
    c.save()
    buf.seek(0)
    return PdfReader(buf).pages[0]


def _register_script_font():
    for name, path in _SCRIPT_CANDIDATES:
        if os.path.exists(path):
            try:
                pdfmetrics.registerFont(TTFont(name, path))
                return name
            except Exception:  # noqa: BLE001
                continue
    return "Helvetica-Oblique"


def _signature_overlay(data):
    """A page-2-sized overlay with the requestor's name in the signature box."""
    name = data.get("signature_name") or data["full_name"].title()
    font = _register_script_font()
    buf = BytesIO()
    c = canvas.Canvas(buf, pagesize=(PAGE_W, PAGE_H))
    c.setFillColor(Color(0, 0, 0.55))
    c.setFont(font, SIGNATURE_SIZE)
    c.drawString(*SIGNATURE_POS, name)
    c.showPage()
    c.save()
    buf.seek(0)
    return PdfReader(buf).pages[0]


def _attachment_page(data):
    buf = BytesIO()
    c = canvas.Canvas(buf, pagesize=(PAGE_W, PAGE_H))
    left, y = 55, PAGE_H - 60
    c.setFont("Helvetica-Bold", 12)
    c.drawString(left, y, data.get("attachment_title", "Attachment"))
    y -= 22
    c.setFont(FONT, 9)
    for ln in data["attachment_lines"]:
        if y < 55:
            c.showPage()
            y = PAGE_H - 60
            c.setFont(FONT, 9)
        c.drawString(left, y, ln)
        y -= 13
    c.showPage()
    c.save()
    buf.seek(0)
    return list(PdfReader(buf).pages)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--template", required=True)
    ap.add_argument("--data", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--debug", action="store_true", help="draw crosshairs at every anchor")
    ap.add_argument("--sign", action="store_true",
                    help="render the requestor's name in the page-2 signature box (script font)")
    args = ap.parse_args()

    with open(args.data, encoding="utf-8") as f:
        data = json.load(f)
    data["_debug"] = args.debug

    base = PdfReader(args.template)
    w = PdfWriter()

    p1 = base.pages[0]
    p1.merge_page(_overlay_page1(data))
    w.add_page(p1)

    p2 = base.pages[1]
    if args.sign:
        p2.merge_page(_signature_overlay(data))
    w.add_page(p2)

    for pg in base.pages[2:]:
        w.add_page(pg)
    for pg in _attachment_page(data):
        w.add_page(pg)

    with open(args.out, "wb") as f:
        w.write(f)
    print(f"wrote {args.out}  ({len(w.pages)} pages)")


if __name__ == "__main__":
    main()
