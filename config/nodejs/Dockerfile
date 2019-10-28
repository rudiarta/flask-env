FROM node:lts-alpine

#RUN npm install -g @vue/cli

# Copy the entrypoint file
RUN mkdir /htdocs
ADD infinite.sh /infinite.sh
RUN chmod +x /infinite.sh

# Start process
ENTRYPOINT ["/bin/sh","/infinite.sh"]
