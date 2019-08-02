import elasticsearch
import curator

# Number of days for which you wish to keep the logs.
DAYS = 14

client = elasticsearch.Elasticsearch()

# Add/Remove as per requirements:
index = {"fb": "filebeat-", "mb": "metricbeat-", "ct": "cloudtrail-"}

for key in index.keys():
    try:
        list_indices = curator.IndexList(client)
        list_indices.filter_by_regex(kind='prefix', value=index[key])
        list_indices.filter_by_age(source='name', direction='older', timestring='%Y.%m.%d', unit='days', unit_count=DAYS)
        delete_indices = curator.DeleteIndices(list_indices)
        delete_indices.do_action()
    except Exception as e:
        print("Exception while trying to delete old indices (" + index[key] + "*):\n" + str(e))
