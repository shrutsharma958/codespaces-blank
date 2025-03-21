from flask import Flask
import os
from datetime import datetime
import subprocess
import getpass

app = Flask(__name__)

@app.route('/htop')
def htop():
    try:
       
        username = getpass.getuser() 
        name = "Shrut sharma"  
        server_time = datetime.now().astimezone().strftime("%Y-%m-%d %H:%M:%S IST")
        
       
        ps_output = subprocess.check_output("ps aux", shell=True).decode("utf-8")
        
       
        return f"""
            <html>
                <head><title>Server Info</title></head>
                <body>
                    <h1>Server Information</h1>
                    <p><b>Name:</b> {name}</p>
                    <p><b>Username:</b> {username}</p>
                    <p><b>Server Time (IST):</b> {server_time}</p>
                    <h3>Process Output:</h3>
                    <pre>{ps_output}</pre>
                </body>
            </html>
        """
    except Exception as e:
        return f"An error occurred: {e}"

if __name__ == '__main__':
    print("Starting Flask app...")
    app.run(host='0.0.0.0', port=5000, debug=True)
