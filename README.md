markdown
# API-BASEBALL MCP Server

## Overview
API-BASEBALL is a comprehensive tool designed for developers to access extensive data related to baseball leagues and cups. It provides real-time and historical data, including livescores, odds, statistics, standings, and more, covering over 60 leagues and cups worldwide.

## Features
- **Livescores & Standings**: Get real-time updates and standings for various baseball leagues and cups.
- **Odds & Bookmakers**: Access pre-match odds and bookmaker information.
- **Statistics & Historical Data**: Delve into detailed statistics and historical data for teams and games.
- **Countries & Seasons**: Explore data across different countries and seasons.

## Usage
The API-BASEBALL MCP server organizes its functionality into several tool groups, each providing specific endpoints to fetch data:

### Timezone
- **timezone**: Retrieve timezone information.

### Teams
- **teams statistics**: Access comprehensive statistics for teams.
- **teams**: Fetch data about specific teams.

### Countries
- **countries**: Get information about countries participating in baseball leagues.

### Games
- **games**: Obtain detailed information about baseball games.
- **head to head**: Analyze head-to-head statistics between teams.

### Leagues
- **leagues**: Discover various baseball leagues and related data.

### Seasons
- **seasons**: Access information about different baseball seasons.

### Standings
- **stages**: Retrieve information about various stages in the leagues.
- **groups**: Get data on different groups within leagues.
- **standings**: Check the current standings in the leagues.

### Search
- **search bets**: Search for betting information.
- **search bookmakers**: Find specific bookmakers.
- **search countries**: Locate country-specific data.
- **search leagues**: Find leagues based on search queries.
- **search teams**: Search for teams using specific criteria.

## Architecture
The API-BASEBALL MCP server is built to ensure high availability and low latency, providing a seamless experience for users accessing baseball data.

## Authentication
Access to the API requires an API key, which should be included in all server requests. Ensure that your application is configured correctly to use the provided API key in the request header.

## Requests Headers & CORS
The server is configured to accept only **GET** requests. Ensure that your requests adhere to the allowed headers:
- `x-rapidapi-host`
- `x-rapidapi-key`

### Note
Adding non-standard headers or making non-GET requests will result in errors. Make sure to configure your application correctly to avoid such issues.

## Conclusion
API-BASEBALL is a robust solution for developers looking to integrate baseball data into their applications. With its wide range of tools and data coverage, it offers a powerful resource for developing sports-related apps and services.