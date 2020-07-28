FROM ubuntu:latest
RUN echo Updating existing packages, installing and upgrading python and pip.
RUN apt-get update -y
RUN apt-get install -y python3-pip python-dev build-essential
RUN echo Copying Anagram Flask service into a service directory.
ADD ./ /AnagramSolverService
WORKDIR /AnagramSolverService
RUN echo Installing Python packages listed
Run python3 -m pip install flask
RUN python3 -m  pip install -r ./requirements.txt
RUN python3 -m  pip install --upgrade nltk
RUN python3 -m nltk.downloader words
RUN echo Starting python and starting the Flask service...
ENTRYPOINT ["python3"]
CMD ["dict_app.py"]