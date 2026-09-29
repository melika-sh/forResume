# -*- coding: utf-8 -*-
"""Generate EN (LTR) versions of the 7 resume pages from the FA sources."""
import re

BASE = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'fa') + '/'
import os
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'en') + '/'

D1 = {
'ملیکا شاهقدمی':'Melika Shahghadami',
'مهارت‌ها':'Skills','نرم‌افزارها':'Software','پروژه‌های کلیدی':'Key Projects','درباره من':'About Me','سوابق کاری':'Work Experience','تحصیلات':'Education',
'Technical Artist و 3D Artist با بیش از ۳ سال تجربه در تولید و آماده‌سازی دارایی‌های Real-time برای بازی، شبیه‌ساز و پروژه‌های VR. تجربه در مدل‌سازی و بهینه‌سازی، PBR Texturing، Rigging و پیاده‌سازی فنی دارایی‌ها در Unity و Unreal Engine. تمرکز بر ایجاد تعادل بین کیفیت بصری و Performance، به‌ویژه در پروژه‌های VR و Meta Quest 3.':
'Technical Artist and 3D Artist with 3+ years of experience producing and preparing real-time assets for games, simulators and VR projects. Experienced in modeling and optimization, PBR texturing, rigging, and technical asset implementation in Unity and Unreal Engine. Focused on balancing visual quality and performance, especially in VR projects and on Meta Quest 3.',
'شرکت آریو سورن – طراح سه‌بعدی و تکنیکال آرتیست':'Ario Sorun — 3D Designer & Technical Artist',
'۱۴۰۲–اکنون':'2023 – Present',
'پیاده‌سازی دارایی‌ها در Unity، چیدمان صحنه، تنظیم متریال و نورپردازی.':'Asset implementation in Unity, scene layout, material setup and lighting.',
'بهینه‌سازی Mesh، Texture و Draw Calls برای بهبود Performance در پروژه‌های VR روی Meta Quest 3.':'Mesh, texture and draw call optimization to improve performance in VR projects on Meta Quest 3.',
'توسعه و استانداردسازی فرآیند تولید دارایی‌ها برای هماهنگی بهتر بین تیم‌های Art و Development.':'Developing and standardizing the asset production pipeline for better coordination between Art and Development teams.',
'شرکت پیشگامان لوتوس – طراح سه‌بعدی و برنامه‌نویس Godot':'Pishgaman Lotus — 3D Designer & Godot Programmer',
'۱۴۰۱–۱۴۰۲':'2022 – 2023',
'طراحی محیط و Modular 3D Assets برای پروژه‌های بازی.':'Environment and modular 3D asset design for game projects.',
'همکاری با تیم Development در پیاده‌سازی فنی و آماده‌سازی Build نهایی.':'Collaborated with the development team on technical implementation and final build preparation.',
'شرکت ترسیم داده – برنامه‌نویس Java':'Tarsim Dadeh — Java Developer',
'۱۴۰۰–۱۴۰۱':'2021 – 2022',
'توسعه و نگهداری ماژول‌های نرم‌افزاری با Java، عیب‌یابی و بهینه‌سازی کد.':'Developed and maintained software modules in Java; debugging and code optimization.',
'لیسانس مهندسی کامپیوتر – دانشگاه شهید بهشتی (۱۳۹۵–۱۴۰۰)':'B.Sc. Computer Engineering — Shahid Beheshti University (2016–2021)',
'کارشناسی ارشد مدیریت کسب‌وکار – تهران مرکز (۱۴۰۰–۱۴۰۳)':'M.Sc. IT Management — University of Tehran, Markazi Branch (2021–2023)',
'ایمیل:':'Email:','تلفن:':'Phone:','۰۹۱۲۴۸۰۵۵۳۷':'0912 480 5537',
}

D2 = {
'محیط صنعتی در Unity':'Industrial Environment in Unity',
'ملیکا شاهقدمی | تکنیکال آرتیست | Environment Art + نورپردازی حجمی':'Melika Shahghadami | Technical Artist | Environment Art + Volumetric Lighting',
'کار اصلی شما - تصویر کامل ارسالی - انبار صنعتی - Unity URP':'Main work — industrial warehouse environment built in Unity URP',
'درباره پروژه':'About the Project',
'محیط انبار صنعتی ساخته‌شده در Unity با استفاده از URP، با تمرکز بر PBR Materials، Volumetric Lighting، Environment Art و طراحی و چیدمان پراپ‌های صنعتی. صحنه برای اجرای Real-time و استفاده در پروژه‌های بازی بهینه شده است.':
'Industrial warehouse environment built in Unity using URP, focusing on PBR materials, volumetric lighting, environment art, and the design and layout of industrial props. The scene is optimized for real-time rendering and use in game projects.',
'مشخصات فنی':'Technical Specs','پایپ‌لاین رندر':'Render Pipeline','نور و مه حجمی':'Volumetric light & fog','بهینه برای بازی':'Optimized for games',
'نورپردازی و اتمسفر':'Lighting & Atmosphere','سطح و جزئیات':'Surfaces & Details',
'• نور حجمی از پنجره‌های شیشه‌ای<br>':'• Volumetric light through glass windows<br>',
'• چراغ‌های صنعتی آویزان متعدد<br>':'• Multiple hanging industrial lamps<br>',
'• بازتاب‌های کف با Reflection':'• Floor reflections with SSR',
'• قفسه‌بندی و چیدمان صنعتی<br>':'• Industrial shelving and layout<br>',
'• جرثقیل سقفی و سازه فلزی<br>':'• Overhead crane and steel structure<br>',
'• متریال PBR زنگ‌زده و کهنه<br>':'• Aged, rusty PBR materials<br>',
'• پراپ‌های متنوع: بشکه، جعبه، پالت':'• Varied props: barrels, crates, pallets',
'نمای جزئیات محیط - 3 زاویه مختلف از انبار - Unity URP':'Environment details — 3 warehouse angles — Unity URP',
'1. کابل‌ها و بشکه‌ها':'1. Cables & barrels','2. قفسه‌بندی و پراپ‌ها':'2. Shelving & props','3. سازه فلزی و پله':'3. Steel structure & stairs',
'انبار صنعتی - Unity URP':'Industrial Warehouse — Unity URP',
}

D3 = {
'شبیه‌ساز رانندگی چندنفره VR - چرخه روز و شب':'Multiplayer VR Driving Simulator — Day/Night Cycle',
'Multiplayer VR Driving Simulator • Day / Night Cycle • Meta Quest 3':'Multiplayer VR Driving Simulator • Day / Night Cycle • Meta Quest 3',
'ملیکا شاهقدمی | تکنیکال آرتیست | طراحی محیط بزرگ مقیاس چندنفره با نورپردازی پویا':'Melika Shahghadami | Technical Artist | Large-scale multiplayer environment with dynamic lighting',
'☀️ روز - دریاچه کوهستانی با نور طبیعی و جزئیات محیطی':'☀️ Day — mountain lake with natural light and ambient detail',
'🌙 شب - نور ماه، بازتاب آب و چراغ‌های محیطی':'🌙 Night — moonlight, water reflections and local lights',
'درباره پروژه چندنفره':'About the Multiplayer Project',
'شبیه‌ساز رانندگی چندنفره VR برای Meta Quest 3 با محیط مشترک و سیستم Day/Night. طراحی محیط شامل جاده کوهستانی، تونل، دریاچه، پوشش گیاهی و سازه‌ها، همراه با نورپردازی پویا و بهینه‌سازی Real-time برای دستیابی به 72+ FPS.':
'Multiplayer VR driving simulator for Meta Quest 3 with a shared environment and day/night cycle. The environment includes a mountain road, tunnel, lake, vegetation and structures, with dynamic lighting and real-time optimization targeting 72+ FPS.',
'ویژگی‌های چندنفره':'Multiplayer Features','دستاوردهای فنی':'Technical Achievements',
'• محیط مشترک چند کاربر با همگام‌سازی<br>':'• Shared multi-user environment with synchronization<br>',
'• بهینه‌سازی Draw Call و LOD برای چندنفره<br>':'• Draw call and LOD optimization for multiplayer<br>',
'• طراحی مسیر و Environment برای تعامل کاربران':'• Route and environment design for user interaction',
'• محیط کوهستانی بزرگ با دریاچه و تونل<br>':'• Large mountain environment with lake and tunnel<br>',
'• نورپردازی روز/شب با ماه و چراغ<br>':'• Day/night lighting with moon and artificial lights<br>',
'☀️ نمای روز - تنوع مسیر':'☀️ Day Views — Route Variety','🌙 نمای شب - سیستم روشنایی':'🌙 Night Views — Lighting System',
'🔄 مقایسه روز و شب - یک مکان، دو نورپردازی':'🔄 Day/Night Comparison — One Location, Two Lightings',
'بیلبورد نوری':'Lit Billboard','بیلبورد':'Billboard','هوایی':'Aerial','کوهستان':'Mountains','جنگل':'Forest','خاکی':'Dirt Road',
'روز - کناره':'Day — Shoreline','شب - کافه':'Night — Café','روز - خاکی':'Day — Dirt Road','روز - تپه':'Day — Hill',
'تونل شب':'Night Tunnel','تونل':'Tunnel','سرعت‌گیر':'Speed Bump','کافه':'Café','ساختمان':'Building',
'پانوراما':'Panorama','جاده اصلی':'Main Road','ماه و آب':'Moon & Water',
'شبیه‌ساز رانندگی چندنفره VR - Day / Night Cycle':'Multiplayer VR Driving Simulator — Day/Night Cycle',
}

D4 = {
'محیط بازی شوتر چندنفره':'Multiplayer Shooter Environment',
'ملیکا شاهقدمی | تکنیکال آرتیست | طراحی محیط FPS با تمرکز بر گیم‌پلی چندنفره':'Melika Shahghadami | Technical Artist | FPS environment design focused on multiplayer gameplay',
'نمای کلی محیط صحرایی با معماری خشتی و پوشش گیاهی':'Overview of the desert environment with adobe architecture and vegetation',
'مسیر رقابتی با کاور و نقاط دید برای گیم‌پلی FPS':'Competitive route with cover and sightlines for FPS gameplay',
'درباره پروژه':'About the Project',
'طراحی محیط بازی شوتر چندنفره اول شخص در فضای صحرایی با معماری خشتی و نخلستان. به عنوان تکنیکال آرتیست، مسئول چیدمان Level، بهینه‌سازی برای اجرای چندنفره، و طراحی مسیر با کاور و نقاط دید مناسب برای تعادل گیم‌پلی. محیط برای Multiplayer FPS با تمرکز بر خوانایی مسیرها، Player Flow و Performance در Unity طراحی شده است.':
'First-person multiplayer shooter environment set in a desert with adobe architecture and palm groves. As technical artist, I was responsible for level layout, optimization for multiplayer, and route design with cover and sightlines for balanced gameplay. The environment is designed in Unity for multiplayer FPS, focusing on route readability, player flow and performance.',
'ویژگی‌های چندنفره':'Multiplayer Features','دستاوردهای فنی':'Technical Achievements',
'• طراحی مسیر با Cover Placement و Sightlines مناسب برای Gameplay<br>':'• Route design with cover placement and gameplay-focused sightlines<br>',
'• بهینه‌سازی Environment برای اجرای Real-time در Multiplayer<br>':'• Environment optimization for real-time multiplayer<br>',
'• Sightlines و Player Flow':'• Sightlines and player flow',
'• Level Layout با تمرکز بر Gameplay<br>':'• Level layout focused on gameplay<br>',
'• PBR Texturing و Desert Lighting<br>':'• PBR texturing and desert lighting<br>',
'• LOD و Draw Call Optimization':'• LOD and draw call optimization',
'نمای کاور و مسیر فرعی':'Cover & Side Route View','نمای رقابتی - مسیر اصلی':'Competitive View — Main Route',
'محیط صحرایی':'Desert','معماری خشتی':'Adobe','نخلستان':'Palms','مسیر FPS':'FPS Route',
}

D5 = {
'محیط سه‌بعدی سینماتیک':'Cinematic 3D Environment',
'ملیکا شاهقدمی | تکنیکال آرتیست | کار اصلی + تنوع نوری':'Melika Shahghadami | Technical Artist | Main piece + lighting variant',
'کار اصلی شما - محیط سینماتیک کامل با آسیاب بادی، کلبه متروکه، برج سنگی و دریاچه - Blender Cycles':'Main work — full cinematic environment with windmill, abandoned hut, stone tower and lake — Blender Cycles',
'درباره پروژه':'About the Project',
'محیط سینماتیک شخصی ساخته‌شده در Blender با ترکیب آسیاب بادی، کلبه متروکه، برج سنگی و دریاچه. صحنه با Cycles، PBR Materials، Atmospheric Lighting، Volumetric Fog و Particle Systems ساخته شده و شامل آب با Reflection و Displacement است.':
'Personal cinematic environment built in Blender combining a windmill, abandoned hut, stone tower and lake. The scene is created with Cycles, PBR materials, atmospheric lighting, volumetric fog and particle systems, and features water with reflections and displacement.',
'ویژگی‌های کار اصلی':'Main Scene Features','کار اصلی':'Main','تنوع نوری':'Lighting Variant',
'حالت دریاچه':'Lake Features','ویژگی‌های دریاچه':'Lake Features',
'• ترکیب 4 عنصر در یک صحنه سینماتیک<br>':'• 4 elements combined in one cinematic scene<br>',
'• چمن و نیزار با Particle System<br>':'• Grass and reeds via particle systems<br>',
'• آب با Reflection و Displacement<br>':'• Water with reflections and displacement<br>',
'• مه حجمی و نورپردازی اتمسفریک':'• Volumetric fog and atmospheric lighting',
'• دریاچه آرام با Reflection کامل<br>':'• Calm lake with full reflections<br>',
'• نیزار با Particle System<br>':'• Reeds via particle system<br>',
'• حس روز ابری بدون مه':'• Overcast daytime mood, no fog',
'تنوع نوری - دریاچه و نیزار - Blender / Cycles':'Lighting variant — lake and reeds — Blender / Cycles',
'دریاچه و نیزار - روز ابری بدون مه - آب آرام':'Lake and reeds — overcast day, still water',
'محیط سه‌بعدی سینماتیک - کار اصلی + تنوع نوری':'Cinematic 3D Environment — Main + Lighting Variant',
}

D6 = {
'کاراکتر گرگ - مدل‌سازی و موی پویا':'Wolf Character — Modeling & Fur',
'ملیکا شاهقدمی | تکنیکال آرتیست | مدل‌سازی و Particle Hair / Fur Grooming':'Melika Shahghadami | Technical Artist | Modeling + Particle Hair / Fur Grooming',
'رندر نهایی - نمای سه‌رخ با نورپردازی استودیویی و جزئیات خز':'Final render — three-quarter view with studio lighting and fur detail',
'رندر نهایی - نمای کناری با PBR Texturing و Fur Grooming':'Final render — side view with PBR texturing and fur grooming',
'درباره پروژه':'About the Project',
'پروژه کاراکتر گرگ با تمرکز بر High/Low Poly Modeling، Retopology، UV، PBR Texturing و Fur Grooming در Blender. سیستم مو با Particle Hair و Grooming ساخته شده و مدل برای Real-time و Offline Rendering آماده شده است.':
'Wolf character project focused on high/low poly modeling, retopology, UVs, PBR texturing and fur grooming in Blender. The fur is built with particle hair and grooming, and the model is prepared for both real-time and offline rendering.',
'ویژگی‌های فنی':'Technical Features','دستاوردهای هنری':'Artistic Achievements',
'• مدل‌سازی Low/High Poly و ریتوپولوژی بهینه<br>':'• Low/high poly modeling with optimized retopology<br>',
'• UV و PBR Texturing با جزئیات Fur<br>':'• UV and PBR texturing with fur detail<br>',
'• Particle Hair و Fur Grooming در Blender':'• Particle hair and fur grooming in Blender',
'• Organic Character Modeling با تمرکز بر Anatomy و Surface Detail<br>':'• Organic character modeling focused on anatomy and surface detail<br>',
'• Particle Hair و Fur Grooming برای Rendering<br>':'• Particle hair and fur grooming for rendering<br>',
'• Studio Lighting و Final Presentation':'• Studio lighting and final presentation',
'Wireframe و Topology':'Wireframe & Topology',
'وایرفریم - نمای پشت با توپولوژی بهینه و Edge Flow تمیز':'Wireframe — back view with optimized topology and clean edge flow',
'وایرفریم - نمای سه‌رخ با نمایش ساختار آناتومیک':'Wireframe — three-quarter view showing anatomical structure',
'جزئیات فنی - Modeling، Texturing و Grooming':'Technical Details — Modeling, Texturing & Grooming',
'نمای نهایی':'Final Render','توپولوژی':'Topology','وایرفریم':'Wireframe',
}

D7 = {
'مدل‌سازی Hard Surface':'Hard Surface Modeling',
'ملیکا شاهقدمی | تکنیکال آرتیست | 4 مدل صنعتی':'Melika Shahghadami | Technical Artist | 4 Industrial Models',
'بسته باتری انرژی - Battery Pack':'Energy Battery Pack','بشکه سوخت FUEL':'FUEL Barrel',
'1. بسته باتری انرژی':'1. Energy Battery Pack','2. بشکه سوخت':'2. Fuel Barrel','3. جعبه ابزار صنعتی':'3. Industrial Toolbox','4. بازوی ربات صنعتی':'4. Industrial Robotic Arm',
'Hard Surface - 4 مدل صنعتی':'Hard Surface — 4 Industrial Models',
}

FILES = [('Page1_FA.html','Page1_EN.html',D1),('Page_Unity_URP_Warehouse.html','Page2_Unity_EN.html',D2),
('page2_VR_creative_full.html','Page3_VR_EN.html',D3),('page3_Shooter_uniform.html','Page4_Shooter_EN.html',D4),
('page4_Environment_uniform.html','Page5_Environment_EN.html',D5),('page5_Wolf_new_creative.html','Page6_Wolf_EN.html',D6),
('page6_HardSurface_uniform.html','Page7_HardSurface_EN.html',D7)]

def flip(s):
    s = s.replace('<html lang="fa" dir="rtl">','<html lang="en" dir="ltr">')
    s = s.replace('text-align:right','text-align:left')
    s = s.replace('padding-right','padding-left')
    s = s.replace('right:0;color:#8B5E3F','left:0;color:#8B5E3F')
    s = s.replace('vertical-align:middle;margin-left:5pt','vertical-align:middle;margin-right:5pt')
    return s

if __name__ == '__main__':
    for src,dst,dic in FILES:
        s = open(BASE+src).read()
        s = flip(s)
        misses=[]
        for fa in sorted(dic, key=len, reverse=True):   # longest first
            en=dic[fa]
            if fa in s: s=s.replace(fa,en)
            else: misses.append(fa[:60])
        leftover=set()
        for m in re.finditer(r'[^\n<>{}]{0,80}[\u0600-\u06FF][^<>{}]*',s):
            t=m.group(0).strip()
            if t: leftover.add(t[:100])
        open(OUT+dst,'w').write(s)
        print(dst,'| misses:',len(misses),'| fa leftover:',len(leftover))
        for t in sorted(leftover)[:12]: print('   -',t)
