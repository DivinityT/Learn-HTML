import Learn_HTML.src.inapp_text.inapp_text as text


def verif_qst(answer):
    return True if answer == 1 else False


def react_qst1(answer, target_text):
    if verif_qst(answer) == True:
        target_text.set(text.true_answ)
    else:
        target_text.set(text.false_answ)
