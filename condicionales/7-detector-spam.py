mail_list = []
banned_words = ["free", "earn money", "exclusive discount", "opportunity","discount"]
message = ""
while True:
    print("<-- Type 0 to continue -->")
    mail = input("Enter the mail: ").lower()
    if mail == "0":
        break
    mail_list.append(mail)

for mail in mail_list:
    if any(
        # para cada palabra (word) en banned_words mira si esta en email
        word in mail
        for word in banned_words
    ):
        message += f"{mail} -> spam\n"
    else:
        message += f"{mail} -> no spam\n"

print(message)
