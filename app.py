from voice.tts import speak_telugu
from agent.memory import memory
from agent.planner import plan
from agent.executor import execute
from agent.evaluator import evaluate

def main():
    speak_telugu("ప్రభుత్వ పథకాల సహాయకునికి స్వాగతం")

    while True:
        action = plan(memory)

        if action == "ASK_AGE":
            speak_telugu("మీ వయస్సు ఎంత?")
            memory["age"] = int(input("Age: "))

        elif action == "ASK_INCOME":
            speak_telugu("మీ ఆదాయం ఎంత?")
            memory["income"] = int(input("Income: "))

        elif action == "ASK_CHILDREN":
            speak_telugu("మీకు పిల్లలు ఉన్నారా?")
            memory["children"] = input("yes/no: ") == "yes"

        elif action == "FIND_SCHEME":
            result = execute(memory)
            status = evaluate(result)

            if status == "SUCCESS":
                for s in result:
                    speak_telugu(f"మీకు {s['name']} అర్హత ఉంది")
            else:
                speak_telugu("క్షమించండి, పథకం లేదు")
            break

main()
