from handwrite import handwrite
# from handwrite import handwrite is used because you only need the handwrite function from the handwrite module. 
# If you used import handwrite instead, you would need to call the function with handwrite.handwrite().

print("Starting")

txt = '''
This is Feature of pywhatkit.
    Sending Message to a WhatsApp Group or Contact
    Sending Image to a WhatsApp Group or Contact
    Converting an Image to ASCII Art
    Converting a String to Handwriting
    Playing YouTube Videos
    Sending Mails with HTML Code
    Install and Use
'''

# Defines the path of my hand writting that in which format i want outpot
sample_path = "C:\\Users\\rajpr\\OneDrive\\Pictures\\Screenshots\\Screenshot 2024-04-22 004954.png"

# The output file name
output = "Handwrittin_demo.svg"

# Use handwrite to convert your text to handwriting
handwrite(txt , sample_path, output)
print("END")
