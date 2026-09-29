# راهنمای ادامه‌ی کار — Resume Source Guide

این پوشه **سورس کامل و قابل ویرایش** رزومه + پورتفولیوی ۷ صفحه‌ای ملیکا شاهقدمی رو نگه می‌داره.
اگر مکالمه/چت قبلی از دست رفت، با همین فایل‌ها بدون هیچ حافظه‌ی قبلی می‌شه کار رو ادامه داد.

This folder is the full editable source of the 7-page FA + EN resume portfolio.
Anyone (or any future chat session) can continue the work from here.

---

## ساختار / Structure

```
source/
├── fa/                        # قالب‌های فارسی (HTML) — راست‌به‌چپ
│   ├── Page1_FA.html                   # صفحه ۱: رزومه
│   ├── Page_Unity_URP_Warehouse.html   # صفحه ۲: انبار Unity
│   ├── page2_VR_creative_full.html     # صفحه ۳: VR Driving Simulator
│   ├── page3_Shooter_uniform.html      # صفحه ۴: Shooter
│   ├── page4_Environment_uniform.html  # صفحه ۵: سینماتیک Blender
│   ├── page5_Wolf_new_creative.html    # صفحه ۶: گرگ
│   └── page6_HardSurface_uniform.html  # صفحه ۷: Hard Surface
├── en/                        # نسخه انگلیسی (LTR) همون صفحات به همان ترتیب
├── fonts/                     # Vazirmatn (Regular/Bold/ExtraBold/Medium/SemiBold)
├── render_all.py              # رندر HTML→PDF و ساخت دو فایل نهایی
├── regenerate_en.py           # بازتولید نسخه انگلیسی از روی فارسی (دیکشنری ترجمه)
└── GUIDE.md                   # همین فایل
```

- عکس‌ها جدا از این پوشه‌اند: `images/` در ریشه‌ی ریپو — HTMLها با مسیر `../../images/...` بهش وصلن.
- قالب (رنگ/چیدمان/کارت‌ها) داخل `<style>` هر HTML ثابته؛ **متن‌ها مستقیم داخل HTML قابل ویرایش‌ان** — هیچ ابزار دیگه‌ای لازم نیست.
- فونت همه‌ی صفحات: **Vazirmatn** (برای فارسی و انگلیسی) — با `url('../fonts/...')` لود می‌شه.

## خروجی نهایی / Outputs

| فایل | توضیح |
|---|---|
| `Melika_Shahghadami_Resume_Portfolio_FA.pdf` | ۷ صفحه فارسی (ریشه ریپو) |
| `Melika_Shahghadami_Resume_Portfolio_EN.pdf` | ۷ صفحه انگلیسی (ریشه ریپو) |

## گردش کار / Workflow

### ۱. نصب محیط ( بعد از هر ریست شدن محیط لازمه )

```bash
pip install playwright pymupdf
playwright install chromium --with-deps
```

### ۲. ویرایش متن

متن فارسی/انگلیسی هر صفحه مستقیم داخل HTML هاست. قواعد مهم:

- **جایگزینی را «یکجا» انجام بده** — کل عبارت را یک‌باره عوض کن، نه کلمه‌کلمه (برای متن راست‌به‌چپ، ویرایش جزیی باعث به‌هم‌ریختن ترتیب کلمات انگلیسی/فارسی می‌شه).
- خطوط انگلیسی در متن فارسی که به‌هم می‌ریزن: دورشون `<span dir="ltr">...</span>` بگذار.
- **قالب را دست نزن** مگر بخواد — فاصله‌ها/کارت‌ها با `pt` در `<style>` تنظیم شده‌اند؛ متن جدید نباید طولانی‌تر از جا بشه.

### ۳. رندر + ادغام

```bash
cd source
python3 render_all.py        # هر دو نسخه FA + EN
python3 render_all.py fa     # فقط فارسی
python3 render_all.py en 3   # فقط صفحه ۳ انگلیسی را دوباره بگیر و merge کن
```

مشخصات چاپ: صفحه A4 — `8.27in × 11.69in`، حاشیه صفر، viewport `794×1123` با `device_scale_factor=2`.

### ۴. کامیت و پوش

```bash
cd ..            # ریشه ریپو
git config user.name "Melika Shahghadami"
git config user.email "shahghadami.me@gmail.com"
git add -A
git commit -m "Describe the change"
git push origin main
```

اگر remote بعد از ریست محیط گم شد: `git remote add origin <repo-url>` (توکن دسترسی را هرگز کامیت نکن).

## بازتولید نسخه انگلیسی

`regenerate_en.py` یک دیکشنری فارسی→انگلیسی دارد و از روی `fa/` هریک از صفحات `en/` را می‌سازد
(dir، text-align و padding را هم LTR می‌کند). بعد از هر تغییر در دیکشنری:

```bash
python3 regenerate_en.py && python3 render_all.py en
```

اگر فقط یک جمله در نسخه انگلیسی را می‌خواهی عوض کنی، ساده‌تر است مستقیم فایل `en/...html` را ویرایش کنی.

## قواعد محتوایی که باید حفظ شوند

- بدون آمار اثبات‌نشده: نه «۱۰۰+ دارایی»، نه «۴۰٪» بدون منبع — تنها استثنا: «40% Draw Call Reduction — Tested on Meta Quest 3» (تست‌شده روی دستگاه شخصی).
- بدون تعریف از خود: «حرفه‌ای، باورپذیر، توانایی من، تجربه اثبات‌شده، عالی، Immersive، خلاقانه» — فقط داده فنی.
- تاریخ سوابق: به میلادی (۲۰۲۳–اکنون / ۲۰۲۲–۲۰۲۳ / ۲۰۲۱–۲۰۲۲) و در نسخه فارسی به شمسی.
- عکس پروفایل صفحه ۱ را هیچ‌وقت ویرایش نکن.

## نکته‌ها درباره محیط Sandbox

- محیط ممکن است ریست شود: پکیج‌ها (playwright/pymupdf)، مرورگر Chromium و تنظیمات git **هر بار دوباره** لازم‌اند.
- فایل‌های مهم همه داخل ریپو/ورک‌اسپیس‌اند؛ پوشه‌های cache (`.cache`, `node_modules`, ...) ذخیره نمی‌شوند.
