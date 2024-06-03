# pip install -r req.txt
from telebot.types import BotCommand
from pytube import YouTube
from rembg import remove
from PIL import Image
from gtts import gTTS
from googletrans import Translator
from datetime import datetime
from googlesearch import search
from server import SERVER
import speedtest
import moviepy.editor
import telebot
import os
import math
#----------------------------------------------- print
print('-'*50)
print("SAZOM v1.3")
print('-')
def time(now):
    now = datetime.now()
    h = now.strftime("%H")
    m = now.strftime("%M")
    s = now.strftime("%S")
    d = now.strftime("%d")
    m = now.strftime("%m")
    y = now.strftime("%Y")
    d = now.date()
#--------------------------------------------
TOKEN = "7113724596:AAE4yYczuklB_raJ2pi4vObn7BzCUpO9YwE"
bot =  telebot.TeleBot(TOKEN)
Commandss = [
    BotCommand("download","To start downloading videos from YouTube, whatever their type"),
    BotCommand("remove","To remove background"),
    BotCommand("speech","text to speech"),
    BotCommand("convert","convert video to audio"),
    BotCommand("location","phone number location"),
    BotCommand("speed","speed test internet"),
    BotCommand("sticker","To convert image to sticker"),
    BotCommand("trans","Translate any text"),
    BotCommand("search","Search for anything"),
    BotCommand("help","Request help")
]
bot.set_my_commands(Commandss)
#------------------------------------------------------------ folders
DOWNLOADS = "./downloads/"
if os.path.exists(DOWNLOADS):
    print("alredy - [downloads]")
    pass
else:
    os.makedirs("downloads")
    print("creat folder - [downloads]")
TEMP = "./temp/"
if os.path.exists(TEMP):
    print("alredy - [temp]")
    pass
else:
    os.makedirs("temp")
    print("creat folder - [temp]")
PROCESSED = "./processed/"
if os.path.exists(PROCESSED):
    print("alredy - [processed]")
    pass
else:
    os.makedirs("processed")
    print("creat folder - [processed]")
SPEECH = "./speech/"
if os.path.exists(SPEECH):
    print("alredy - [processed]")
    pass
else:
    os.makedirs("speech")
    print("creat folder - [speech]")
CONVERT = "./convert/"
if os.path.exists(CONVERT):
    print("alredy - [convert]")
    pass
else:
    os.makedirs("convert")
    print("creat folder - [convert]")
LOCATION = "./location/"
if os.path.exists(LOCATION):
    print("alredy - [location]")
    pass
else:
    os.makedirs("location")
    print("creat folder - [location]")
STICKER = "./sticker/"
if os.path.exists(STICKER):
    print("alredy - [sticker]")
    pass
else:
    os.makedirs("sticker")
    print("creat folder - [sticker]")
TRANSLATE = "./translate/"
if os.path.exists(TRANSLATE):
    print("alredy - [translate]")
    pass
else:
    os.makedirs("translate")
    print("creat folder - [translate]")
SEARCH = "./search/"
if os.path.exists(SEARCH):
    print("alredy - [search]")
    pass
else:
    os.makedirs("search")
    print("creat folder - [search]")
#-----------------------------------------------------------------
@bot.message_handler(commands=["start"])
def start(message):
    chat_id=message.chat.id
    bot.send_message(chat_id=chat_id,text=f"""
    SAZOM Company
    ------------------------------
     مرحبا ({message.from_user.first_name})
     هذا هو بوت شركة SAZOM الرسمي هناك الكثير من الخدمات المجانية والتي ستجدها عن الآخرين بالدفع الإلكتروني.
حسنا:
1) ما هي شركة SAZOM ؟
في الواقع SAZOM هي شركة برمجية ظهرت في الفترة الأخيرة لها الكثير من الخدمات البرمجية التي تتيح للمستخدم سهولة العمل بكافة الخدمات المجانية المتاحة لدى هذه الشركة.
2) ما الخدمات التي تقدمها الشركة بشكل مختصر؟
1️⃣ /download وهي تعني تنزيل أي فيديو من اليوتيوب حصرا بأعلى دقة ممكنة
2️⃣ /remove وهي تعني حذف خلفية أي صورة بالذكاء الإصطناعي يعني: اذا كانت لديك صورة وورائك خلفية لا تريدها فقط ارسلها للبوت وهو سيقوم بحذف هذه الخلفية لك.
3️⃣ /speech وهي تعني تحويل أي نص تكتبه الى كلام باللغة العربية مع مراعاة التشكيل, مثلا: مازنٌ يمشي في الحديقةِ.
4️⃣ /convert وهي تعني تحويل الفيديو الى موسيقى, أي: أنا لدي فيديو وأريد تحويله الى موسيقى كل ما عليك فعله فقط إرسال هذا الفيديو الى بوت وهو سيقوم بتحويله
5️⃣ /location هي خدمة جديدة وقوية ولكن هي قيد التطوير فكرتها ببساطة أنها تستطيع من خلال الرقم الذي ترسله لها معرفة اسم الدولة مثلا: +963 ستعرف مباشرة أنها لدولة سوريا وتعرف أيضا اسم الشركة الصانعة مثلا: 51****** هذه لشركة MTN ومن خلال هذه المعلومات تأخذ إحداثيات هذا الرقم وعندها ترسل ملف بلاحقة HTML لتعرف مكان صاحب هذا الرقم. ولكن للأسف الشديد هذه الخدمة قيد التطوير وسيتم تشغيلها قريبا
6️⃣ /speed وهي تعني Speed Test Internet يعني قياس سرعة الانترنت لديك.
7️⃣ /sticker وهي تعني تحويل صورة ترسلها للبوت الى ملصق.
8️⃣ /trans وهي تعني ترجمة أي نص إلى اللغة العربية
9️⃣ /search وهي تعني بحث عن أي شيء في محرك البحث جوجل بمجرب ما إن تبحث عن أي شيء سيظهر لك رابط به الشيء الذي بحثت عنه

ملاحظة:📝 كل هذه الخدمات تحافظ على خصوصية المستخدم بمجرد ما إن تنتهي ال function من العمل تحذف كل الوسائط والرسائل التي حفظت بالبوت من أجل الاستخدام والمعالجة.
ملاحظة2: 📝 البوت في حالة تطوير دائمة لذلك يتوقف لمدة لا تتجاوز ال 8 ساعات للتطوير ولا تقلق سيتم إعلام المستخدمين بالوقت الذي سيتم إطفاء البوت فيه.
عموما: أرجو الاستفادة من هذا البوت ونشره لأكبر قدر من المستخدمين على الأقل لأصدقائك ❤️‍🩹💯
إذا أردت التواصل مع المبرمجين 📨📩:
Alaa Safi علاء صافي 
@AlaaSafiProgrammer218 
+96395144936
___________________________________

Zaid Makhzoom  زيد مخزوم
@Zaidmakhzoom
+963 992 883 477
""")
    bot.send_message(message.chat.id,text=f"""
                لآخر تحديث حصل في:
                Day: 17
                Month: 04
                Year: 24
                Hour: 23
                Min: 05
                Sec: 53
                datetime: 2024-04-17 23:05:53.021730
                تمت إضافة خاصية البحث من جوجل 🆕                 
            """)
    bot.send_message(chat_id="6020331913",text=f"""
        New User!
        Name: {message.from_user.first_name}
        ID User: {message.from_user.id}
        {datetime.now()}
    """)
    bot.send_message(chat_id="6618502081",text=f"""
        New User!
        Name: {message.from_user.first_name}
        ID User: {message.from_user.id}
        {datetime.now()}
    """)
@bot.message_handler(commands=["help"])
def help(message):
    chat_id=message.chat.id
    bot.send_message(chat_id=chat_id,text="""
     هذا هو بوت شركة SAZOM الرسمي هناك الكثير من الخدمات المجانية والتي ستجدها عن الآخرين بالدفع الإلكتروني.
حسنا:
1) ما هي شركة SAZOM ؟
في الواقع SAZOM هي شركة برمجية ظهرت في الفترة الأخيرة لها الكثير من الخدمات البرمجية التي تتيح للمستخدم سهولة العمل بكافة الخدمات المجانية المتاحة لدى هذه الشركة.
2) ما الخدمات التي تقدمها الشركة بشكل مختصر؟
1️⃣ /download وهي تعني تنزيل أي فيديو من اليوتيوب حصرا بأعلى دقة ممكنة
2️⃣ /remove وهي تعني حذف خلفية أي صورة بالذكاء الإصطناعي يعني: اذا كانت لديك صورة وورائك خلفية لا تريدها فقط ارسلها للبوت وهو سيقوم بحذف هذه الخلفية لك.
3️⃣ /speech وهي تعني تحويل أي نص تكتبه الى كلام باللغة العربية مع مراعاة التشكيل, مثلا: مازنٌ يمشي في الحديقةِ.
4️⃣ /convert وهي تعني تحويل الفيديو الى موسيقى, أي: أنا لدي فيديو وأريد تحويله الى موسيقى كل ما عليك فعله فقط إرسال هذا الفيديو الى بوت وهو سيقوم بتحويله
5️⃣ /location هي خدمة جديدة وقوية ولكن هي قيد التطوير فكرتها ببساطة أنها تستطيع من خلال الرقم الذي ترسله لها معرفة اسم الدولة مثلا: +963 ستعرف مباشرة أنها لدولة سوريا وتعرف أيضا اسم الشركة الصانعة مثلا: 51****** هذه لشركة MTN ومن خلال هذه المعلومات تأخذ إحداثيات هذا الرقم وعندها ترسل ملف بلاحقة HTML لتعرف مكان صاحب هذا الرقم. ولكن للأسف الشديد هذه الخدمة قيد التطوير وسيتم تشغيلها قريبا
6️⃣ /speed وهي تعني Speed Test Internet يعني قياس سرعة الانترنت لديك.
7️⃣ /sticker وهي تعني تحويل صورة ترسلها للبوت الى ملصق.
8️⃣ /trans وهي تعني ترجمة أي نص إلى اللغة العربية
9️⃣ /search وهي تعني بحث عن أي شيء في محرك البحث جوجل بمجرب ما إن تبحث عن أي شيء سيظهر لك رابط به الشيء الذي بحثت عنه

ملاحظة:📝 كل هذه الخدمات تحافظ على خصوصية المستخدم بمجرد ما إن تنتهي ال function من العمل تحذف كل الوسائط والرسائل التي حفظت بالبوت من أجل الاستخدام والمعالجة.
ملاحظة2: 📝 البوت في حالة تطوير دائمة لذلك يتوقف لمدة لا تتجاوز ال 8 ساعات للتطوير ولا تقلق سيتم إعلام المستخدمين بالوقت الذي سيتم إطفاء البوت فيه.
عموما: أرجو الاستفادة من هذا البوت ونشره لأكبر قدر من المستخدمين على الأقل لأصدقائك ❤️‍🩹💯
إذا أردت التواصل مع المبرمجين 📨📩:
Alaa Safi علاء صافي 
@AlaaSafiProgrammer218 
+96395144936
___________________________________

Zaid Makhzoom  زيد مخزوم
@Zaidmakhzoom
+963 992 883 477
""")
    bot.send_message(message.chat.id,text=f"""
                لآخر تحديث حصل في:
                Day: 17
                Month: 04
                Year: 24
                Hour: 23
                Min: 05
                Sec: 53
                datetime: 2024-04-17 23:05:53.021730
                تمت إضافة خاصية البحث من جوجل 🆕                 
            """)
    bot.send_message(chat_id="6020331913",text=f"""
        Asking a Help!
        Name: {message.from_user.first_name}
        ID User: {message.from_user.id}
        {datetime.now()}
    """)
    bot.send_message(chat_id="6618502081",text=f"""
        Asking a Help!
        Name: {message.from_user.first_name}
        ID User: {message.from_user.id}
        {datetime.now()}
    """)
    
#--------------------------------------------------------------- download func
@bot.message_handler(commands=["download"])
def start_down(message):
    chat_id=message.chat.id
    defdown=bot.send_message(chat_id=chat_id,text=f"أهلا بك يا {message.from_user.first_name} في خدمة تنزيل الفيديو من اليوتيوب بأعلى دقة, كل ما عليك فعله هو أن ترسل لي الرابط")
    bot.register_next_step_handler(defdown,download_sazom)
def download_sazom(message):
    try:
        chat_id=message.chat.id
        url = message.text
        yt = YouTube(url)
        bot.send_message(chat_id=chat_id,text=f"نحن نقوم بتنزيل الفيديو الخاص بك ('''{yt.title}''')(720p) الرجاء الإتظار...")
        video = yt.streams.get_highest_resolution()
        filename = f"./downloads/SAZOM.mp4"
        video.download(filename=filename)
        mediadownload = open("./downloads/SAZOM.mp4",'rb')
        bot.send_video(chat_id=chat_id,video=mediadownload)
        bot.send_message(chat_id=chat_id,text="شكرا لاستخدامك هذا البوت, أرجو أن يكون قد نال إعجابك, يمكنك دعمنا بأن تنشر هذا البوت على الأقل لأصدقائك 💯💯")
        mediadownload.close()
        os.remove("./downloads/SAZOM.mp4")
        bot.send_message(message.chat.id,text=f"""
                لآخر تحديث حصل في:
                Day: 17
                Month: 04
                Year: 24
                Hour: 23
                Min: 05
                Sec: 53
                datetime: 2024-04-17 23:05:53.021730
                تمت إضافة خاصية البحث من جوجل 🆕                 
            """)
        bot.send_message(chat_id="6020331913",text=f"""
        [Download Youtube Video]: - Done Using
        Name: {message.from_user.first_name}
        ID User: {message.from_user.id}
        {datetime.now()}
        """)
        bot.send_message(chat_id="6618502081",text=f"""
        [Download Youtube Video]: - Done Using
        Name: {message.from_user.first_name}
        ID User: {message.from_user.id}
        {datetime.now()}
        """)
    except Exception as e:
        bot.reply_to(message, "عذرا هناك خطأ ما, الرجاء إعادة المحاولة.")
        bot.send_message(chat_id="6020331913",text=f"""
        [Download Youtube Video]: - Falid is ((({e})))
        Name: {message.from_user.first_name}
        ID User: {message.from_user.id}
        {datetime.now()}
        """)
        bot.send_message(chat_id="6618502081",text=f"""
        [Download Youtube Video]: - Falid is ((({e})))
        Name: {message.from_user.first_name}
        ID User: {message.from_user.id}
        {datetime.now()}
        """)
    
#---------------------------------------------------------- Remove Background Image func
@bot.message_handler(commands=["remove"])
def remove_sazom(message):
    chat_id=message.chat.id
    defremove=bot.send_message(chat_id=chat_id,text=f"أهلا {message.from_user.first_name} الرجاء إرسال الصورة المراد حذف خلفيتها")
    bot.register_next_step_handler(defremove,handle_photo)
def handle_photo(message):
    chat_id=message.chat.id
    try:
        photo = message.photo[-1]
        file_id = photo.file_id
        bot.send_message(chat_id=chat_id,text="نحن نقوم بمعالجة الصورة. الرجاء الإنتظار...")
        file_info = bot.get_file(file_id)
        file_path = file_info.file_path
        save_path = "temp/SAZOM.jpg"
        downloaded_file = bot.download_file(file_path)
        with open(save_path, 'wb') as new_file:
            new_file.write(downloaded_file)
        input_path = "./temp/SAZOM.jpg"
        output_path = "./processed/SAZOM.png"
        input = Image.open(input_path)
        output = remove(input)
        output.save(output_path)
        os.remove("./temp/SAZOM.jpg")
        mediarembg = open("./processed/SAZOM.png",'rb')
        bot.send_photo(chat_id=chat_id,photo=mediarembg)
        bot.send_message(chat_id=chat_id,text="شكرا لاستخدامك هذا البوت, أرجو أن يكون قد نال إعجابك, يمكنك دعمنا بأن تنشر هذا البوت على الأقل لأصدقائك 💯💯")
        mediarembg.close()
        os.remove("./processed/SAZOM.png")
        bot.send_message(message.chat.id,text=f"""
                لآخر تحديث حصل في:
                Day: 17
                Month: 04
                Year: 24
                Hour: 23
                Min: 05
                Sec: 53
                datetime: 2024-04-17 23:05:53.021730
                تمت إضافة خاصية البحث من جوجل 🆕                 
            """)
        bot.send_message(chat_id="6020331913",text=f"""
        [Remove Background]: - Done Using
        Name: {message.from_user.first_name}
        ID User: {message.from_user.id}
        {datetime.now()}
        """)
        bot.send_message(chat_id="6618502081",text=f"""
        [Remove Background]: - Done Using
        Name: {message.from_user.first_name}
        ID User: {message.from_user.id}
        {datetime.now()}
        """)
    except Exception as e:
        bot.reply_to(message, "عذرا هناك خطأ ما, الرجاء إعادة المحاولة.")
        bot.send_message(chat_id="6020331913",text=f"""
        [Remove Background]: - Falid is ((({e})))
        Name: {message.from_user.first_name}
        ID User: {message.from_user.id}
        {datetime.now()}
        """)
        bot.send_message(chat_id="6618502081",text=f"""
        [Remove Background]: - Falid is ((({e})))
        Name: {message.from_user.first_name}
        ID User: {message.from_user.id}
        {datetime.now()}
        """)
#-------------------------------------------------------text to speech
@bot.message_handler(commands=["speech"])
def speech_sazom(message):
    chat_id = message.chat.id
    speech = bot.send_message(chat_id=chat_id,text=f"أهلا بك {message.from_user.first_name} الرجاء كتابة النص المراد تحويله الى صوت")
    bot.register_next_step_handler(speech,text_to_speech)
def text_to_speech(message):
    try:
        chat_id = message.chat.id
        text = message.text
        bot.send_message(chat_id=chat_id,text="نحن نقوم بمعالجة النص الذي كتبته. الرجاء الإنتظار...")
        tts = gTTS(text=text, lang='ar', slow=False)
        tts.save("./speech/SAZOM.mp3")
        mediaspeech = open("./speech/SAZOM.mp3","rb")
        bot.send_audio(chat_id=chat_id,audio=mediaspeech)
        bot.send_message(chat_id=chat_id,text="شكرا لاستخدامك هذا البوت, أرجو أن يكون قد نال إعجابك, يمكنك دعمنا بأن تنشر هذا البوت على الأقل لأصدقائك 💯💯")
        mediaspeech.close()
        os.remove("./speech/SAZOM.mp3")
        bot.send_message(message.chat.id,text=f"""
                لآخر تحديث حصل في:
                Day: 17
                Month: 04
                Year: 24
                Hour: 23
                Min: 05
                Sec: 53
                datetime: 2024-04-17 23:05:53.021730
                تمت إضافة خاصية البحث من جوجل 🆕                 
            """)
        bot.send_message(chat_id="6020331913",text=f"""
        [Speech]: - Done Using
        Name: {message.from_user.first_name}
        ID User: {message.from_user.id}
        {datetime.now()}
        """)
        bot.send_message(chat_id="6618502081",text=f"""
        [Speech]: - Done Using
        Name: {message.from_user.first_name}
        ID User: {message.from_user.id}
        {datetime.now()}
        """)
    except Exception as e:
        bot.reply_to(message, "عذرا هناك خطأ ما, الرجاء إعادة المحاولة.")
        bot.send_message(chat_id="6020331913",text=f"""
        [Speech]: - Falid is ((({e})))
        Name: {message.from_user.first_name}
        ID User: {message.from_user.id}
        {datetime.now()}
        """)
        bot.send_message(chat_id="6618502081",text=f"""
        [Speech]: - Falid is ((({e})))
        Name: {message.from_user.first_name}
        ID User: {message.from_user.id}
        {datetime.now()}
        """)

#----------------------------------------------------mp4 to mp3
@bot.message_handler(commands=["convert"])
def conver_welc(message):
    chat_id=message.chat.id
    defconvert=bot.send_message(chat_id=chat_id,text=f"أهلا بك {message.from_user.first_name} الرجاء ارسال الفيديو الذي تريد تحويله الى موسيقى")
    bot.register_next_step_handler(defconvert,convert_sazom)
def convert_sazom(message):
    try:
        chat_id=message.chat.id
        video = message.video
        file_id = video.file_id
        file_info = bot.get_file(file_id)
        file_path = file_info.file_path
        save_path = "convert/SAZOM.mp4"
        downloaded_file = bot.download_file(file_path)
        with open(save_path, 'wb') as new_file:
            new_file.write(downloaded_file)
        bot.send_message(chat_id=chat_id,text="نحن نقوم بمعالجة الفيديوالذي ارسلته. الرجاء الإنتظار...")
        input= "./convert/SAZOM.mp4"
        mp4 = moviepy.editor.VideoFileClip(input)
        mp3 = mp4.audio
        mp3.write_audiofile("./convert/SAZOM.mp3")
        mediaconvert=open("./convert/SAZOM.mp3",'rb')
        bot.send_audio(chat_id=chat_id,audio=mediaconvert)
        bot.send_message(chat_id=chat_id,text="شكرا لاستخدامك هذا البوت, أرجو أن يكون قد نال إعجابك, يمكنك دعمنا بأن تنشر هذا البوت على الأقل لأصدقائك 💯💯")
        mediaconvert.close()
        mp4.close()
        os.remove("./convert/SAZOM.mp3")
        os.remove("./convert/SAZOM.mp4")
        bot.send_message(message.chat.id,text=f"""
                لآخر تحديث حصل في:
                Day: 17
                Month: 04
                Year: 24
                Hour: 23
                Min: 05
                Sec: 53
                datetime: 2024-04-17 23:05:53.021730
                تمت إضافة خاصية البحث من جوجل 🆕                 
            """)
        bot.send_message(chat_id="6020331913",text=f"""
        [Convert]: - Done Using
        Name: {message.from_user.first_name}
        ID User: {message.from_user.id}
        {datetime.now()}
        """)
        bot.send_message(chat_id="6618502081",text=f"""
        [Convert]: - Done Using
        Name: {message.from_user.first_name}
        ID User: {message.from_user.id}
        {datetime.now()}
        """)
    except Exception as e:
        bot.reply_to(message, text="عذرا هناك خطأ ما, الرجاء إعادة المحاولة.")
        bot.send_message(chat_id="6020331913",text=f"""
        [Convert]: - Falid is ((({e})))
        Name: {message.from_user.first_name}
        ID User: {message.from_user.id}
        {datetime.now()}
        """)
        bot.send_message(chat_id="6618502081",text=f"""
        [Convert]: - Falid is ((({e})))
        Name: {message.from_user.first_name}
        ID User: {message.from_user.id}
        {datetime.now()}
        """)
#---------------------------------------------------------- phone number location
@bot.message_handler(commands=["location"])
def location(message):
    bot.reply_to(message,text="عذرا هذه الخدمة قيد التطوير حاليا سيتم إضافتها بأقرب وقت ممكن وسيتم إعلام جميع المستخدمين.")
    bot.send_message(message.chat.id,text=f"""
                لآخر تحديث حصل في:
                Day: 17
                Month: 04
                Year: 24
                Hour: 23
                Min: 05
                Sec: 53
                datetime: 2024-04-17 23:05:53.021730
                تمت إضافة خاصية البحث من جوجل 🆕                 
            """)
    bot.send_message(chat_id="6020331913",text=f"""
        [Location Number]: - Asking This Service
        Name: {message.from_user.first_name}
        ID User: {message.from_user.id}
        {datetime.now()}
        """)
    bot.send_message(chat_id="6618502081",text=f"""
        [Location Number]: - Asking This Service
        Name: {message.from_user.first_name}
        ID User: {message.from_user.id}
        {datetime.now()}
        """)
#------------------------------------------- speed test
@bot.message_handler(commands=["speed"])
def speed_welc(message):
    chat_id=message.chat.id
    defspeed=bot.send_message(chat_id=chat_id,text="نحن نقوم بقياس سرعة الإنترنت لديك, الرجاء الإنتظار قد يستغؤق هذا بضع دقائق...")
    bot.register_next_step_handler(defspeed,speed_sazom)
def speed_sazom(message):
    try:
        chat_id=message.chat.id
        sp = speedtest.Speedtest()
        def bytes_to_mb(size_bytes):
            i = int(math.floor(math.log(size_bytes,1024)))
            power = math.pow(1024,i)
            size = round(size_bytes / power,2)
            return f"{size} Mpbs"
        down = sp.download()
        up = sp.upload()
        server = []
        sp.get_servers(server)
        bot.send_message(chat_id=chat_id,text=f"""
            
                                -------------------------
            Download: {bytes_to_mb(down)}
            -------------------------
            Upload: {bytes_to_mb(up)}
            -------------------------
            Ping: {sp.results.ping}
        """)
        bot.send_message(chat_id=chat_id,text="شكرا لاستخدامك هذا البوت, أرجو أن يكون قد نال إعجابك, يمكنك دعمنا بأن تنشر هذا البوت على الأقل لأصدقائك 💯💯")
        bot.send_message(message.chat.id,text=f"""
                لآخر تحديث حصل في:
                Day: 17
                Month: 04
                Year: 24
                Hour: 23
                Min: 05
                Sec: 53
                datetime: 2024-04-17 23:05:53.021730
                تمت إضافة خاصية البحث من جوجل 🆕                 
            """)
        bot.send_message(chat_id="6020331913",text=f"""
        [Speed Test Internet]: - Done Using
        Name: {message.from_user.first_name}
        ID User: {message.from_user.id}
        {datetime.now()}
        """)
        bot.send_message(chat_id="6618502081",text=f"""
        [Speed Test Internet]: - Done Using
        Name: {message.from_user.first_name}
        ID User: {message.from_user.id}
        {datetime.now()}
        """)
    except Exception as e:
        bot.reply_to(message, text="عذرا هناك خطأ ما, الرجاء إعادة المحاولة.")
        bot.send_message(chat_id="6020331913",text=f"""
        [Speed Test Internet]: - Falid is((({e})))
        Name: {message.from_user.first_name}
        ID User: {message.from_user.id}
        {datetime.now()}
        """)
        bot.send_message(chat_id="6618502081",text=f"""
        [Speed Test Internet]: - Falid is((({e})))
        Name: {message.from_user.first_name}
        ID User: {message.from_user.id}
        {datetime.now()}
        """)
#--------------------------------------------------- image to sticker
@bot.message_handler(commands=["sticker"])
def sticker_welc(message):
    chat_id=message.chat.id
    defsticker=bot.send_message(chat_id=chat_id,text=f"اهلا بك {message.from_user.first_name} الرجاء ارسال الصورة المراد تحويلها الى ملصق.")
    bot.register_next_step_handler(defsticker,sticker_sazom)
def convert_to_sticker(image_path):
    try:
        input_image = Image.open(image_path)
        sticker_size = (512, 512)
        input_image.thumbnail(sticker_size)
        if input_image.size[0] != sticker_size[0] or input_image.size[1] != sticker_size[1]:
            background = Image.new('RGBA', sticker_size, (255, 255, 255, 0))
            background.paste(input_image, ((sticker_size[0] - input_image.size[0]) // 2, (sticker_size[1] - input_image.size[1]) // 2))
            input_image = background
        sticker_path = './sticker/SAZOM.webp'
        input_image.save(sticker_path)
        return sticker_path
    except Exception as e:
        print("عذرا هناك خطأ ما, الرجاء إعادة المحاولة.")
def sticker_sazom(message):
    try:
        file_id = message.photo[-1].file_id
        chat_id=message.chat.id
        file_info = bot.get_file(file_id)
        downloaded_file = bot.download_file(file_info.file_path)
        bot.send_message(chat_id=chat_id,text="نحن نقوم بمعالجة الصورة التي ارسلتها , الرجاء الإنتظار...")
        with open('./sticker/SAZOM.jpg', 'wb') as new_file:
            new_file.write(downloaded_file)
        sticker_path = convert_to_sticker('./sticker/SAZOM.jpg')
        if sticker_path:
            sticker_file = open(sticker_path, 'rb')
            bot.send_sticker(message.chat.id, sticker_file)
            bot.send_message(chat_id=chat_id,text="شكرا لاستخدامك هذا البوت, أرجو أن يكون قد نال إعجابك, يمكنك دعمنا بأن تنشر هذا البوت على الأقل لأصدقائك 💯💯")
            sticker_file.close()
            os.remove("./sticker/SAZOM.jpg")
            os.remove("./sticker/SAZOM.webp")
            bot.send_message(message.chat.id,text=f"""
                لآخر تحديث حصل في:
                Day: 17
                Month: 04
                Year: 24
                Hour: 23
                Min: 05
                Sec: 53
                datetime: 2024-04-17 23:05:53.021730
                تمت إضافة خاصية البحث من جوجل 🆕                 
            """)
            bot.send_message(chat_id="6020331913",text=f"""
            [Sticker]: - Done Using
            Name: {message.from_user.first_name}
            ID User: {message.from_user.id}
            {datetime.now()}
            """)
            bot.send_message(chat_id="6618502081",text=f"""
            [Sticker]: - Done Using
            Name: {message.from_user.first_name}
            ID User: {message.from_user.id}
            {datetime.now()}
            """)
        else:
            bot.send_message(message.chat.id, "عذرا هناك خطأ ما, الرجاء إعادة المحاولة.")
    except Exception as e:
        bot.reply_to(message,text="عذرا هناك خطأ ما, الرجاء إعادة المحاولة.")
        bot.send_message(chat_id="6020331913",text=f"""
        [Sticker]: - Falid is ((({e})))
        Name: {message.from_user.first_name}
        ID User: {message.from_user.id}
        {datetime.now()}
        """)
        bot.send_message(chat_id="6618502081",text=f"""
        [Sticker]: - Falid is ((({e})))
        Name: {message.from_user.first_name}
        ID User: {message.from_user.id}
        {datetime.now()}
        """)
#-------------------------------------------------- Translate
@bot.message_handler(commands=["trans"])
def tran_welc(message):
    chat_id = message.chat.id
    deftrans = bot.send_message(chat_id=chat_id,text=f"أهلا بك {message.from_user.first_name}. الرجاء إرسال أي نص تريد ترجمته من أي لغة إلى العربية")
    bot.register_next_step_handler(deftrans,sazom_trans)
def sazom_trans(message):
    try:
        chat_id=message.chat.id
        translator = Translator()
        with open("./translate/SAZOM.txt",'w',encoding="utf-8") as file:
            file.write(message.text)
        bot.send_message(chat_id=chat_id,text="نحن نقوم بمعالجة النص الذي ارسلته, الرجاء الإنتظار...")
        with open("./translate/SAZOM.txt","r",encoding="utf-8") as file:
            SAZOM_file = file.read()
        SAZOM_ar = translator.translate(text=SAZOM_file,src="auto",dest="ar").text
        with open("./translate/SAZOM_ar.txt","w", encoding="utf-8") as file:
            file.write(SAZOM_ar)
        text = open("./translate/SAZOM_ar.txt","rb")
        bot.send_message(chat_id=chat_id,text=text)
        bot.send_message(chat_id=chat_id,text="شكرا لاستخدامك هذا البوت, أرجو أن يكون قد نال إعجابك, يمكنك دعمنا بأن تنشر هذا البوت على الأقل لأصدقائك 💯💯")
        text.close()
        os.remove("./translate/SAZOM_ar.txt")
        os.remove("./translate/SAZOM.txt")
        bot.send_message(message.chat.id,text=f"""
                لآخر تحديث حصل في:
                Day: 17
                Month: 04
                Year: 24
                Hour: 23
                Min: 05
                Sec: 53
                datetime: 2024-04-17 23:05:53.021730
                تمت إضافة خاصية البحث من جوجل 🆕                 
            """)
        bot.send_message(chat_id="6020331913",text=f"""
            [Translate]: - Done Using
            Name: {message.from_user.first_name}
            ID User: {message.from_user.id}
            {datetime.now()}
            """)
        bot.send_message(chat_id="6618502081",text=f"""
            [Translate]: - Done Using
            Name: {message.from_user.first_name}
            ID User: {message.from_user.id}
            {datetime.now()}
            """)
    except Exception as e:
        bot.reply_to(message,text="عذرا هناك خطأ ما, الرجاء إعادة المحاولة.")
        bot.send_message(chat_id="6020331913",text=f"""
            [Translate]: - Falid is: ((({e})))
            Name: {message.from_user.first_name}
            ID User: {message.from_user.id}
            {datetime.now()}
            """)
        bot.send_message(chat_id="6618502081",text=f"""
            [Translate]: - Falid is: ((({e})))
            Name: {message.from_user.first_name}
            ID User: {message.from_user.id}
            {datetime.now()}
            """)
#--------------------------------------------- search
@bot.message_handler(commands=["search"])
def search_welc(message):
    defsearch = bot.send_message(message.chat.id,text=f"أهلا بك {message.from_user.first_name}. للبحث على أي شيء في محركات البحث جوجل فقط أرسل الذي تريد كتابته في جوجل")
    bot.register_next_step_handler(defsearch,sazom_search)
def sazom_search(message):
    with open("./search/SAZOM.txt","w",encoding="utf-8") as file:
        bot.send_message(message.chat.id,text="نحن نقوم بمعالجة النص الذي كتبته, الرجاء الإنتظار...")
        try:
            query =message.text
            search_results = search(query,num_results=10)
            for result in search_results:
                file.write(result + '\n')
            file.close()
            searched = open("./search/SAZOM.txt","rb")
            bot.send_message(message.chat.id,text=searched)
            bot.send_message(message.chat.id,text="شكرا لاستخدامك هذا البوت, أرجو أن يكون قد نال إعجابك, يمكنك دعمنا بأن تنشر هذا البوت على الأقل لأصدقائك 💯💯")
            bot.send_message(message.chat.id,text=f"""
                لآخر تحديث حصل في:
                Day: 17
                Month: 04
                Year: 24
                Hour: 23
                Min: 05
                Sec: 53
                datetime: 2024-04-17 23:05:53.021730
                تمت إضافة خاصية البحث من جوجل 🆕                 
            """)
            searched.close()
            os.remove("./search/SAZOM.txt")
        except Exception as e:
            bot.reply_to(message,text="عذرا هناك خطأ ما, الرجاء إعادة المحاولة.")
#--------------------------------------------- start
print('-'*50)
print("The Bot is Running in v1.3...!")
SERVER()
bot.infinity_polling()
