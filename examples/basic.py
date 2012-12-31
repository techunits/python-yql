import yql

yqlObject = yql.Public()
queryStr = 'SELECT * FROM flickr.photos.search WHERE text=@text AND api_key="<API KEY>" LIMIT 3';
yqlObject.execute(queryStr, {
    "text": "panda"
})
