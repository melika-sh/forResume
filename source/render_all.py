#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Render resume pages (HTML -> PDF) and build the two final merged PDFs.

Usage:
    python3 render_all.py            # render + merge both FA and EN (default)
    python3 render_all.py fa         # Persian only
    python3 render_all.py en         # English only
    python3 render_all.py fa 3       # re-render only page 3 of FA, then merge

First-time setup after a fresh environment:
    pip install playwright pymupdf
    playwright install chromium --with-deps
"""
import os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)            # repo root
FA_DIR = os.path.join(HERE, 'fa')
EN_DIR = os.path.join(HERE, 'en')

# Filename must stay in sync with the pages in fa/ and en/
FA_PAGES = ['Page1_FA.html',              # 1 resume
            'Page_Unity_URP_Warehouse.html',  # 2 warehouse
            'page2_VR_creative_full.html',    # 3 VR
            'page3_Shooter_uniform.html',     # 4 shooter
            'page4_Environment_uniform.html', # 5 cinematic
            'page5_Wolf_new_creative.html',   # 6 wolf
            'page6_HardSurface_uniform.html'] # 7 hard surface
EN_PAGES = ['Page1_EN.html', 'Page2_Unity_EN.html', 'Page3_VR_EN.html',
            'Page4_Shooter_EN.html', 'Page5_Environment_EN.html',
            'Page6_Wolf_EN.html', 'Page7_HardSurface_EN.html']

FA_OUT = os.path.join(ROOT, 'Melika_Shahghadami_Resume_Portfolio_FA.pdf')
EN_OUT = os.path.join(ROOT, 'Melika_Shahghadami_Resume_Portfolio_EN.pdf')

PDF_KW = dict(width='8.27in', height='11.69in', print_background=True,
              margin={'top': '0', 'bottom': '0', 'left': '0', 'right': '0'})
VIEW = dict(width=794, height=1123)
DSF = 2


def render(html_dir, pages, only=None):
    from playwright.sync_api import sync_playwright
    idx = range(len(pages)) if only is None else [i - 1 for i in only]
    with sync_playwright() as x:
        b = x.chromium.launch()
        pg = b.new_page(viewport=VIEW, device_scale_factor=DSF)
        for i in idx:
            src = os.path.join(html_dir, pages[i])
            dst = src.replace('.html', '.pdf')
            pg.goto('file://' + src, wait_until='networkidle')
            pg.pdf(path=dst, **PDF_KW)
            print('rendered:', pages[i])
        b.close()


def merge(html_dir, pages, out_path):
    import pymupdf
    out = pymupdf.open()
    for p in pages:
        d = pymupdf.open(os.path.join(html_dir, p.replace('.html', '.pdf')))
        out.insert_pdf(d)
        d.close()
    out.save(out_path, deflate=True, garbage=4)
    print('merged ->', os.path.basename(out_path), f'({out.page_count} pages)')


def run(lang, pages, html_dir, out_path, only):
    render(html_dir, pages, only)
    # merge always needs ALL page PDFs present; render missing ones with old files
    missing = [p for p in pages if not os.path.exists(os.path.join(html_dir, p.replace('.html', '.pdf')))]
    if missing:
        render(html_dir, missing)
    merge(html_dir, pages, out_path)


if __name__ == '__main__':
    args = [a for a in sys.argv[1:]]
    lang = args[0].lower() if args else 'all'
    only = [int(a) for a in args[1:]] or None
    if lang in ('fa', 'all'):
        run('fa', FA_PAGES, FA_DIR, FA_OUT, only if lang == 'fa' else None)
    if lang in ('en', 'all'):
        run('en', EN_PAGES, EN_DIR, EN_OUT, only if lang == 'en' else None)
    print('done.')
