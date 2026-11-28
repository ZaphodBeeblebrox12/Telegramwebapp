# TradeThesis Telegram Mini App

A static, mobile-first Telegram Mini App for TradeThesis. The initial version is framework-free and hosted with GitHub Pages.

## Included

- Home, Challenges, Tools, Learn and About views
- Position-size calculator
- Risk/reward calculator
- Indicative margin calculator
- Simplified FX pip-value calculator
- Telegram Web Apps SDK integration with ordinary-browser fallback
- Optional challenge banner and archive driven by `data/challenges.json`

## GitHub Pages deployment

The repository uses the **Deploy TradeThesis Mini App** GitHub Actions workflow. It deploys the root of `main` to GitHub Pages whenever a commit is pushed.

Published site URL:

`https://zaphodbeeblebrox12.github.io/Telegramwebapp/`

Repository Settings → Pages should use **GitHub Actions** as its source.

## Launch it from the main Telegram channel

Telegram Mini Apps support direct links that can be shared in any chat, including a channel. The direct link format is:

`https://t.me/<bot_username>/<app_short_name>`

The existing TradeThesis notification bot can own the Mini App. Register the app with @BotFather using `/newapp`, choose the existing notification bot, set the app title/short name and enter the published GitHub Pages URL.

Then create a channel post with a URL button pointing to the direct Mini App link and pin that post. The channel remains the member-facing entry point; members do not need to open a separate bot conversation.

For campaign-specific links, append a Telegram `startapp` value to the direct
link, for example `?startapp=challenge_6`. The Mini App reads that value and
opens the matching individual campaign page inside Telegram.

A Telegram channel does not have the same customizable persistent Mini App menu button as a bot chat. The pinned post is the permanent launch entry point. Once the app opens, its own bottom navigation remains available.

Suggested pinned post:

> **TradeThesis Trading Desk**
>
> Your trading companion is ready.
>
> Open the TradeThesis Mini App for practical trading tools, challenges and learning resources — all in one place.
>
> **Open TradeThesis**
>
> [Insert the direct Mini App link]

## Add a challenge

Edit `data/challenges.json`. For example:

```json
{
  "challenges": [
    {
      "id": "gold-series-01",
      "name": "Gold Trading Series",
      "subtitle": "A focused market campaign",
      "description": "Campaign overview and participation details.",
      "active": true,
      "archived": false,
      "public_url": "https://example.com"
    }
  ]
}
```

Set `active` to `false` to remove the campaign banner from Home. Archived campaigns can be displayed in Challenges by setting `archived` to `true`.

## Run locally

Open `index.html` through a local static server (for example, `python -m http.server 8000`) and visit `http://localhost:8000`.

## Security

Never put Telegram bot tokens, GitHub tokens, API keys, private user data, or broker credentials in this repository or in frontend JavaScript. A GitHub Pages site is public.

## Calculation notes

All calculators are planning aids, not broker-grade pricing engines. Position sizing assumes a user-supplied per-price-unit value and does not infer contract multipliers. Margin is a simple notional/leverage estimate. Pip value assumes quote currency equals account currency.


## Individual challenge pages

The challenge catalogue links each campaign by its unique `id`, not by asset class or display name. During the GitHub Pages workflow, `scripts/generate_challenge_pages.py` reads `data/challenges.json` and generates one static route per record:

- `/challenges/1/`
- `/challenges/2/`
- `/challenges/3/`

The shared page layout lives in `challenge-template.html`. Each detail page loads the challenge data and selects exactly one record by ID, so campaigns for the same asset (for example, multiple Gold challenges) keep separate balances and trade histories. New challenge IDs are generated automatically on the next Pages deployment.

To preview the generated routes locally, run:

```bash
python3 scripts/generate_challenge_pages.py
python3 -m http.server 8000
```

Then open `http://localhost:8000/challenges/1/`. Generated challenge folders are build output; edit the shared template and source JSON instead.


### Challenge navigation origin

Challenge URLs retain the page from which the user opened them:

- `/challenges/1/?from=home` returns to Home.
- `/challenges/1/?from=challenges` returns to the Challenges catalogue.
- A direct/shared challenge URL without `from` defaults to the Challenges catalogue.

The visible back link and Telegram Mini App BackButton use the same return destination.

Individual challenge pages also retain the app's fixed five-tab bottom navigation
(Home, Challenges, Tools, Learn and About), so users can move to another app
section without first returning to the catalogue.


The exact expedition image is kept as an ASCII base64 source file at
assets/barrel-run-expedition.webp.b64.partNN fragments. GitHub Pages runs
scripts/prepare_campaign_assets.py before generating the challenge pages, rebuilding
assets/barrel-run-expedition.webp for the deployed site. Run that script locally before
previewing the campaign pages outside GitHub Pages.
