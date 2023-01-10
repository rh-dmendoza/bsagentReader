# bsagentReader

Script that looks for errors in the bsagent logs and separates them into files whose name is the BOPOS Suite transaction id.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

The things you need before installing the software.

* Python 3.x (On terminal)

### Installation

```
NOT SUPPORTED YET
```

## Usage

There are two scripts, one for local files and the other that brings them from the ftp.

**search.py**
```
# Clone this repository
$ git clone https://github.com/rh-dmendoza/bsagentReader.git

# Go into the repository
$ cd bsagentReader

# Execute script
$ python search.py

# Type the route of the folder with the logs
$ D:\logsqa\BSAGENT\missingtrx

# The execute log will tell you the file that is been validate and if it found and error
![imagen](https://user-images.githubusercontent.com/77275632/211556251-c4df52ad-e848-475e-8ecd-81131815a67b.png)

# At the end of the process, you'll know how many error were found
![imagen](https://user-images.githubusercontent.com/77275632/211556477-9c4c96c9-a2c6-411b-b042-fe80cdadaacd.png)

# This will create a folder call "transacciones" in which the found errors will stored
![imagen](https://user-images.githubusercontent.com/77275632/211556510-179b17e2-d1f1-4795-a0eb-afdba700d208.png)

```

## Deployment

NOT SUPPORTED YET

### Branches

* Main: Base functional code

## Additional Documentation and Acknowledgments


