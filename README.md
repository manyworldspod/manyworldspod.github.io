# Where Many Worlds Fit

This is the main website for the podcast, including all articles, scripts,
stories, and investigations. It uses the [Millennial](LeNPaul/Millennial)
theme for [Jekyll](https://jekyllrb.com/).

## Publishing articles

Articles that have gone through internal peer review can be published here
by adding a [markdown](https://www.markdownguide.org/basic-syntax/) file.
The file should be placed under `_posts` and follow the naming convention

```bash
_posts/<date>-<slug>.md
```

where `date` is the publish date in `YYYY-MM-DD` format and `slug` is the
article's shortname under which it will later be found. Often the slug is
simply the title of the article in all lowercase letters with spaces replaced
by dashes. For example, the first article published here can be found at

```bash
_posts/2022-03-09-restorative-justice-northeast-syria.md
```

After the new file is pushed to `origin/main`, it will automatically go to a
[deployment](https://github.com/manyworldspod/manyworldspod.github.io/deployments)
and, failing any issues, will be published online under

```bash
https://manyworldspod.github.io/<slug>
```

For example, the first article can be found at
`https://manyworldspod.github.io/restorative-justice-northeast-syria`.

## Publishing zines

After publication to the website, you can format your article as a PDF and
impose it on A4 paper for printing as a zine. To do this, remember your stub
and navigate to the `_zines` directory, then run

```bash
make <slug>
```

For example, to prepare the first article you can run

```bash
make restorative-justice-northeast-syria
```

See the [zine docs](_zines/README.md) in that directory for more information.

## Contributing code
