spam_words = ["free","winner","prize"]

email = "Theres a meeting tommoro at 10pm"

email = email.lower()

is_spam = False

for word in spam_words:
    if word in email:
        is_spam = True
        break

if is_spam:
    print("Spam")
else:
    print("Not Spam")
