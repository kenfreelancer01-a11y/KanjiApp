"""Tạo lại data/kanji.json từ KanjiVG + bảng Excel.

Cách dùng:
  python3 tools/make_data.py <thư mục KanjiVG đã giải nén (chứa thư mục kanji/)> <2000kanji.xlsx> data/kanji.json

Yêu cầu: pip install openpyxl
Bảng Excel: sheet đầu, dữ liệu từ hàng 4, cột C..L = #, chữ, bộ, số nét, grade,
tiếng Anh, cách đọc, Hán Việt, nghĩa, On-romaji.
"""
import json, re, sys
from xml.etree import ElementTree as ET
from openpyxl import load_workbook

SVG = "{http://www.w3.org/2000/svg}"
kvg_dir, xlsx, out_path = sys.argv[1], sys.argv[2], sys.argv[3]

def s(v):
    if v is None: return ""
    if v is True: return "true"
    if v is False: return "false"
    return str(v).replace("\u3000", " ").replace("\xa0", " ").strip()

def parse(ch):
    root = ET.parse("%s/kanji/%05x.svg" % (kvg_dir, ord(ch))).getroot()
    ps = []
    for p in root.iter(SVG + "path"):
        m = re.search(r"-s(\d+)$", p.get("id", ""))
        if m: ps.append((int(m.group(1)), p.get("d")))
    ps.sort()
    nps = []
    for t in root.iter(SVG + "text"):
        m = re.search(r"matrix\(\s*1 0 0 1\s+([-\d.]+)\s+([-\d.]+)\)", t.get("transform", ""))
        if m and (t.text or "").strip().isdigit():
            nps.append((int(t.text), float(m.group(1)), float(m.group(2))))
    nps.sort()
    d = [p[1] for p in ps]
    return d, ([[x, y] for _, x, y in nps] if len(nps) == len(d) else None)

wb = load_workbook(xlsx, read_only=True)
rows = [r[2:12] for r in wb.active.iter_rows(min_row=4, values_only=True) if r[2] is not None]
out = []
for r in rows:
    ch = s(r[1])[0]          # bỏ ghi chú như "茨 [5]"
    d, np = parse(ch)
    item = {"i": r[0], "c": ch, "r": s(r[2]), "n": len(d), "g": s(r[4]), "en": s(r[5]),
            "rd": s(r[6]), "hv": s(r[7]), "vi": s(r[8]), "d": d}
    if np: item["np"] = np
    out.append(item)
json.dump(out, open(out_path, "w", encoding="utf-8"), ensure_ascii=False, separators=(",", ":"))
print("Đã ghi", len(out), "chữ ->", out_path)
