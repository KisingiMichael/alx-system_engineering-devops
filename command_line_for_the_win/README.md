Command line for the win

SFTP STEPS
1. Navigate to the local directory where the screenshoots are saved through command line
root@conscious-virtual-machine:/home/conscious/Pictures/Screenshots#
2. In the Command line enter sftp command the enter
root@conscious-virtual-machine:/home/conscious/Pictures/Screenshots#sftp
3. Then connect to the remote server using the username, server name and password
sftp>d4cc92bb759b@d4cc92bb759b.b5d6cecd.alx-cod.online
4. Navigate to the remote directory where you want to move the files
sftp>cd alx-system_engineering-devops/command_line_for_the_win
5. Move the files from local environment to remote server using 'put' command
sftp>put 0-first_9_tasks.jpg
sftp>put 0-first_9_tasks.png
sftp>put 1-next_9_tasks.jpg
sftp>put 1-next_9_tasks.png
sftp>put 2-next_9_tasks.jpg
sftp>put 2-next_9_tasks.png
6. Exit sftp
sftp>exit
