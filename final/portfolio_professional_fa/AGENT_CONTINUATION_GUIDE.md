# 🎯 Melika Portfolio - Agent Continuation Guide
# برای چت بعدی - اگر این چت به لیمیت خورد - 100% کار می‌کنه

## 📁 ساختار فعلی GitHub
```
final/
├── Melika_Shahghadami_Portfolio_Professional_VR_First_FA.pdf (اصلی - 4 صفحه نهایی)
├── Melika_Shahghadami_Resume_Page1_FA.pdf
└── portfolio_professional_fa/
    ├── Page2_VR_Final_Professional_14Images_OnePage.pdf ← آخرین نسخه حرفه‌ای 1 صفحه‌ای 14 تصویر
    ├── Portfolio_FA_4Pages_Final_Professional_Mixed.pdf (4 صفحه نهایی با نسخه 1 صفحه‌ای)
    ├── page2_VR_final_professional.html ← TEMPLATE اصلی حرفه‌ای
    ├── TEMPLATE_MAIN.html ← کپی template برای چت بعدی
    ├── new_vr_day_clean/ (9 تصویر روز تمیز)
    ├── new_vr_night_clean/ (6 تصویر شب تمیز)
    ├── new_vr_day_raw/ و new_vr_night_raw/
    └── Pages قدیمی: Page3_Shooter_FA.pdf, Page4_Environment_FA.pdf, Page5_Wolf_FA.pdf
```

## 🎨 TEMPLATE اصلی - 14 تصویر یک صفحه
فایل: `TEMPLATE_MAIN.html` یا `page2_VR_final_professional.html`
- A4: 595.2pt x 841.92pt, outer 559.2pt x 816pt
- هدر 64pt با آواتار
- 2 هیرو 96pt (روز vs شب)
- بخش درباره پروژه
- 2 ستون ویژگی‌ها
- 3 ردیف گالری: 5 + 5 + 4 = 14 تصویر
- فوتر 16pt
- فونت Vazirmatn فارسی RTL

متن حرفه‌ای نمونه (بدون AI):
عنوان: شبیه‌ساز رانندگی چندنفره در واقعیت مجازی
زیرعنوان: Multiplayer VR Driving Simulator • Day / Night Cycle • Meta Quest 3
درباره: پروژه چندنفره VR برای Quest 3 با محیط مشترک. مسئولیت من: طراحی کامل محیط، نورپردازی پویا روز/شب، بهینه‌سازی VR 72+ FPS، 40% بهینه‌سازی. توانایی در خلق فضای Immersive.

❌ استفاده نکن: "قاطی شده", "قاطی", "منتخب جدید", "ترکیبی قاطی"
✅ استفاده کن: "چرخه پویا", "یکپارچه", "سیستم روشنایی", "محیط مشترک", "بزرگ مقیاس"

## 🖼️ تمیز کردن تصاویر جدید
```python
from PIL import Image
import pathlib
src = pathlib.Path('/home/user/uploads')
dst = pathlib.Path('/home/user/resume/portfolio_fa/img/new_project')
dst.mkdir(parents=True, exist_ok=True)

for f in src.glob('*.png'):
    im = Image.open(f)
    w,h = im.size
    # روز با UI: left 36, top 0, right w*0.94, bottom h*0.965
    # شب با UI: left 0, top 22, right w*0.975, bottom h*0.975
    # اگر تمیز بود: crop 0,0,w,h
    if w > 1900:  # با UI
        left, top, right, bottom = 36, 0, int(w*0.94), int(h*0.965)
    else:
        left, top, right, bottom = 0, 0, w, h
    cropped = im.crop((left, top, right, bottom))
    cropped.convert('RGB').save(dst / (f.stem + '_clean.jpg'), 'JPEG', quality=92)
```

## 📄 تولید PDF با Playwright
```bash
pip install playwright pymupdf
playwright install chromium --with-deps
```
```python
from playwright.sync_api import sync_playwright
import pathlib, pymupdf

html_path = pathlib.Path('/home/user/resume/portfolio_fa/page2_VR_final_professional.html').resolve()
pdf_path = pathlib.Path('/home/user/resume/portfolio_fa/Page2_VR_Final_Professional_14Images_OnePage.pdf')

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True, args=['--no-sandbox'])
    page = browser.new_page()
    page.goto(f'file://{html_path}', wait_until='networkidle')
    page.wait_for_timeout(1200)
    page.pdf(path=str(pdf_path), width='8.27in', height='11.69in', print_background=True, margin={'top':'0','bottom':'0','left':'0','right':'0'})
    browser.close()

# Preview
doc = pymupdf.open(str(pdf_path))
pix = doc[0].get_pixmap(dpi=220)
pix.save('/home/user/work/preview.png')
```

### مرج 4 صفحه
```python
import pymupdf
order = [
    'resume/portfolio_fa/Page2_VR_Final_Professional_14Images_OnePage.pdf',
    'resume/portfolio_fa/Page3_Shooter_FA.pdf',
    'resume/portfolio_fa/Page4_Environment_FA.pdf',
    'resume/portfolio_fa/Page5_Wolf_FA.pdf',
]
merged = pymupdf.open()
for path in order:
    merged.insert_pdf(pymupdf.open(path))
merged.save('resume/portfolio_fa/Portfolio_FA_4Pages_Final_Professional_Mixed.pdf')
```

## 🚀 پوش به GitHub
```bash
cd /tmp && rm -rf forResume && git clone https://github.com/melika-sh/forResume.git forResume -q
cd forResume
git config user.email "melika@example.com"
git config user.name "Melika Shahghadami"
cp /home/user/resume/portfolio_fa/*.pdf final/portfolio_professional_fa/
cp /home/user/resume/portfolio_fa/*.html final/portfolio_professional_fa/
mkdir -p final/portfolio_professional_fa/new_images_clean
cp /home/user/resume/portfolio_fa/img/new_images/*.jpg final/portfolio_professional_fa/new_images_clean/
git add .
git commit -m "Update portfolio"
# توکن رو از کاربر بگیر
git remote set-url origin https://TOKEN@github.com/melika-sh/forResume.git
git push origin main
```

## 📝 چک لیست چت بعدی
1. تصاویر از /home/user/uploads/ بخون
2. با PIL تمیز کن (UI حذف)
3. بریز تو resume/portfolio_fa/img/new_project/
4. TEMPLATE_MAIN.html رو کپی و ویرایش کن
5. متن حرفه‌ای multiplayer VR بنویس (بدون کلمات AI)
6. PDF با Playwright بساز
7. Preview PNG بساز و present کن
8. پوش به GitHub
9. فایل‌های لوکال پاک کن

## 📌 پروژه‌ها
- ✅ VR روز 9 تصویر - انجام
- ✅ VR شب 5 تصویر - انجام
- ✅ روز و شب یک صفحه 14 تصویر - نهایی
- ⏳ بعدی: Shooter / Wolf / Environment - منتظر تصاویر جدید

## 💡 نکات
- کاربر فارسی/فینگلیش - جواب فینگلیش
- همه چی تو یه صفحه جا بشه
- از کلمات AI پرهیز
- توضیحات حرفه‌ای multiplayer VR
- بعد از پوش فایل‌های لوکال پاک کن
- فایل نهایی present کن

آخرین آپدیت: 2025-09-20 - نسخه نهایی 14 تصویر یک صفحه‌ای - 100% تست شده
