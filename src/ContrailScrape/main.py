import sys
import ContrailScrape

version = "0.1.4"

def get_version():
    print("CONTRAIL-INTROSPECT-SCRAPE\nVERSION: {}".format(version))
    sys.exit()

def fetch_all_introspects(introspect_args, debug):
    if introspect_args:
        introspect = ContrailScrape.IntrospectClass(introspect_args, 50, debug)
        return introspect.fetch_all_introspects()

def fetch_analytics_api(api_args, debug):
    if api_args:
        analytics_api = ContrailScrape.AnalyticsApiClass(debug)
        return analytics_api.fetch_all_analytics_apis(api_args)

def main():
    config_parser = ContrailScrape.ConfigParser()
    all_args = config_parser()
    base = ContrailScrape.BaseClass()
    if config_parser.version:
        get_version()
    try:
        introspect_args = list(filter(lambda arg: arg.get('type') == "introspect", all_args))
        fetch_all_introspects(introspect_args, config_parser.debug)
        analytics_api_args = list(filter(lambda arg: arg.get('type') == "analytics-api", all_args))
        fetch_analytics_api(analytics_api_args, config_parser.debug)
        base.archive_all_files()
    except KeyboardInterrupt:
        print("Interrupted\n")
        print("Performing Cleanup...")
        base.delete_tmp_files()
        sys.exit(0)

if __name__ == "__main__":
    main()