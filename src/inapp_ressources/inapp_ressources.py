import Learn_HTML.src.inapp_text.inapp_text as text


def verif_qst(answer):
    if answer > 1:
        return None

    return True if answer == 1 else False


def react_qst1(answer, target_text):
    answer = verif_qst(answer)
    if answer == True:
        target_text.set(text.true_answ)
    elif answer == None:
        target_text.set(text.no_answ)
    else:
        target_text.set(text.false_answ)
