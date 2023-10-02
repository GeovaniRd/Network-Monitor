import speedtest
import datetime
import time

def calculate_jitter(st):
    pings = [st.get_best_server()['latency'] for _ in range(5)]
    jitter = max(pings) - min(pings)
    return jitter

def get_network_details():
    st = speedtest.Speedtest()

    user_name = input("Enter your full name: ")
    # Only letters validation
    while not user_name.replace(' ', '').isalpha():
        print("Please enter a valid name containing only letters.")
        user_name = input("Enter your full name: ")

    download_speed = st.download() / 1_000_000  # Convert to mbps
    upload_speed = st.upload() / 1_000_000
    ping = st.results.ping
    jitter = calculate_jitter(st)
    ip_address = st.results.client['ip']

    # Return the results as a dictionary
    return {
        "Date/Time": datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        "Logged By": user_name,
        "Speed Test Method": "Script Running",
        "IP Address": ip_address,
        "Ping(ms)": ping,
        "Jitter(ms)": jitter,
        "Download(mbps)": download_speed,
        "Upload(mbps)": upload_speed
    }

def main():
    results = get_network_details()

    # Ask for notes
    notes = input("Do you want to add any notes to this test? (y/n) ")
    if notes.lower() == 'y':
        results["Notes"] = input("Enter your notes: ")
    else:
        results["Notes"] = None

    # Save results to a text file
    with open("speedtest_results.txt", "a") as f:
        for key, value in results.items():
            f.write(f"{key}: {value}\n")
        f.write("\n")

    # Ask user if they want to see the results in terminal
    display = input("Do you want to see the info in the terminal? (y/n) ")
    if display.lower() == 'y':
        for key, value in results.items():
            print(f"{key}: {value}")

    # Ask user if they want to run the script indefinitely
    loop = input("Do you want to keep running the script on your computer indefinitely? (y/n) ")
    if loop.lower() == 'y':
        print("The script is running. Please minimize this window. If you want to stop the script, just close the terminal or type 'stop'.")
        try:
            while True:
                command = input()  # Wait for user input
                if command.lower() == 'stop':
                    print("Stopping the script.")
                    break
                
                results = get_network_details()
                with open("speedtest_results.txt", "a") as f:
                    for key, value in results.items():
                        f.write(f"{key}: {value}\n")
                    f.write("\n")
                
                time.sleep(1800)  # Sleep for 30 minutes
        except KeyboardInterrupt:
            print("\nStopping the script.")

if __name__ == "__main__":
    main()