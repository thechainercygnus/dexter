# Functionality

## Spotify API Access

Dexter can perform some basic interactions with the Spotify API at this time.

### Similar Artists

Dexter can be used to find artists similar to the one provided. Currently, this functionality is limited to returning the first 5 results. 

Syntax: `$similarto Jarv`

Output:

```
Pulp
Suede
Graham Coxon
Supergrass
The Divine Comedy
```

### Top Songs for Artist

Dexter can also tell you top "top" 5 songs for an artist.

Syntax: `$topsongs Jarv`

Output:

```
Escargot
Fly to the Moon
Slack-Jaw
Satie / Orch. Ducros: Gymnopédie No. 1
Jar of Hearts
```

## CoinGecko API Access

Dexter provides a quick way to see some immediate Crypto Price data, including the ability to check a balance.

### Verify the API is up

Syntax: `$cryptotest`

Output: `(V3) To the Moon!` if up

### Get the current USD price of a specified token

Returns the USD Value of the provided token.

Syntax: `$pricecheck bitcoin`

Output: `$61477.0`

### Check the value of a set amount of a token

If you want to see how much .00006 ETH is worth...

Syntax: `$balance ethereum 0.00006`

Output: `$0.15`

