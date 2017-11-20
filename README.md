# SSHCrack
SSHCrack is a python program used to gain access to computers running Secure Shell via a dictionary attack. This is a great tool for gaining unauthorized access to computers running SSH in a given network. Ensue that you have used pip to install the paramiko module (which is how the program connects to computers using SSH.)
To install paramiko module, just run 'pip install paramiko' in terminal.
Upon running the program, assuming you properly installed paramiko, you will be prompted for the target's IP and username, as well as a dictionary file to use in the cracking process. The dictionary file should have passwords organized in the following structure:

password
admin
easypassword

You get the idea ;)
Ensure that the target computer is running the SSH service. Otherwise, this attack will not work. Of course, you can do this by using nmap or using a custom port scanner.

This program writes the cracking results to a text file that you specify, or sshcrack.txt if no file name is specified. The file will be saved in your working directory, and will show information on cracking time, IP address, username and password credentials. Please ensure that you dont have any other text files by the name that you save the results as, as this could result in unwanted overwriting of files.

Finally, this program will operate quite slowly and does generate a lot of noise on a target network. This is because each password the program attempts to use, it makes an attempt to connect the remote host and waits for a response back. This means that the program can really only check about 1 password every 2-3 seconds. This process can be lengthy, but doesnt require much processing power. Unlike hash cracking, the CPU isnt slowing us down, only network communications. 
