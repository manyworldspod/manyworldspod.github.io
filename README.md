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
simply the title of the article in all lowercase letters, with spaces replaced
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
[`https://manyworldspod.github.io/restorative-justice-northeast-syria`](
https://manyworldspod.github.io/restorative-justice-northeast-syria).

## Publishing zines

After publication to the website, you can format your article as a PDF and
[impose](https://en.wikipedia.org/wiki/Imposition) it on A4 paper for printing
as a zine. To do this, remember your stub and navigate to the `_zines`
directory, then run

```bash
make <slug>
```

For example, to prepare the first article you can run

```bash
make restorative-justice-northeast-syria
```

See the [zine docs](_zines/README.md) in that directory for more information.

## Contributing code

**Note:** This section is written presuming you're familiar with the basics
of git. If you want to contribute code but haven't used git before or would
like a refresher, [this simple guide](https://rogerdudler.github.io/git-guide/)
might help. You can also [reach out](mailto:many.worlds.pod@protonmail.com)
any time for guidance, or check out the
[issue tickets](https://github.com/manyworldspod/manyworldspod.github.io/issues)
if you're looking for a place to start. Even if you've never coded before but
would like to learn, projects like this are a natural opportunity to do that.
Truly, compa, we welcome you and want your help!
:heart::yellow_heart::green_heart:

This repository uses
[github flow](https://docs.github.com/en/get-started/quickstart/github-flow)
to manage contributions. Our goal is to cultivate a collaborative environment
that is social first and only as technical as it needs to be. With that in
mind, issue tickets and pull requests can be thought of as fora for building
consensus. Issues can **propose, not impose** alternative language, technology,
features, and bug reports, and pull requests can **lead by obeying** to
mutually address the needs of organizers and journalists.

The proposed workflow would proceed like so:

1. For bug reports, post-publication edits, organizational notes, and feature
   requests, post an issue ticket and solicit feedback from the community of
   other contributors.
2. To address or otherwise take action on an issue ticket, clone the repository
   and create a new branch. This branch is your sandbox, within which you can
   implement all the changes you would like to propose.
3. From this branch, open a pull request to merge your changes into the `main`
   branch. Until it's ready for review you can start its title with `WIP:`
   (short for "work-in-progress") to mark it as a draft.
4. During the review you will have an opportunity to build consensus with
   other contributors. Please don't be concerned if they suggest changes --
   both code and writing samples often benefit from extra eyeballs, and this
   space is meant to be intentionally non-competitive. Things like comments and
   suggestions from your compas are a gift.
5. When consensus is reached the pull request is merged, whence your changes
   will automatically deploy to the live website. You can safely delete your
   local working branch after this happens.

***Where Many Worlds Fit*** is a living, active media project that thrives on
collaboration and is sustained by diversity. It is, by design, a world where
many worlds fit. Even this proposed workflow is subject to consensus. If you
have strong feelings about it, we hope you won't hesitate to speak up!
