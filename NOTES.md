# SiscoApp – ملاحظات للمحادثة الجديدة (تحديث 2026-11-25)

## المالك
Louai Saleh. بيحكي عربي لبناني / Arabizi. بدو أجوبة قصيرة بالعربي. مش مبرمج.
لا تسوّي شي بدون طلب. إذا سأل "yes or no" جاوب بس.

## الأنظمة
- التطبيق (PWA إشارات XAUUSD) على Render: خدمة `siscohub` (srv-dbs9lh6i0phs73ch6ajg)، workspace tea-dbs96fe1egvs73d73h9g، رابط https://siscohub.onrender.com ، autoDeploy عند commit على main.
- ريبو السيرفر: siscohub/-sisco-gold-signel- (server.py، static/index.html، static/admin.html).
- ريبو التحليل: siscohub/sisco-analysis (latest.json, agenda.json, lesson.json, result.json, track.json). السيرفر بيسحبهم كل 120 ثانية وبينشرهم للأعضاء.
- result.json = رسالة بتنزل لكل الأعضاء (kind analysis، push عنوانه "Analysis update").
- مفتاح VAPID للإشعارات موجود على الـdisk (/data) عبر PEM_PATH، مش بالريبو (انحذف من الريبو 25/11).
- الصفحات (/ و /admin) بتنخدم مع Cache-Control: no-cache (حل مشكلة النسخة القديمة على iOS).
- زر "Make Sisco Team" موجود بكرت العضو بالأدمن.
- إشعار 410 Unregistered = جهاز العضو ألغى الإشعارات، والسيرفر بيحذف اشتراكه تلقائياً.

## المهام المجدولة (توقيت فيينا)
- الأجندة: 07:47 أيام العمل
- تحليل لندن: 08:04 أيام العمل
- الدرس اليومي: 12:22 يومياً
- تحديث قبل نيويورك: 13:41 أيام العمل
- متتبّعات الصفقات: :07 و :37 من 8 لـ21 أيام العمل
- مراجعة أسبوعية: السبت 10:17
- النشر على التطبيق بيطلع حوالي 10 دقايق بعد الدفع للريبو.

## TradingView
- متصل. تنبيه "Sisco OANDA" شغّال على OANDA:XAUUSD دقيقة (مؤشر Siscohub Gold SMC).
- Backtest: بدّك initial_capital 1,000,000 وعمولة. تاريخ 1m حوالي 3 أسابيع، 5m حوالي 3.5 شهر، 15m حوالي 10 أشهر.
- نتائج: أفضل استراتيجية واقعية TP 8/16/24 مع break-even (PF 1.20). مؤشره الحالي جهة BUY ضعيفة (1 من 4 رابحة حياً).
- لا توصّل مؤشر جديد على webhook الزبائن بدون موافقته.

## شغل معلّق
- رسالة BUY LIMIT 3583 انبعتت للأعضاء (result.json). اسأله إذا هو بعتها كمان (تكرار محتمل).
- تتبّع BUY LIMIT 3583 بـ track.json فقط إذا طلب. SELL LIMIT 3642.97 متتبّعة.
- تدوير WEBHOOK_SECRET و ADMIN_KEY (انكشفوا) وتحديث نص تنبيه TradingView.
- Google Play: تحقق الهوية، حالة trader، closed test.
- فكرة: منصة شارت "Sisco Trading" بنفس أدوات الرسم. ممكنة فقط بمكتبة TradingView Charting Library (ترخيص بطلب). ما بدأنا شي.
- فحص اليوم: تأكد أن تحليل لندن (id 2026-11-25-am) والأجندة ظهروا بالتطبيق.
