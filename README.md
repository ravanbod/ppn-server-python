# Private Push Notification (Server side)
##What is PPN?
Private Push Notification (PPN) is a project that you can connect your client app to your server app and send messages as push notification to your client app from server app.
For using of this project you have to run Server App on your server and import Client Library in your client app.
**At this moment just Android Library (Java) is now written for the client section**.
 you can start server app on any OS which has python3.
##Why i started this project?
This is a fun project for me, i started this project to learning socket programming in java and python and now i want to share it with you.
##Installing the server app
###Installing on Linux & MacOS
####Cloning files 
`sudo mkdir ~/Development`

`cd ~/Development`

`git clone https://github.com/behradrvb/ppn-server-python.git`
####Open firewall port
you have to open project ports on your firewall. find this port in `config/config.py` file.
####Run project
`cd ~/Development/ppn-server-python`

`python3 run.py`
###Installing on Windows
####Cloning files 
You can get file of this project as zip from https://github.com/behradrvb/ppn-server-python/archive/master.zip or clone them with `git clone https://github.com/behradrvb/ppn-server-python.git`.
####Open firewall port
you have to open project ports on your firewall. find this port in `config/config.py` file.
####Run project
go to project folder `......./ppn-server-python`.

open cmd in this directory and run this command. `python3 run.py`

###After running
if program works good you should see this output.

`Server was launched successfully.(Thu Oct 17 15:01:48 2019)
address:192.168.1.103:21000
Waiting...`

if you see that address is 127.0.0.1 instead of 192.168.x.x or your server ip, it has problem in running socket. connect your pc to a router and run project again..
##Send push notification to clients.
Any clients have to send `session_id` after connecting to server app. in Android Library you send this when you are initializing connection (Read more in client project page).
###Send push notification with an API
Not ready yet...
###Send push notification directly from terminal/cmd
In cmd/terminal which you started run.py, type `send` to send push notification to a client or type `send2all` to send push notification to all clients.
##Client Libraries
After running server app, you need client library to connect.

Android: https://github.com/behradrvb/ppn-client-android

