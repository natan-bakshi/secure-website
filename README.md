# secure-website
הקמנו אתר מאובטח הכולל צד לקוח, צד שרת ובסיס נתונים.

#          צד הלקוח 
כולל ארבעה קבצי HTML
1. welcome.html- קובץ פתיחה לכניסה ראשונית לאתר, המציג את אפשרויות הכניסה (login, sign up)
2. log_in.html- דף המשרת משתמשים הרשומים לאתר, ונותן להם את האופציה להכנס על ידי שימוש בשם משתמש וסיסמא
3. sign_up.html- משמש משתמש חדש להקים משתמש במערכת לכניסה עתידית
4. hom.html- דף הבית אחר הכניסה למערכת

# צד השרת 
כולל שני קבצי פייתון
1. app.py- מפעיל את השרת, שולח ומקבל נתנוים מהלקוח, שומר את הנתונים בבסיס נתונים ומשתמש בהם לפי הצורך.
2. helper.py- קובץ המכיל פונקציות שמשרתות את השרת, כמו בדיקת סיסמאות, משתמשים ואבטחה.

#  בסיס הנתונים 
כולל שלושה קבצים עיקריים
1. db-create.py- יוצר קובץ בסיס נתנוים חדש
2. db-insert.py- קובץ המשמש להטענת נתונים חדשים לבסיס הנתונים
3. users.db- קובץ הכולל את הנתונים עצמם

# פונקציונליות
האתר יודע להתגונן מפני מתקפות sqli ומצפין את הסיסמאות לפני האיחסון שלהם.

# קצת על התהליך
במהלך התהליך למדנו להכיר עולמות חדשים של קוד שלא נפגשנו איתו בעבר, כתיבת קבצי HTML, ניהול שרת ולקוח והבנה עמוקה של תהליכים שבעבר נראו כמובנים מאליהם.
הדרך לא היתה פשוטה, נתקלנו בהמון באגים לא מוסברים ונאלצנו ללמוד המון לבד, וכשכבר עמד אתר על תילו, הרסנו אותו לגמרי שניסינו להוסיף אבטחה מינימלית. נפלנו וקמנו ושוב קמנו עד שהמוצר הזה הגיע אליכם. תתייחסו אליו יפה, זה מגיע לו.