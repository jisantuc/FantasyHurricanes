#Fantasy Hurricanes

##The Background

It's getting to be the time of year where the thing to do becomes making predictions about how many receiving yards and touchdowns Odell Beckham Jr. will accrue relative to Calvin Johnson. This is a fun sort of prediction to make, but maybe not an inclusive sort of prediction to make. I propose instead a league of predictions about something that everyone has an interest in: hurricane landfall latitude/longitude pairs!

Ok, maybe not everyone.

Maybe this has been done before? [This guy](http://www.thefargos.com/weather/hurricane/hurricane_landfall_predictions.htm) is all over it at least. But I don't know if it's been done in a *league*. Let's do it in a league.

##The Rules

Players have three days to upload a prediction once a hurricane crosses some arbitrary threshold of longitude (thinking 55deg west, but it's pretty arbitrary) on its way from Africa to America, players have a day to upload a predicted lat/lon of landfall.

Players use [Hurdat 2](http://www.aoml.noaa.gov/hrd/hurdat/hurdat2-1851-2014-060415.txt) (Nice huge csv will be available if people need it) data to train whatever models they want, or whatever else they feel like using. This can include random guessing. Guesses are locked at the close of the day after the hurricane crosses the longitude threshold in whatever timezone the game admin chooses. Then we wait and root for good favor from the gods of probability.

## TODO:
(help gleefully accepted with any of this)

- [ ] set up cleaning program for Hurdat2 data
- [ ] set up ftp link for big csv of hurricane data
- [ ] set up RESTful API for submission of landfall predictions
- [ ] solicit participants