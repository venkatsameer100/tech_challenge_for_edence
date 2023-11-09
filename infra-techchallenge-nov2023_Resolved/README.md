# Nov-2023 Infra Tech Challenge

The purpose of this tech challenge is to help us evaluate your ability to troubleshoot a broken web app deployment.

We're giving you a broken container composition and your goal will be to get it up and running again.

## Requirements

You will need functional installations of:

1. Docker Desktop: <https://www.docker.com/products/docker-desktop/> - **My MAC is an old version hence I had to follow other route to Install the docker desktop using home-brew**
3. Git: <https://git-scm.com/downloads> - **Installed** (2.42.2)
4. A modern web browser - **Updated** - Chrome (118.0.5)
5. A code editor - **Installed** - Pycharm free version without license 

## Notes

* Consult the [Dockerfile reference](https://docs.docker.com/engine/reference/builder/) for documentation of the proper syntax of the `Dockerfile` - **Read**

* Consult the [Compose file reference](https://docs.docker.com/compose/compose-file/compose-file-v3/) for documentation of the proper syntax of the file `docker-compose.yml` - **Read**

* Consult the [bottle.py docs](http://bottlepy.org/docs/dev/) for documentation about the very simple lightweight web framework we're using here. - **Read**

* Consult the [traefik docs](https://docs.traefik.io/) for documentation about the HTTP reverse proxy and load balancer we use in this project (traefik is amazing and powerful) - **Read**

## Steps

1. Clone the repo locally using a command like: **DONE**

		git clone https://github.com/edencehealth/infra-techchallenge-nov2023.git

2. Start the containers by using a command like: **DONE**

		docker compose up -d --build

3. Visit the containers in a browser: <http://127.0.0.1:8000/> : **DONE**

4. Explore the container composition and then identify and fix the following reported bugs:

	* **BUG #1**: "The static assets on the page aren't loading or something. The page looks wrong and is missing proper formatting." - **FIXED**

	* **BUG #2**: "The left column of the page should contain a version of the job description. Currently there is only placeholder text. Something isn't loading right." - **FIXED**

	* **BUG #3**: "The right column of the page should contain ten animated gifs of puppies! It is currently showing up empty." - **FIXED**

	* **BUG #4**: "Super embarrassing: we have a typo in our page heading. We're in November not Movember." - **FIXED**

5. Make sure your fixes work, commit them to your local git repo, THEN bundle the repo: **DONE**

		git bundle create send2eh.bundle --all

6. Email the `send2eh.bundle` file to your edenceHealth point of contact. **DONE**