import pyttsx3


def speak_text():
    engine = pyttsx3.init()

    print("Welcome to RoboSpeaker 1.1 created by almas")

    # Ask the user for their language choice
    language_choice = input("Choose a language ('hindi' or 'urdu'): ").lower()

    while True:
        text = input("Enter what you want me to speak (or 'q' to quit): ")

        if text.lower() == 'q':
            engine.say('bye bye friend')
            engine.runAndWait()
            break

        # Set the voice based on the language choice
        if language_choice == 'hindi':
            engine.setProperty('voice', 'hi')  # Hindi voice
        elif language_choice == 'urdu':
            engine.setProperty('voice', 'ur')  # Urdu voice

        engine.say(text)
        engine.runAndWait()


if __name__ == '__main__':
    speak_text()