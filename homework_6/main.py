# 1. паспорт генератор v2(with***kwargs)
# функция жаз passport_generator(**kwargs)
# Колдонуучунун аты жашы жынысы бойу жана жарандыгын кабыл алып паспорт форматында чыгарсын


def passport_generator(**kwargs):
    passport = (
      f'Паспорт:'
      f'Аты: {kwargs.get("name", "")}'
      f'Жашы: {kwargs.get("age", "")}'
      f'Жынысы: {kwargs.get("gender", "")}'
      f'Бойу: {kwargs.get("height", "")}'
      f'Жарандыгы: {kwargs.get("citizenship", "")}'
    )
    print(passport)


passport_generator(
   name="Omurbek",
   age=29,
   gender="Мужской",
   height="170 см",
   citizenship="Кыргызстан"
)
