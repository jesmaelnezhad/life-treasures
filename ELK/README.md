## Deploying ELK stack to collect docker container logs

Note: the material in this repository is based on [this blog post](https://towardsdatascience.com/running-securing-and-deploying-elastic-stack-on-docker-f1a8ebf1dc5b).

### Pre-requisites
1. Linux and its `sysctl` command
1. Docker
1. Docker Compose

### Setting the variables
All variables used in the installation are stored in the `.env` file under root. Examples are ELK version and Elasticsearch username and password. 

**Change Elasticsearch password in the `.env` file under root before setup.**

Also ...

**Change `ELASTICSEARCH_HOST`, `KIBANA_HOST`, `LOGSTASH_HOST` and `ELASTIC_DISCOVERY_SEEDS` to the server's public IP.**

### ELK Deployment

After cloning the repository, cd into the root directory and use the following commands to setup the keystore and generate the certificates.

```bash
docker-compose -f docker-compose.setup.yml run --rm keystore
docker-compose -f docker-compose.setup.yml run --rm certs
```

Next, increase the `max_map_count` system parameter on the machine (needed by Elasticsearch): open the /etc/sysctl.conf file and add the following line to the file:

```bash
vm.max_map_count=262144
```
Then, run the following command to refresh the system with the new parameter:

```bash
sudo sysctl -p
```

Finally, use docker compose to start Elasticsearch, Logstash, and Kibana:

```bash
docker-compose up -d
```

### Filebeat Deployment

Clone this repository on every machine whose logs must be sent to Logstash, and do the following steps:

1. Change the Filebeat config file and place Logstash IP in it. Also use a value for tags to identify the logs from this filebeat deployment. This config file is at `./beats/filebeat/config/filebeat.yml`.
	```yaml
	filebeat.inputs:
	  - type: log
	    enabled: true
	    paths:
	      - /hostfs/var/lib/docker/containers/*/*-json.log
	    tags: [“<Logs Identifier>”]
            json.keys_under_root: true
            json.add_error_key: true
	output.logstash:
	  hosts: ["<Logstash IP Address>:5044"]
	```
1. Run the following commands to deploy Filebeat:
	```bash
	cd beats
	docker-compose up -d
	```
