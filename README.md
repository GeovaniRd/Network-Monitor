# Network Information Script
Description:

This script allows users to obtain information about their network, such as IP address, download/upload speeds, ping, jitter, and more. Once executed, users can opt to continue running the script indefinitely, recording the network details at set intervals and saving them to a text file.

## Libraries & Packages Used:
* ***'speedtest-cli':*** Enables us to interface with the Speedtest CLI to fetch network metrics.
* ***'datetime':*** Used for fetching the current date and time.
* ***'time':*** Used for adding delays in script execution.

## Getting Started:
***1. Clone the Repository:***
```
git clone https://github.com/GeovaniRd/Network-Monitor.git
cd Network-Monitor
```

***2. Using Conda Environment:***
The project is based on a Conda environment to manage dependencies. The environment is located in the main folder and is named ***'.env'***.

***Activate the Environment:***

On Windows:
```
conda activate .\.env
```

On macOS and Linux:
```
conda activate ./.env
```

***3. Executing the Script:***

Once the environment is active, execute the script using:
```
python network_info.py
```

Follow the on-screen instructions to get your network details.
