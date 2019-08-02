<a href="https://work.amit.cloud"><img src="https://s3-ap-south-1.amazonaws.com/amitcloud/work.amit.cloud/wp-content/uploads/2019/04/19101016/logo.svg?sanitize=true" title="amit.cloud" alt="Amit Sharma" height="50"></a>

Checkout my profile and other projects at [amit.cloud](http://work.amit.cloud)

# ELK-Delete-Old-Logs
Script to delete logs older then set number of days (File beat, metric beat, cloudtrail).

### Usage with AWS CloudWatch Rules:
1. Copy the script to the ELK master server.
2. Install the Extra Packages if needed.
    >pip install elasticsearch
    >
    >pip install curator
3. Update the days (Default set to 14 days) in the script.
4. Run the script as 
     >python clean_elk.py
### INDEX Considered for Cleanup
Following three indices are considered for cleanup:
- Filebeat
- Metricbeat
- Cloudtrail
You could append your custom indices or remove the once not required by updating line #10 in code:  
> index = {"fb": "filebeat-", "mb": "metricbeat-", "ct": "cloudtrail-"}

### Use Case:
This script would delete old logs from ELK master/data nodes and ensure that old logs does not occupy all the space in nodes.

### Other Details
- Python Version = 3.7.2
- elasticsearch (Python module) = 7, 0, 2
- curator (Python module) = 5.5.4