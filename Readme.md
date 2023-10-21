# GoDaddy IP Updater

**GoDaddy IP Updater** is a Python script that facilitates the updating of DNS records for domains registered on GoDaddy. The utility allows users to set their domain's "A" record to reflect their current public IP address. This can be particularly useful if you're hosting a server on a dynamic IP address and want to use a domain name to point to it. 

## TL.DR

To point a DNS record to a device with a changing IP address, execute the following command on the desired device:

```bash
docker run --name www.fredrikai.com -d --restart unless-stopped --env GD_NAME=YOUR_GODADDY_NAME \
    --env GD_DOMAINS=YOUR_GODADDY_DOMAINS \
    --env GD_KEY=YOUR_GODADDY_KEY \
    --env GD_SECRET=YOUR_GODADDY_SECRET \
    fredrikluo/godaddyupdater:1.0
```

for example

      ``` bash
    docker run --name www.fredrikai.com -d --restart unless-stopped --env GD_NAME=www \
        --env GD_DOMAINS=fredrikai.com,bpservice.co \
        --env GD_KEY=YOUR_GODADDY_KEY\
        --env GD_SECRET=YOUR_GODADDY_SECRET\
        fredrikluo/godaddyupdater:1.0
  ```

Create your key and secret at GoDaddy Developer Portal.

## Features

1. **Auto-fetch current public IP address:** The script uses the `public_ip` module to retrieve the current public IP of the machine.
2. **List all domains:** The script can fetch and list all domains associated with the provided GoDaddy API credentials.
3. **Update specific domain or multiple domains:** Specify one or multiple domains (comma-separated) to update their DNS "A" records to the current public IP. The script will check if an update is needed and make the necessary changes.

## How to Use

1. **Install Dependencies:** Before using the script, make sure to install the necessary Python modules:

    ```bash
    pip install -r requirements.txt
    ```

2. **Command-line Interface:** The script uses the `typer` module for a CLI experience. The following commands are available:

   - **Updating the DNS Record:**

        ```bash
        python main.py update --api_key YOUR_API_KEY --api_secret YOUR_API_SECRET --domains YOUR_DOMAIN1,YOUR_DOMAIN2
        ```

        Replace `YOUR_API_KEY` with your GoDaddy API key, `YOUR_API_SECRET` with your GoDaddy API secret, and `YOUR_DOMAIN1,YOUR_DOMAIN2` with a comma-separated list of your domains.

   - **List All Domains:**

        ```bash
        python main.py ls --api_key YOUR_API_KEY --api_secret YOUR_API_SECRET
        ```

        This command lists all domains associated with the provided GoDaddy API credentials.

## Important Notes

- Make sure your GoDaddy API key has the required permissions to read and update DNS records.
- The script currently supports "A" record updates only.
- Always double-check the DNS records via the GoDaddy dashboard after making changes using the script to ensure correctness.

## Run this as an auto updater to point a DNS record to a device with a changing IP address

1. Build the docker image for this, run:

  ``` bash
  docker build . -t yourusername/godaddy:latest
  ```

2. On the target machine, run the docker image or you can also use a prebuilt docker image:

  ``` bash
    docker run --name www.fredrikai.com -d --restart unless-stopped --env GD_NAME=YOUR_GODADDY_NAME \
        --env GD_DOMAINS=YOUR_GODADDY_DOMAINS \
        --env GD_KEY=YOUR_GODADDY_KEY\
        --env GD_SECRET=YOUR_GODADDY_SECRET \
        fredrikluo/godaddyupdater:1.0
  ```

## Contribution

Feel free to fork, raise issues, or submit pull requests. Your contributions are always welcome!

---

**Disclaimer**: This tool is not affiliated with or endorsed by GoDaddy. Use it at your own risk and always ensure you have backups of your DNS settings.
