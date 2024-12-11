def send_email(message, recipient, sender="university.help@gmail.com"):
    if "@" not in recipient or "@" not in sender or not sender(("com", ".ru", "net")) or not recipient(
            ("com", ".ru", "net")):
        print("Невозможно отправить письмо с адреса на адрес")

    elif sender == recipient:
        print("нельзя отправить письмо самому себе!")
    else:
        sender = ("university.help@gmail.com")
        print("Письмо успешно отправлено", sender.__add__(recipient))

        if sender != "university.help@gmail.com":
            print("НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ!", sender.__add__(recipient))
