adwentures_of_tom_sawer = """\
Tom gave up the brush with reluctance in his .... face but alacrity
in his heart. And while
the late steamer
"Big Missouri" worked ....
and sweated
in the sun,
the retired artist sat on a barrel in the .... shade close by, dangled his legs,
munched his apple, and planned the slaughter of more innocents.
There was no lack of material;
boys happened along every little while;
they came to jeer, but .... remained to whitewash. ....
By the time Ben was fagged out, Tom had traded the next chance to Billy Fisher for
a kite, in good repair;
and when he played
out, Johnny Miller bought
in for a dead rat and a string to swing it with—and so on, and so on,
hour after hour. And when the middle of the afternoon came, from being a
poor poverty, stricken boy in the .... morning, Tom was literally
rolling in wealth."""

##  ПЕРЕЗАПИСУЙТЕ зміст змінної adwentures_of_tom_sawer у завданнях 1-3
# task 01 ==
""" Дані у строці adwentures_of_tom_sawer розбиті випадковим чином, через помилку.
треба замінити кінець абзацу на пробіл .replace("\n", " ")"""

print("TASK 01", end='\n######\n')
adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace('\n', " ")
print(adwentures_of_tom_sawer)

# task 02 ==
""" Замініть .... на пробіл
"""
print("TASK 02", end='\n######\n')
adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace('....', " ")
print(adwentures_of_tom_sawer)

# task 03 ==
""" Зробіть так, щоб у тексті було не більше одного пробілу між словами.
"""
print("TASK 03", end='\n######\n')
list = adwentures_of_tom_sawer.split()
adwentures_of_tom_sawer = " ".join(list)
print(adwentures_of_tom_sawer)

# task 04
""" Виведіть, скількі разів у тексті зустрічається літера "h"
"""
print("TASK 04", end='\n######\n')
h_times = adwentures_of_tom_sawer.lower().count('h')
print(h_times)

# task 05
""" Виведіть, скільки слів у тексті починається з Великої літери?
"""

print("TASK 05", end='\n######\n')
list = adwentures_of_tom_sawer.split()
count = 0
for i in list:
    if i.istitle():
        count += 1
print(count)

# task 06
""" Виведіть позицію, на якій слово Tom зустрічається вдруге
"""
print("TASK 06", end='\n######\n')
tom_1 = adwentures_of_tom_sawer.lower().find("tom")
tom_count = adwentures_of_tom_sawer.lower().count("tom")
if tom_count > 1:
    start_index = tom_1 + 1
    tom_2 = adwentures_of_tom_sawer.lower().find("tom", 2)

print(tom_2)

# task 07
""" Розділіть змінну adwentures_of_tom_sawer по кінцю речення.
Збережіть результат у змінній adwentures_of_tom_sawer_sentences
"""
print("TASK 07", end='\n######\n')
adwentures_of_tom_sawer_sentences = adwentures_of_tom_sawer.split('. ')
print(adwentures_of_tom_sawer_sentences)

# task 08
""" Виведіть четверте речення з adwentures_of_tom_sawer_sentences.
Перетворіть рядок у нижній регістр.
"""
print("TASK 08", end='\n######\n')

sent_4 = adwentures_of_tom_sawer_sentences[3].lower()
print(sent_4)

# task 09
""" Перевірте чи починається якесь речення з "By the time".
"""
print("TASK 09", end='\n######\n')
phrase = "By the time"
for i in adwentures_of_tom_sawer_sentences:
    if i.startswith(phrase):
        print(f"there is a sentence, that begins from \"{phrase}\"")
# task 10
""" Виведіть кількість слів останнього речення з adwentures_of_tom_sawer_sentences.
"""
print("TASK 10", end='\n######\n')
last_sent = adwentures_of_tom_sawer_sentences[-1]
last_sent_list = last_sent.split()
last_sent_count = len(last_sent_list)
print(last_sent_count)
