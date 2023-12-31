# confusion-2014-03-02

The Great Language Game confusion dataset, containing user guesses to language game questions.

## Version

2014-03-02

## Description

This dataset contains language confusion information generated by users of the [Great Language Game](http://greatlanguagegame.com). It consists of 16,511,224 JSON records of questions answered by users, one record per line, like so:

```javascript
{"target": "Turkish", "sample": "af0e25c7637fb0dcdc56fac6d49aa55e", "choices": ["Hindi", "Lao", "Maltese", "Turkish"], "guess": "Maltese", "date": "2013-08-19", "country": "AU"}
```

It is intended to provide researchers and hobbyists with useful information on what languages are confused with one another when a non-speaker hears them spoken aloud.

## Files

- `confusion-2014-03-02.json`: the main dataset, one JSON record per line
- `schema.json`: a [JSON Schema](http://json-schema.org/) file which each record of the dataset should meet

## Fields

- `sample`: a checksum of the audio file played to the user
- `target`: the language of the audio file
- `choices`: the options presented to the user (always includes the target)
- `guess`: the user's selected answer
- `date`: the date the question was asked
- `country`: the GeoIP detected country code of the user, or `_` if none was available

## License

This dataset is available under the [Creative Commons Attribution 3.0 Australia](https://creativecommons.org/licenses/by/3.0/au/legalcode) license. This merely requires that you give credit when using the dataset. A reference or link to the [Great Language Game](http://greatlanguagegame.com/) or its [dataset page](http://lars.yencken.org/datasets/languagegame/) somewhere in your post, paper or in the about page of your site is sufficient.

This license is not meant to be onerous -- datasets are made to be used. If complying would be difficult for the use you intend, please just shoot me a short email about it.

Lars Yencken <lars@yencken.org>
