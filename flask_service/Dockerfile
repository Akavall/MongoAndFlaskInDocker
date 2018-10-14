FROM ubuntu 
            # Choses base image
            # I guess our docker is using ubuntu :)
            # alpine is populare too, because it is much smaller 

# RUN vs CMD
# RUN is triggered while we build the docker image
# CMD is triggered when we run the created docker image
# We can only have one CMD command 

RUN apt-get update
RUN apt-get install -y apt-utils
RUN apt-get install -y python python-dev python-distribute python-pip

RUN pip install flask
RUN pip install pymongo

#EXPOSE 5000

COPY service service
                   # copies files directories over from
                   # main machine to docker container

                   # vs ADD, COPY has less functionality, but more
                   # predictable; it remmended to use COPY unless
                   # ADD is needed
                   # https://stackoverflow.com/questions/24958140/what-is-the-difference-between-the-copy-and-add-commands-in-a-dockerfile

CMD python service/my_file.py
