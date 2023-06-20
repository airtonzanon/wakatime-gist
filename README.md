### Publishes amount of time spent in a language on Gist from Wakatime

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/airtonzanon/wakatime-gist)

[Deploy to DigitalOcean Serverless Functions](https://github.com/airtonzanon/wakatime-gist/tree/digitalocean)

If you would like to understand more about this project, [here](https://airton.dev/article/exibindo-no-github-metricas-de-tempo-gasto-em-linguagens-usando-wakatime/) is a good tutorial (in pt-br, but you can use google translator to understand).
Se você quer entender mais sobre esse projeto, fiz um tutorial para você deployar no Heroku seu próprio script.
[https://airton.dev/article/exibindo-no-github-metricas-de-tempo-gasto-em-linguagens-usando-wakatime/](https://airton.dev/article/exibindo-no-github-metricas-de-tempo-gasto-em-linguagens-usando-wakatime/)


### Necessary env var

* `WAKATIME_API_KEY` = https://wakatime.com/settings/api-key
* `WAKATIME_USER_ID` = https://wakatime.com/me (You will find this in the URL, copy with the @ in the beginning) 
* `GITHUB_TOKEN` = https://github.com/settings/tokens
* `GIST_ID` = The hash on the gist url, like this one: `https://gist.github.com/airtonzanon/3020f8e67064870431740213ba3eb611` => `3020f8e67064870431740213ba3eb611`
