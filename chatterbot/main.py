from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for your entire Flask app
ip = '192.168.0.108'
@app.route('/api', methods=['POST'])
def chatbot():
    data = request.get_json()
    user_message = data.get('message', '')

    # Print the incoming message to the console
    print("Received message:", user_message)
    # with open("logs.txt","+a") as p:
    #     p.writelines(user_message)

    # You can perform more sophisticated bot logic here
    # For now, just return "Hello" for every message
    
    bot_response = bot(user_message)

    return jsonify({'message': bot_response})

messages ={
    "About sspm?":"sspm is collage of engineering in sindhudurg established in 1999",
    "Could you provide an overview of the Computer Science program offered at SSPM College of Engineering?":"Certainly! The Computer Science program at SSPM College of Engineering is a comprehensive four-year undergraduate program designed to equip students with a strong foundation in computer science. It covers a wide range of subjects, including programming languages, algorithms, data structures, and computer architecture. The program also emphasizes hands-on learning through lab work and real-world projects",
    "How can I get in touch with the admissions office for inquiries regarding the application process?":"You can contact the admissions office at SSPM College of Engineering through the following methods:",
    "Hello":"Hello there! How can I assist you?",
}
def bot(message): # --> str message
    for i,j in messages.items():
        if i == message:
            return j 

    return "hello " + message



@app.route('/home',methods=['GET'])
def homes():
    return 'welcome to my homepage'

# if __name__ == '__main__':
app.run(host=ip, port=3030, debug=True)