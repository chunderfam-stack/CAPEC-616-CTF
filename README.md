# CAPEC 616 CTF
This is a simple ctf designed to help you understand CAPEC 616, Establish Rogue Location. To do this ctf, go through the setup and then post the flag at:

## Setup

using the terminal, cd into a folder that you are willing to clone into this page. Then run the following command:
``` bash
git clone https://github.com/chunderfam-stack/CAPEC-616-CTF
cd ./CAPEC-616-CTF/ctfFiles
```

Then make sure that docker desktop is open. Once it is, run the following command:
``` bash
docker build -t rogue-location-ctf .
docker run -d --name ctf_container rogue-location-ctf
docker exec -it ctf_container bash
```

if you need to restart the container for any reason, run the following command:
``` bash
docker build -t rogue-location-ctf .
docker stop ctf_container
docker rm ctf_container
docker run -d --name ctf_container rogue-location-ctf
docker exec -it ctf_container bash
```

## Instructions

Your goal in this ctf is to find and stop the rogue software running on the linux distro you are given.

### Hints
<details>
<summary>Hint 1</summary>
The walkthrough has several possible locations for a rogue script to be located.
</details>

<details>
<summary>Hint 2</summary>
What is a crontab?
</details>

## Submission
