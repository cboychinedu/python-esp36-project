# Importing the necessary modues 
from machine import Pin
import socket 

# Setting the led pin 
led = Pin(2, Pin.OUT); 

# Creating a function for the information page 
def information_page(): 
    # Creating the html page 
    html = """
        <html lang="en"> 
            <head> 
                <style> 
                    body {
                        font-family: 'Poppins'; 
                    }
                    .para {
                        color: blue; 
                        font-size: 26px; 
                    }
                </style> 
                <link href='https://fonts.googleapis.com/css?family=Poppins' rel='stylesheet'>
                <meta charset="UTF-8">
                <meta http-equiv="X-UA-Compatible" content="IE=edge">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title> ESP SERVER </title> 
            </head> 
            <body> 
                <p class="para"> INFORMATION SECTION </p>
                
                <button class="but" id="but"> PRIVACY AND FREEDOM IS A HUMAN RIGHT !!! </button>
                
                <script>
					// Getting the dom elements
					let button = document.getElementById("but");
					button.addEventListener("click", () => {
						console.log("Hello Chinedum"); 
                        
					})
                
                </script> 

            </body> 

        </html> 
    """; 

    # Returning the html page 
    return html; 

# Creating a function for the webpage 
def home_page(): 
    # Creating the html page 
    html = """
        <html lang="en"> 
            <head> 
                <style> 
                    body {
                        font-family: 'Poppins'; 
                    }
                    .para {
                        color: blue; 
                        font-size: 26px; 
                    }
                </style> 
                <link href='https://fonts.googleapis.com/css?family=Poppins' rel='stylesheet'>
                <meta charset="UTF-8">
                <meta http-equiv="X-UA-Compatible" content="IE=edge">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title> ESP SERVER </title> 
            </head> 
            <body> 
                <p class="para"> Hello Chinedum </p>
                
                <button class="but" id="but"> Send Money </button>
                
                <script>
					// Getting the dom elements
					let button = document.getElementById("but");
					button.addEventListener("click", () => {
						console.log("Hello Chinedum"); 
                        location.href = "/information"; 
					})
                
                </script> 

            </body> 

        </html> 
    """; 

    # Returning the html page 
    return html; 

# Creating the webserver using the "socket" module 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
s.bind(('', 80))
s.listen(5) 

# Running the server using a while loop 
running = True; 
while running: 
    # Accept incoming connections, and send bytes with 
    # a chunk value of "1024"
    conn, addr = s.accept() 
    print(f"Got a connection from {str(addr)}")
    request = conn.recv(1024) 
    request = str(request)
    print('Content = %s' % request)
		
	# Creating a route for the information page
    if request.find("/information") == 6:
        # Execute the block of code below if the user wants
        # # to access the /information page
        informationPage = information_page(); 

        # Setting the headers configurations 
        conn.send('HTTP/1.1 200 OK\n')
        conn.send('Content-Type: text\html\n')
        conn.send('Connection: close \n\n')
        conn.sendall(informationPage)
        conn.close(); 

    # Creating a routing mechanism
    # Getting the requested route
    else:
        # Execute the block of code below if the user wants
        # # to access the home page
        # # Sending the web page
        homePage = home_page();
		
		# Setting the headers configurations
        conn.send('HTTP/1.1 200 OK\n')
        conn.send('Content-Type: text\html\n')
        conn.send('Connection: close \n\n')
        conn.sendall(homePage);
        conn.close();

		
		
		

