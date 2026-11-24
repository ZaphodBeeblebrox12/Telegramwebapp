# TradeThesis Telegram Mini App

A static, mobile-first Telegram Web App for TradeThesis. The initial version is intentionally framework-free and can be hosted on GitHub Pages.

## Included

- Home, Challenges, Tools, Learn and About views
- Position-size calculator
- Risk/reward calculator
- Indicative margin calculator
- Simplified FX pip-value calculator
- Telegram Web Apps SDK integration with ordinary-browser fallback
- Optional challenge banner and challenge archive driven by `data/challenges.json`

## Run locally

Open `index.html` through a local static server (for example, `python -m http.server 8000`) and visit `http://localhost:8000`.

## Publish with GitHub Pages

In the repository settings, open **Pages**, choose **Deploy from a branch**, select `main` and `/(root)`, then save. The app will be published at:

`https://zaphodbeeblebrox12.github.io/Telegramwebapp/`

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

Set `active` to `false` to remove the campaign banner from Home. Archived campaigns can be displayed in the Challenges view by setting `archived` to `true`.

## Security

Never put Telegram bot tokens, GitHub tokens, API keys, private user data, or broker credentials in this repository or in frontend JavaScript. A GitHub Pages site is public even when its source repository is private.

## Calculation notes

All calculators are planning aids, not broker-grade pricing engines. Position sizing assumes a user-supplied per-price-unit value and does not infer contract multipliers. Margin is a simple notional/leverage estimate. Pip value assumes quote currency equals account currency.
