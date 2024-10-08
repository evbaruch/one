# מבנה שפות תוכנה - תרגיל 1 

# name: Evyatar Baruch 
# I.D: 323916403

# name: Sapir Bashan
# I.D: 214103368

from functools import reduce
from itertools import chain
from operator import or_




# 1. Penta Numbers
def getPentaNum(n):
    """
    מחשבת את ה-Penta Number ה-n.
    פונקציה טהורה: התוצאה תלויה רק בקלט n.
    """
    return n * (3 * n - 1) // 2

def pentaNumRange(n1, n2):
    """
    מחזירה רשימה של Penta Numbers בין n1 ל-n2 (לא כולל n2).
    פונקציה טהורה: משתמשת ב-list comprehension.
    """
    return list(map(getPentaNum, range(n1, n2)))

# 2. סכום ספרות
def sumDigit(n):
    """
    מחשבת את סכום הספרות של מספר שלם.
    פונקציה טהורה: משתמשת ב-sum ו-generator expression.
    """
    return sum(map(int, str(abs(n))))

# 3. חישוב גימטריה
def gematria_value(word):
    """
    מחשבת את הערך הגימטרי של מילה בעברית.
    פונקציה טהורה: משתמשת במילון קבוע.
    """
    return sum(map(lambda char: get_gematria_dict().get(char, 0), word))

def get_gematria_dict():
    """
     יוצרת מילון עם ערכי הגימטריה של אותיות העברית .
    פונקציה טהורה: משתמשת ב-dictionary comprehension.
    """
    return {
        'א': 1, 'ב': 2, 'ג': 3, 'ד': 4, 'ה': 5, 'ו': 6, 'ז': 7, 'ח': 8, 'ט': 9,
        'י': 10, 'כ': 20, 'ל': 30, 'מ': 40, 'נ': 50, 'ס': 60, 'ע': 70, 'פ': 80, 'צ': 90,
        'ק': 100, 'ר': 200, 'ש': 300, 'ת': 400
    }


# 4. Twin Primes
def is_prime(n):
    """בודקת אם מספר הוא ראשוני."""
    return n > 1 and all(map(lambda i: n % i != 0, range(2, int(n**0.5) + 1)))

def find_twin_prime(n):
    """מוצאת את התאום הראשוני של מספר ראשוני נתון."""
    return next(filter(lambda x: x is not None, map(lambda t: t if is_prime(t) else None, [n-2, n+2])), None) if is_prime(n) else None

def prime_twins_dict(n):
    """יוצרת מילון של מספרים ראשוניים והתאומים שלהם עד n."""
    return reduce(
        lambda acc, p: {**acc, p: twin} if (twin := find_twin_prime(p)) is not None else acc,
        filter(is_prime, range(2, n+1)),
        {}
    )

# 5. Merging Dictionaries (אתגר)

def add3dicts(d1, d2, d3):
    """
    ממזגת שלושה מילונים לפי הכללים שהוגדרו.
    פונקציה טהורה: יוצרת מילון חדש ללא שינוי המילונים המקוריים.
    ללא שימוש בלולאות for מכל סוג.
    """
    all_keys = reduce(or_, map(set, (d1, d2, d3)))
    
    return dict(
        zip(
            all_keys,
            map(
                lambda k: tuple(set(filter(None, map(lambda d: d.get(k), (d1, d2, d3))))),
                all_keys
            )
        )
    )
    
    
# 6. Functions as First-Class Objects

def double(x):
    """פונקציה טהורה: מכפילה מספר ב-2."""
    return x * 2

def square(x):
    """פונקציה טהורה: מעלה מספר בריבוע."""
    return x ** 2

def inverse(x):
    """פונקציה טהורה: מחשבת את ההופכי של מספר."""
    return 1 / x if x != 0 else None

def apply_functions(numbers, functions):
    """
    מפעילה רשימת פונקציות על אוסף מספרים.
    פונקציה טהורה: מדגימה שימוש בפונקציות כאובייקטים מסדר ראשון.
    
    1. מקבלת פונקציות כארגומנט
    2. משתמשת בתכונות של הפונקציות (כמו __name__)
    3. מפעילה את הפונקציות
    """
    return {
        func.__name__: list(filter(None, map(func, numbers)))
        for func in functions
    }

# דוגמת שימוש:
if __name__ == "__main__":
  
    print("Penta Numbers:", pentaNumRange(1, 6), "\n")
    print("Sum of digits of 123:", sumDigit(123), "\n")
    print("Gematria of 'אבג':", gematria_value('אבג'), "\n")
    print("Twin primes up to 20:", prime_twins_dict(20), "\n")
    print("Merging dictionaries:", add3dicts({'a': 1}, {'b': 2}, {'c': 3, 'a': 4}), "\n")
    
    numbers = [1, 2, 3, 4, 5]
    functions = [double, square, inverse]
    print("Applying functions:", apply_functions(numbers, functions), "\n")