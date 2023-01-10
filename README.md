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

# At the end of the process, you'll know how many error were found

# This will create a folder call "transacciones" in which the found errors will stored

```

**searchFromFtp.py**
```
# Clone this repository
$ git clone https://github.com/rh-dmendoza/bsagentReader.git

# Go into the repository
$ cd bsagentReader

# You need connection to the controller's ftp, through vpn most likely
# [The base connection is to EPA QA, if you want to change it, edit the .py file, lines 33 and 34 ]

# Execute script
$ python searchFromFtp.py

# At the start, the script will create a folder call "archivos_ftp", to store the log files

# The execute log will tell you the file that is been validate and if it found and error

# At the end of the process, you'll know how many error were found

# This will create a folder call "transacciones" in which the found errors will stored

```

## Deployment

NOT SUPPORTED YET

### Branches

* Main: Base functional code

## Additional Documentation and Acknowledgments

* TODO: config file for ftp script
* TODO: default folder for local script
