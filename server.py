import requests
from datetime import datetime
from typing import Union, Literal, List
from mcp.server import FastMCP
from pydantic import Field
from typing import Annotated
from mcp.server.fastmcp import FastMCP
from fastmcp import FastMCP, Context
import os
from dotenv import load_dotenv
load_dotenv()
rapid_api_key = os.getenv("RAPID_API_KEY")

__rapidapi_url__ = 'https://rapidapi.com/api-sports/api/api-baseball'

mcp = FastMCP('api-baseball')

@mcp.tool()
def timezone() -> dict: 
    '''timezone'''
    url = 'https://api-baseball.p.rapidapi.com/timezone'
    headers = {'x-rapidapi-host': 'api-baseball.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def teams_statistics(date: Annotated[Union[str, None], Field(description='')] = None,
                     league: Annotated[Union[str, None], Field(description='')] = None,
                     season: Annotated[Union[str, None], Field(description='')] = None,
                     team: Annotated[Union[str, None], Field(description='')] = None) -> dict: 
    '''teams statistics'''
    url = 'https://api-baseball.p.rapidapi.com/teams/statistics'
    headers = {'x-rapidapi-host': 'api-baseball.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'date': date,
        'league': league,
        'season': season,
        'team': team,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def teams(league: Annotated[Union[int, float, None], Field(description='Default: 1')] = None,
          country: Annotated[Union[str, None], Field(description='')] = None,
          search: Annotated[Union[str, None], Field(description='')] = None,
          name: Annotated[Union[str, None], Field(description='')] = None,
          id: Annotated[Union[int, float, None], Field(description='Default: 0')] = None,
          season: Annotated[Union[int, float, None], Field(description='Default: 2020')] = None,
          country_id: Annotated[Union[int, float, None], Field(description='Default: 0')] = None) -> dict: 
    '''teams'''
    url = 'https://api-baseball.p.rapidapi.com/teams'
    headers = {'x-rapidapi-host': 'api-baseball.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'league': league,
        'country': country,
        'search': search,
        'name': name,
        'id': id,
        'season': season,
        'country_id': country_id,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def countries(name: Annotated[Union[str, None], Field(description='')] = None,
              code: Annotated[Union[str, None], Field(description='')] = None,
              search: Annotated[Union[str, None], Field(description='')] = None,
              id: Annotated[Union[int, float, None], Field(description='Default: 0')] = None) -> dict: 
    '''countries'''
    url = 'https://api-baseball.p.rapidapi.com/countries'
    headers = {'x-rapidapi-host': 'api-baseball.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'name': name,
        'code': code,
        'search': search,
        'id': id,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def games(league: Annotated[Union[int, float, None], Field(description='Default: 0')] = None,
          season: Annotated[Union[int, float, None], Field(description='Default: 0')] = None,
          team: Annotated[Union[int, float, None], Field(description='Default: 0')] = None,
          id: Annotated[Union[int, float, None], Field(description='Default: 1')] = None,
          date: Annotated[Union[str, datetime, None], Field(description='Date (yyyy-mm-dd)')] = None,
          timezone: Annotated[Union[str, None], Field(description='')] = None) -> dict: 
    '''games'''
    url = 'https://api-baseball.p.rapidapi.com/games'
    headers = {'x-rapidapi-host': 'api-baseball.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'league': league,
        'season': season,
        'team': team,
        'id': id,
        'date': date,
        'timezone': timezone,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def head_to_head(h2h: Annotated[str, Field(description='')],
                 season: Annotated[Union[int, float, None], Field(description='Default: 0')] = None,
                 timezone: Annotated[Union[str, None], Field(description='')] = None,
                 league: Annotated[Union[int, float, None], Field(description='Default: 0')] = None,
                 date: Annotated[Union[str, datetime, None], Field(description='Date (yyyy-mm-dd)')] = None) -> dict: 
    '''games head to head'''
    url = 'https://api-baseball.p.rapidapi.com/games/h2h'
    headers = {'x-rapidapi-host': 'api-baseball.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'h2h': h2h,
        'season': season,
        'timezone': timezone,
        'league': league,
        'date': date,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def leagues(country_id: Annotated[Union[int, float, None], Field(description='Default: 0')] = None,
            search: Annotated[Union[str, None], Field(description='')] = None,
            type: Annotated[Union[str, None], Field(description='')] = None,
            country: Annotated[Union[str, None], Field(description='')] = None,
            season: Annotated[Union[int, float, None], Field(description='Default: 0')] = None,
            id: Annotated[Union[int, float, None], Field(description='Default: 0')] = None,
            name: Annotated[Union[str, None], Field(description='')] = None) -> dict: 
    '''leagues'''
    url = 'https://api-baseball.p.rapidapi.com/leagues'
    headers = {'x-rapidapi-host': 'api-baseball.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'country_id': country_id,
        'search': search,
        'type': type,
        'country': country,
        'season': season,
        'id': id,
        'name': name,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def seasons() -> dict: 
    '''seasons'''
    url = 'https://api-baseball.p.rapidapi.com/seasons'
    headers = {'x-rapidapi-host': 'api-baseball.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def stages(season: Annotated[Union[int, float], Field(description='Default: 2020')],
           league: Annotated[Union[int, float], Field(description='Default: 1')]) -> dict: 
    '''stages'''
    url = 'https://api-baseball.p.rapidapi.com/standings/stages'
    headers = {'x-rapidapi-host': 'api-baseball.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'season': season,
        'league': league,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def groups(season: Annotated[Union[int, float], Field(description='Default: 2020')],
           league: Annotated[Union[int, float], Field(description='Default: 1')]) -> dict: 
    '''groups'''
    url = 'https://api-baseball.p.rapidapi.com/standings/groups'
    headers = {'x-rapidapi-host': 'api-baseball.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'season': season,
        'league': league,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def standings(group: Annotated[Union[str, None], Field(description='')] = None,
              league: Annotated[Union[int, float, None], Field(description='Default: 1')] = None,
              team: Annotated[Union[int, float, None], Field(description='Default: 0')] = None,
              stage: Annotated[Union[str, None], Field(description='')] = None,
              season: Annotated[Union[int, float, None], Field(description='Default: 2020')] = None) -> dict: 
    '''standings'''
    url = 'https://api-baseball.p.rapidapi.com/standings'
    headers = {'x-rapidapi-host': 'api-baseball.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'group': group,
        'league': league,
        'team': team,
        'stage': stage,
        'season': season,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def search_bets(search: Annotated[str, Field(description='')]) -> dict: 
    '''search bets'''
    url = 'https://api-baseball.p.rapidapi.com/odds/bets'
    headers = {'x-rapidapi-host': 'api-baseball.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'search': search,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def search_bookmakers(search: Annotated[str, Field(description='')]) -> dict: 
    '''search bookmakers'''
    url = 'https://api-baseball.p.rapidapi.com/odds/bookmakers'
    headers = {'x-rapidapi-host': 'api-baseball.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'search': search,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def search_countries(search: Annotated[str, Field(description='')]) -> dict: 
    '''search countries'''
    url = 'https://api-baseball.p.rapidapi.com/countries'
    headers = {'x-rapidapi-host': 'api-baseball.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'search': search,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def search_leagues(search: Annotated[str, Field(description='')]) -> dict: 
    '''search leagues'''
    url = 'https://api-baseball.p.rapidapi.com/leagues'
    headers = {'x-rapidapi-host': 'api-baseball.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'search': search,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def search_teams(search: Annotated[str, Field(description='')]) -> dict: 
    '''search teams'''
    url = 'https://api-baseball.p.rapidapi.com/teams'
    headers = {'x-rapidapi-host': 'api-baseball.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'search': search,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()



if __name__ == '__main__':
    import sys
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 9997
    mcp.run(transport="stdio")
