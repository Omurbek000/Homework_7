import re

# 1. Бардык "This" деген сөздөрдү тап
sozu = "User1: This class is fire! User2: This topic is crazy. User3: this one? meh."
result_1 = re.findall(r'\bThis\b', sozu)
print(result_1)  # Жыйынтык: ['This', 'This']

# 2. "ab", "abb", "abbb" ж.б. сыяктуу сөздөрдү тап
sozu = "Haha ab abbb abb a abbbbbbb lol"
result_2 = re.findall(r'\bab+\b', sozu)
print(result_2)  # Жыйынтык: ['ab', 'abbb', 'abb', 'ab', 'abbbbbbb']

# 3. 3 орундуу сандарды тап
sozu = "Hey, your code is 123. Mine was 999. But 45 is too short. And 4444 is too long."
result_3 = re.findall(r'\b\d{3}\b', sozu)
print(result_3)  # Жыйынтык: ['123', '999', '444']

# 4. Ali, андан кийин i болушу мүмкүн/жок, андан кийин din менен бүтмөкчү
sozu = "Alidin joined the chat. Aldin left. Aledin typing..."
result_4 = re.findall(r'\bAli?din\b', sozu)
print(result_4)  # Жыйынтык: ['Alidin', 'Aldin']

# 5. Чат ., !, же ? менен бүтөбү?
sozu = "Did you finish this message?"
result_5 = bool(re.search(r'[.!?]$', sozu))
print(result_5)  # Жыйынтык: True

# 6. cat же dog сөздөрүн тап
sozu = "I love my cat! My sister has a dog. My cousin has a parrot."
result_6 = re.findall(r'\b(cat|dog)\b', sozu)
print(result_6)  # Жыйынтык: ['cat', 'dog']