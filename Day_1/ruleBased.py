def input_validation(text):
    return text.strip().lower()
def intent_detection(text):
    if "price" in text:
        return "price"
    elif "hello" in text:
        return "greet"
    elif "bye" in text:
        return "exit"
    else:
        return:"unknown"
def knowledege_base(text):
    data={
        "price":"product price $100",
        "greet":"how can i help you","exit":"Have a good day",
        "unknown":"i dont understand"
        }
return data[intent_detection]
        