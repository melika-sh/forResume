# 🎯 Melika Portfolio - Agent Continuation Guide
# برای چت بعدی - اگر این چت به لیمیت خورد

## 📁 ساختار فعلی GitHub
```
final/
├── Melika_Shahghadami_Portfolio_Professional_VR_First_FA.pdf (اصلی - 4 صفحه نهایی)
├── Melika_Shahghadami_Resume_Page1_FA.pdf
└── portfolio_professional_fa/
    ├── Page2_VR_Final_Professional_14Images_OnePage.pdf ← آخرین نسخه حرفه‌ای 1 صفحه‌ای
    ├── Portfolio_FA_4Pages_Final_Professional_Mixed.pdf
    ├── page2_VR_final_professional.html ← TEMPLATE اصلی
    ├── TEMPLATE_MAIN.html
    ├── new_vr_day_clean/ (9 تصویر روز)
    ├── new_vr_night_clean/ (6 تصویر شب)
    └── Pages: Page3_Shooter_FA.pdf, Page4_Environment_FA.pdf, Page5_Wolf_FA.pdf
```

## 🎨 TEMPLATE اصلی
فایل: `page2_VR_final_professional.html` - 14 تصویر یک صفحه - A4 595.2pt x 841.92pt
هدر 64pt، فوتر 16pt، 2 هیرو 96pt، 3 ردیف گالری 58pt

متن حرفه‌ای نمونه (بدون AI):
عنوان: شبیه‌ساز رانندگی چندنفره در واقعیت مجازی
زیرعنوان: Multiplayer VR Driving Simulator • Day / Night Cycle • Meta Quest 3
درباره: پروژه چندنفره VR برای Quest 3 با محیط مشترک. مسئولیت من: طراحی کامل محیط، نورپردازی پویا روز/شب، بهینه‌سازی VR. توانایی در خلق فضای Immersive.

❌ استفاده نکن: "قاطی شده", "قاطی", "منتخب جدید"
✅ استفاده کن: "چرخه پویا", "یکپارچه", "سیستم روشنایی", "محیط مشترک"

## 🖼️ تمیز کردن تصاویر
```python
from PIL import Image
# روز: left 36, top 0, right w*0.94, bottom h*0.965
# شب: left 0, top 22, right w*0.975, bottom h*0.975
cropped = im.crop((left, top, right, bottom))
cropped.convert('RGB').save(out_path, 'JPEG', quality=92)
```

## 📄 تولید PDF
```bash
pip install playwright pymupdf
playwright install chromium --with-deps
```
```python
from playwright.sync_api import sync_playwright
import pathlib
html_path = pathlib.Path('/home/user/resume/portfolio_fa/page2_VR_final_professional.html').resolve()
pdf_path = pathlib.Path('/home/user/resume/portfolio_fa/Page2_VR_Final_Professional_14Images_OnePage.pdf')
with sync_playwright() as p:
    browser = p.chromium.launch(headless=True, args=['--no-sandbox'])
    page = browser.new_page()
    page.goto(f'file://{html_path}', wait_until='networkidle')
    page.wait_for_timeout(1200)
    page.pdf(path=str(pdf_path), width='8.27in', height='11.69in', print_background=True, margin={'top':'0','bottom':'0','left':'0','right':'0'})
    browser.close()
```

## 🚀 پوش به GitHub
```bash
git clone https://github.com/melika-sh/forResume.git
cd forResume
git config user.email "melika@example.com"
git config user.name "Melika Shahghadami"
cp /home/user/resume/portfolio_fa/*.pdf final/portfolio_professional_fa/
git add .
git commit -m "Update"
# توکن رو از کاربر بگیر
git remote set-url origin https://TOKEN@github.com/melika-sh/forResume.git
git push origin main
```

## 📝 چک لیست چت بعدی
1. تصاویر از /home/user/uploads/ بخون
2. با PIL تمیز کن
3. بریز تو resume/portfolio_fa/img/new_project/
4. HTML template رو کپی و ویرایش کن
5. متن حرفه‌ای multiplayer VR بنویس
6. PDF بساز
7. Preview نشون بده
8. پوش به GitHub
9. فایل‌های لوکال پاک کن

## 📌 پروژه‌ها
- ✅ VR روز 9 تصویر - انجام
- ✅ VR شب 5 تصویر - انجام
- ✅ روز و شب یک صفحه 14 تصویر - نهایی
- ⏳ بعدی: Shooter / Wolf / Environment

## 💡 نکات
- کاربر فارسی/فینگلیش - جواب فینگلیش
- همه چی تو یه صفحه جا بشه
- از کلمات AI پرهیز
- بعد از پوش فایل‌های لوکال پاک کن
- فایل نهایی present کن

آخرین آپدیت: 2025-09-20
