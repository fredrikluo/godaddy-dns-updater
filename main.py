""" Update GoDaddy DNS records with current public IP address"""
from godaddypy import Client, Account
import typer
import public_ip as ip

app = typer.Typer()


def get_client(api_key: str, api_secret: str) -> Client:
    """Get a GoDaddy client object"""
    my_acct = Account(api_key=api_key, api_secret=api_secret)
    if not my_acct:
        print("Failed to get account")
        return None

    client = Client(my_acct)
    if not client:
        print("Failed to get client")
        return None

    return client


@app.command()
def update(api_key: str, api_secret: str, domains: str):
    """Update GoDaddy DNS records with current public IP address"""
    client = get_client(api_key, api_secret)
    if client is None:
        return

    for domain in domains.split(","):
        domain = domain.strip()
        record = client.get_records(domain, record_type="A")
        if (record is None) or (len(record) == 0):
            print(f"no record found for {domain}")
            continue

        current_ip = ip.get()
        if record[0].get("data") == current_ip:
            print(f"no update needed for {domain}, ip is {current_ip}")
            continue

        print(f"updating {domain} with {current_ip} ")
        if not client.update_ip(ip.get(), domains=[domain]):
            print("Failed to update IP")


@app.command()
def ls(api_key: str, api_secret: str):
    """List all domains"""
    client = get_client(api_key, api_secret)
    if client is None:
        return

    domains = client.get_domains()
    for domain in domains:
        print(domain)


if __name__ == "__main__":
    app()
