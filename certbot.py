import json
import subprocess
import sys


def run():
    """Runs certbot based on configuration defined in certbot-config.json.
    Is called by nginx_listener.py once nginx starts.
    """

    config_file = open("certbot-config.json", "r")
    config = json.loads(config_file.read())
    config_file.close()
    domains = config["domains"]
    domain_args = [component for domain in domains
                   for component in ("-d", domain)]
    extra_args = ["--non-interactive", "--nginx", "--expand"]

    if "account_id" in config and "email" not in config:
        extra_args.append("--account")
        extra_args.append(config["account_id"])
    elif "email" in config and "account_id" not in config:
        extra_args.append("--email")
        extra_args.append(config["email"])
        extra_args.append("--agree-tos")
    else:
        raise ValueError("Config must contain either account_id or email,"
                         "but not both")
    # Must .wait() after running this. Otherwise, the process will not run.
    subprocess.Popen(["certbot"] + extra_args + domain_args,
                     stdout=sys.stderr).wait()
