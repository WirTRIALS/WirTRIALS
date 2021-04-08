# WirTRIALS

:fast_forward: *Fast-Forwarding your Ideas into Reality*

![Imgur Image](https://i.imgur.com/bHaZtsg.jpg)

 
## Product

### Researchee  

Our product ***Researchee*** is here. We focus on Linked Data and research information. We provide a script to generate RDF Graph of professors and researchers of TU Chemnitz.

# Requirements

Python 

## Configuration

You need a [VPN service](https://www.tu-chemnitz.de/urz/network/access/vpn.html.en) to run the script because we are using [LDAP](https://www.tu-chemnitz.de/urz/idm/services/ldap.html) service of TU Chemnitz to fetch the names of the staff members.

## Setup via pip

To run this project locally, clone this repository. Go to the ***researchee*** directory and install the required dependencies first using pip which is the package installer for python.
```
$ pip install package-name
```
Then run the following command to generate the RDF graph of faculty members.
```
$ python RDF.py
```
We had to put a timeout in multiple scripts to avoid being blocked by multiple servers(LDAP, ResearchGate...). So, please have patience. Also we have more than 2000 professors and researchers along with their expertise data, so the script will take time to generate the RDF graph.

If you don't have the time, open **database.xml**  from the researchee directory to see the type of data this script will generate.

## Website

Check out our website and play around with some cool features and visualize the data. Go to the ***webapp*** directory and check the ***README. md*** file on instructions to setup the webapp locally.

Link to the Website: [WirTRIALS](https://www.wirtrials.com/)


## Social Networks

[Facebook](https://www.facebook.com/Wirtrials2020-111172150801612)

[Instagram](https://www.instagram.com/wirtrials2020/)

[LinkedIn](https://www.linkedin.com/company/wirtrials)

## Acknowledgement

- Supervisors from TU Chemnitz for providing valuable feedback and suggestions.

- Friends who helped in testing the website.

- All people whose boilerplate code we reused.

- Stackoverflow :wink:

It wouldn't be possible without your support. Thank You!

## Disclaimer

This website does not belong to a real company. It is a Planspiel (Startup experience) Web Engineering project.