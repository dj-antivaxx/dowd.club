# dowd.club

our amazing web service for all the cool parties. currently available at www.dowd.club

i can show u how to deploy it to ur machine. first need docker [(source)](https://docs.docker.com/engine/install/ubuntu/): 

```
sudo apt-get update

sudo apt-get install \
    ca-certificates \
    curl \
    gnupg \
    lsb-release

sudo mkdir -p /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg

echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

sudo apt-get update

sudo apt-get install docker-ce docker-ce-cli containerd.io docker-compose-plugin
```

then clone this project (dowd.club) to ur machine and build the container:

```
docker build . -t dowd:1
```

do `docker images` to checko the image id and then:

```
docker run -dit -p 5000:5000 <urimageid>
```

the website will be running at port 5000

in case something goes wrong - `docker ps -a` shows stopped containers, and u can copy the logs to a local text file like `logs.txt` via `docker cp <urcontainerid>:/home/tmp/report logs.txt` (works even if the container is stopped). 

accessing the data from the database is a bit not-very-well-designed atm but for now u can do this: `docker cp <urcontainerid>:/home/artifacts/database.db database.db`, so `database.db` will appear at ur local directory. [here is](https://inloop.github.io/sqlite-viewer/) some online sqlite db viewer i found on the internet. 

feel free to reach out if u have any questions or inquries! “%s.%s@%s.%s” % ("dj", "antivaxx", “gmail”, “com”) or @dj_antivaxx on ig

yowza!
