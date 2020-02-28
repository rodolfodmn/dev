FROM base:1.1

ADD start.sh /home/rods/start.sh 
RUN chmod +x /home/rods/start.sh 
USER rods
ENTRYPOINT /home/rods/start.sh && /bin/bash
