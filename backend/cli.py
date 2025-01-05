
import argparse
from core import FESCore

def main():
    parser = argparse.ArgumentParser(description="FES Core CLI")
    parser.add_argument("--fetch-data", type=str, help="Fetch RODS-compatible data from the provided API URL")
    parser.add_argument("--alert-threat", nargs=2, type=str, metavar=("THREAT_LEVEL", "LOCATION"),
                        help="Alert authorities about a biothreat based on detected signals")
    args = parser.parse_args()

    core = FESCore()

    if args.fetch_data:
        try:
            data = core.fetch_rods_data(args.fetch_data)
            print("Data fetched successfully:", data)
        except Exception as e:
            print(f"Error fetching data: {str(e)}")

    if args.alert_threat:
        try:
            threat_level = int(args.alert_threat[0])
            location = args.alert_threat[1]
            core.alert_biothreat(threat_level, location)
        except ValueError:
            print("Invalid threat level. Please provide an integer.")
        except Exception as e:
            print(f"Error alerting threat: {str(e)}")

if __name__ == "__main__":
    main()
