# This repo contains code for http://aidevs.pl training.

In order to fully utilize provided code you need to be part of the course.

If you would like to know more here are authors of the course:
- Adam Gospodarczyk (@overment)
- Jakub Mrugalski (@unknow)
- Mateusz Chrobok (@MateuszChrobok)

You can use this code as a guidance how to connect and talk with OpenAI.

To launch tasks you need .env file with tokens
- AI_DEVS_SERVER
- AI_DEVS_USER_TOKEN
- OPENAI_API_KEY

It's possible to use LANGCHAIN_TRACING by specifying: 
- LANGCHAIN_TRACING_V2
- LANGCHAIN_ENDPOINT
- LANGCHAIN_API_KEY
- LANGCHAIN_PROJECT

Project uses python 3.11 & poetry to resolve dependencies.
It also uses:
- Black for formatting
- python-dotenv to load env files

I used samples from: https://github.com/Majkee/aidevs2

PS. Logger is a mess at the moment.