#!/bin/bash
HOST='yourdomain.com'

USER='user'
PASSWD='password'

ftp -n $HOST << EOT
prompt
binary
user $USER $PASSWD
lcd output
mput *
bye
EOT