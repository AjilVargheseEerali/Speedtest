import sys, time
from socket import *
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import speedtest
count = 1000
BUFSIZE = 1024000
st = speedtest.Speedtest()
root=Tk()
root.title('SPEED TEST')                 #parent window
root.geometry('420x250+250+150')
root.config(background='#31112c')
label=ttk.Label(root,text='SPEED TEST')
label.grid(row=0,column=1,sticky='snew',padx=3,pady=5)
test=ttk.Button(root,text='TEST SPEED')
test.grid(row=1,column=0,columnspan=2,padx=3,pady=3)

root.rowconfigure(0,weight=1)
root.rowconfigure(1,weight=1)
root.columnconfigure(0,weight=1)
root.columnconfigure(1,weight=1)
# Functioning

def spt():
    servernames =[]
    st.get_servers(servernames)
    messagebox.showinfo(title='SPEED TEST',message='Download Speed : {} MBPS\nUpload Speed : {} MBPS\nPing : {}'.format(st.download()/(1024*1024),st.upload()/(1024*1024),st.results.ping))

test.config(command=spt)


# Style
style=ttk.Style()
style.theme_use('clam')
style.configure('TLabel',background='#31112c',foreground='#f4f4f4',font=('Arial',30))
style.configure('TButton',background='#ffc93c',font=('Arial',20))
style.map('TButton',background=[('pressed','#ec0101')])

root.mainloop()

ip="127.0.0.1"
port=2023
def client():                                   #  souce to destination
    testdata = 'x' * (BUFSIZE-1) + '\n'         #maximum utilization,,set the buffer size to lowered to reduce latency for more accurately for monitoring
    t1 = time.time()                            # finding time before socket creatation
    s = socket(AF_INET, SOCK_STREAM)                                                             # present time in code
    t2 = time.time()                            # finding time after socket creation
    s.connect((ip, int(port)))
    t3 = time.time()                            # finding time after connecting           #connecting to server
    i = 0
    while i < count:                            #count 1000     
        i = i+1
        s.send(bytearray(testdata,"utf-8"))     # test data is send to the server in byte array
    s.shutdown(1)
    t4 = time.time()                             #finding time after sending data
    data = s.recv(BUFSIZE)                      
    t5 = time.time()                            # finding time after reciving
    print (data.decode())                       
    print ('ping:', (t3-t2)+(t5-t4)/2)          #sorce to destation to source 
    print ('Time:', t4-t3)                       # total time take to send data
    print ('Bandwidth:', round((BUFSIZE*count*0.001) / (t4-t3), 3),)  #1 sec total data /time taken  bytes to kilo bytees ponit 3 place
    print ('Kb/sec.')
client()

