FROM base:1.0

ADD start.sh /home/rods/start.sh 
RUN chmod +x /home/rods/start.sh 
USER rods
ENTRYPOINT /home/rods/start.sh && bash
