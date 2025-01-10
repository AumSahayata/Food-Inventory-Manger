import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import pickle
import numpy as np

category = {'F&V': 1, 'Dairy': 2}
products = {"Milk":1, "Bread":2, "Eggs":3, "Apple":4, "Tomato":5, "Cucumber":6, "Chilli":7, "Cheese":8}

def predict(data: list, model_loc: str = 'src\ml_model\PolyStock1.pkl'):
    with open(model_loc, 'rb') as file:
        model = pickle.load(file)
        # data = [month, name, category, day, holiday]
        
        data[1] = products.get(data[1])
        data[2] = category.get(data[2])
        data[4] = 1 if data[3] > 5 else 0

        data = np.array(data)
        data = data.reshape(-1, 5)
        
        prediction = model.predict(data)
        prediction = list(prediction)
        return prediction

def send_email(data: list):
    
    data = ", ".join(data)
    
    sender_email = "opt.chatbot@gmail.com"
    password = "yqttzxhfcxzlrxfd"  # Hardcoded for testing
    receiver_email = "mansuriaafi@gmail.com"
    subject = "Test Email"
    body = f"The following products are about to expire please access the dashboard to take an action.\n {data}"

    try:
        # Use a context manager to manage the SMTP connection
        with smtplib.SMTP("smtp.gmail.com", 587) as smtp_server:
            smtp_server.starttls()  # Start TLS encryption
            smtp_server.login(sender_email, password)  # Login to the SMTP server

            # Create the email
            message = MIMEMultipart()
            message['From'] = sender_email
            message['To'] = receiver_email
            message['Subject'] = subject
            message.attach(MIMEText(body, 'plain'))

            # Send the email
            smtp_server.sendmail(sender_email, receiver_email, message.as_string())

        return {"message": "Email sent successfully"}

    except smtplib.SMTPAuthenticationError:
        return {"error": "Authentication failed. Check email credentials."}
    except Exception as e:
        return {"error": f"An error occurred: {str(e)}"}
