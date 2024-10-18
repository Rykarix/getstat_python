# Introduction

`getstat_python` is a *work in progress* python client for the [GetStat API](https://help.getstat.com/knowledgebase/requests-and-responses/).


# Installation:

1. `pip install -e git+https://github.com/Rykarix/getstat_python.git#egg=getstat`
1. Rename `.env_tmp` to `.env` and **update vars** as required


# Usage:

Initialise the client & call the endpoints as methods:

## Example 1: 
Output a json response from the `projects/list` endpoint:
```py
from getstat import GetStat
import json

client = GetStat(subdomain=subdomain, apikey=apikey)
endpoint = client.projects.list()
project_list_json = endpoint.execute()

print(json.dumps(project_list_json, indent=2))
```

Output:
```json
{
   "Response":{
      "resultsreturned":"11",
      "responsecode":"200",
      "Result":[
         {
            "Id":"1",
            "Name":"celebrity",
            "TotalSites":"3",
            "CreatedAt":"2009-12-18",
            "UpdatedAt":"2009-12-18",
            "RequestUrl":"/sites/list?project_id=1&format=json"
         },
         ...
      ]
   }
}
```

## Example 2:
Output a pandas dataframe from the sites/list endpoint:
```py
from getstat import GetStat

client = GetStat(subdomain=subdomain, apikey=apikey, dataframe=True)
endpoint = client.sites.list(project_id=project_id)
site_list_dataframe = endpoint.execute()
```

Output:

| Id  | FolderId | FolderName | Title               | Url                  | Synced | TotalKeywords | CreatedAt  | UpdatedAt  | RequestUrl                                     |
| --- | -------- | ---------- | ------------------ | -------------------- | ------ | ------------- | ---------- | ---------- | ---------------------------------------------- |
| 1   | 22       | Blog       | tourismvancouver.com | tourismvancouver.com | NaN    | 63            | 2011-01-25 | 2011-01-25 | /keywords/list?site_id=1&format=json           |
| 2   | NaN      | NaN        | perezhilton.com    | perezhilton.com      | 1      | 63            | 2011-01-25 | 2011-01-25 | /keywords/list?site_id=2&format=json           |

## Other notes
Required inputs should be self explanatory via peaking at methods or you can review the documentation or review the [Methods](#methods) section below:


# TODO:
## Add API endpoints to client
- ~~projects~~
- ~~sites~~
- ~~tags~~
- ~~keywords~~
- bulk
- ~~rankings~~
- ~~serps~~
- subaccounts


## Utils
- add tests
- add utils for json initialised client
## refactor & improve codebase
- revisit pydantic models


# Methods:

Methods are categorised by endpoint path heirarchy. You can see each endpoint here: `https://help.getstat.com/knowledgebase/requests-and-responses/` and I've included a python file fetches all teh endpoints from this url & organises them & their params into a dictionary for easy reference:

```json
{
  "bulk/delete": "id={bulkjobId}",
  "bulk/list": "",
  "bulk/ranks": "date={YYYY-MM-DD}[&site_id={siteIds}][&rank_type={ranktype}][&engines={engines}][&currently_tracked_only={boolean}][&crawled_keywords_only={boolean}]",
  "bulk/site_ranking_distributions": "date={YYYY-MM-DD}",
  "bulk/status": "id={bulkjobId}",
  "bulk/tag_ranking_distributions": "date={YYYY-MM-DD}",
  "keywords/create": "site_id={siteId}&market={market}&keyword={keywords}[&location={location}][&device={device}][&tag={tags}]",
  "keywords/delete": "id={keywordId}",
  "keywords/list": "site_id={siteId}[&start={start}][&results={results}]",
  "projects/create": "name={projectId}",
  "projects/delete": "id={projectId}",
  "projects/list": "",
  "projects/update": "id={projectId}&name={name}",
  "rankings/list": "keyword_id={keywordId}[&from_date={YYYY-MM-DD}][&to_date={YYYY-MM-DD}][&start={start}][&results={results}]",
  "serps/show": "keyword_id={keywordId}&engine={engine}&date={YYYY-MM-DD}",
  "sites/all": "?start={start}][&results={results}]",
  "sites/create": "project_id={projectId}&url={url}[&drop_www_prefix={boolean}][&drop_directories={boolean}]",
  "sites/delete": "id={siteId}",
  "sites/list": "project_id={projectId}",
  "sites/most_frequent_domains": "id={siteId}&engine={engine}",
  "sites/ranking_distributions": "id={siteId}&from_date={YYYY-MM-DD}&to_date={YYYY-MM-DD}",
  "sites/sov": "id={siteId}&from_date={YYYY-MM-DD}&to_date={YYYY-MM-DD}[&start={start}][&results={results}]",
  "sites/update": "id={siteId}[&url={url}][&title={title}][&drop_www_prefix={boolean}][&drop_directories={boolean}]",
  "subaccounts/list": "",
  "tags/list": "site_id={siteId}[&start={start}][&results={results}]",
  "tags/most_frequent_domains": "id={tagId}&engine={engine}",
  "tags/ranking_distributions": "id={tagId}&from_date={YYYY-MM-DD}&to_date={YYYY-MM-DD}",
  "tags/sov": "id={tagId}&from_date={YYYY-MM-DD}&to_date={YYYY-MM-DD}[&start={start}][&results={results}]"
}
```

