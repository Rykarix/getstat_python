# Installation:

1. `pip install -e git+repo_link`
2. Rename `.env_tmp` to `.env` and update vars
3. [Optional] run `pip install -m update`
4. run `pip install -r requirements.txt`

# Usage:

1. initialise client with `client=GetStat(subdomain=subdomain, apikey=apikey, return_dataframe=True)`
2. call methods as needed

# TODO:
- ~~projects~~
- ~~sites~~
- ~~tags~~
- keywords
- bulk
- rankings
- serps
- subaccounts

# Methods:

Methods are categorised by endpoint path heirarchy. You can see each endpoint here: `https://help.getstat.com/knowledgebase/requests-and-responses/` and I've included a python file that puts all endpoints + their params into a dictionary for easy reference:

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

