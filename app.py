

from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

knowledge_base = {
    🙏 What is the Bhagavad Gita
The Bhagavad Gita is one of the most prominent Hindu texts, forming a part of the Indian epic known as Mahabharata.
Originally written in Sanskrit, the Bhagavad Gita is believed to have been composed between the 5th and 2nd century BCE.
It is a guidebook to lead an enjoyable and blissful life. In other words, it is a user’s manual to lead a meaningful human life
Lord Krishna imparted this knowledge to Arjuna in the battlefield of Kurukshetra, when the latter was in a distressful condition
Upon receiving this knowledge returned to his happy and stable position
All of us undergo difficult situations in life and often become overwhelmed by those situations not knowing where to find a solution
The Bhagavad-Gita guides us out of such delusions and reestablishes us in our original position of eternity, knowledge and bliss
If we follow the instructions as given by Lord Krishna, then we can attain the same blissful state as Arjuna did
🌸 How relevant is it in modern times
The Bhagavad-gita is manual given by the Supreme Lord Krishna which guides us in making the best use of this human life and to deriving real happiness from it.
In the modern times when people are more confused and misdirected, the Gita become all the more relevant for the individual as well as the society at large in bringing back the stability and happiness in life.
What is The Bhagavad Gita
The Gita is a dialogue between the warrior-prince Arjuna and the god Krishna who is serving as his charioteer at the Battle of Kurukshetra fought between Arjunas family and allies (the Pandavas) and those of the prince Duryodhana and his family (the Kauravas) and their allies.

🚀 About Us
Bhagavad Gita is a practical guide to ones life that guides you to re-organise your life, achieve inner peace and approach the Supreme Lord (the Ultimate Reality). BhagavadGita.io is a modern Bhagavad Gita app with a simple, beautiful and easy to use interface, helping you focus on reading. It is an app built for Bhagavad Gita readers, by Bhagavad Gita readers.
}

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    question = data.get('question', '').lower()
    answer = "I'm sorry, I don't have an answer for that. Try asking about karma, duty, wisdom, etc."

    for keyword in knowledge_base:
        if keyword in question:
            answer = knowledge_base[keyword]
            break

    return jsonify({"answer": answer})

if __name__ == '__main__':
    app.run(debug=True)
